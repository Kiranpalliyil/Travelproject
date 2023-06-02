from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import face
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1=face.objects.all()

    # return HttpResponse("hello world")
    #   name="django"
    return render(request,"index.html",{'result':obj,'result1':obj1})



# def find(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res1=x+y
#     res2=x-y
#     res3=x/y
#     return render(request,"result.html",{'resultaddition':res1,'resultsubtraction':res2,'resultdivision':res3})
# def subtraction(request, res2=None):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res2=x-y
#     return render(request,"result.html",{'resultaddition':res2})
# # def division(request):
#     x=int(request.GET['num5'])
#     y=int(request.GET['num6'])
#     res=x/y
#     return render(request,"result.html",{'result':res})