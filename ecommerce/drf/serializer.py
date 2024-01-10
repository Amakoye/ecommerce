from rest_framework import serializers
from ecommerce.inventory.models import (
    Product,
    ProductInventory,
    Brand,
    Category,
    ProductAttributeValue,
    Media,
)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name"]


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        exclude = ["id"]


class MediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = Media
        fields = ["img_url", "alt_text"]
        read_only = True

    def get_img_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.img_url.url)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name"]
        read_only = True
        editable = False


class AllProducts(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        # exclude = ["name"]
        read_only = True
        editable = False


class ProductInventorySerializer(serializers.ModelSerializer):
    # brand = BrandSerializer(many=False, read_only=True)
    # attributes = ProductAttributeValueSerializer(source="attribute_values", many=True)
    # image = MediaSerializer(source="media_product_inventory", many=True)

    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ProductInventory
        fields = [
            "id",
            "sku",
            "store_price",
            "is_default",
            # "image",
            "product",
            # "product_type",
            # "brand",
            # "attributes",
        ]
        readonly = True
        # depth = 2
