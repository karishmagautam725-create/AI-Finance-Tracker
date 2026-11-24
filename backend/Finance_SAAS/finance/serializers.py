from rest_framework import serializers

from .models import Category, Transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=["id","user","name","type"]

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.none(),
        source="category",
        write_only=True   
        )
    
    
    class Meta:
        model=Transaction
        fields=["amount","category","date","description","category_id"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request=self.context.get("request")
        if request:
            self.fields["category_id"].queryset=Category.objects.filter(user=request.user)
