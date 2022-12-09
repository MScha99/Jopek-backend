#from msilib.schema import Media
from unicodedata import category
from rest_framework import serializers
from inventory.models import Product, Category, Comment, Profile, Order, OrderProduct, RentProduct
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token

"""
serializer.py jest używany do konwertowania złożonych typów danych na typ danych mogący być renderowany do formatu JSON
każda klasa zawiera serializer obsługujący wskazaneny model i określa pola które powinny być reprezentowane
"""

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','password']

        extra_kwargs = {'password':{
            'write_only':True,
            'required':True
        }}
    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
    

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class AllProducts(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Product
        fields = ( 
            "id",
            "name",
            "slug",
            "price",
            "brand",
            "description",
            "stock",
            "is_active",
            "category",
            "image",
            "displayrent",
            "renteduntill"
        )

class Product(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ( 
            "id",
            "name",
            "price",
            
           
        )
        
class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Comment
        fields = ["id","product","body","created_on","owner"]


class OrderProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name", read_only=True)
    price = serializers.IntegerField(source="product.price", read_only=True)
    
    class Meta:
        model = OrderProduct
        fields = [
            "id",
            "order",
            "product",
            "quantity",
            "name",
            "price"
            
        ]
        def to_representation(self, instance):
            response = super().to_representation(instance)
            response['name'] = instance.id# also response['other_field'] = otherSerializer(instance.model)    
            return response

class OrderSerializer(serializers.ModelSerializer):
    
    OrderProduct = OrderProductSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = ["id","OrderProduct","order_date", "notes","price","city","street","zipcode","status"]
        

        
class RentProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name", read_only=True)    
    renteduntill=serializers.DateField(source="product.renteduntill", read_only=True)
    class Meta:
        model = RentProduct
        fields = [
            "id",  
            "product",          
            "name",
            "renteduntill",
            
        ]

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    userid = serializers.ReadOnlyField(source='user.id')
    order = OrderSerializer(read_only=True, many=True)  
    RentProduct = RentProductSerializer(read_only=True, many=True)
    class Meta:
        model = Profile
        fields = ( 
            
            "username",
            "userid",
            "order",
            "RentProduct"
            
        )
