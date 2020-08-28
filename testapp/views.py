from django.shortcuts import render
from testapp.models import Registation
from django.http import JsonResponse
# Create your views here.
def index_views(request):
    if request.method=='POST':
        nm=request.POST['input_name']
        ph=request.POST['input_phone']
        em=request.POST['input_email']
        pwd=request.POST['input_password']
       # print(nm,ph,em,pwd)
        user=Registation(Name=nm,Phone=ph,Email=em,Password=pwd)
        user.save()
    return render(request,'index.html')

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
def checkName_views(request):
    nm=request.POST.get('nameval')
    try:
        Registation.objects.get(Name=nm)
        data={'error':'name taken'}
    except Registation.DoesNotExist:
        data={'message':'name avliable'}   
    return JsonResponse(data)    
