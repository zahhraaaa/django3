from django.shortcuts import render, get_object_or_404
from .models import main
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def main_list(request):
    object_list = main.objects.filter(status='published')
    paginator = Paginator(object_list, 3) # 2 posts in each page
    page = request.GET.get('page')
    try:
        mains = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        mains = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        mains = paginator.page(paginator.num_pages)
    return render(request,'main/post/list.html',
                        {'page': page,
                        'mains': mains})


def main_detail(request, year, month, day, main):
 main = get_object_or_404(main, slug=main,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day)
 main.visits = main.visits +1
 main.save()       
 return render(request,
 'main/post/detail.html',
 {'main': main})     