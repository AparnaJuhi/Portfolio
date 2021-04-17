from django.shortcuts import render,HttpResponse
def index(request):
    context={
        'variable':'This is sent by views to index.'
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
