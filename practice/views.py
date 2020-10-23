from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from utils.classfiy import predict


def imag(request):
    if request.method == "POST":
        imag = request.FILES.get("imag", "")
        if imag == "":
            return JsonResponse({'errcode': 201, 'errmsg': 'imag不能为空'}, json_dumps_params={'ensure_ascii': False})
        else:
            m = predict(imag)
            return JsonResponse({'errcode': 200, 'data': m}, json_dumps_params={'ensure_ascii': False})