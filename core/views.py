from django.http import HttpResponse
# pelajari https://docs.djangoproject.com/en/3.2/ref/request-response/
# jika ingin mengetahui kenapa ada argumen itu?

def borrower(request):
    return HttpResponse("halo dunia")

def credit(request):
    return HttpResponse("bayarmu kreditmu")

