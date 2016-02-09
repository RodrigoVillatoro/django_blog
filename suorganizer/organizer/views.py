from django.shortcuts import get_object_or_404, render


from .forms import TagForm
from .models import Startup, Tag


def startup_list(request):
    startups = Startup.objects.all()
    return render(
        request, 'organizer/startup_list.html', {'startup_list': startups})


def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(
        request, 'organizer/startup_detail.html', {'startup': startup})


def tag_list(request):
    tags = Tag.objects.all()
    return render(
        request, 'organizer/tag_list.html', {'tag_list': tags})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(
        request, 'organizer/tag_detail.html', {'tag': tag})


def tag_create(request):
    form = TagForm()
    return render(request, 'organizer/tag_form.html', {'form': form})
