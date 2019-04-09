from django.http import HttpResponse


def homepage(request):
    print(request)
    return HttpResponse("Hello, world. You're at the polls index. 你好")
