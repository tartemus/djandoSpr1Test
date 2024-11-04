from django.shortcuts import render

posts = [
    # ваш список публикаций
]

def index(request):
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, id):
    post = next((post for post in posts if post['id'] == id), None)
    return render(request, 'detail.html', {'post': post})

def category_posts(request, category_slug):
    return render(request, 'category.html', {'category_slug': category_slug})
