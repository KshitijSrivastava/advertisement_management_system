from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

app_name ='blog'

urlpatterns = [
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('signup/',views.SignUp.as_view(template_name="blog/signup.html"),name='signup'),
    path('',views.PostListView.as_view(),name='post_list'),
    path('new/',views.CreateView.as_view(),name='post_view'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/comment/',views.add_comment_to_post,name='add_comment_to_post'),
    path('dashboard/',views.PostReviewerListView.as_view(), name = 'dashboard'),
    # path('post/<int:pk>/<str:email>/accept/', views.AcceptView.as_view(), name = 'accept'),
    # path('post/<int:pk>/<str:email>/reject/', views.RejectView.as_view(), name = 'reject'),
    path('post/rejected/',views.PostRejectedListView.as_view(), name = 'rejected_post'),
    path('post/<int:pk>/delete/>',views.PostDelete.as_view(),name='delete_post'),

]
