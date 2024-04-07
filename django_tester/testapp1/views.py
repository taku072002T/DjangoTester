from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name="index.html"
class ErrorView(TemplateView):
    template_name="error.html"
    
from django.shortcuts import render

# Create your views here.

def index(request):
    message = {
        'title':'testapp1',
        'text':'Hello',
    }
    return render(request, 'app01/index.html', message)
    