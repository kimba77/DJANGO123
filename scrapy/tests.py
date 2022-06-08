from django.test import TestCase
from . import models


class TestWatchs(TestCase):
    def test_create_model_post_success(self):
        payload = {
            "link": "Какая та ссылка",
            "image": "prosto_image",
            "title": "Test Title",
            "price": 400,
        }
        post = models.Watchs.objects.create(**payload)
        self.assertEqual(post.link, payload["link"])
        self.assertEqual(post.image, payload["image"])
        self.assertEqual(post.title, payload["title"])
        self.assertEqual(post.price, payload["price"])

    def test_create_model_post_fail(self):
        payload = {
            "link": "Какая та ссылка",
            "image": "fffee",
            "title": "Test Title",
            "price": "Four",
        }
        with self.assertRaises(ValueError):
            post = models.Watchs.objects.create(**payload)

    def test_update_model_post(self):
        payload = {
            "link": "Какая та ссылка",
            "image": "fffee",
            "title": "Test Title",
            "price": 500,
        }
        new_image = "Мир.png"
        post = models.Watchs.objects.create(**payload)
        post.image = new_image
        post.save()
        post.refresh_from_db()
        self.assertEqual(post.image, new_image)

    def test_delete_model_post(self):
        payload = {
            "link": "Какая та ссылка",
            "image": "fffee",
            "title": "Test Title",
            "price": 500,
        }
        post = models.Watchs.objects.create(**payload)
        pk = post.pk
        post.delete()
        with self.assertRaises(models.Watchs.DoesNotExist):
            models.Watchs.objects.get(pk=pk)


class TestTehnodom(TestCase):
    def test_create_model_post_success(self):
        payload = {
            "image": "prosto_image",
            "title": "Test Title",
            "price": 400,
        }
        post = models.Tehchnodom.objects.create(**payload)
        self.assertEqual(post.image, payload["image"])
        self.assertEqual(post.title, payload["title"])
        self.assertEqual(post.price, payload["price"])

    def test_create_model_post_fail(self):
        payload = {
            "image": "ff-fee",
            "title": "Test Title",
            "price": "Four",
        }
        with self.assertRaises(ValueError):
            post = models.Tehchnodom.objects.create(**payload)

    def test_update_model_post(self):
        payload = {"image": "fffee", "title": "Test Title", "price": 500}
        new_image = "Мир.png"
        post = models.Tehchnodom.objects.create(**payload)
        post.image = new_image
        post.save()
        post.refresh_from_db()
        self.assertEqual(post.image, new_image)

    def test_delete_model_post(self):
        payload = {"image": "fffee", "title": "Test Title", "price": 500}
        post = models.Tehchnodom.objects.create(**payload)
        pk = post.pk
        post.delete()
        with self.assertRaises(models.Tehchnodom.DoesNotExist):
            models.Tehchnodom.objects.get(pk=pk)
