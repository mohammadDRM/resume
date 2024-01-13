from django.shortcuts import render
from   . import models
# Create your views here.
def index(request):
    data=models.khadamat.objects.all()
    data1=models.nemone.objects.all()
    data2=models.karmand.objects.all()
    return render(request,'resume/index.html',{'khadamat':data,
                                               'nemone': data1,
                                               'karmand':data2})