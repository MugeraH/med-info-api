from django.urls import path
from .views import IllnessListView,IllnessDetailView,IllnessSearchDetailView,DrugListView,DrugDetailView,DrugSearchDetailView,PostReplyDetailView,PostListView,PostDetailView,ReplyListView,ReplyDetailView,UserPostsView


from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

path('illness',IllnessListView.as_view(),name="illness-list"),  
path('illness/<int:pk>',IllnessDetailView.as_view(),name="illness-detail"),  
path('illness/<str:search_term>',IllnessSearchDetailView.as_view(),name="searched-illness"), 

path('drug',DrugListView.as_view(),name="drug-list"),  
path('drug/<int:pk>',DrugDetailView.as_view(),name="drug-detail"),  
path('drug/<str:search_term>',DrugSearchDetailView.as_view(),name="searched-drug"), 

path('post',PostListView.as_view(),name="post-list"),  
path('post/<int:pk>',PostDetailView.as_view(),name="post-detail"), 
path('post/user/<int:id>',UserPostsView.as_view(),name="user-post-detail"), 

path('reply',ReplyListView.as_view(),name="reply-list"),  
path('reply/<int:pk>',ReplyDetailView.as_view(),name="reply-detail"), 
path('post/reply/<int:id>',PostReplyDetailView.as_view(),name="post-reply-detail"), 


]

urlpatterns = format_suffix_patterns(urlpatterns)
