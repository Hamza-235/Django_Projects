from django.shortcuts import render
#from .models import carlist
from .forms import carform
from .models import carlist
#from django.shortcuts import HttpResponse 

#def car__list(request):
  
    ##form = carform()
    #if request.method == 'POST':
    #    form = carform(request.POST)
    #    if form.is_valid():
     #       form.save()
    #return render(request,'car.html',{'form':form})

def table(request):
    menulist = carlist.objects.all()
    menu_dict= {'menu': menulist}
    return render(request,'table.html', menu_dict)
                        
#def base(request):
    #return render(request,'base.html')
def index(request):
    return render(request, 'index.html')
#def header(request):
   # return render(request, 'header.html')








#def car_list(request):
   # carr=carlist.objects.all()
    #return render(request,'projectapp/carlist.html',{'carr':carr})
'''from datetime import datetime
def index(request):
    return HttpResponse('Hello world') 
def date(request):
    date=datetime.today().year
    return HttpResponse(date)
def car(request,model):
    md={'Mitsubishi':'Lancer',
        'Ford':'Mustang',
        'Ferrari':'480 Spyder'
       }
    out=md[model]
    return HttpResponse(f"{model}"+" "+out)'''
# Create your views here.
