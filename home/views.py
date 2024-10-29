from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import jobserializer  # Ensure this serializer is correctly implemented

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

@api_view(['POST'])
def post_job(request):
    try:
        # Use request.POST to access form data
        data = request.POST
        print("Parsed data:", data)

        serializer = jobserializer(data=data)
        if serializer.is_valid():
            serializer.save()  # Save the data if valid
            return Response({
                "response": 200,
                "message": "Success"
            })
        else:
            return Response({
                "status": 400,
                "message": "Invalid data",
                "errors": serializer.errors
            })
    except Exception as e:
        print(e)
        return Response({
            "status": 500,
            "message": "An error occurred: " + str(e)
        })