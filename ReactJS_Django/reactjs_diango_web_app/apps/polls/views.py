# project_name/apps/polls/views.py
'''
    from django.shortcuts import render

def index(request):
    return render(request, 'polls/index.html')

'''

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")