from django.shortcuts import render
from rest_framework import viewsets, generics

from Course.models import Mentor, Student, Course
from Course.my_generics import ListMixinAPI, CreateMixinAPI, MyAPIView, RetrieveMixinAPI, DeleteMixinAPI, UpdateMixinAPI
from Course.serializers import MentorSerializer, StudentSerializer, CourseSerializer


# class MentorViewSet(viewsets.ModelViewSet):
#     queryset = Mentor.objects.all()
#     serializer_class = MentorSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class StudentCreateListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# class CourseListCreateAPIView(ListMixinAPI, CreateMixinAPI, MyAPIView):
#     serializer_class = CourseSerializer
#     model = Course
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class CourseRetrieveUpdateDestroyAPIView(RetrieveMixinAPI,
#                                           DeleteMixinAPI,
#                                           UpdateMixinAPI,
#                                           MyAPIView):
#     serializer_class = CourseSerializer
#     model = Course
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# class CourseFrankensteinViewSet(ListMixinAPI, CreateMixinAPI, UpdateMixinAPI, DeleteMixinAPI, viewsets.ViewSetMixin, MyAPIView):
#     serializer_class = CourseSerializer
#     model = Course
#     queryset = Course.objects.all()
#
#
# class StudentListCreateAPIView(ListMixinAPI, CreateMixinAPI, MyAPIView):
#     serializer_class = StudentSerializer
#     model = Student
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class StudentRetrieveUpdateDestroyAPIView(RetrieveMixinAPI,
#                                           DeleteMixinAPI,
#                                           UpdateMixinAPI,
#                                           MyAPIView):
#     serializer_class = StudentSerializer
#     model = Student
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#
# class StudentFrankensteinViewSet(ListMixinAPI, CreateMixinAPI,
#                                  UpdateMixinAPI, DeleteMixinAPI,
#                                  viewsets.ViewSetMixin, MyAPIView):
#     serializer_class = StudentSerializer
#     model = Student
#     queryset = Student.objects.all()


class MentorListCreateAPIView(ListMixinAPI, CreateMixinAPI, MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MentorRetrieveUpdateDestroyAPIView(RetrieveMixinAPI,
                                          DeleteMixinAPI,
                                          UpdateMixinAPI,
                                          MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MentorFrankensteinViewSet(ListMixinAPI, CreateMixinAPI, UpdateMixinAPI, DeleteMixinAPI, RetrieveMixinAPI,
                                viewsets.ViewSetMixin, MyAPIView):
    serializer_class = MentorSerializer
    model = Mentor
    queryset = Mentor.objects.all()
