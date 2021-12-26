from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError

def main_view(request):
    return HttpResponse('Hi')