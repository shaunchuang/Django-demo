from django.http import HttpResponse



def index_view(request):

    STRING = "<h1>Hello World</h1>"
    return HttpResponse(STRING)
 