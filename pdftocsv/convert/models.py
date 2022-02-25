from attr import attrs
from django.db import models
from django.db.models.base import Model

# Create your models here.
class UploadPDF(models.Model):
    upload = models.FileField(upload_to='documents/pdf')

    def __str__(self):
        return str(self.upload)