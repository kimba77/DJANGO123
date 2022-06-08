from django.test import TestCase
from datetime import date
from . import models


class TestModel(TestCase):
    def test_create_model_post_success(self):
        payload = {
            "title": "Test title",
            "description": "test description",
            "img": "prosto photo",
            "created_date": date.today(),
            "updated_date": date.today(),
            "author": "Марк",
            "genre": "Horor",
            "tom": 5,
        }
        post = models.Bookshows.objects.create(**payload)
        self.assertEqual(post.title, payload["title"])
        self.assertEqual(post.description, payload["description"])
        self.assertEqual(post.img, payload["img"])
        self.assertEqual(post.created_date, payload["created_date"])
        self.assertEqual(post.updated_date, payload["updated_date"])
        self.assertEqual(post.author, payload["author"])
        self.assertEqual(post.genre, payload["genre"])
        self.assertEqual(post.tom, payload["tom"])

    def test_create_model_post_fail(self):
        payload = {
            "title": " New title",
            "description": "test description",
            "img": "prosto_photo",
            "created_date": date.today(),
            "updated_date": date.today(),
            "author": "Марк",
            "genre": "Horor",
            "tom": "five",
        }
        with self.assertRaises(ValueError):
            post = models.Bookshows.objects.create(**payload)
        # with self.assertRaises(ZeroDivisionError):
        #     post = models.Bookshows.objects.create(**payload)

    def test_update_model_post(self):
        payload = {
            "title": " New title",
            "description": "test description",
            "img": "prosto_photo",
            "created_date": date.today(),
            "updated_date": date.today(),
            "author": "Марк",
            "genre": "Horor",
            "tom": 5,
        }
        new_ganre = "Romantic"
        post = models.Bookshows.objects.create(**payload)
        post.genre = new_ganre
        post.save()
        post.refresh_from_db()
        self.assertEqual(post.genre, new_ganre)

    def test_delete_model_post(self):
        payload = {
            "title": " New title",
            "description": "test description",
            "img": "prosto_photo",
            "created_date": date.today(),
            "updated_date": date.today(),
            "author": "Марк",
            "genre": "Horor",
            "tom": 5,
        }
        post = models.Bookshows.objects.create(**payload)
        pk = post.pk
        post.delete()
        with self.assertRaises(models.Bookshows.DoesNotExist):
            models.Bookshows.objects.get(pk=pk)
