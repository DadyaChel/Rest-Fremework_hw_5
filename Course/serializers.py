from rest_framework import serializers

from .models import Course, Student, Mentor


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = "__all__"


# class MentorSerializer(serializers.Serializer):
#     FIO = serializers.CharField(max_length=99)
#     work_experience = serializers.IntegerField()
#
#     def create(self, validated_data):
#         mentor = Mentor.objects.create(
#             FIO=validated_data['FIO'],
#             work_experience=validated_data['work_experience']
#         )
#         return mentor
#
#     def update(self, instance, validated_data):
#         instance.FIO = validated_data['FIO']
#         instance.work_experience = validated_data['work_experience']
#         instance.save()
#         return instance


# class StudentSerializer(serializers.Serializer):
#     FIO = serializers.CharField(max_length=99)
#     date_birth = serializers.DateField()
#
#     def create(self, validated_data):
#         student = Student.objects.create(
#             FIO=validated_data['FIO'],
#             date_birth=validated_data['date_birth']
#         )
#         return student
#
#     def update(self, instance, validated_data):
#         instance.FIO = validated_data['FIO']
#         instance.birth_date = validated_data['birth_date']
#         instance.save()
#         return instance


# class CourseSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=99)
#     course_duration = serializers.IntegerField()
#     student_id = serializers.IntegerField()
#     mentor_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         course = Course.objects.create(
#             name=validated_data['name'],
#             course_duration=validated_data['course_duration'],
#             student_id=validated_data['student_id'],
#             mentor_id=validated_data['mentor_id']
#         )
#         return course
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data['name']
#         instance.course_duration = validated_data['course_duration']
#         instance.student = validated_data['student']
#         instance.mentor = validated_data['mentor']
#         instance.save()
#         return instance