from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.db.models import Count
from django.contrib import messages
from .models import Blog, Category, Newsletter
from .forms import ContactForm, NewsletterForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            messages.success(request, 'You have successfully subscribed to our newsletter!')
            return redirect('/')
    else:
        form = NewsletterForm()

    category_colors = {
        'Lifestyle': 'green-500',
        'Technology': 'purple-500',
        'Food': 'red-500',
        'Design': 'pink-500',
        'Travel': 'yellow-500',
        'Business': 'blue-500',
        'default': 'gray-500',
    }

    featured_post = Blog.objects.all().order_by('?')[:3]
    recent_post = Blog.objects.all().order_by('-publishedtime')[:6]
    categories = Category.objects.annotate(
        article_count=Count('blogs')
    ).order_by('-article_count')

    context = {
        'form': form,
        'featured_post': featured_post,
        'recent_post': recent_post,
        'category_colors': category_colors,
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    blog.increment_views()
    context = {"blog":blog}
    return render(request, 'blog/blogpost.html', context)

def blog_category(request, slug):
    category_colors = {
        'Lifestyle': 'green-500',
        'Technology': 'purple-500',
        'Food': 'red-500',
        'Design': 'pink-500',
        'Travel': 'yellow-500',
        'Business': 'blue-500', 
        'default': 'gray-500', 
    }
    category = get_object_or_404(Category, slug=slug)
    blogs = Blog.objects.filter(category=category)
    context = {"category":category, "blogs":blogs, "category_colors":category_colors}
    return render(request, 'blog/blog_category.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            form.save()  # Saves the form data to the model  
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to a success page after submission
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html')

def search(request):
    query = request.GET.get('q')
    if query:
        posts = Blog.objects.filter(title__icontains=query)
    else:
        posts = Blog.objects.none()
    context = {'posts': posts, 'query': query}
    return render(request, 'blog/search.html', context)

def legal(request):
    return render(request, 'blog/legal.html')