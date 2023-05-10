import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse, HttpRequest

def get_links(request: HttpRequest):
    url = request.GET.get('url')  # Obtém a URL fornecida pelo usuário nos parâmetros da requisição

    # Realiza o web scraping da página
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extrai os links da página
    links = []
    for link_tag in soup.find_all('a'):
        link_href = link_tag.get('href')
        
        if link_href:
            link = {
                'nome': link_tag.text,
                'url': link_href
            }
            links.append(link)
    if links:
        return JsonResponse(links, safe=False, status=200)
    return JsonResponse({'error' : 'Nenhum link encontrado'}, status=404)
