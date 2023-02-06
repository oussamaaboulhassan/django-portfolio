from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name="app/index.html")

def compo(request):
    return render(request, template_name="app/components.html")