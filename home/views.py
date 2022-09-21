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
    print("==>tag",tag)
    
    context = {
        categories: categories
    }
    return render(request,"home/index.html",context)

# def blogSingle(request):    
#     context = {
#     }
#     return render(request,"home/index.html",context)
def tagList(request, slug):    
    context = {
        'slug': slug
    }
    print("-------tagList-------",context)
    return render(request,"home/blog_list.html",context)


def categoryList(request, slug):    
    context = {
        'slug': slug
    }
    print("-------categoryList-------",context)
    return render(request,"home/blog_list.html",context)


def blogDetail(request, cat_slug, blog_slug):    
    context = {
        'cat_slug': cat_slug,
        'blog_slug': blog_slug,
    }
    print("--------------")
    print("--------------",context)
    return render(request, "home/blog_detail.html",context)