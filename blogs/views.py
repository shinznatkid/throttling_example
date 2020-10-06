from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.decorators import throttle_classes


class BlogList(APIView):
    """
    Dummy List
    """

    def get(self, request, format=None):
        return Response([])


# class BlogList(APIView):
#     """
#     Dummy List
#     """
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]

#     def get(self, request, format=None):
#         return Response([])


# @throttle_classes([AnonRateThrottle, UserRateThrottle])
# class BlogList(APIView):
#     """
#     Dummy List
#     """
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]

#     def get(self, request, format=None):
#         return Response([])


# class BlogList(APIView):
#     """
#     Dummy List
#     """
#     throttle_scope = 'blogs'

#     def get(self, request, format=None):
#         return Response([])
