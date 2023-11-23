from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, "index.html")

def contacts(request):
	return render(request, "contactUs.html")

def submit_resume(request):
	full_name = request.POST.get("full_name", "Undefined")
	date_of_birth = request.POST.get("date_of_birth", "Undefined")
	hobbies = request.POST.get("hobbies", "None")
	work_experience = request.POST.getlist("work_experience", [])

	return HttpResponse(f"""
	        <h2>Full Name: {full_name}</h2>
	        <div>Date of Birth: {date_of_birth}</div>
	        <div>Hobbies: {hobbies}</div>
	        <div>Work Experience: {', '.join(work_experience) if work_experience else "None"}</div>
	    """)


