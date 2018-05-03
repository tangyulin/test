from django.shortcuts import render


# Create your views here.



def mine(request):
    return render(request, "user-control/mine/mine.html")


def regist(request):
    return render(request, "user-control/mine/regist.html")
