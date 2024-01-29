from rest_framework.exceptions import APIException
from rest_framework import status
class Server_Error(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'some thing is wrong! please try later'