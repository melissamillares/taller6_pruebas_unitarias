from django.test import RequestFactory
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from courses.views import *
from mixer.backend.django import mixer
from django.test import TestCase
import pytest

@pytest.mark.django_db
class TestViews:
	
	def test_course_list_authenticated(self):
		path = reverse('courses:list')
		request = RequestFactory().get(path)
		request.user = mixer.blend(User)
		response = course_list(request)
		assert response.status_code == 200

	def test_course_list_unauthenticated(self):
		path = reverse('courses:list')
		request = RequestFactory().get(path)
		request.user = AnonymousUser()
		response = course_list(request)
		assert 'accounts/login' in response.url