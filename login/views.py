
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

class LoginView(View):
    def get(self, request):
        return render(request, 'login/vxod.html')
    def post(self, request):
        return JsonResponse(request.POST, json_dumps_params={'indent':4})
class RegisterView(View):
    def get(self, request):
        return render(request, 'login/index.html')
    def post(self, request):
        return JsonResponse(request.POST, json_dumps_params={'indent': 4})

