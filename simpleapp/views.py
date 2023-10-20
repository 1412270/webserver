import requests
from django.http import JsonResponse

proxies = {
   'http': 'http://localhost:8000',
   'https': 'https://localhost:8000'
}


# Make a request to the proxy server running on localhost:8080.
# The proxy server will forward the request to the Express API server
def user_view(request):
    url = 'http://localhost:3000/users'
    response = requests.get(url, proxies=proxies)
    user_data = response.json()
    return JsonResponse(user_data, safe=False)

