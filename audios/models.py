from django.db import models

# Create your models here.
class AudioClass(models.Model):
    audio_class_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Audio class'
        verbose_name_plural = 'Audio classes'

    def __str__(self):
        return self.audio_class_name

class AudioClassWeek(models.Model):
    audio_class = models.ForeignKey(AudioClass, on_delete=models.CASCADE)
    week_name = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to='uploads/audios', default='')

    class Meta:
        verbose_name = 'Audio class week'
        verbose_name_plural = 'Audio class weeks'

    def __str__(self):
        return self.week_name