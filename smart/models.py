# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.timezone import now

class User_info(models.Model):
    Account = models.CharField(max_length=255, blank=True,null=True)
    Role = models.CharField(max_length=255, blank=True,null=True)
    Pwd = models.CharField(max_length=255, blank=True,null=True)
    Name = models.CharField(max_length=255, blank=True,null=True)
    Birthday = models.DateField(blank=True,null=True)
    Sex = models.NullBooleanField(blank=True, null=True)
    Tel = models.CharField(max_length=255, blank=True,null=True)
    IDCard = models.CharField(max_length=255, blank=True,null=True)
    Politics = models.IntegerField(blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Student_info(models.Model):
    StuID = models.CharField(max_length=255, blank=True,null=True)
    StuAccount = models.ForeignKey(User_info)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Teacher_info(models.Model):
    TeachID = models.CharField(max_length=255, blank=True,null=True)
    TeachAccount = models.ForeignKey(User_info)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Parent_info(models.Model):
    ParAccount = models.CharField(max_length=255, blank=True,null=True)
    StuID = models.ForeignKey(Student_info)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Class_info(models.Model):
    ClassID = models.CharField(max_length=255, blank=True,null=True)
    ClassName = models.CharField(max_length=255, blank=True,null=True)
    ChineseID = models.CharField(max_length=255, blank=True,null=True)
    MathID = models.CharField(max_length=255, blank=True,null=True)
    EnglishID = models.CharField(max_length=255, blank=True,null=True)
    PhysicsID = models.CharField(max_length=255, blank=True,null=True)
    ChemistryID = models.CharField(max_length=255, blank=True,null=True)
    BiologyID = models.CharField(max_length=255, blank=True,null=True)
    ScienceID = models.CharField(max_length=255, blank=True,null=True)
    SportID = models.CharField(max_length=255, blank=True,null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Class_stu(models.Model):
    ClassID = models.ForeignKey(Class_info)
    StuID = models.ForeignKey(Student_info)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Book(models.Model):
    BookID = models.CharField(max_length=255, blank=True,null=True)
    BookName = models.CharField(max_length=255, blank=True,null=True)
    Introduce = models.CharField(max_length=255, blank=True,null=True)
    Author = models.CharField(max_length=255, blank=True,null=True)
    PubDate = models.DateField(blank=True,null=True)
    Press = models.CharField(max_length=255, blank=True,null=True)
    Keywords = models.CharField(max_length=255, blank=True,null=True)
    InputTime = models.DateField(default=now().date())
    ReadNum = models.IntegerField(blank=True, null=True)
    Charges = models.FloatField(blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Course(models.Model):
    CourseID = models.CharField(max_length=255, blank=True,null=True)
    CourceName = models.CharField(max_length=255, blank=True,null=True)
    ClassID = models.ForeignKey(Class_info)
    TeachID = models.ForeignKey(Teacher_info)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Course_Chapter(models.Model):
    ChapterID = models.CharField(max_length=255, blank=True,null=True)
    CourseID = models.ForeignKey(Course)
    ChapterName = models.CharField(max_length=255, blank=True,null=True)
    ChapterContent = models.CharField(max_length=255, blank=True,null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Course_Knowledge(models.Model):
    KnowledgeID = models.CharField(max_length=255, blank=True,null=True)
    ChapterID = models.ForeignKey(Course_Chapter)
    KnowledgeName = models.CharField(max_length=255, blank=True,null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Online_Course(models.Model):
    OLCourseID = models.CharField(max_length=255, blank=True,null=True)
    OLCoursename = models.CharField(max_length=255, blank=True,null=True)
    Introduction = models.CharField(max_length=255, blank=True,null=True)
    Author = models.CharField(max_length=255, blank=True,null=True)
    PubTime = models.DateField(blank=True,null=True)
    InputTime = models.DateField(default=now().date(),blank=True,null=True)
    Statistics = models.IntegerField(blank=True, null=True)
    Charges = models.FloatField(blank=True, null=True)
    Admin = models.ForeignKey(User_info)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Online_Course_Knowledge(models.Model):
    KnownledgeID = models.CharField(max_length=255, blank=True,null=True)
    OLCourseID = models.ForeignKey(Online_Course)
    Name = models.CharField(max_length=255, blank=True,null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Topic(models.Model):
    TopicID = models.CharField(max_length=255, blank=True,null=True)
    Type = models.NullBooleanField(blank=True, null=True)
    Content = models.CharField(max_length=255, blank=True,null=True)
    InputDate = models.DateField(default=now().date(),blank=True,null=True)
    Options = models.CharField(max_length=255, blank=True,null=True)
    Reference = models.CharField(max_length=255, blank=True,null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Topic_Knowledge(models.Model):
    TopicID = models.ForeignKey(Topic)
    Knowledge = models.CharField(max_length=255, blank=True,null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Exam_info(models.Model):
    ExamID = models.CharField(max_length=255, blank=True,null=True)
    Type = models.IntegerField(blank=True, null=True)
    Name = models.CharField(max_length=255, blank=True,null=True)
    Description = models.CharField(max_length=255, blank=True,null=True)
    GroupNum = models.IntegerField(blank=True, null=True)
    CourseID = models.ForeignKey(Course)
    Creator = models.ForeignKey(User_info)
    CreateTime = models.DateTimeField(blank=True, null=True)
    StartTime = models.DateTimeField(blank=True, null=True)
    EndTime = models.DateTimeField(blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Exam_Student(models.Model):
    StuID = models.ForeignKey(Student_info)
    ExamID = models.ForeignKey(Exam_info)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Exam_topic(models.Model):
    ExamID = models.ForeignKey(Exam_info)
    TopicID = models.ForeignKey(Topic)
    GroupID = models.CharField(max_length=255, blank=True,null=True)
    MarkID = models.CharField(max_length=255, blank=True,null=True)
    Score = models.CharField(max_length=255, blank=True,null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Exam_Answer(models.Model):
    ExamID = models.ForeignKey(Exam_info)
    StuID = models.ForeignKey(Student_info)
    TopicID = models.ForeignKey(Topic)
    Answer = models.CharField(max_length=255, blank=True,null=True)
    Score = models.CharField(max_length=255, blank=True,null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Favorites(models.Model):
    StuID = models.ForeignKey(Student_info)
    Type = models.IntegerField(blank=True, null=True)
    OLCourseID = models.ForeignKey(Online_Course)
    BookID = models.ForeignKey(Book)
    Purchased = models.NullBooleanField(default=False)
    AddTime = models.DateTimeField(blank=True, null=True)
    StartTime = models.DateTimeField(blank=True, null=True)
    LatestTime = models.DateTimeField(blank=True, null=True)
    Progress = models.IntegerField(blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Wrong_topic(models.Model):
    StuID = models.ForeignKey(Student_info)
    ExamID = models.ForeignKey(Exam_info)
    TopicID = models.ForeignKey(Topic)
    Times = models.IntegerField(blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Payment(models.Model):
    PayID = models.CharField(max_length=255, blank=True,null=True)
    PayerID = models.CharField(max_length=255, blank=True,null=True)
    Description = models.CharField(max_length=255, blank=True,null=True)
    TransSubTime = models.DateTimeField(blank=True, null=True)
    PayTime = models.DateTimeField(blank=True, null=True)
    PayAmount = models.FloatField(blank=True, null=True)
    Status = models.CharField(max_length=255, blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Message_Info(models.Model):
    Tpye = models.IntegerField(blank=True, null=True)
    SenderID = models.CharField(max_length=255, blank=True,null=True)
    Content = models.CharField(max_length=255, blank=True,null=True)
    SentTime = models.DateTimeField(blank=True, null=True)
    ExpTime = models.DateTimeField(blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Message_Unicast(models.Model):
    MsgID = models.ForeignKey(Message_Info)
    ReceiverID = models.ForeignKey(User_info)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Message_Multicast(models.Model):
    MsgID = models.ForeignKey(Message_Info)
    RoleID = models.IntegerField(blank=True, null=True)
    GroupID = models.IntegerField(blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name


class Msg_Received(models.Model):
    MsgID = models.ForeignKey(Message_Info)
    ReceiverID = models.ForeignKey(User_info)
    ReadTime = models.DateTimeField(blank=True, null=True)
    isDelete = models.NullBooleanField(default=False)
    def __unicode__(self):
        return self.name




