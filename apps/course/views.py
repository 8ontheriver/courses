from django.shortcuts import render, redirect
from .models import Course, Description

# Create your views here.
def index(request):
	print request.method
	context = {
		"courses" : Course.objects.all(), 
		"descript" : Description.objects.get(course_descript__content="content")
	}
	return render(request, 'course/index.html', context)

def submit(request):
	if request.method == 'POST':
		print request.POST['coursename']
		print request.POST['description']

		Course.objects.create(course_name = request.POST['coursename'])
		# this_course = Course.objects.get(id=id)
		# this_descript = Description.objects.create(course = request.POST['description'], course=Course.objects.get(id=id))

		return redirect('/')

def delete(request, id):
	context = {
		"courses" : Course.objects.filter(id=id),

		# "names": Description.objects.get(course_id=id)
		# "descript" : Description.objects.all()
	}
	print context
	# # if request.method == 'POST':
	# 	Course.objects.get()


	return render(request, 'course/delete.html', context)

def back(request):
	return redirect('/')

def crush(request, id):
	if request.method == 'POST':
		Course.objects.filter(id=id).delete()
		


		# "class" = Course.objects.get(course_name=id)
		# class.delete()
		return redirect('/')
