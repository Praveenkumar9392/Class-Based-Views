from django.shortcuts import render
from .models import *
from rest_framework import viewsets,status
from rest_framework.response import Response
from message_framework.serializers import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 10000

class welcomeViewset(viewsets.ModelViewSet):
    queryset = welcomemessage.objects.all()
    serializer_class = WelcomeMessageSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.request.method  != 'GET':
            return CreateWelcomeMessageSerializer
        return WelcomeMessageSerializer

class ChatOptionViewset(viewsets.ModelViewSet):
    queryset = ChatOption.objects.all()
    serializer_class = ChatOptionSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['parent', 'is_exit_option','is_root','title']
                
    def get_serializer_class(self):
        if self.request.method  != 'GET':
            return CreateChatOptionSerializer
        return ChatOptionSerializer
   
    def create(self, request):
        title = request.data.get("title")
        value = request.data.get("value")
        parent_id = request.data.get("parent")
        is_exit_option = request.data.get("is_exit_option")
        messages_data = request.data.get('messages', [])
        is_root = request.data.get("is_root")
        parent = None
        if parent_id is not None:
            try:
                parent = ChatOption.objects.get(id=parent_id)
            except ChatOption.DoesNotExist:
                return Response({"error": "Parent ChatOption does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        chat_option = ChatOption.objects.create(title=title,value=value,parent=parent,is_exit_option=is_exit_option,is_root=is_root)
        messages_list = []
        if isinstance(messages_data, list):
            for message_data in messages_data:
                if 'message' in message_data:
                    chat_message = ChatOptionMessage.objects.create(chat_option=chat_option, **message_data)
                    messages_list.append({"message": chat_message.message})
        return Response({"id": chat_option.id, "title": chat_option.title,"value":chat_option.value,"messages":messages_list}, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        child_options = ChatOption.objects.filter(parent=instance)
        if child_options.exists():
            return Response({"error": "Delete associated ChildOption records first before deleting the ParentOption."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        ChatOptionMessage.objects.filter(chat_option=instance).delete()
        self.perform_destroy(instance)
        return Response({"message": "ChatOption and associated messages deleted successfully."}, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)
        is_root_param = self.request.query_params.get('is_root', None)
        if is_root_param is not None:
            is_root = is_root_param.lower() == 'true'
            queryset = queryset.filter(is_root=is_root)
        parent_id = self.request.query_params.get('parent', None)
        if parent_id is not None:
            queryset = queryset.filter(parent=parent_id)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({'results':serializer.data})

class ChatOptionMessageViewset(viewsets.ModelViewSet):
    queryset = ChatOptionMessage.objects.all()
    serializer_class = ChatOptionMessageSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['chat_option','message']

    def get_serializer_class(self):
        if self.request.method  != 'GET':
            return CreateChatOptionMessageSerializer
        return ChatOptionMessageSerializer
    
class ChatQueryViewset(viewsets.ModelViewSet):
    queryset = ChatQueryLeads.objects.all()
    serializer_class = ChatQueryLeadsSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status','name']

    def get_serializer_class(self):
        if self.request.method  != 'GET':
            return CreateChatQueryLeadsSerializer
        return ChatQueryLeadsSerializer
    
@api_view(['PATCH'])
def update_chatbot_message(request, *args, **kwargs,):
    chat_option_id = request.data.get('chat_optionid')
    title = request.data.get("title")
    messages_data = request.data.get('messages', [])
    try:
        chat_option = ChatOption.objects.get(id=chat_option_id)
        if chat_option and title:
            chat_option.title=title
            chat_option.save()
        chat_messages = list(ChatOptionMessage.objects.filter(chat_option=chat_option))
        for index, message_data in enumerate(messages_data):
            if index < len(chat_messages):
                chat_message = chat_messages[index]
                chat_message.message = message_data
                chat_message.save()
            else:
                ChatOptionMessage.objects.create(
                    chat_option=chat_option,
                    message=message_data
                )
        if len(messages_data) < len(chat_messages):
            extra_messages = chat_messages[len(messages_data):]
            for extra_message in extra_messages:
                extra_message.delete()
        return Response({"success": "Messages updated successfully."}, status=200)
    except ChatOption.DoesNotExist:
        return Response({"error": "Chat option not found."}, status=404)


@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def chat(request):
    user_input = request.data.get('selected_value')
    description = request.data.get('description')
    ipaddress = request.data.get('ipaddress')
    browser_type = request.data.get("browser_type")

    chat_query, created = ChatQueryLeads.objects.get_or_create(ipaddress=ipaddress,browser_type=browser_type,status='Inprogress')
    if not user_input:
        try:
            obj = welcomemessage.objects.get(id=1)
        except welcomemessage.DoesNotExist:
            return Response({'message': 'Welcome message not found.'}, status=status.HTTP_404_NOT_FOUND)

        welcome_message = {'message': obj.message}
        next_message = {
            'message': 'Which city are you from?',
            'content_attributes': {
                'items': [
                    {'title': 'Hyderabad', 'value': '/hyderabad'},
                    {'title': 'Bangalore', 'value': '/bangalore'},
                    {'title': 'Chennai', 'value': '/chennai'},
                    {'title': 'Mumbai', 'value': '/mumbai'},
                    {'title': 'Other', 'value': '/other'}
                ]
            }
        }
        return Response({'welcome_message': welcome_message,'next_message': next_message}, status=status.HTTP_200_OK)
    
    if user_input in ['/hyderabad', '/bangalore', '/chennai', '/mumbai']:
        chat_query.location = user_input.lstrip('/').capitalize()
        chat_query.save()
    if user_input in ['/hyderabad', '/bangalore', '/chennai', '/mumbai', '/back']:
        top_level_options = ChatOption.objects.filter(parent__isnull=True)
        next_message = [{
            'message': 'Which service are you looking for?',
            'content_attributes': {
                'items': [{'id': option.id, 'title': option.title, 'value': option.value} for option in top_level_options]
            }
        }]
        return Response({'content': next_message}, status=status.HTTP_200_OK)

    elif user_input == "/other" and not description:
        next_message = [{'message': 'Please provide the location','title':'/other','input_type': "text"}]
        return Response({'content': next_message}, status=status.HTTP_200_OK)
    
    if user_input == '/other' and description:
        chat_query.location = description 
        chat_query.save()
        top_level_options = ChatOption.objects.filter(parent__isnull=True)
        next_message = {
            'message': 'Which service are you looking for?',
            'content_attributes': {
                'items': [{'id': option.id, 'title': option.title, 'value': option.value} for option in top_level_options]
            }
        }
        return Response({'next_message': [next_message]}, status=status.HTTP_200_OK)

    selected_option = ChatOption.objects.filter(value=user_input).first()
    if selected_option and user_input == '/others':
        if selected_option.value == user_input:
            response_messages = []
            option_messages = ChatOptionMessage.objects.filter(chat_option=selected_option)
            for message in option_messages:
                response_messages.append({'message': message.message,'title':'/service','input_type': "text"})
            return Response({'content': response_messages}, status=status.HTTP_200_OK)
    if selected_option:
        if not chat_query.service:
            chat_query.service = selected_option.title
            chat_query.save()
    if user_input == '/service' and description:
            chat_query.service = description
            chat_query.save()
            next_message=[]
            next_message.append({'message': "Please enter the domain.",'title': '/domain','input_type': "text"})
            return Response({'next_message': next_message,}, status=status.HTTP_200_OK)
    if user_input == '/domain' and description:
        chat_query.service_domain = description  
        chat_query.save()
        next_message=[]
        next_message.append({'message': 'To assist you better, could you please share a few details'})
        next_message.append({'message': "Please enter your name.",'title': '/name','input_type': "text"})
        return Response({'next_message': next_message,}, status=status.HTTP_200_OK)

    option_messages = ChatOptionMessage.objects.filter(chat_option=selected_option)
    
    response_messages = []

    for message in option_messages:
        sub_options = selected_option.sub_options.all()
        if sub_options:
            response_messages.append({
                'message': message.message,
                'content_attributes': {
                    'items': [
                        {
                            'id': option.id,
                            'title': option.title,
                            'value': option.value,
                            'parent': {
                                'id': option.parent.id,  
                                'title': option.parent.title,
                                'value': option.parent.value
                            } if option.parent else None 
                        } 
                        for option in sub_options
                    ]
                },
            })

    if selected_option is not None:
        sub_options = selected_option.sub_options.all()
        if not sub_options:
            selected_option_title = selected_option.title
            for message in option_messages:
                chat_query.service_domain = selected_option_title
                chat_query.save()
                response_messages.append({'message': message.message})
            response_messages.append({'message': "Please enter your name.", 'title': '/name','is_back': '/back', 'input_type': "text"})

    if user_input.startswith('/name'):
        chat_query.name = description 
        chat_query.save() 
        next_message=[]
        next_message.append({'message':f"{description}. Please enter your email.",'title': '/email','input_type':"text"})
        return Response({'next_message': next_message,}, status=status.HTTP_200_OK)

    elif user_input.startswith('/email'):
        email_validator = EmailValidator()
        try:
            email_validator(description)
        except ValidationError:
            next_message = [{'message': "Please enter a valid email address",'title': '/email','input_type':"text"}]
            return Response({'next_message': next_message}, status=status.HTTP_200_OK)
        chat_query.email = description 
        chat_query.save()
        next_message = [{'message': "Got it. Now, please enter your mobile number.", 'title': '/mobile','input_type':"number"}]
        return Response({'next_message': next_message}, status=status.HTTP_200_OK)

    elif user_input.startswith('/mobile'):
        chat_query.mobileno = description  
        chat_query.status = "Completed" 
        chat_query.save()
        next_message=[]
        next_message.append({'message':"Thank you! Our team will call you shortly."})
        return Response({'next_message': next_message,}, status=status.HTTP_200_OK)

    return Response({'content': response_messages,}, status=status.HTTP_200_OK)

def copy_option_with_children(original_option, new_parent=None, is_root_flag=True):
    is_root = is_root_flag and new_parent is None
    new_option = ChatOption.objects.create(title=original_option.title,value=original_option.value,parent=new_parent,is_root=is_root,is_exit_option=original_option.is_exit_option)
    for message in original_option.messages.all():
        ChatOptionMessage.objects.create(chat_option=new_option,message=message.message)
    for child in original_option.sub_options.all():
        copy_option_with_children(child, new_option, is_root_flag=False)
    return new_option

@api_view(['POST'])
def copy_chat_option(request):
    chat_option_id = request.data.get("chat_option_id")
    paste_option_id = request.data.get("paste_option_id", None)
    if chat_option_id == paste_option_id:
        return Response({'error': 'Cannot copy and paste the same option'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        original_option = ChatOption.objects.get(id=chat_option_id)
        paste_option_obj = None
        if paste_option_id:
            paste_option_obj = ChatOption.objects.get(id=paste_option_id)
        new_option = copy_option_with_children(original_option, paste_option_obj, is_root_flag=(paste_option_id is None))
        serializer = ChatOptionSerializer(new_option)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except ChatOption.DoesNotExist:
        return Response({'error': 'ChatOption not found'}, status=status.HTTP_404_NOT_FOUND)
    
class chatLogoViewset(viewsets.ModelViewSet):
    queryset = chatLogo.objects.all()
    serializer_class = chatLogoSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title','sub_title']

    def get_serializer_class(self):
        if self.request.method  != 'GET':
            return CreatechatLogoSerializer
        return chatLogoSerializer