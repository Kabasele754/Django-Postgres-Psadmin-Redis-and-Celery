import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article, Contact
import sweetify

# Create your views here.


def indexView(request, template_name="blog/pages/index.html"):
    # context permet envoyer les codes python vers html
    # declaration de notre context
    context = {}
    bonjour = "Bonjour tout le monde ici c'est django"
    # affectaction la clef et valeur dans contex
    #          Key      Value

    # instance article
    # SELECT * FROM Article; with SQL
    # With ORM
    list_article = Article.objects.all()

    context['name'] = bonjour
    context['article'] = list_article

    return render(request, template_name, context)


def contactView(request, template_name="blog/pages/contact.html"):
    context = {}
    # SELECT * FROM Contact
    contacts = Contact.objects.all()
    # Utilisation du context
    context["contacts"] = contacts

    #  ici la condition on verifie si la mathode de la request et == POST
    if request.method == "POST":
        # On recupere les valeurs entrer par l'utilisateur

        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        print("je veux le nom", name)

        #  On creer notre Contact
        obj_contact = Contact(
            name= name,
            email= email,
            content = content
        )
        obj_contact.save()
        
        sweetify.success(request, 'Perfect', text='vous avez modifier avec success',
                          position='top-end',
                         timer=1500,
                         timerProgressBar='true',
                         )

    return render(request, template_name, context)


def gestionContactView(request, template_name="blog/pages/gestion_contact.html"):
    context = {}
    # SELECT * FROM Contact
    contacts = Contact.objects.all()
    # Utilisation du context
    context["contacts"] = contacts
    #  ici la condition on verifie si la mathode de la request et == POST
    if request.method == "POST":
        # On recupere les valeurs entrer par l'utilisateur

        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']

        print("je veux le nom", name)

        #  On creer notre Contact
        obj_contact = Contact(
            name=name,
            email=email,
            content=content
        )
        obj_contact.save()

    return render(request, template_name, context)

# fonction  update

def updateCotactView(request,contact_id, template_name="blog/pages/gestion_contact.html"):
    contact_one = Contact.objects.get(id=contact_id)
    print("id", contact_one)
    context = {}
    contacts = Contact.objects.all()
    context['contacts'] = contacts
    context['contact_one'] = contact_one
    #  la condition == post
    if request.method == "POST":
        # recuper les donnees qui se trouve dans input et on le modifie
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        #  assign de valeurs input
        contact_one.name = name
        contact_one.email = email
        contact_one.content = content
        # on sauvegarde la modification
        contact_one.save()

    return render(request, template_name, context)


def deleteContactView(request, contact_id):
    contact_one = Contact.objects.get(id=contact_id)
    contact_one.delete()

    return redirect('gestion_contact')

def gestionArticleView(request, template_name="blog/pages/gestion_article.html"):
    context = {}
    articles = Article.objects.all()
    context['articles'] = articles

    return render(request, template_name, context)


def addArticleView(request):

    # la condition pour la methode POST s'il est dans le request
    if request.method == "POST":
        title = request.POST['title']
        image = request.FILES['image']
        description = request.POST['description']

        # instance object Article
        article = Article(
            title = title,
            image = image,
            description = description,
            publication= True
        )
        # save object article
        article.save()
        # message de success
        # messages.success(request, f"Vous avez ajoute avec succee {article.title} ")
        sweetify.success(request, 'Perfect', text='vous avez ajouter avec success',
                         persistent='OK',

                         )
        return redirect('gestion_article')


def updateArticleView(request, article_id, template_name="blog/pages/gestion_article.html"):

    article_one = Article.objects.get(id=article_id)
    print("id", article_one)
    context = {}
    #  la condition == post
    if request.method == "POST":
        # recuper les donnees qui se trouve dans input et on le modifie
        if len(request.FILES) != 0:
            if len(article_one.image) > 0:
                os.remove(article_one.image.path)
            article_one.image = request.FILES['image']

        title = request.POST['title']
        #image = request.FILES['image'] or None
        description = request.POST['description']
        #  assign de valeurs input
        article_one.title = title
        #article_one.image = image
        article_one.description = description
        # on sauvegarde la modification
        article_one.save()
        #messages.success(request, f"Vous avez modifier avec success {article_one.title}")
        sweetify.success(request, 'Perfect', text='vous avez modifier avec success',
                          position='top-end',
                         timer=1500,
                         timerProgressBar='true',
                         )

        return redirect('gestion_article')

    else:
        messages.error(request, f"Erreur d'ajout ")
    return render(request, template_name, context)


def deleteArticleView(request, article_id):
    article_one = Article.objects.get(id=article_id)

    article_one.delete()
    messages.success(request, f'Vous avez supprimer avec success')

    return redirect('gestion_article')

