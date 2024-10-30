from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import jobserializer  # Ensure this serializer is correctly implemented
from .models import *
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == "GET":
        return Response({
            "Response": 200,
            "Working": "GET"
        })
    elif request.method == "POST":
        return Response({
            "Response": 200,
            "Working": "POST"
        })
    elif request.method == "PATCH":
        return Response({
            "Response": 200,
            "Working": "PATCH"
        })
    else:
        return Response({
            "response": 400,
            "Working": "Method out of Scope"
        })
@csrf_exempt

@api_view(['POST'])
def post_job(request):
    try:
        # request.data automatically contains both form data and file data if it's multipart/form-data
        serializer = jobserializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()  # Save the job posting if the data is valid
            return Response({
                "status": 200,
                "message": "Success",
                "data": serializer.data
            })
        else:
            return Response({
                "status": 400,
                "message": "Invalid data",
                "errors": serializer.errors
            })
    except Exception as e:
        print(e)  # Log the exception for debugging
        return Response({
            "status": 500,
            "message": "An error occurred: " + str(e)
        })

    
@api_view(['GET'])
def getjob(request):
    try:
        # Attempt to retrieve job listings from the database
        joblist = JOBSLISTING.objects.all()  # Ensure this is correct for your model

        # Check if any jobs were foundx
        if not joblist:
            return Response({"status": 404, "message": "No jobs found."})

        # Serialize the job listings
        serializer = jobserializer(joblist, many=True)
        return Response({"status": 200, "jobs": serializer.data})

    except Exception as e:
        return Response({"status": 500, "message": str(e)})