from django.urls import path
from .views import dashboard_main_view, dashboard_community_view, dashboard_chatbot_view, dashboard_faq_view, \
    dashboard_subscription_view

urlpatterns = [
    path('', dashboard_main_view, name='dashboard-main'),
    path('community/', dashboard_community_view, name='dashboard-community'),
    path('chatbot/', dashboard_chatbot_view, name='dashboard-chatbot'),
    path('faq/', dashboard_faq_view, name='dashboard-faq'),
    path('manage-subscribtion/', dashboard_subscription_view, name='dashboard-subscription'),

]
