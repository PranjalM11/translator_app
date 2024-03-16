from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from googletrans import Translator

def translator_home(request):
    return render(request, 'translator_app/home.html')

@csrf_protect
def translate_text(request):
    """
    A view that takes a POST request with 'text' parameter and translates it to French.
    
    Parameters:
    request (HttpRequest): the incoming request object
    
    Returns:
    JsonResponse: a JSON response containing the translated text
    """
    if request.method == 'POST':
        text = request.POST.get('text')
        translation = Translator(service_urls=['translate.google.com']).translate(text, dest='fr').text

        return JsonResponse({'translation': translation})
