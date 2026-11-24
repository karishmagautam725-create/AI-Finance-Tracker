import uuid

from django.db import models

# Create your models here.
class Category(models.Model):
    EXPENSE="expense"
    INCOME="income"
    CATEGORY_TYPE_CHOICES=[
        (EXPENSE,"Expense"),
        (INCOME,"Income"),
    ]
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name="categories")
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=50,choices=CATEGORY_TYPE_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=("user","name")
        indexes=[
            models.Index(fields=["user"]),
        ]
    def __str__(self):
        return f"{self.name} ({self.type})"
    
class Transaction(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name="transactions")
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name="transactions")
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    description=models.CharField(max_length=100,blank=True)
    date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        indexes=[
            models.Index(fields=["user","date"]),
            models.Index(fields=["category"]),
        ]
        ordering=["-date"]
    def __str__(self):
        return f"{self.user.email}-{self.amount}"
class Budget(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user=models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name="budget")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="budget",null=True,blank=True)
    month=models.IntegerField()
    year=models.IntegerField()
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    class Meta:
        unique_together=("user","category","month","year")
        indexes=[
            models.Index(fields=["user","category","year","month"]),
        ]
        
    def __str__(self):
        return f"{self.user.email}-{self.month}/{self.year}"
    
