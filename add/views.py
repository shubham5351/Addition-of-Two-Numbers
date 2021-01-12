from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'add/home.html')


def result(request):
    n1 = request.POST.get("num1")
    n2 = request.POST.get("num2")
    result = int(n1) + int(n2)
    return render(request, 'add/result.html', {'result': result})
