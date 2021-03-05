from django.db import models
import os

# Create your models here.
class AudioClass(models.Model):
    audio_class_name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Audio class'
        verbose_name_plural = 'Audio classes'

    def __str__(self):
        return self.audio_class_name

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        filename = '{}-{}.{}'.format(instance.audio_class.audio_class_name, instance.week_name, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

class AudioClassWeek(models.Model):
    audio_class = models.ForeignKey(AudioClass, on_delete=models.CASCADE)
    week_name = models.CharField(max_length=200)
    audio_file = models.FileField(upload_to=path_and_rename('audios'), default='', blank=True, null=True)

    class Meta:
        verbose_name = 'Audio class week'
        verbose_name_plural = 'Audio class weeks'

    def __str__(self):
        return self.audio_class.audio_class_name + ' ' + self.week_name
