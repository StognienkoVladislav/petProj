
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate, login
from .models import Order
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from django.views.generic import View
from django.urls import reverse_lazy
from .forms import UserForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def OrderList(request):
    if request.method == 'GET':
        snippets = Order.objects.all()
        serializer = OrderSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def OrderDetail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = OrderSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrderSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


class IndexView(generic.ListView):
    template_name = 'orders/index.html'
    #context_object_name = 'all_albums'

    def get_queryset(self):
        return Order.objects.all()


class DetailView(generic.DetailView):
    model = Order
    template_name = 'orders/detail.html'


class OrderCreate(CreateView):
    model = Order
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class OrderUpdate(UpdateView):
    model = Order
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:index')

class UserFormView(View):

    form_class = UserForm
    template_name = 'orders/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit = False)

            #cleaned (normalized) data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns User objects if credentials are correct

            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('orders:index')

        return render(request, self.template_name, {'form' : form})