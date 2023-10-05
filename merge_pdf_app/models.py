from django.db import models

# Create your models here.

from django.db import models

class PDFFile(models.Model):
    file = models.FileField(upload_to='pdfs/')
