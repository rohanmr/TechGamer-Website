
from django.shortcuts import render

from core.models import mainpost

# Create your views here.
def home(request):
    return render(request,'core/index.html')

def data(request):
    return render(request,'core/data2.html')

def data1(request):
    return render(request,'core/data3.html')

def latest1(request):
    return render(request,'core/latest.html')

def latest2(request):
    return render(request,'core/latest2.html')

def latest3(request):
    return render(request,'core/latest3.html')

def all(request):
    post=mainpost.objects.all()
    data={
        'mainpost':post
    }
    return render(request,'core/allitems.html',data)

    
def search(request):
    things=mainpost.objects.all()
    if request.method=="POST":
        searched=request.POST['searched']
        if searched!=None:
          things=mainpost.objects.filter(title__icontains=searched)
        return render(request,'core/search.html',{'searched':searched,'things':things})
    # postdata=mainpost.objects.all()
    # if request.method=="GET":
    #     st=request.GET.get('postname')
    #     if st!=None:
    #         postdata=mainpost.objects.filter(title__icontains=st)
    # alldata={
    #     'postdata':postdata
    # }

    # return render(request,'core/search.html',alldata)