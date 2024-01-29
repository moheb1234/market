from django.db import models
from users.models import Users
from datetime import date , datetime

class Package(models.Model):
    name = models.CharField(max_length=32 )
    user = models.ForeignKey(Users , on_delete= models.CASCADE)
    package_type = models.CharField(max_length=16)
    discount_code = models.IntegerField(null= True)
    number_of_exchange = models.IntegerField()
    number_of_currencies = models.IntegerField()  # value -1 for all 
    number_of_position_for_each_exchange_in_month = models.IntegerField()
    number_of_create_strategy = models.IntegerField()
    can_use_timeout = models.BooleanField()
    can_access_to_zone = models.BooleanField()
    can_access_to_spread = models.BooleanField(null=True)
    can_access_to_allow_price = models.BooleanField()
    trade_history = models.BooleanField()
    can_use_stop_loss = models.BooleanField()
    can_use_profit = models.BooleanField()
    can_check_position_on_chart = models.BooleanField()
    get_notifications = models.CharField(max_length=16)
    can_download_result = models.BooleanField(null=True)
    professional_report = models.CharField(max_length=32 , null=True)
    open_position = models.IntegerField() # value -1 for full access
    start_data = models.DateField(auto_now_add=True,)
    period_validity = models.IntegerField()  # (1 month  , 3 month  ,...)


    def is_expired(self):
        today = date.today()
        difference = today - self.start_data
        if difference.days >= self.period_validity*30:
            return True
        return False

