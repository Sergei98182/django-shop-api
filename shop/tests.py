from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

from shop.models import Category, SubCategory, Product


class ShopAPITest(APITestCase):

    def setUp(self):
        # создаем пользователя
        self.user = User.objects.create_user(username='testuser', password='12345')

        # создаем категорию
        self.category = Category.objects.create(
            name='Напитки',
            slug='napitki',
            image=''
        )

        # создаем подкатегорию
        self.subcategory = SubCategory.objects.create(
            name='Кофе',
            slug='coffee',
            image='',
            category=self.category
        )

        # создаем продукт
        self.product = Product.objects.create(
            name='Американо',
            slug='americano',
            price=100,
            subcategory=self.subcategory,
            image_small='',
            image_medium='',
            image_large=''
        )

    def test_get_categories(self):
        url = '/api/categories/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_add_to_cart(self):
        # авторизация
        self.client.force_authenticate(user=self.user)

        url = '/api/cart/add/'
        data = {
            "product_id": self.product.id,
            "quantity": 2
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["message"], "Product added to cart")