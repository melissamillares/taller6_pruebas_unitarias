# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mixer.backend.django import mixer
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime
import pytest
from courses.models import Student

@pytest.mark.django_db
class TestModels:
	
	def test_course_is_available(self):
		#definimos un objeto tipo datetime a partir de una fecha en string
		start_date = make_aware(datetime.strptime("2018-01-01", "%Y-%m-%d"))
		end_date = make_aware(datetime.strptime("2018-12-12", "%Y-%m-%d"))
		#Simulamos un objeto de tipo Course
		course = mixer.blend('courses.Course', start_date=start_date, end_date
		= end_date)
		#Validamos que el test sea correcto
		assert course.is_available == True

	def test_calculate_approval_percentaje(self):
		student = Student()
		score_correct = 4.0
		score_string = '3'
		score_zero = 0
		scale_correct_5 = 5
		scale_correct_10 = 10
		scale_string = '1 - 10'
		scale_zero = 0
		assert student.approval_percentaje(score_correct, scale_correct_5) == 80
		assert student.approval_percentaje(score_correct, scale_correct_10) == 40
		assert student.approval_percentaje(score_string, scale_correct_5).args[0] == "unsupported operand type(s) for /: 'unicode' and 'int'"
		assert student.approval_percentaje(score_zero, scale_correct_5) == 0
		assert student.approval_percentaje(score_correct, scale_string).args[0] == "unsupported operand type(s) for /: 'float' and 'unicode'"
		assert student.approval_percentaje(score_correct, scale_zero).args[0] == "float division by zero"