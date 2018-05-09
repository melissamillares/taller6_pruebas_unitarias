# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from mixer.backend.django import mixer
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime
import pytest
import mock
from courses.models import Course, Student

@pytest.mark.django_db
class TestModels:
	
	def test_course_is_available(self):
		#definimos un objeto tipo datetime a partir de una fecha en string
		start_date = make_aware(datetime.strptime("2018-01-01", "%Y-%m-%d"))
		end_date = make_aware(datetime.strptime("2018-12-12", "%Y-%m-%d"))
		#Simulamos un objeto de tipo Course
		course = mixer.blend('courses.Course', start_date=start_date, end_date = end_date)
		#Validamos que el test sea correcto
		assert course.is_available == True
	
	def test_course_is_not_available(self):
		#definimos un objeto tipo datetime a partir de una fecha en string
		start_date = make_aware(datetime.strptime("2017-01-01", "%Y-%m-%d"))
		end_date = make_aware(datetime.strptime("2017-12-12", "%Y-%m-%d"))
		#Simulamos un objeto de tipo Course
		course = mixer.blend('courses.Course', start_date=start_date, end_date = end_date)
		#Validamos que el test sea correcto
		assert course.is_available == False

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

	def test_student_registration(self):
		#Creamos un mock de tipo course para usar su método is_available como verdadero
		course_available = mock.Mock(Course)

		#Creamos un mock de tipo course para usar su método is_available como falso
		course_not_available = mock.Mock(Course)

		#definimos que el metodo is_available del mock course_available retorne un valor verdadero
		course_available.is_available = True 
		
		#definimos que el metodo is_available del mock course_not_available retorne un valor falso
		course_not_available.is_available = False 

		#creamos el objeto student
		student = Student()

		#verificamos la respuesta
		assert student.student_registration(course_available) == "Estudiante puede matricularse"
		assert student.student_registration(course_not_available) == "Estudiante no se puede matricular"

	def test_approved_course(self):
		#Creamos un mock de tipo student para usar su método approval_percentaje resultando un valor >= 90
		student_higher = mock.Mock(Student)
		
		#Creamos un mock de tipo student para usar su método approval_percentaje resultando un valor < 90
		student_lower = mock.Mock(Student)

		#definimos el metodo approval_percentaje del mock student_higher con un valor de 99 (>=90)
		student_higher.approval_percentaje = 99

		#definimos el metodo approval_percentaje del mock student_lower con un valor de 50 (<90)
		student_lower.approval_percentaje = 50

		#creamos el objeto curso
		curso = Course()

		#verificamos respuestas
		assert curso.approved_course(student_higher) == "El estudiante aprobo el curso"
		assert curso.approved_course(student_lower) == "El estudiante no aprobo el curso"



