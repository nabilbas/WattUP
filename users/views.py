from django.shortcuts import render, get_object_or_404
from .models import Section, Range, Borne

def home(request):
    sections = Section.objects.all()
    return render(request, 'users/home.html', {'sections': sections})

def borne_list(request):
    bornes = Borne.objects.all()
    return render(request, 'borne_list.html', {'bornes': bornes})

# Individual Borne detail view
def borne_detail(request, borne_id):
    borne = get_object_or_404(Borne, id=borne_id)
    return render(request, 'borne_detail.html', {'borne': borne})

# If Ombriere is a model you have, you'll need to import it.
def ombriere_list(request):
    ombrieres = Ombriere.objects.all()
    return render(request, 'ombriere_list.html', {'ombrieres': ombrieres})

def user_list(request):
    # For now, let's render a simple template.
    # Replace 'user_list.html' with the appropriate template name.
    return render(request, 'user_list.html')

def home_view(request):
    sections = Section.objects.all()
    return render(request, 'home.html', {'sections': sections})

def products_view(request):
    sections = Section.objects.all()
    return render(request, 'products.html', {'sections': sections})

def some_view(request):
    sections = Section.objects.all()
    context = {'sections': sections}
    return render(request, 'your_template.html', context)
