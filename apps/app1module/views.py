from django.shortcuts import render,redirect,get_object_or_404
from .models import Game,Developer

def Home_Page(request):
      return render(request, 'app1module/Home_Page.html')
def List_Games(request):
   books = Game.objects.select_related('Developer').all()
   return render(request, 'app1module/List_Games.html', {'books': books})

