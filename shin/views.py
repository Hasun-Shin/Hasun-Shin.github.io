from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    # return HttpResponse('<h1>Index1</h1>')
    return render(
        request, 'shin/main.html',{}
        )

