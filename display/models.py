from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.files.storage import default_storage
from display.storage import OverwriteStorage
import os
# Create your models here.
SCREEN_CHOICES = [
    ("1","Screen 1"),
    ("2","Screen 2"),
    ("3","Screen 3"),
    ("4","Screen 4"),
]


def video_storage_directory(instance,filename):
    return os.path.join(f'screen_{instance.screen_number}', "video.mp4")

class screen(models.Model):
    screen_number = models.CharField(max_length=10, choices= SCREEN_CHOICES, default= "1", help_text='Select screen')
    video_file = models.FileField(upload_to=video_storage_directory,storage=OverwriteStorage(), validators=[FileExtensionValidator(['mp4'])])
    

def __str__(self):
    return f"Screen {self.id}"