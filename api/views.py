from urllib import request
from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import UpdateView
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.models import CustomUser
from author.models import Author
from book.models import Book
from order.models import Order
from .serializers import *  # AuthorSerializer, UserSerializer


# USER = get_user_model()

# class VIEWS FOR USER (authentication) API
# class CustomUserView(generics.CreateAPIView):
#     model = USER
#     queryset = CustomUser.get_all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


# class VIEWS FOR AUTHOR API
class AuthorListCreateView(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.get_all()
    # permission_classes = (IsAdminUser,)


class AuthorListDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.get_all()
    # permission_classes = (AllowAny,)


class AuthorAPIDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.get_all()
    # permission_classes = (IsAdminUser,)
    messages = 'success deleted'


# ALL BOOK Views

# class BookAPIView(generics.ListCreateAPIView, mixins.ListModelMixin,
#                   mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                   mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     queryset = Book.objects.all()
#     lookup_field = 'id'
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
#     serializer_class = BookSerializer
#     def get(self, request, id = None):
#         if id: return self.retrieve(request)
#         else: return self.list(request)
#     def post(self, request, *args, **kwargs):
#         return self.create(request)
#     def put(self,request, id =None):
#         return self.update(request, id)
#     def delete(self,request, id):
#         return self.destroy(request, id)


class BookAPIView(APIView):
    # class BookAPIView(generics.ListCreateAPIView):
    #     # permission_classes = (IsAuthenticated,)
    #     # authentication_classes = (TokenAuthentication,)
    queryset = Book.objects.all().values()

    def get(self, request, id=None):
        if id:
            book = Book.get_by_id(id)
            return Response({'one book from GET': BookSerializer(book).data})
        else:
            lst = Book.objects.all()
            return Response({'all books from GET': BookSerializer(lst, many=True).data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

        # book_new = Book.objects.create(
        #     name=request.data['name'],
        #     description=request.data['description'],
        #     count=request.data['count'],
        #     authors=request.data['authors'])
        # return Response({'post': BookSerializer(book_new).data})

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({'error': "method PUT not allowed here, no ID"})
        try:
            book_to_update = Book.get_by_id(id)
        except:
            return Response({'error': "method PUT, Book not Found"})
        serializer = BookSerializer(data=request.data, instance=book_to_update)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({'error': "method DELETE not allowed here, no ID"})
        try:
            book_to_delete = Book.get_by_id(id)
        except:
            return Response({'error': "method DELETE, Book not Found"})
        book_to_delete.delete()
        return Response({"post": "Delete book id = " + str(id)})


# class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = [IsAuthenticated, IsLibrarian]
#     serializer_class = BookSerializer
#     queryset = Book.get_all()


# ORDER VIEWS HERE:

class OrderViewSet(viewsets.ModelViewSet):
    ''' only for single orders'''
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def get(self, request, pk): Працює без цього добре
    #     order= get_list_or_404(Order, pk=pk)
    #     data = OrderSerializer(order).data
    #     return Response(data, status=status.HTTP_200_OK)


class UserOrderView(viewsets.ModelViewSet):
    """ for user.id + order.id"""
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.kwargs['user_id']
        order = self.kwargs['order_id']
        print('usr', user, 'ORDER', order)
        return Order.objects.filter(user_id=user, id=order)

# class OrderViewSet(viewsets.ViewSet):
#     def list(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk =None):
#         queryset = Order.objects.all()
#         order = get_object_or_404(queryset, pk= pk)
#         serializer = OrderSerializer(order)
#         return Response(serializer.data)
