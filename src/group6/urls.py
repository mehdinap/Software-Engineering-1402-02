from django.urls import path

from .views import FAQChildrenView, FAQRootsView

urlpatterns = [
    path('faq/<int:parent_id>/children/', FAQChildrenView.as_view(), name='faq-children'),
    path('faq/roots/', FAQRootsView.as_view(), name='faq-roots'),
]
