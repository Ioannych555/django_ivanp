from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
#    path('', views.index, name='quality_control'),
#    path('bugs/', views.bug_list, name='bug_list'),
#    path('bugs/add_bug/', views.create_bug, name='create_bug'),
#    path('bugs/<bug_id>/', views.bug_detail, name='bug_detail'),
#     path('bugs/<bug_id>/update/', views.update_bug, name='update_bug'),
#     path('bugs/<bug_id>/delete/', views.delete_bug, name='delete_bug'),
#
#    path('features/', views.feature_list, name='feature_list'),
#    path('features/add_feature/', views.create_feature, name='create_feature'),
#    path('features/<feature_id>/', views.feature_id_detail, name='feature_id_detail'),
#     path('features/<feature_id>/update/', views.update_feature, name='update_feature'),
#     path('features/<feature_id>/delete/', views.delete_feature, name='delete_feature'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugListView.as_view(), name='bug_list'),
    path('bugs/add_bug/', views.BugCreateView.as_view(), name='create_bug'),
    path('bugs/<bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('bugs/<bug_id>/update/', views.BugUpdateView.as_view(), name='update_bug'),
    path('bugs/<bug_id>/delete/', views.BugDeleteView.as_view(), name='delete_bug'),
    path('features/', views.FeatureRequestListView.as_view(), name='feature_list'),
    path('features/add_feature/', views.FeatureCreateView.as_view(), name='create_feature'),
    path('features/<feature_id>/', views.FeatureRequestDetailView.as_view(), name='feature_id_detail'),
    path('features/<feature_id>/update/', views.FeatureUpdateView.as_view(), name='update_feature'),
    path('features/<feature_id>/delete/', views.FeatureDeleteView.as_view(), name='delete_feature'),
]
