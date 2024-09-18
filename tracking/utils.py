# tracking/utils.py
import uuid
import redis
import uuid
from django.conf import settings
from rest_framework import serializers
from datetime import datetime
from django.core.exceptions import ValidationError
from datetime import datetime
import pytz

def validate_date(value):
    try:
        datetime.fromisoformat(value)
    except ValueError:
        raise ValidationError("Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z].")

class RFC3339DateTimeField(serializers.DateTimeField):
    def to_internal_value(self, value):
        try:
            # Parse the RFC 3339 formatted string into a datetime object
            parsed_date = datetime.fromisoformat(value)
            
            # Ensure it's timezone-aware
            if parsed_date.tzinfo is None:
                # If it's naive (i.e., no timezone info), convert it to UTC
                parsed_date = pytz.utc.localize(parsed_date)
                
            return parsed_date
        except ValueError:
            raise serializers.ValidationError(
                "Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
            )

    def to_representation(self, value):
        if value is None:
            return None
        # Format datetime object to RFC 3339 string
        return value.isoformat()
# Use the custom field in your serializer
class TrackingNumberRequestSerializer(serializers.Serializer):
    origin_country_id = serializers.CharField(max_length=2)
    destination_country_id = serializers.CharField(max_length=2)
    weight = serializers.DecimalField(max_digits=10, decimal_places=3)
    created_at = RFC3339DateTimeField()  # Custom RFC 3339 field
    customer_id = serializers.UUIDField()
    customer_name = serializers.CharField(max_length=255)
    customer_slug = serializers.SlugField(max_length=255)

def generate_unique_tracking_number():
    return str(uuid.uuid4()).replace('-', '').upper()[:10]


# Set up Redis connection
redis_client = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)

def generate_unique_tracking_number():
    return str(uuid.uuid4()).replace('-', '').upper()[:10]

def generate_and_store_tracking_number():
    lock = redis_client.lock("tracking_number_lock", timeout=5)

    # Acquire the lock
    with lock:
        # Generate the tracking number
        tracking_number = generate_unique_tracking_number()

        # Save to database (can be moved to the view)
        from .models import Parcel  # Import inside the function to avoid circular import issues
        parcel = Parcel.objects.create(tracking_number=tracking_number)
    
    return tracking_number
