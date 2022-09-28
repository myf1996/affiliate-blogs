from django.shortcuts import render
from .models import Categories,Entry
from taggit.models import Tag

# Create your views here.
def home(request):
    categories = Categories.objects.filter(isActive=True)
    entries = Entry.objects.filter(is_published=True)
    recent = entries.order_by('-published_timestamp')
    tags = Tag.objects.all()
    
    
    blog = {}
    for cat in categories:
        blog[cat.name+'___'+cat.slug] = recent.filter(category=cat)[:4]


    for tag in tags:
        print("88888888888888888888888",tag.name)
        print(recent.filter(tags=tag))

    print("=============================")
    print("==>category:",categories)
    print("==>entry:",entries)
    print("==>recent:",recent[:1])
    print("==>blog",blog)
    print("==>tag",tags)
    
    context = {
        'categories': categories,
        'entries': entries,
        'recents': recent[:4],
        'tags': tags
    }
    return render(request,"home/index.html",context)

# def blogSingle(request):    
#     context = {
#     }
#     return render(request,"home/index.html",context)
def tagList(request, slug):    
    categories = Categories.objects.filter(isActive=True)
    category = categories.get(isActive=True, slug=slug)
    entries = Entry.objects.filter(is_published=True)
    recents = entries.order_by('-published_timestamp')
    tags = Tag.objects.all()
    context = {
        'categories': categories,
        'category': category,
        'entries': entries,
        'recents': recents[:4],
        'tags': tags
    }
    return render(request,"home/blog_list.html",context)


def categoryList(request, slug):
    categories = Categories.objects.filter(isActive=True)
    category = categories.get(isActive=True, slug=slug)
    entries = Entry.objects.filter(is_published=True)
    recents = entries.order_by('-published_timestamp')
    tags = Tag.objects.all()
    context = {
        'categories': categories,
        'category': category,
        'entries': entries,
        'recents': recents[:4],
        'tags': tags
    }
    return render(request,"home/blog_list.html",context)


def blogDetail(request, cat_slug, blog_slug):    
    categories = Categories.objects.filter(isActive=True)
    category = categories.get(isActive=True, slug=cat_slug)
    entries = Entry.objects.filter(is_published=True, category=category)
    entry = Entry.objects.get(is_published=True, slug=blog_slug)
    recents = entries.order_by('-published_timestamp')
    tags = Tag.objects.all()
    context = {
        'categories': categories,
        'entries': entries,
        'entry': entry,
        'recents': recents[:4],
        'tags': tags
    }
    return render(request, "home/blog_detail.html",context)