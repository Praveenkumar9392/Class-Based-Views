from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('chatoptions',ChatOptionViewset,basename='chatoptions')
router.register('chatmessages',ChatOptionMessageViewset,basename='chatmessages')
router.register('welcome_mesaasge',welcomeViewset,basename='welcome_mesaasge')
router.register('queryleads',ChatQueryViewset,basename='queryleads')
router.register('chatlogo',chatLogoViewset,basename='chatlogo')

urlpatterns = [
    path('',include(router.urls)),
    path('chat/',chat,name='chat'),
    path('update_chatbot_message/',update_chatbot_message,name='update_chatbot_message'),
    path('copy-paste/',copy_chat_option,name='copy-paste')
]