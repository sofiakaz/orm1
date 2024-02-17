from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    content = Phone.objects.all()
    template = 'catalog.html'
    sort = request.GET.get('sort', ' ')
    if sort == 'name':
        content = list(Phone.objects.all().order_by('name').values())
    elif sort == 'min_cost':
        content = list(Phone.objects.all().order_by('price').values())
    else:
        content = list(Phone.objects.all().order_by('-price').values())
    context = {

        'phones': content
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    content = Phone.objects.get(slug=slug)
    context = {
        'phone': content
    }
    return render(request, template, context)

