from django.shortcuts import render, redirect
from myapp.formulaire import StudentsForm
from myapp.models import Students
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from django.shortcuts import render, redirect
from .forms import UserRegisterForm



# Create your views here.

 
def index(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request , 'registration/signup.html' , {'form': form})


#def index(request):
  #  template = loader.get_template('index.html')
    #return HttpResponse(template.render())


# ** def add_form(request):
    #if request.method == 'POST':
       # form = StudentsForm(request.POST, request.FILES)
        #if form.is_valid():
           # form.save()
            #return redirect('/myapp')
   # else:
       # object_list = Students.objects.all()
       # paginator = Paginator(object_list, 3)
       ## page_number = request.GET.get('page')
        #try:
          #  page_object = paginator.page(page_number)
            #except PageNotAnInteger:
               # page_object = paginator.page(1)
            #except EmptyPage:
               # page_object = paginator.page(paginator.num_pages())    
        
        #form = StudentsForm()
        #return render(request, 'forms.html', {'form': form, 'dataOject': Students.objects.all()}) **#   