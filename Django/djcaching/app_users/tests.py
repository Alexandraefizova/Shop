from django.test import TestCase

import datetime

from django.urls import reverse
from django.utils import timezone

from app_users.models import User


class LoginUserTest(TestCase):

    def setUp(self):
        # Создание двух пользователей
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='12345')
        resp = self.client.get(reverse('login'))

        # Проверка того, что мы используем правильный шаблон
        self.assertTemplateUsed(resp, 'users/login.html')
