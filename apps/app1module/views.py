from django.shortcuts import render,redirect,get_object_or_404

def index(request):
# render the appropriate template for this request
   return render(request, 'app1module/index.html')
