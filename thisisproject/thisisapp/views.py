from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from .models import Thisisapp
# Create your views here.

def gotohome(request):
    blog=Blog.objects.all()

    return render(request,'home.html',{'blogs':blog})

def detail(request,blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html',{'detail':detail})

def test(request):
    return render(request,'test.html')

def create(request):
    blog = Blog()
    blog.title=request.GET['title']
    blog.pub_date = timezone.datetime.now()
    blog.body=request.GET['body']
    blog.save()

    return redirect('/detail/'+str(blog.id))
from django.utils import timezone

def delete(request,blog_id):
    get_object_or_404(Blog,pk=blog_id).delete()
    return redirect('/')

def edit(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'edit.html',{'blog':blog})

def update(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.save()

    return redirect('/detail/'+str(blog.id))

def gotomain(request):
    bunsu=Thisisapp.objects.all()
    
    return render(request,'port/main.html',{'bunsu':bunsu})