from rest_framework import PageNumberPagination

class CommentPagination(PageNumberPagination):
    page_size = 4