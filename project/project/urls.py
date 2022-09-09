from django.contrib import admin
from django.urls import path
from stripeAPI.views import (
    CreateCheckoutSessionView, 
    ProductLandingPageView, 
    SuccessView,
    CancelView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item/<pk>/', ProductLandingPageView.as_view(), name='landing-page'),
    path('buy/<pk>/', CreateCheckoutSessionView.as_view(), name='buy')
]