from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from shop.models import Category, Product, Cart, CartItem
from .serializers import CategorySerializer, ProductSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def get_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart


class AddToCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        product = Product.objects.get(id=product_id)
        cart = get_cart(request.user)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        item.quantity = item.quantity + quantity if not created else quantity
        item.save()

        return Response({"message": "Product added to cart"})


class CartDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = get_cart(request.user)
        items = cart.items.all()

        total = 0
        data = []

        for item in items:
            item_total = item.product.price * item.quantity
            total += item_total

            data.append({
                "product": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity,
                "total": item_total
            })

        return Response({
            "items": data,
            "total_price": total
        })


class RemoveFromCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        cart = get_cart(request.user)

        CartItem.objects.filter(cart=cart, product_id=product_id).delete()

        return Response({"message": "Item removed"})


class ClearCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = get_cart(request.user)
        cart.items.all().delete()

        return Response({"message": "Cart cleared"})