import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


@method_decorator(csrf_exempt, name='dispatch')
class CatListCreateView(View):

    def get(self, request):
        categories = Category.objects.all()
        response = []
        for cat in categories:
            response.append({'id': cat.pk, 'name': cat.name})
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        cat = Category.objects.create(**data)
        return JsonResponse({'id': cat.pk}, safe=False)



class CatDetailView(DetailView):
    model = Category

    def get(self, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.pk, 'name': cat.name}, safe=False)