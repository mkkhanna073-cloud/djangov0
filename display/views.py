from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import screen
from django.http import JsonResponse

# Create your views here.

def media(request):
    return HttpResponse('Hello, World!')

def second(request):
    template = loader.get_template('htmlfile.html')
    return HttpResponse(template.render())

def video(request):
    template = loader.get_template('video.html')
    return HttpResponse(template.render())

def screen_1(request):
    template = loader.get_template('screen_1.html')
    return HttpResponse(template.render())

def screen_4(request):
    screen_4_object = screen.objects.get(screen_number = 4)
    screen_id = screen_4_object.pk
    screen_object = screen.objects.get(id=screen_id)

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        modified = screen.video_file.storage.get_modified_time(screen.video_file.name)
        return JsonResponse({"modified": modified.timestamp()})

    return render(request, "screen_4.html", {"screen_object":screen_object})

