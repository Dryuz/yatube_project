from re import template
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group(request):
    return HttpResponse('Groups')


def group_posts(request, slug):
    return HttpResponse(f'Group: {slug}')