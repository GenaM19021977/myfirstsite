from django.http import HttpResponse

def home(request):
    return HttpResponse("<b1><h1>Добро пожаловать на стартовую страницу New site!<h1></b1>")