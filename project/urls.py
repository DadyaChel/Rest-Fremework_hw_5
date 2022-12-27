from django.contrib import admin
from django.urls import path, include
from Course import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('course', views.CourseViewSet)
# router.register('student', views.StudentViewSet)
# router.register('mentor', views.MentorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # path('api/course/', views.CourseListCreateAPIView.as_view()),
    # path('api/course/<int:pk>/', views.CourseRetrieveUpdateDestroyAPIView.as_view()),

    # path('api/student/', views.StudentListCreateAPIView.as_view()),
    # path('api/student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),

    path('api/student/', views.StudentCreateListView.as_view()),
    path('api/student/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view()),

    path('api/mentor/', views.MentorListCreateAPIView.as_view()),
    path('api/mentor/<int:pk>/', views.MentorRetrieveUpdateDestroyAPIView.as_view()),

    # path('api/v-1/course/', views.CourseFrankensteinViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # path('api/v-1/course/<int:pk>/', views.CourseFrankensteinViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    #
    # path('api/v-1/student/', views.StudentFrankensteinViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # })),
    # path('api/v-1/student/<int:pk>/', views.StudentFrankensteinViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),

    path('api/v-1/mentor/', views.MentorFrankensteinViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/v-1/mentor/<int:pk>/', views.MentorFrankensteinViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]
