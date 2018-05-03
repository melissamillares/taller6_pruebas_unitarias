# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.decorators import login_required
from .models import Course
from django.shortcuts import render
from django.http import HttpResponseRedirect

def course_list(request):
    if request.user.is_authenticated():
        courses = Course.objects.all()
        return render(request, 'courses/course_list.html', {'object_list': courses})
    else:
        return HttpResponseRedirect("/accounts/login/")

def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except:
        course = None
    return render(request, 'courses/course_detail.html', {'course': course})

class CourseCreation(CreateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'start_date', 'end_date', 'description']

class CourseUpdate(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['name', 'start_date', 'end_date', 'description']

class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')
