from django.db import models
from users.models import Users
from datetime import date
import string , random




class Package(models.Model):
    name = models.CharField(max_length=32 )
    user = models.ForeignKey(Users , on_delete= models.CASCADE)
    package_type = models.CharField(max_length=16)
    number_of_exchange = models.IntegerField(null= True)
    number_of_currencies = models.IntegerField(null= True)  # value -1 for all 
    number_of_position_for_each_exchange_in_month = models.IntegerField(null= True)
    number_of_create_strategy = models.IntegerField(null= True)
    number_of_sig_for_each_day = models.IntegerField(null=True)
    number_of_coins_for_signals  = models.IntegerField(null=True)
    num_of_scan_for_each_exchange_per_day = models.IntegerField(null=True)
    can_use_timeout = models.BooleanField(null= True)
    can_access_to_zone = models.BooleanField(null= True)
    can_access_to_spread = models.BooleanField(null=True)
    can_access_to_allow_price = models.BooleanField(null= True)
    can_view_trade_history = models.BooleanField(null= True)
    can_use_stop_loss = models.BooleanField(null= True)
    can_use_profit = models.BooleanField(null= True)
    can_check_position_on_chart = models.BooleanField(null= True)
    get_notifications = models.CharField(max_length=16)
    can_download_result = models.BooleanField(null=True)
    professional_report = models.CharField(max_length=32 , null=True)
    open_position = models.IntegerField(null= True) # value -1 for full access
    start_data = models.DateField(auto_now_add=True,)
    period_validity = models.IntegerField(null=True)  # (1 month  , 3 month  ,...)
    automate_manual = models.CharField(max_length=16 , null=True)
    price = models.IntegerField(null= True)



    def is_expired(self):
        if self.period_validity is None:
            return False
        today = date.today()
        difference = today - self.start_data
        if difference.days >= self.period_validity*30:
            return True
        return False



class Discount(models.Model):
    package = models.ForeignKey(Package , on_delete = models.CASCADE , related_name = 'discounts')
    code = models.CharField(max_length = 16,unique= True)
    percent = models.IntegerField()
    descriptions = models.CharField(max_length = 256 , null = True)
    created_date = models.DateField(auto_now_add = True)
    period_validity = models.IntegerField(null=True)  # number of days


    def generate_code(self):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits , k = 7))
        return f'MXJ{code}'
    
    def is_expired(self):
        today = date.today
        difference = today - self.created_date
        if difference.days > self.period_validity:
            return True
        return False
    