from django.db import models
from users.models import User
import uuid
class Budgets(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null= True, blank = True, related_name = 'budgets' )
    name  = models.CharField(max_length= 50, blank= False, null= False)
    limit = models.DecimalField(decimal_places= 2, max_digits= 9, blank= False)
    start_date = models.DateField(blank = True)
    category = models.CharField(max_length= 50 , blank = True, null = True)
    current_spending = models.DecimalField(decimal_places= 2, max_digits= 9)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def remaining(self):
        return self.limit - self.current_spending
    
    @property
    def percentage_used(self):
        if self.limit and self.limit > 0:
            return(self.current_spending / self.limit  * 100)
        return 0

    def __str__(self):
        return f"{self.get_category_display()} budget ({self.user.username})"
    