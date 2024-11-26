
# blog/context_processors.py
from .models import Category

def category_list(request):
    categories = Category.objects.all()  # Fetch all categories
    return {'categories': categories}