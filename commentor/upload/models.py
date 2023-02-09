from django.db import models

#교수자가 업로드하는 모델
class Document(models.Model):
	title = models.CharField(max_length=200)
	videoFile = models.FileField(upload_to='%Y-%m-%d-%H-%M-%S')
	docFile = models.FileField(upload_to='%Y-%m-%d-%H-%M-%S')
	dateTimeOfUpload = models.DateTimeField(auto_now=True)
