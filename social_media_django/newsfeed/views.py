from django.shortcuts import render

# Create your views here.
def newsfeed(request):
    context = {}
    return render(request, 'newsfeed/newsfeed.html', context)

def post(request, pk):
    context = {}
    return render(request, 'newsfeed/post.html', context)