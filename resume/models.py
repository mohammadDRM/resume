from django.db import models

# Create your models here.


class khadamat(models.Model):
    title=models.CharField(max_length=50)
    dec=models.CharField(max_length=50)



    def __str__(self):
        return str(self.title)



class nemone(models.Model):
    title=models.CharField(max_length=20)
    dec=models.CharField(max_length=30)
    image=models.ImageField(upload_to="resume/media")


    def __str__(self):
        return str(self.title)





class karmand(models.Model):
    name=models.CharField(max_length=30,null=True)
    job=models.CharField(max_length=30,null=True)
    image=models.ImageField(upload_to="resume/media",null=True)


    def __str__(self):
        return str(self.name)










