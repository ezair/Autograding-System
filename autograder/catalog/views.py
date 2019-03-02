from django.shortcuts import render


# view for our catalog/ page.
# aka the homepage.
def index(request):
    return render(request, 'catalog/index.html')
