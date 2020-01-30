from django.shortcuts import render
def name(request):
    return render(request, '/templates/money/fl.html', {})