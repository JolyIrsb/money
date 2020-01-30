from django.shortcuts import render

def fl(request):
    return render(request, 'money/moon.html', {})