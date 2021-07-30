from django.shortcuts import render
from django.http import Http404

# third party imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status

from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated


from .models import Illness,Drug,Post,Reply
from .serializers import PostSerializer,IllnessSerializer,DrugSerializer,ReplySerializer


class IllnessListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = IllnessSerializer
    queryset = Illness.objects.all()
    
    def get(self,request,*args,**kwargs): 
        return self.list(self,request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs): 
        return self.create(request,*args,**kwargs)
    
    
class IllnessDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class = IllnessSerializer
    queryset = Illness.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class IllnessSearchDetailView(APIView):
    def get(self,request,search_term):
        illnesses = Illness.search_illness_by_search_term(search_term)
        serializer = IllnessSerializer(illnesses, many=True)
        return Response(serializer.data)
    
    
    
    
class DrugListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()
    
    def get(self,request,*args,**kwargs): 
        return self.list(self,request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs): 
        return self.create(request,*args,**kwargs)
    
    
class DrugDetailView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class DrugSearchDetailView(APIView):
    def get(self,request,search_term):
        drugs = Drug.search_drug_by_search_term(search_term)
        serializer = DrugSerializer(drugs, many=True)
        return Response(serializer.data)
    
class PostListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class =  PostSerializer
    queryset = Post.objects.all()
    
    def get(self,request,*args,**kwargs): 
        return self.list(self,request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs): 
        return self.create(request,*args,**kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class PostDetailView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class =  PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class UserPostsView(APIView):
    def get(self,request,id):
        posts = Post.get_post_by_user_id(id)
        serializer = PostSerializer( posts, many=True)
        return Response(serializer.data)
    
class ReplyListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    serializer_class =  ReplySerializer
    queryset = Reply.objects.all()
    
    def get(self,request,*args,**kwargs): 
        return self.list(self,request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs): 
        return self.create(request,*args,**kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class ReplyDetailView(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    serializer_class =  ReplySerializer
    queryset = Reply.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class PostReplyDetailView(APIView):
    def get(self,request,id):
       replies = Reply.get_replies_by_post(id)
       serializer = ReplySerializer(replies, many=True)
       return Response(serializer.data)
