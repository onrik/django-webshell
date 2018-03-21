# coding: utf-8
from django.test import TestCase
from django.conf import settings
from django.contrib.auth import get_user_model
try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

from webshell.models import Script

User = get_user_model()


class WebshellTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='user', is_staff=True, is_superuser=True)
        self.user.set_password('123456')
        self.user.save()
        self.url = reverse('execute-script')
        self.login_url = '%s?next=%s' % (settings.LOGIN_URL, self.url)

    def login(self):
        self.assertTrue(self.client.login(
            username=self.user.username, password='123456'))

    def test_wrong_method(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_login_required(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, self.login_url, 302, 404)

    def test_superuser_required(self):
        self.user.is_superuser = False
        self.user.save()
        self.login()
        response = self.client.post(self.url)
        self.assertRedirects(response, self.login_url, 302, 404)

    def test_success(self):
        self.login()

        response = self.client.post(self.url, data={'source': 'print(1)'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'1\n')

    def test_success_exception(self):
        self.login()

        response = self.client.post(self.url, data={'source': '[1][1]'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'IndexError: list index out of range', response.content)

    def test_admin(self):
        self.login()

        script = Script.objects.create(name='Test')

        urls = (
            reverse('admin:webshell_script_add'),
            reverse('admin:webshell_script_change', args=[script.id]),
            reverse('admin:webshell_script_changelist'),
        )

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
