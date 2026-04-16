from rest_framework import serializers
from shop.models import Category, SubCategory, Product


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'image']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image', 'subcategories']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'slug',
            'price',
            'category',
            'subcategory',
            'image_small',
            'image_medium',
            'image_large',
        ]

    def get_category(self, obj):
        return {
            "id": obj.subcategory.category.id,
            "name": obj.subcategory.category.name
        }

    def get_subcategory(self, obj):
        return {
            "id": obj.subcategory.id,
            "name": obj.subcategory.name
        }