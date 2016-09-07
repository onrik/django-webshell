# coding: utf-8
from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class WebshellTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user')
        self.user.set_password('123456')
        self.user.save()
        self.url = reverse('execute-script')
        self.login_url = '%s?next=%s' % (settings.LOGIN_URL, self.url)

    def test_wrong_method(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 405)

    def test_login_required(self):
        response = self.client.post(self.url)
        self.assertRedirects(response, self.login_url, 302, 404)

    def test_superuser_required(self):
        self.assertTrue(
            self.client.login(username=self.user.username, password='123456'))
        response = self.client.post(self.url)
        self.assertRedirects(response, self.login_url, 302, 404)

    def test_success(self):
        self.user.is_superuser = True
        self.user.save()

        self.assertTrue(
            self.client.login(username=self.user.username, password='123456'))
        response = self.client.post(self.url, data={'source': 'print(1)'})
        self.assertEqual(response.content, b'1\n')
