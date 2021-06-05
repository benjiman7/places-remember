from django.shortcuts import redirect, render

def main_page(request):
    return render(request, 'website/main_page.html')
