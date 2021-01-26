from django.db import models

def fileupload(instance):
    return 'Images/{}/Posters_1.jpg'.format(instance.id)

class Image(models.Model):
    image=models.ImageField(upload_to=fileupload,null=True)