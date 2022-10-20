from django.test import TestCase
from django.http import HttpRequest
import myblog.views as views
import myblog.views_tag as views_tag
from .models import Article, Tag


class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST["title"] = "My title"
        self.request.POST["content"] = "lorem ipsum content"
        return super().setUp()

    def test_create_article(self):
        response = views.create_article(self.request)
        article = Article.objects.first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(article.title, "My title")
        self.assertEqual(article.content, "lorem ipsum content")

    def test_update_article(self):
        self.test_create_article()

        self.request.POST["title"] += " updated"
        self.request.POST["content"] += " updated"

        article = Article.objects.first()
        response = views.update_article(self.request, article.id)
        article.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(article.title, "My title updated")
        self.assertEqual(article.content, "lorem ipsum content updated")


class TagTestCase(TestCase):
    def setUp(self) -> None:
        self.request = HttpRequest()
        self.request.method = 'POST'
        self.request.POST["tag"] = "My tag"
        return super().setUp()

    def test_create_tag(self):
        response = views_tag.create_tag(self.request)
        tag = Tag.objects.first()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(tag.name, "My tag")
    
    def test_create_two_same_tags(self):
        self.test_create_tag()
        self.assertRaisesMessage(Exception, "Tag already exists", self.test_create_tag)


class ViewsTestCase(TestCase):

    def test_home(self):
        request = HttpRequest()
        request.method = 'GET'

        response = views.home(request)

        self.assertEqual(response.status_code, 200)
