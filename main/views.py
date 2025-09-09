from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406495956',
        'name': 'Cristian Dillon Philbert',
        'class': 'PBP A'
    }

    return render(request, "main/main.html", context)

# Create your views here.
