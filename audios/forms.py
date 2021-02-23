from django import forms
from .models import AudioClassWeek

class AudioClassWeekUploadForm(forms.ModelForm):
    class Meta:
        model = AudioClassWeek
        fields = ['audio_file'] 