from django.shortcuts import render


def home(request):
	import requests
	import json

	# try to get aapl from API
	api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_7aebabcf2e5b422fb0cd4d8b19e27450")

	try:
		api = json.loads(api_request.content) #Parse the data if posible

	except Exception as e:
		api = "Error..."


	return render(request, 'home.html', {'api': api})


def about(request):
	return render(request, 'about.html', {})
