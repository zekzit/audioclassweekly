from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import AudioClass, AudioClassWeek
from .forms import AudioClassWeekUploadForm

def index(request):
    audio_classes = AudioClass.objects.all().order_by('id')
    context = {'audio_classes': audio_classes}
    return render(request, 'audios/index.html', context)

def details(request, class_id, week_id):
    week = AudioClassWeek.objects.get(pk=week_id)
    response = None
    if week.audio_file:
        response = HttpResponseRedirect('/' + str(class_id) + '/' + str(week_id) + '/listen')
    else:
        response = HttpResponseRedirect('/' + str(class_id) + '/' + str(week_id) + '/upload')
    return response

def listen(request, class_id, week_id):
    audio_class = AudioClass.objects.get(pk=class_id)
    week = AudioClassWeek.objects.get(pk=week_id)
    context = { 'audio_class': audio_class, 'week': week}
    return render(request, 'audios/listen.html', context)

def upload_form(request, class_id, week_id):
    exists_week = AudioClassWeek.objects.get(pk=week_id)
    if request.method == 'POST':
        form = AudioClassWeekUploadForm(request.POST, request.FILES, instance=exists_week)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/' + str(class_id) + '/' + str(week_id) + '/listen')
    else:
        form = AudioClassWeekUploadForm()
    return render(request, 'audios/upload.html', {'form': form, 'class_id': class_id, 'week_id': week_id, 'week': exists_week})
