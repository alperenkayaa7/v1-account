import sys  # noqa
sys.path.insert(0, 'source/package')  # noqa

import validators
import PKSShared
import simplejson as sjson
import uuid
from decimal import Decimal
from .account import Account
import os
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def check_health(event, context):
    try:
        return PKSShared.BaseSuccessResponse({"status": "ok", "stage": os.environ.get('STAGE')}).response()
    except Exception as e:
        logger.error(f"check_health error: {str(e)}")
        return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error due to {str(e)}")]).response(500)
def create_account(event, context):
    try:
        if "body" not in event or event["body"] is None:
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InvalidRequest", "Invalid request")]).response(400)
        
        body = sjson.loads(event["body"], use_decimal=True)

        if os.environ.get('STAGE') == 'dev':
            body["account_id"] = str(uuid.uuid4())
        else:
            body["account_id"] = str(uuid.uuid4())

        account = Account.from_dict(body)

        errors = account.validate()
        if errors:
            return PKSShared.BaseErrorResponse(errors=errors).response()
        
        tableName = os.environ.get('TABLE_NAME')
        if tableName is None:
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error")]).response(500)
        print("table name", tableName)
        
        table = boto3.resource('dynamodb').Table(tableName)
        response = table.put_item(Item=account.to_dict())
        
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return PKSShared.BaseSuccessResponse(account.to_dict()).response()
        else:
            logger.error("DynamoDB put_item unexpected HTTPStatusCode")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error")]).response(500)
    except Exception as e:
        logger.error(f"create_account error: {str(e)}")
        return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error due to {str(e)}")]).response(500)
def update_account(event, context):
    try:
        if "body" not in event or event["body"] is None:
            logger.error("Invalid request: No body found")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InvalidRequest", "Invalid request")]).response(400)
        
        body = sjson.loads(event["body"], use_decimal=True)

        if os.environ.get('STAGE') == 'dev':
            body["account_id"] = "71aedae2-e2a5-4769-a366-9847f90dfaa4"
        else:
            body["account_id"] = event["requestContext"]["authorizer"]["claims"]["sub"]

        account = Account.from_dict(body)

        errors = account.validate()
        if errors:
            logger.error(f"Validation errors: {errors}")
            return PKSShared.BaseErrorResponse(errors=errors).response()
        
        tableName = os.environ.get('TABLE_NAME')
        if tableName is None:
            logger.error("TABLE_NAME environment variable is not set")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error")]).response(500)
        
        table = boto3.resource('dynamodb').Table(tableName)
        response = table.put_item(Item=account.to_dict())
        
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return PKSShared.BaseSuccessResponse(account.to_dict()).response()
        else:
            logger.error("DynamoDB put_item unexpected HTTPStatusCode")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error")]).response(500)
    except Exception as e:
        logger.error(f"update_account error: {str(e)}")
        return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error due to {str(e)}")]).response(500)

def get_account(event, context):
    try:
        if "pathParameters" not in event or event["pathParameters"] is None:
            logger.error("Invalid request: No pathParameters found")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InvalidRequest", "Invalid request")]).response(400)
        
        account_id = event["pathParameters"].get("account_id")
        if not account_id:
            logger.error("Invalid request: account_id not provided in pathParameters")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InvalidRequest", "account_id is required")]).response(400)

        tableName = os.environ.get('TABLE_NAME')
        if tableName is None:
            logger.error("TABLE_NAME environment variable is not set")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error")]).response(500)
        
        table = boto3.resource('dynamodb').Table(tableName)
        response = table.get_item(Key={"account_id": account_id})
        
        if "Item" not in response:
            logger.warning(f"Account not found: {account_id}")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.NotFound", "Account not found")]).response(404)
        else:
            return PKSShared.BaseSuccessResponse(response["Item"]).response()
    except Exception as e:
        logger.error(f"get_account error: {str(e)}")
        return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error due to {str(e)}")]).response(500)

def passivate_account(event, context):
    try:
        if "pathParameters" not in event or event["pathParameters"] is None:
            logger.error("Invalid request: No pathParameters found")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InvalidRequest", "Invalid request")]).response(400)
        
        account_id = event["pathParameters"]["account_id"]

        tableName = os.environ.get('TABLE_NAME')
        if tableName is None:
            logger.error("TABLE_NAME environment variable is not set")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error")]).response(500)
        
        table = boto3.resource('dynamodb').Table(tableName)
        response = table.delete_item(Key={"account_id": account_id})
        
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            logger.info(f"Account passivated: {account_id}")
            return PKSShared.BaseSuccessResponse({"message": "Account passivated successfully"}).response()
        else:
            logger.error("DynamoDB delete_item unexpected HTTPStatusCode")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error")]).response(500)
    except Exception as e:
        logger.error(f"passivate_account error: {str(e)}")
        return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error due to {str(e)}")]).response(500)

def list_accounts(event, context):
    try:
        tableName = os.environ.get('TABLE_NAME')
        if tableName is None:
            logger.error("TABLE_NAME environment variable is not set")
            return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error")]).response(500)
        
        table = boto3.resource('dynamodb').Table(tableName)
        response = table.scan()
        
        if "Items" not in response:
            logger.warning("No items found in DynamoDB table scan")
            return PKSShared.BaseSuccessResponse([]).response()
        else:
            return PKSShared.BaseSuccessResponse(response["Items"]).response()
    except Exception as e:
        logger.error(f"list_accounts error: {str(e)}")
        return PKSShared.BaseErrorResponse(errors=[PKSShared.BaseError("error.default.InternalServerError", "Internal Server Error due to {str(e)}")]).response(500)



            
        