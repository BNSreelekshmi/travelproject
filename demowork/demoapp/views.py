from django.http import HttpResponse
from django.shortcuts import render
from . models import placedetail, teamdetail
# Create your views here.

# static web page task
# def demostatic(request):
#     return render(request,"index.html")



#  orm dynamic page
def demostatic(request):
    obj = placedetail.objects.all()
    obj1 = teamdetail.objects.all()
    return render(request,"index.html",{'result': obj,'result1':obj1})





# New project task
# def funhome(request):
#     return HttpResponse("WELCOME......... This is Lorem Ipsum home page")
# def funcontact(request):
#     return render(request,"contact.html")
# def fundetail(request):
#     return render(request,"details.html")
# def funabout(request):
#     return render(request,"about.html")
# def funthanx(request):
#     return HttpResponse("Thank you.... Visit the page again")


# passing value task

# def funhome(request):
#     return render(request, "userdata.html")
# def operations(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     result1 = x + y
#     result2 = x - y
#     result3 = x * y
#     result4 = x / y
#     return render(request,"result.html",{'output1':result1,'output2':result2,'output3':result3,'output4':result4})
