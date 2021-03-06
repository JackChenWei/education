# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 09:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookID', models.CharField(blank=True, max_length=255, null=True)),
                ('BookName', models.CharField(blank=True, max_length=255, null=True)),
                ('Introduce', models.CharField(blank=True, max_length=255, null=True)),
                ('Author', models.CharField(blank=True, max_length=255, null=True)),
                ('PubDate', models.DateField(blank=True, null=True)),
                ('Press', models.CharField(blank=True, max_length=255, null=True)),
                ('Keywords', models.CharField(blank=True, max_length=255, null=True)),
                ('InputTime', models.DateField(default=datetime.date(2016, 2, 29))),
                ('ReadNum', models.IntegerField(blank=True, null=True)),
                ('Charges', models.FloatField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Class_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClassID', models.CharField(blank=True, max_length=255, null=True)),
                ('ClassName', models.CharField(blank=True, max_length=255, null=True)),
                ('ChineseID', models.CharField(blank=True, max_length=255, null=True)),
                ('MathID', models.CharField(blank=True, max_length=255, null=True)),
                ('EnglishID', models.CharField(blank=True, max_length=255, null=True)),
                ('PhysicsID', models.CharField(blank=True, max_length=255, null=True)),
                ('ChemistryID', models.CharField(blank=True, max_length=255, null=True)),
                ('BiologyID', models.CharField(blank=True, max_length=255, null=True)),
                ('ScienceID', models.CharField(blank=True, max_length=255, null=True)),
                ('SportID', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Class_stu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.NullBooleanField(default=False)),
                ('ClassID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Class_info')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(blank=True, max_length=255, null=True)),
                ('CourceName', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('ClassID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Class_info')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChapterID', models.CharField(blank=True, max_length=255, null=True)),
                ('ChapterName', models.CharField(blank=True, max_length=255, null=True)),
                ('ChapterContent', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KnowledgeID', models.CharField(blank=True, max_length=255, null=True)),
                ('KnowledgeName', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('ChapterID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Course_Chapter')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Answer', models.CharField(blank=True, max_length=255, null=True)),
                ('Score', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Exam_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ExamID', models.CharField(blank=True, max_length=255, null=True)),
                ('Type', models.IntegerField(blank=True, null=True)),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('GroupNum', models.IntegerField(blank=True, null=True)),
                ('CreateTime', models.DateTimeField(blank=True, null=True)),
                ('StartTime', models.DateTimeField(blank=True, null=True)),
                ('EndTime', models.DateTimeField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('CourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.NullBooleanField(default=False)),
                ('ExamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Exam_info')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupID', models.CharField(blank=True, max_length=255, null=True)),
                ('MarkID', models.CharField(blank=True, max_length=255, null=True)),
                ('Score', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('ExamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Exam_info')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.IntegerField(blank=True, null=True)),
                ('Purchased', models.NullBooleanField(default=False)),
                ('AddTime', models.DateTimeField(blank=True, null=True)),
                ('StartTime', models.DateTimeField(blank=True, null=True)),
                ('LatestTime', models.DateTimeField(blank=True, null=True)),
                ('Progress', models.IntegerField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('BookID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Message_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tpye', models.IntegerField(blank=True, null=True)),
                ('SenderID', models.CharField(blank=True, max_length=255, null=True)),
                ('Content', models.CharField(blank=True, max_length=255, null=True)),
                ('SentTime', models.DateTimeField(blank=True, null=True)),
                ('ExpTime', models.DateTimeField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message_Multicast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoleID', models.IntegerField(blank=True, null=True)),
                ('GroupID', models.IntegerField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('MsgID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Message_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Message_Unicast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isDelete', models.NullBooleanField(default=False)),
                ('MsgID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Message_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Msg_Received',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReadTime', models.DateTimeField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('MsgID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Message_Info')),
            ],
        ),
        migrations.CreateModel(
            name='Online_Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OLCourseID', models.CharField(blank=True, max_length=255, null=True)),
                ('OLCoursename', models.CharField(blank=True, max_length=255, null=True)),
                ('Introduction', models.CharField(blank=True, max_length=255, null=True)),
                ('Author', models.CharField(blank=True, max_length=255, null=True)),
                ('PubTime', models.DateField(blank=True, null=True)),
                ('InputTime', models.DateField(blank=True, default=datetime.date(2016, 2, 29), null=True)),
                ('Statistics', models.IntegerField(blank=True, null=True)),
                ('Charges', models.FloatField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Online_Course_Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KnownledgeID', models.CharField(blank=True, max_length=255, null=True)),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('OLCourseID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Online_Course')),
            ],
        ),
        migrations.CreateModel(
            name='Parent_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ParAccount', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PayID', models.CharField(blank=True, max_length=255, null=True)),
                ('PayerID', models.CharField(blank=True, max_length=255, null=True)),
                ('Description', models.CharField(blank=True, max_length=255, null=True)),
                ('TransSubTime', models.DateTimeField(blank=True, null=True)),
                ('PayTime', models.DateTimeField(blank=True, null=True)),
                ('PayAmount', models.FloatField(blank=True, null=True)),
                ('Status', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StuID', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeachID', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TopicID', models.CharField(blank=True, max_length=255, null=True)),
                ('Type', models.NullBooleanField()),
                ('Content', models.CharField(blank=True, max_length=255, null=True)),
                ('InputDate', models.DateField(blank=True, default=datetime.date(2016, 2, 29), null=True)),
                ('Options', models.CharField(blank=True, max_length=255, null=True)),
                ('Reference', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Topic_Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Knowledge', models.CharField(blank=True, max_length=255, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('TopicID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account', models.CharField(blank=True, max_length=255, null=True)),
                ('Role', models.CharField(blank=True, max_length=255, null=True)),
                ('Pwd', models.CharField(blank=True, max_length=255, null=True)),
                ('Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Birthday', models.DateField(blank=True, null=True)),
                ('Sex', models.NullBooleanField()),
                ('Tel', models.CharField(blank=True, max_length=255, null=True)),
                ('IDCard', models.CharField(blank=True, max_length=255, null=True)),
                ('Politics', models.IntegerField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Wrong_topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Times', models.IntegerField(blank=True, null=True)),
                ('isDelete', models.NullBooleanField(default=False)),
                ('ExamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Exam_info')),
                ('StuID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Student_info')),
                ('TopicID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='teacher_info',
            name='TeachAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.User_info'),
        ),
        migrations.AddField(
            model_name='student_info',
            name='StuAccount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.User_info'),
        ),
        migrations.AddField(
            model_name='parent_info',
            name='StuID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Student_info'),
        ),
        migrations.AddField(
            model_name='online_course',
            name='Admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.User_info'),
        ),
        migrations.AddField(
            model_name='msg_received',
            name='ReceiverID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.User_info'),
        ),
        migrations.AddField(
            model_name='message_unicast',
            name='ReceiverID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.User_info'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='OLCourseID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Online_Course'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='StuID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Student_info'),
        ),
        migrations.AddField(
            model_name='exam_topic',
            name='TopicID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Topic'),
        ),
        migrations.AddField(
            model_name='exam_student',
            name='StuID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Student_info'),
        ),
        migrations.AddField(
            model_name='exam_info',
            name='Creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.User_info'),
        ),
        migrations.AddField(
            model_name='exam_answer',
            name='ExamID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Exam_info'),
        ),
        migrations.AddField(
            model_name='exam_answer',
            name='StuID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Student_info'),
        ),
        migrations.AddField(
            model_name='exam_answer',
            name='TopicID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Topic'),
        ),
        migrations.AddField(
            model_name='course',
            name='TeachID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Teacher_info'),
        ),
        migrations.AddField(
            model_name='class_stu',
            name='StuID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.Student_info'),
        ),
    ]
