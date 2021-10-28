from rest_framework.pagination import PageNumberPagination

class ComponentPagination(PageNumberPagination):
    page_size = 4