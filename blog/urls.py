from django.urls import path, reverse_lazy
from django.contrib.auth import views as authViews
from . import views as userViews

app_name = 'blog'

urlpatterns = [
    # function based view
    # path('', userViews.home, name='blog-home'),
    # class based view
    path('', userViews.PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', userViews.UserPostListView.as_view(), name='blog-user-posts'),


    path('post/<int:pk>/', userViews.PostDetailView.as_view(), name='blog-post-detail'),

    path('post/new/', userViews.PostCreateView.as_view(), name='blog-post-create'),
    path('post/<int:pk>/update/', userViews.PostUpdateView.as_view(), name='blog-post-update'),
    path('post/<int:pk>/delete/', userViews.PostDeleteView.as_view(), name='blog-post-delete'),

    path('about/', userViews.about, name='blog-about'),
    path('register/', userViews.register, name='blog-register'),

    path('profile/', userViews.profile, name='blog-profile'),

    path('login/', authViews.LoginView.as_view(template_name='blog/login.html'), name='blog-login'),
    path('logout/', authViews.LogoutView.as_view(template_name='blog/logout.html'), name='blog-logout'),

    path('password-reset/', 
        authViews.PasswordResetView.as_view(template_name='blog/password_reset.html', 
                                            email_template_name = 'blog/password_reset_email.html',
                                            success_url = reverse_lazy('blog:password_reset_done')), 
        name='blog-password-reset'),

    path('password-reset/done/', 
        authViews.PasswordResetDoneView.as_view(template_name='blog/password_reset_done.html'), 
        name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', 
        authViews.PasswordResetConfirmView.as_view(template_name='blog/password_reset_confirm.html'), 
        name='password_reset_confirm'),

    path('password-reset-complete/', 
        authViews.PasswordResetCompleteView.as_view(template_name='blog/password_reset_complete.html'), 
        name='password_reset_complete'),
]


    # url(r'^password_reset/$', auth_views.password_reset,{'email_template_name':'accounts/registration/password_reset_email.html',
    #                                                 'subject_template_name':'accounts/registration/password_reset_subject.txt',
    #                                                 'post_reset_redirect':'accounts:password_reset_done',
    #                                                 'from_email':'accounts@django.com',
    #                                                 },name='password_reset'),

    # url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'accounts/registration/password_reset_done.html'}, name='password_reset_done')