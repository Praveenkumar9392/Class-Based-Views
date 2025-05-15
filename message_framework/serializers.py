from .models import *
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title','is_suspended', 'description', 'category', 'priority', 'status', 'created_by', 'assigned_to', 'created_at', 'updated_at']
        depth = 1

class CreateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'title','is_suspended', 'description', 'category', 'priority', 'status', 'created_by', 'assigned_to', 'created_at', 'updated_at']

class ChatRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRecord
        fields = '__all__'
        depth = 1

class CreateChatRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRecord
        fields = '__all__'

class ChatOptionMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatOptionMessage
        fields = ['id', 'chat_option', 'message']

class CreateChatOptionMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatOptionMessage
        fields = '__all__'


class ChatOptionSerializer(serializers.ModelSerializer):
    messages = ChatOptionMessageSerializer(many=True, read_only=True)
    class Meta:
        model = ChatOption
        fields = ['id', 'title', 'value', 'parent','is_exit_option','is_root','messages'] 

class CreateChatOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatOption
        fields = '__all__' 

class WelcomeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = welcomemessage
        fields = '__all__'

class CreateWelcomeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = welcomemessage
        fields = '__all__'

class ChatQueryLeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatQueryLeads
        fields = '__all__'

class CreateChatQueryLeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatQueryLeads
        fields = '__all__'

class chatLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatLogo
        fields = '__all__'

class CreatechatLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatLogo
        fields = '__all__'

