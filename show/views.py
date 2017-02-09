# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
        friends = ['pigbloodcake', 'aliveoctopus', 'grasshopper', 'pigeon', 'durian']
        return render_to_response('index.html', {'friends':friends})
    
def pigbloodcake(request):
        return render_to_response('pigbloodcake.html')
  
def aliveoctopus(request):
        return render_to_response('aliveoctopus.html')
  
def grasshopper(request):
        return render_to_response('grasshopper.html')
  
def pigeon(request):
        return render_to_response('pigeon.html')
  
def durian(request):
        return render_to_response('durian.html')