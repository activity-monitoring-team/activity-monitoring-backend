from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    date_update=models.DateTimeField()




class Orders(BaseModel):
    
    name = models.CharField(max_length=25, null=True)
    verif_code = models.CharField(max_length=50)
    chat_id = models.CharField(max_length=50)
    bank_details = models.CharField(max_length=250)
    amount = models.IntegerField()
    limit = models.IntegerField(null=True)
    date_craete=models.DateTimeField()
    status = models.CharField(max_length=20, null=True)
    bill = models.ImageField(null=True)
    
    class Meta:
        db_table = 'orders'


class Menagers(BaseModel):
    
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    verif_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    class Meta:
        db_table = 'menagers'

class Users(BaseModel):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, null=True)
    verif_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    chat_id = models.IntegerField(null = True)
    
    class Meta:
        db_table = 'users'

class Reports(BaseModel):
    
    manager = models.ForeignKey(Menagers, on_delete=models.CASCADE)
    amount_sum = models.IntegerField()
    
    class Meta:
        db_table='reports'
        
    def get_amount_sum(self):
        amounts = Orders.objects.filter(verif_code=self.manager.verif_code)
        all_orders_amount = sum(amounts.amount)
        return all_orders_amount


