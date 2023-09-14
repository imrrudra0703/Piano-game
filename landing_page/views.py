from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import time
import pygame


def index(request):
    return render(request, 'landing_page/templates/index.html')

def play_violin(request):
    pygame.mixer.init()
    pygame.mixer.music.load('media/violin_music.mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()
    return HttpResponse("Payment Successful")
