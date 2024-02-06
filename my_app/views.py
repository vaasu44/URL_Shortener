
from sqlite3 import Date
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import LongToShort


# Create your views here.

def home_page(request): 
    #by default making it as fault 
    context={
        "submitted":False,
        "error":False
    }
    if request.method=='POST':
        #print(request.POST)
        
        #accessing the long url
        data=request.POST#dictionary which contains all the data
        long_url=data['longurl']
        custom_name=data['custom_name']

        print(long_url)
        print(custom_name)
        
        #CREATE
        try:
            obj=LongToShort(long_url=long_url,short_url=custom_name)
            obj.save()


            #READ
            date=obj.date
            clicks=obj.clicks

            #displaying url dynamically
            context["long_url"]=long_url
            context["short_url"]=request.build_absolute_uri() +custom_name   #for returning the url we use this inbuilt methods
            context["date"]=date #date updating
            context["clicks"]=clicks #clicks updating
            #when its submitted then changing it as true
            context["submitted"]=True
        except:
            context["error"]=True    
        
   
    # else:
    #     return HttpResponse("user not found")

     #for html we have to use render 
    

    return render(request,"index.html",context) 
    

def redirect_url(request,short_url):
    #fetching the url from database
    row=LongToShort.objects.filter(short_url=short_url)
    #print(row)

    #handled the errorr
    if len(row)==0:
        return render(request,"notfound.html")
    
    obj=row[0]
    long_url=obj.long_url

    #saved the clicks based on the user  visiting that link
    obj.clicks=obj.clicks+1
    obj.save()

    
    return redirect(long_url)





def all_analytics(request):
    rows=LongToShort.objects.all()
    context={
        'rows':rows,
    }
    return render(request,"all-analytics.html",context)