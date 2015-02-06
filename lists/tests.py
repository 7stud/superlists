from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_goes_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_has_correct_title(self):
        requ = HttpRequest()
        resp = home_page(requ)
        html = resp.content

        self.assertTrue(html.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith(b'</html>'))






