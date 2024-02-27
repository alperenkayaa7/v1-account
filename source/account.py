import sys  # noqa
sys.path.insert(0, 'source/package')  # noqa

import validators
import PKSShared
import datetime
import simplejson as sjson
import uuid
from decimal import Decimal


class Account:
    def __init__(self,
                account_id: str = None,
                account_name: str = None,
                account_balance: Decimal = None,
                account_risk: Decimal = None,
                daily_target: Decimal = None,
                weekly_target: Decimal = None,
                monthly_target: Decimal = None,
                yearly_target: Decimal = None,
                max_daily_loss: Decimal = None,
                max_weekly_loss: Decimal = None,
                max_monthly_loss: Decimal = None,
                max_yearly_loss: Decimal = None,
                daily_trade_limit: Decimal = None,
                weekly_trade_limit: Decimal = None,
                monthly_trade_limit: Decimal = None,
                yearly_trade_limit: Decimal = None,
                favorite_pair: str = None,
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.account_balance = account_balance
        self.account_risk = account_risk
        self.daily_target = daily_target
        self.weekly_target = weekly_target
        self.monthly_target = monthly_target
        self.yearly_target = yearly_target
        self.max_daily_loss = max_daily_loss
        self.max_weekly_loss = max_weekly_loss
        self.max_monthly_loss = max_monthly_loss
        self.max_yearly_loss = max_yearly_loss
        self.daily_trade_limit = daily_trade_limit
        self.weekly_trade_limit = weekly_trade_limit
        self.monthly_trade_limit = monthly_trade_limit
        self.yearly_trade_limit = yearly_trade_limit
        self.favorite_pair = favorite_pair
    def validate_account_id(self) -> [PKSShared.BaseError]:
        errors = []
        if self.account_id is None or not isinstance(self.account_id, str) or not validators.uuid(self.account_id):
            errors.append(PKSShared.BaseError(
                "Account.accountId.invalid", "Account Id is invalid"))
        return errors
    def validate_account_name(self) -> [PKSShared.BaseError]:
        errors = []
        if self.account_name is None or not isinstance(self.account_name, str) or len(self.account_name) < 1:
            errors.append(PKSShared.BaseError(
                "Account.accountName.invalid", "Account Name is invalid"))
        return errors
    def validate_account_balance(self) -> [PKSShared.BaseError]:
        errors = []
        if self.account_balance is None or not isinstance(self.account_balance, Decimal) or self.account_balance < 0:
            errors.append(PKSShared.BaseError(
                "Account.accountBalance.invalid", "Account Balance is invalid"))
        return errors
    def validate_account_risk(self) -> [PKSShared.BaseError]:
        errors = []
        if self.account_risk is None or not isinstance(self.account_risk, Decimal) or self.account_risk < 0:
            errors.append(PKSShared.BaseError(
                "Account.accountRisk.invalid", "Account Risk is invalid"))
        return errors
    def validate_daily_target(self) -> [PKSShared.BaseError]:
        errors = []
        if self.daily_target is None or not isinstance(self.daily_target, Decimal) or self.daily_target < 0:
            errors.append(PKSShared.BaseError(
                "Account.dailyTarget.invalid", "Daily Target is invalid"))
        return errors
    def validate_weekly_target(self) -> [PKSShared.BaseError]:
        errors = []
        if self.weekly_target is None or not isinstance(self.weekly_target, Decimal) or self.weekly_target < 0:
            errors.append(PKSShared.BaseError(
                "Account.weeklyTarget.invalid", "Weekly Target is invalid"))
        return errors
    def validate_monthly_target(self) -> [PKSShared.BaseError]:
        errors = []
        if self.monthly_target is None or not isinstance(self.monthly_target, Decimal) or self.monthly_target < 0:
            errors.append(PKSShared.BaseError(
                "Account.monthlyTarget.invalid", "Monthly Target is invalid"))
        return errors
    def validate_yearly_target(self) -> [PKSShared.BaseError]:
        errors = []
        if self.yearly_target is None or not isinstance(self.yearly_target, Decimal) or self.yearly_target < 0:
            errors.append(PKSShared.BaseError(
                "Account.yearlyTarget.invalid", "Yearly Target is invalid"))
        return errors
    def validate_max_daily_loss(self) -> [PKSShared.BaseError]:
        errors = []
        if self.max_daily_loss is None or not isinstance(self.max_daily_loss, Decimal) or self.max_daily_loss < 0:
            errors.append(PKSShared.BaseError(
                "Account.maxDailyLoss.invalid", "Max Daily Loss is invalid"))
        return errors
    def validate_max_weekly_loss(self) -> [PKSShared.BaseError]:
        errors = []
        if self.max_weekly_loss is None or not isinstance(self.max_weekly_loss, Decimal) or self.max_weekly_loss < 0:
            errors.append(PKSShared.BaseError(
                "Account.maxWeeklyLoss.invalid", "Max Weekly Loss is invalid"))
        return errors
    def validate_max_monthly_loss(self) -> [PKSShared.BaseError]:
        errors = []
        if self.max_monthly_loss is None or not isinstance(self.max_monthly_loss, Decimal) or self.max_monthly_loss < 0:
            errors.append(PKSShared.BaseError(
                "Account.maxMonthlyLoss.invalid", "Max Monthly Loss is invalid"))
        return errors
    def validate_max_yearly_loss(self) -> [PKSShared.BaseError]:
        errors = []
        if self.max_yearly_loss is None or not isinstance(self.max_yearly_loss, Decimal) or self.max_yearly_loss < 0:
            errors.append(PKSShared.BaseError(
                "Account.maxYearlyLoss.invalid", "Max Yearly Loss is invalid"))
        return errors
    def validate_daily_trade_limit(self) -> [PKSShared.BaseError]:
        errors = []
        if self.daily_trade_limit is None or not isinstance(self.daily_trade_limit, Decimal) or self.daily_trade_limit < 0:
            errors.append(PKSShared.BaseError(
                "Account.dailyTradeLimit.invalid", "Daily Trade Limit is invalid"))
        return errors
    def validate_weekly_trade_limit(self) -> [PKSShared.BaseError]:
        errors = []
        if self.weekly_trade_limit is None or not isinstance(self.weekly_trade_limit, Decimal) or self.weekly_trade_limit < 0:
            errors.append(PKSShared.BaseError(
                "Account.weeklyTradeLimit.invalid", "Weekly Trade Limit is invalid"))
        return errors
    def validate_monthly_trade_limit(self) -> [PKSShared.BaseError]:
        errors = []
        if self.monthly_trade_limit is None or not isinstance(self.monthly_trade_limit, Decimal) or self.monthly_trade_limit < 0:
            errors.append(PKSShared.BaseError(
                "Account.monthlyTradeLimit.invalid", "Monthly Trade Limit is invalid"))
        return errors
    def validate_yearly_trade_limit(self) -> [PKSShared.BaseError]:
        errors = []
        if self.yearly_trade_limit is None or not isinstance(self.yearly_trade_limit, Decimal) or self.yearly_trade_limit < 0:
            errors.append(PKSShared.BaseError(
                "Account.yearlyTradeLimit.invalid", "Yearly Trade Limit is invalid"))
        return errors
    def validate_favorite_pair(self) -> [PKSShared.BaseError]:
        errors = []
        if self.favorite_pair is None or not isinstance(self.favorite_pair, str) or len(self.favorite_pair) < 1:
            errors.append(PKSShared.BaseError(
                "Account.favoritePair.invalid", "Favorite Pair is invalid"))
        return errors
    def validate(self) -> [PKSShared.BaseError]:
        errors = []
        errors.extend(self.validate_account_id())
        errors.extend(self.validate_account_name())
        errors.extend(self.validate_account_balance())
        errors.extend(self.validate_account_risk())
        errors.extend(self.validate_daily_target())
        errors.extend(self.validate_weekly_target())
        errors.extend(self.validate_monthly_target())
        errors.extend(self.validate_yearly_target())
        errors.extend(self.validate_max_daily_loss())
        errors.extend(self.validate_max_weekly_loss())
        errors.extend(self.validate_max_monthly_loss())
        errors.extend(self.validate_max_yearly_loss())
        errors.extend(self.validate_daily_trade_limit())
        errors.extend(self.validate_weekly_trade_limit())
        errors.extend(self.validate_monthly_trade_limit())
        errors.extend(self.validate_yearly_trade_limit())
        errors.extend(self.validate_favorite_pair())
        return errors
    

    @staticmethod
    def from_dict(data):
        accountId = data.get('account_id') if data.get('account_id') is not None else str(uuid.uuid4())
        accountName = data.get('account_name')
        accountBalance = None
        if data.get('account_balance') is not None and isinstance(data.get('account_balance'), (Decimal, int, float)):
            accountBalance = Decimal(data.get('account_balance'))
        accountRisk = None
        if data.get('account_risk') is not None and isinstance(data.get('account_risk'), (Decimal, int, float)):
            accountRisk = Decimal(data.get('account_risk'))
        dailyTarget = None
        if data.get('daily_target') is not None and isinstance(data.get('daily_target'), (Decimal, int, float)):
            dailyTarget = Decimal(data.get('daily_target'))
        weeklyTarget = None
        if data.get('weekly_target') is not None and isinstance(data.get('weekly_target'), (Decimal, int, float)):
            weeklyTarget = Decimal(data.get('weekly_target'))
        monthlyTarget = None
        if data.get('monthly_target') is not None and isinstance(data.get('monthly_target'), (Decimal, int, float)):
            monthlyTarget = Decimal(data.get('monthly_target'))
        yearlyTarget = None
        if data.get('yearly_target') is not None and isinstance(data.get('yearly_target'), (Decimal, int, float)):
            yearlyTarget = Decimal(data.get('yearly_target'))
        maxDailyLoss = None
        if data.get('max_daily_loss') is not None and isinstance(data.get('max_daily_loss'), (Decimal, int, float)):
            maxDailyLoss = Decimal(data.get('max_daily_loss'))
        maxWeeklyLoss = None
        if data.get('max_weekly_loss') is not None and isinstance(data.get('max_weekly_loss'), (Decimal, int, float)):
            maxWeeklyLoss = Decimal(data.get('max_weekly_loss'))
        maxMonthlyLoss = None
        if data.get('max_monthly_loss') is not None and isinstance(data.get('max_monthly_loss'), (Decimal, int, float)):
            maxMonthlyLoss = Decimal(data.get('max_monthly_loss'))
        maxYearlyLoss = None
        if data.get('max_yearly_loss') is not None and isinstance(data.get('max_yearly_loss'), (Decimal, int, float)):
            maxYearlyLoss = Decimal(data.get('max_yearly_loss'))
        dailyTradeLimit = None
        if data.get('daily_trade_limit') is not None and isinstance(data.get('daily_trade_limit'), (Decimal, int, float)):
            dailyTradeLimit = Decimal(data.get('daily_trade_limit'))
        weeklyTradeLimit = None
        if data.get('weekly_trade_limit') is not None and isinstance(data.get('weekly_trade_limit'), (Decimal, int, float)):
            weeklyTradeLimit = Decimal(data.get('weekly_trade_limit'))
        monthlyTradeLimit = None
        if data.get('monthly_trade_limit') is not None and isinstance(data.get('monthly_trade_limit'), (Decimal, int, float)):
            monthlyTradeLimit = Decimal(data.get('monthly_trade_limit'))
        yearlyTradeLimit = None
        if data.get('yearly_trade_limit') is not None and isinstance(data.get('yearly_trade_limit'), (Decimal, int, float)):
            yearlyTradeLimit = Decimal(data.get('yearly_trade_limit'))
        favoritePair = data.get('favorite_pair')
        return Account(
            accountId,
            accountName,
            accountBalance,
            accountRisk,
            dailyTarget,
            weeklyTarget,
            monthlyTarget,
            yearlyTarget,
            maxDailyLoss,
            maxWeeklyLoss,
            maxMonthlyLoss,
            maxYearlyLoss,
            dailyTradeLimit,
            weeklyTradeLimit,
            monthlyTradeLimit,
            yearlyTradeLimit,
            favoritePair
        )

        

    
    def to_dict(self):
        return {
            "accountId": self.account_id,
            "accountName": self.account_name,
            "accountBalance": self.account_balance,
            "accountRisk": self.account_risk,
            "dailyTarget": self.daily_target,
            "weeklyTarget": self.weekly_target,
            "monthlyTarget": self.monthly_target,
            "yearlyTarget": self.yearly_target,
            "maxDailyLoss": self.max_daily_loss,
            "maxWeeklyLoss": self.max_weekly_loss,
            "maxMonthlyLoss": self.max_monthly_loss,
            "maxYearlyLoss": self.max_yearly_loss,
            "dailyTradeLimit": self.daily_trade_limit,
            "weeklyTradeLimit": self.weekly_trade_limit,
            "monthlyTradeLimit": self.monthly_trade_limit,
            "yearlyTradeLimit": self.yearly_trade_limit,
            "favoritePair": self.favorite_pair
        }
    


        
            
            
            