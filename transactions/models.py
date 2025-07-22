from django.db import models
from users.models import User

class Transactions(models.Model):
    frequency = {
        'Weekly' : 'weekly',
        'Daily' : 'daily',
        'Monthly' : 'monthly',
        'Yearly' : 'yearly'
    }

    TRANSACTION_TYPE = {
        'Income': 'income',
        'Expense' : 'expense'
    }

    
    id = models.CharField(primary_key= True, max_length=50, blank = False, null = False)
    user_id = models.ForeignKey(User,  on_delete= models.SET_NULL, null= True, blank = True, related_name = 'transactions')
    amount = models.DecimalField(decimal_places=2, max_digits= 10,max_length= 10)
    transaction_type = models.CharField(blank = True, null=True, max_length= 50)
    category = models.CharField(max_length=50, choices=TRANSACTION_TYPE, default="-------")
    description = models.CharField(max_length= 100, blank= True, null= True)
    date = models.DateField(auto_now_add=  True)
    is_recurring = models.CharField(max_length= 10,)
    recurring_frequency = models.CharField(max_length= 10, choices= frequency)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        pass
