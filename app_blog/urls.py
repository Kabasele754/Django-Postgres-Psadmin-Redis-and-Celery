from  django.urls import  path
from .views import  indexView, contactView, gestionContactView,\
    updateCotactView, deleteContactView, gestionArticleView, \
    addArticleView, updateArticleView, deleteArticleView


urlpatterns = [
    path('', indexView, name="index"),
    # gestion de contact
    path('contact/', contactView, name='contact'),
    path('gestion-contact/', gestionContactView, name="gestion_contact"),
    path('gestion-contact/update/<int:contact_id>/', updateCotactView, name="update_contact"),
    path('gestion-contact/delete/<int:contact_id>/', deleteContactView, name="delete_contact"),

    # gestion des article
    path('gestion-article/', gestionArticleView, name="gestion_article" ),
    path('add-article/', addArticleView, name="add_article"),
    path('edit-article/<int:article_id>/',updateArticleView, name="edit_article" ),
    path('delete-article/<int:article_id>/',deleteArticleView, name="delete_article" ),




]

