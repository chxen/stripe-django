import stripe
import environ
from django.views.generic import TemplateView
from django.views import View
from django.http import JsonResponse
from rest_framework import generics
from .models import Item


env = environ.Env()
environ.Env.read_env()
stripe.api_key = env("STRIPE_SECRET_KEY")

class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"

class ProductLandingPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        context = super(ProductLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "item": item,
            "STRIPE_PUBLIC_KEY": env("STRIPE_PUBLIC_KEY"),
        })
        return context

class CreateCheckoutSessionView(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                        'description': item.description,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=env("YOUR_DOMAIN") + '/success/',
            cancel_url=env("YOUR_DOMAIN") + '/cancel/',
        )
        return JsonResponse({
            'id': session.id
        })
