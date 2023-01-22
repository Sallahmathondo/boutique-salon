# Create your views here.
from django.http import HttpResponse
from .models import salon, salonName
from django.template import loader
from django.shortcuts import render,  get_object_or_404


def index(request):
    """View function for home page of site."""
    salon_list = salon.objects.order_by('-launch_date')
    num_salons = salon.objects.all().count()
    # template = loader.get_template('saloncatalog/index.html')
    context = {
        'salon_list': salon_list,
        'num_salons': num_salons,
    }
    return HttpResponse(render(request, 'saloncatalog/index.html', context))


def detail(request, phone_id):
    salon = get_object_or_404(salon, pk=salon_id)
    return render(request, 'saloncatalog/detail.html', {'salon': salon})
