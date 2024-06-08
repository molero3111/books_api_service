from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response


def get_delete_response(delete_request):
    object_to_delete = delete_request.get_object()  # gets the object to delete instance, the model itself
    serialized_object = (delete_request.serializer_class(
        object_to_delete
    ).data)  # extracts and serializes to json the model data before it is deleted
    if not serialized_object:
        return Response(
            {
                "message": "Data not found.",
                "deleted_user": serialized_object
            },
            status=HTTP_404_NOT_FOUND
        )
    object_to_delete.delete()
    return Response(
        {
            "message": "Data deleted successfully.",
            "data": serialized_object
        },
        status=HTTP_200_OK
    )


def validate_auth_header_format(request):
    authorization_header = request.headers.get('Authorization')
    if not authorization_header:
        return {
            "is_valid": False,
            "response": Response({'error': 'Authorization header is missing'}, status=400)
        }
    # Check if the header starts with 'Bearer '
    if not authorization_header.startswith('Bearer '):
        return {
            "is_valid": False,
            "response": Response({'error': 'Invalid token format'}, status=400)
        }
    return {"is_valid": True,
            "header": authorization_header
            }
