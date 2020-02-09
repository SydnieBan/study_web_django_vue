# Generated by Django 2.2.5 on 2019-09-20 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Video')),
            ],
        ),
        migrations.CreateModel(
            name='UserCourseware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iswatch', models.IntegerField(default=0)),
                ('courseware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Courseware')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='SelectCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc_date', models.DateTimeField(auto_now_add=True)),
                ('iscomplete', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('qv_date', models.DateTimeField(auto_now_add=True)),
                ('question_video', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_course.QuestionVideo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Video')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionCourseware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('qc_date', models.DateTimeField(auto_now_add=True)),
                ('courseware', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Courseware')),
                ('question_courseware', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_course.QuestionCourseware')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='CourseEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('eva_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('col_date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
