# Configuração de URLs no Django

Aqui estão as configurações das URLs no Django para os endpoints da API Word Analyzer.

## Configuração das URLs

As URLs abaixo mapeiam os endpoints da API para suas respectivas views:

```python
from django.urls import path
from .views import VowelCountView, SortView

urlpatterns = [
    path('vowel_count/', VowelCountView.as_view(), name='vowel-count'),
    path('sort/', SortView.as_view(), name='sort-words'),
]
```

- **`/vowel_count/`**
    - **Descrição:**
    Endpoint para contar vogais em uma lista de palavras.
    - **Método HTTP:**
    `POST`
    - **View associada:**
    `VowelCountView`
    - **Nome da URL:**
    `vowel-count`

- **`/sort/`**
    - **Descrição:**
    Endpoint para ordenar uma lista de palavras.
    - **Método HTTP:**
    `POST`
    - **View associada:**
    `SortView`
    - **Nome da URL:**
    `sort-words`

    **Descrição**

    Estas URLs configuram os endpoints da API Word Analyzer no Django, permitindo que os usuários enviem requisições para contar vogais em listas de palavras e para ordenar listas de palavras. Cada endpoint está associado à sua respectiva view (VowelCountView e SortView), garantindo que as requisições sejam processadas corretamente de acordo com as operações especificadas.

    Este documento fornece uma descrição detalhada das configurações de URLs para a API Word Analyzer no Django, facilitando a compreensão e o uso por parte dos desenvolvedores que interagem com esses endpoints.