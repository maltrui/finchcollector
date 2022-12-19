from django.shortcuts import render

from django.http import HttpResponse

class Finch: 
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Mike', 'Finch 1', 'Weird Finch', 3),
  Finch('Bro', 'Finch 2', 'Cool Finch', 0),
  Finch('Sam', 'Finch 3', 'Normal Finch', 4)
]

def home(request):
    return HttpResponse('<h1>Home</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })