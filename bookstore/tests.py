import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Author, Book


class BookTests(APITestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name='John',
            last_name='Doe',
            birth_date='1970-01-01',
        )
        self.book = Book.objects.create(
            title='Book Title',
            author=self.author,
            description='Book Description',
            published_date='2022-01-01',
        )

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        books = Book.objects.all()
        data = [{'id': book.id, 'title': book.title, 'description': book.description} for book in books]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), data)
