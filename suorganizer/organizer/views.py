from django.shortcuts import get_object_or_404, render


from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()
    return render(
        request, 'organizer/tag_list.html', {'tag_list': tag_list}
    )


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(
        request, 'organizer/tag_detail.html', {'tag': tag}
    )
