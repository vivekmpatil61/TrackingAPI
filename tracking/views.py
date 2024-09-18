from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
import uuid
from .utils import TrackingNumberRequestSerializer

def tracking_form(request):
    return render(request, 'tracking/tracking.html')

@api_view(['GET'])
@permission_classes([AllowAny])
def generate_tracking_number(request):
    try:
        # Print query parameters for debugging
        print(f"Query Parameters: {request.query_params}")

        serializer = TrackingNumberRequestSerializer(data=request.query_params)
        if serializer.is_valid():
            tracking_number = str(uuid.uuid4()).replace('-', '').upper()[:12]
            return Response({'tracking_number': tracking_number}, status=status.HTTP_200_OK)
        
        # Log validation errors
        print(f"Validation Errors: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(f"Error generating tracking number: {e}")
        return Response({"detail": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
