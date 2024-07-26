from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


# Create your views here.



class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    
    def perform_create(self, seriazlier):
        if seriazlier.is_valid():
            seriazlier.save(author=self.request.user)
        else:
            print(seriazlier.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class =NoteSerializer
    permission_classes = [IsAuthenticated]
    
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)






class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]