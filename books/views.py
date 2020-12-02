from rest_framework.generics import ListAPIView, CreateAPIView, \
    RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ViewSet, ModelViewSet

from core.models import Books
from .serializers import BookSerializer


class BookPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class BookList(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination


class BookCreate(CreateAPIView):
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class BookRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    lookup_field = 'id'
    serializer_class = BookSerializer

    def delete(self, request, *args, **kwargs):
        book_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('book_data_{}'.format(book_id))
        return response

    def partial_update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 201:
            from django.core.cache import cache
            book = response.data
            cache.set('book_data_{}'.format(book['id']), {
                'book_name': book['book_name'],
                'author': book['author'],
                'publish_date': book['publish_date'],
                'desc': book['desc'],
            })
        return response


class BookViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer

