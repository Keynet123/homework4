## -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return HttpResponse(requests, 'index.html')
