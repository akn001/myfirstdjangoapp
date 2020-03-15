from django.shortcuts import render

from mcatagory.models import mcatagory , sub_catagory

def home (request):
    cat = mcatagory.objects
    scat = sub_catagory.objects
    return render(request,'index.html', {'mcatagory': cat, 'sub_catagory':scat})





