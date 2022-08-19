from django.http import HttpResponse
from django.views.generic import TemplateView


def helloworldfunction(request):
    returnobject = HttpResponse("<h1>helloworld")
    return returnobject


class HelloWorldClass(TemplateView):
    template_name = "hello.html"
