from django.shortcuts import render
def fl(request):
    return render(request, '/templates/money/fl.html', {})