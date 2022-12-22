from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Twig
from .forms import FoodForm

def home(request):
    return HttpResponse('<h1>Home</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', { 'finches': finches })

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    food_form = FoodForm()
    return render(request, 'finches/detail.html',{ 'finch': finch, 'food_form': food_form})
def add_food(request, finch_id):
    form = FoodForm(request.POST)
    if form.is_valid():
        new_food = form.save(commit=False)
        new_food.finch_id = finch_id
        new_food.save()
    return redirect('detail', finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/finches/'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'

class TwigList(ListView):
    model = Twig

class TwigDetail(DetailView):
    model = Twig

class TwigCreate(CreateView):
    model = Twig
    fields = '__all__'

class TwigUpdate(UpdateView):
    model = Twig
    fields = '__all__'

class TwigDelete(DeleteView):
    model = Twig
    success = '/twigs/'