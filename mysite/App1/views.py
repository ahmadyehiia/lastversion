from django.http import HttpResponse , HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from .models import book

# Create your views here.
#def index(request):
    #return  HttpResponse("it Works!!!!!!!!!!")
x='yehia haha'

monthly_challenge={
    "january":"eat no meat for the entire month",
    "feburary":"walk for atleast 20 ,min",
    "march":"eat a little more meat ",
    "april":"drink a little more ",
    "june":"hiii",
    "july":"asjsss",
    "august":"km,hc",
    "september":"jdhsjsjy",
    "november":"yshs",
    "december":"shtsjjs",
}

#DINAMIC STRING TEST MOVE TO HTML PAGE
def monthly_challenges_by_number(request,month):     #to make all months work in the url when typing 1 it gets jan in the dectionary 

    months= list(monthly_challenge.keys())
    if month > len(months):
       return HttpResponseNotFound("invalid")
    redirect_month = months[month -1]
    print(redirect_month)
    return HttpResponseRedirect("/App1/" +redirect_month)

def monthly_challenges(request,month):   #to render to the html page and show the text
    try:    
      challenges_text=monthly_challenge[month]
      return HttpResponse(challenges_text)
    except:
     return render(request, "shahd/challenges.html",{"text":challenges_text} )
 
# to fetch data from database 
#step1: import tables up 
#step 2 type the following function to get
def index(request):
 books = book.objects.all() # to fetch all of books table and all records
 return render(request, "/shahd/database.html",{"books":books})

#bygbha 3la shakl list w bt3rdha fe el html as a for loop in the html file 
#DONE IT IN FILE CALLED DATABASE HTML

