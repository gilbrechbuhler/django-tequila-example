# django-tequila-example
A simple application example in Django with django-tequila


## Explications

### URLs

Les urls sont définies dans les fichiers `urls.py`, si on regarde le fichier `src/config/settings/urls.py` :

```
urlpatterns = [
    url(r'^$', homepage),
    url(r'^orders/', include('example.urls')),
    url(r'^admin/', admin.site.urls),
]
```

Chaque entrée se compose au moins d'une expression régulière et d'une vue (ou l'inclusion d'autres urls).
Ici par exemple, toutes les URLs de la forme `domain.com/orders/` sont matchées contre les URLs contenues 
dans le fichier `src/example/urls.py` qui contient lui-même :

```
urlpatterns = [
    url(r'^$', orders_list, name='orders_list'),
    url(r'create$', edit_order, name='create_order'),
    url(r'edit/(?P<pk>[0-9]*)/$', edit_order, name='edit_order'),
]
```

Ainsi l'URL `domain.com/orders/` appelle la vue `orders_list` lorsque'elle est accédée par un client.
Les URL `domain.com/orders/create` et  `domain.com/orders/edit/1` appellent toutes les deux la vue `edit_order`,
la première en ne passant aucun paramètre à la vue, la seconde en passant le paramètre 'pk=1' à la vue.


### Vues

Les vues utilisent les modèles et les requêtes pour envoyer des réponses HTTP à l'utilisateur. Par exemple :

```
@login_required
def orders_list(request):
    orders = Order.objects.order_by('pk')
    context = {'orders': orders}
    return render(request, 'example/orders_list.html', context)
```

Cette vue prends tous les objets `Order` enregistrés en base de données et retourne à l'utilisateur une page HTML générée à partir du template se trouvant
dans le dossier `src/example/templates/example/orders_list.html`.


### Modèles

Les modèles représentent la partie métier de notre application, pour chaque modèle Django utilise les migrations pour créer une table
en base de données, les migrations servent à faire en sorte que le schéma de la base de données corresponde toujours au
schéma de nos modèles.
