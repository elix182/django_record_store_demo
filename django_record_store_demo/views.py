from django.shortcuts import render
def welcome(request):
  return render(request, 'index.html')
def privacy(request):
  return render(request, 'privacy.html')