from django.urls import path

from . import views


# Namespacing URL names
    # The tutorial project has just one app, polls. 
    # In real Django projects, there might be five, ten, twenty apps or more. 
    # How does Django differentiate the URL names between them? 
    # For example, the polls app has a detail view, and so might an app on the same project that is for a blog. 
    # How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?

    # The answer is to add namespaces to your URLconf. 
    # In the 'polls/urls.py' file, go ahead and add an app_name to set the application namespace:
app_name = 'basics'

urlpatterns = [
    # ex: /basics/ello
    # the 'name' value as called by the {% url %} template tag
    path('ello/', views.funcView_ello, name='functionEllo'),

    # ex: /basics/dummyList
    # the 'name' value as called by the {% url %} template tag
    path('dummyList/', views.funcView_query, name='dummyList'),
    
    # ex: /basics/dummyIndex
    # the 'name' value as called by the {% url %} template tag
    path('dummyIndex/', views.dummy_index, name='dummyIndex'),

    # ex: /basics/5/detail
    # the 'name' value as called by the {% url %} template tag
    path('<int:dummy_id>/detail/', views.detail, name='dummyDetail'),

]
