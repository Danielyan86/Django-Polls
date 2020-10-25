from django.http import HttpResponse


def homepage(request):
    print(request)
    return HttpResponse("Hello, 123 world. You're at the polls index. 你好")
