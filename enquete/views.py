from django.http import HttpResponse

def index(request):
    saudacao = "Hello World!!!"
    return HttpResponse(saudacao)

# Create your views here.
