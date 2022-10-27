from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from .models import Stock
from .forms import StockForm
from django.contrib import messages


def home(request):
	import requests
	import json

	if request.method == 'POST':
		try:
		    ticker = request.POST['ticker']
		except MultiValueDictKeyError:
		    ticker = "aapl"
		# ticker has the value form the searchbar

		# try to get 'ticker' from API
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_7aebabcf2e5b422fb0cd4d8b19e27450")

		try:
			api = json.loads(api_request.content) #Parse the data if posible
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})

	else:
		return render(request, 'home.html', {'ticker': "Enter a ticker symbol above..."})


	# try to get aapl from API
	# api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_7aebabcf2e5b422fb0cd4d8b19e27450")

	# try:
	# 	api = json.loads(api_request.content) #Parse the data if posible

	# except Exception as e:
	#	api = "Error..."
	


	return render(request, 'home.html', {'api': api})


def about(request):
	return render(request, 'about.html', {})


def add_stock(request):

	if request.method == 'POST':
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Stock has been added"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		return render(request, 'add_stock.html', {'ticker': ticker})


def delete(request, stock_id):
	item = Stock.objects.get(pk=stock_id)

