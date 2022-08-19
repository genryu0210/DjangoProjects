from django.http import HttpResponse


def helloworldfunction(request):
    returnobject = HttpResponse("helloworld")
    return returnobject
