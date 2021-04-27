from django.urls import path
import resume_builder.views as rb_views
urlpatterns = [
    path('', rb_views.resume_home, name='resume-home'),
    path('contact/', rb_views.contact,name="resume-contact"),
    path('skills/',rb_views.skills,name="resume-skills"),
    path('skills/edit/<int:id>',rb_views.skills_edit,name="resume-skills-edit"),
    path('skills/delete/<int:id>',rb_views.skills_delete,name="resume-skills-delete"),
    path('education/',rb_views.education,name="resume-education"),
    path('education/edit/<int:id>',rb_views.education_edit,name="resume-education-edit"),
    path('educaiton/delete/<int:id>',rb_views.education_delete,name="resume-education-delete"),
    path('IExperience/',rb_views.internship,name="resume-internship"),
    path('IExperience/edit/<int:id>',rb_views.internship_edit,name="resume-internship-edit"),
    path('IExperience/delete/<int:id>',rb_views.internship_delete,name="resume-internship-delete"),
    path('training/',rb_views.training,name="resume-training"),
    path('training/edit/<int:id>',rb_views.training_edit,name="resume-training-edit"),
    path('training/delete/<int:id>',rb_views.training_delete,name="resume-training-delete"),
    path('project/',rb_views.project,name="resume-project"),
    path('project/edit/<int:id>',rb_views.project_edit,name="resume-project-edit"),
    path('project/delete/<int:id>',rb_views.project_delete,name="resume-project-delete"),
    path('extra/',rb_views.extra,name="resume-extra"),
    path('extra/edit/<int:id>', rb_views.extra_edit, name="resume-extra-edit"),
    path('extra/delete/<int:id>', rb_views.extra_delete, name="resume-extra-delete"),
    path('language/',rb_views.language,name="resume-language"),
    path('language/edit/<int:id>',rb_views.language_edit,name="resume-language-edit"),
    path('language/delete/<int:id>',rb_views.language_delete,name="resume-language-delete"),
    path('achievement/',rb_views.achievement,name="resume-achievement"),
    path('achievement/edit/<int:id>',rb_views.achievement_edit,name="resume-achievement-edit"),
    path('achievement/delete/<int:id>',rb_views.achievement_delete,name="resume-achievement-delete"),
    path('preview/', rb_views.preview, name="resume-preview"),
    path('preview-resume/', rb_views.preview_template, name="resume-preview-template"),
]
