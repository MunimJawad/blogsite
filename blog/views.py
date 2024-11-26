from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator
from .models import Post, Category
from .forms import CategorySearchForm

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    comments = post.comments.all()  # Retrieve comments related to this post
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post  # Associate the comment with the post
        comment.save()
        return redirect('post_detail', id=post.id)  # Redirect to the same post page after submission

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })


from django.db.models import Q

from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import render

def post_list(request):
    query = request.GET.get('q', '')  # Default to empty string if not provided
    category_name = request.GET.get('category_name', '')  # Default to empty string if not provided

    # Start with all posts
    posts = Post.objects.all().order_by('-created_at')

    # Filter by search query if provided
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    # Filter by category name if provided
    if category_name:
        posts = posts.filter(category__name__icontains=category_name)

    # Paginate the results
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)

    # Get recent posts
    recent_posts = Post.objects.order_by('-created_at')[:5]

    # Get all categories for the search form
    categories = Category.objects.all()
    
    # Create the search form instance
    form = CategorySearchForm(request.GET or None)

    return render(request, 'blog/post_list.html', {
        'page_obj': page_obj,
        'query': query,
        'categories': categories,
        'recent_posts': recent_posts,
        'form': form  # Pass the form to the template if needed
    })


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})




from django.contrib.auth import logout
from django.contrib import messages

def custom_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('post_list')  # Redirect to the home page





# blog/views.py
# blog/views.py
def category_posts_view(request, slug):
    category = get_object_or_404(Category, slug=slug)  # Get the category by slug
    posts = category.posts.all()  # Use the related_name to get all posts of this category
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})



from django.shortcuts import render
from .models import Category

def home(request):
    categories = Category.objects.all()  # Retrieve all categories
    form = CategorySearchForm(request.GET or None)
    posts = Post.objects.all()

    # Check if the form is submitted and process the input
    if form.is_valid():
        category_name = form.cleaned_data.get('category_name')
        if category_name:
            # Filter posts by category name (case insensitive)
            posts = posts.filter(category__name__icontains=category_name)

    return render(request, 'blog/home.html', {
        'categories': categories,  # Pass categories to the template
        'form': form,
        'posts': posts,
    })

def about_view(request):
    return render(request, 'blog/about.html')



