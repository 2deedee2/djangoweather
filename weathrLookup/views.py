from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=16FD3EA9-3C3C-412E-894D-33CC7D676FAA")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error...."

		if api[0]['Category']['Name'] == "Good" :
			category_description = "0-50: GOOD"
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
	  		category_description = "51-100: Moderate"
	  		category_color = "moderate"

		return render(request, 'home.html',{
			'api': api,
			'category_description':category_description,
			'category_color':category_color
			})

	else:
		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=16FD3EA9-3C3C-412E-894D-33CC7D676FAA")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error...."

		if api[0]['Category']['Name'] == "Good" :
			category_description = "0-50: GOOD"
			category_color = "good"
		elif api[0]['Category']['Name'] == "Moderate":
	  		category_description = "51-100: Moderate"
	  		category_color = "moderate"



		return render(request, 'home.html',{
			'api': api,
			'category_description':category_description,
			'category_color':category_color
			})

def about(request):
	return render(request, 'about.html',{})