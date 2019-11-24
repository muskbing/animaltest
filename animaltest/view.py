from django.http import HttpResponse
 
def hello(request):
    return HttpResponse("Hello,This is Fliex's website!")
