from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import URL
from .forms import URLForm

def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = URLForm()
    
    urls = URL.objects.all().order_by('-created_at')
    return render(request, 'shortener/home.html', {'form': form, 'urls': urls})

def redirect_view(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.clicks += 1
    url.save()
    return HttpResponseRedirect(url.original_url)