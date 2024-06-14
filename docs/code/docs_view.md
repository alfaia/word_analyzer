# Detalhamento das Views da API

Neste documento, vamos detalhar as classes de view da API `word_analyzer` utilizando o framework Django REST Framework.

## View para Contagem

A classe `VowelCountView` é responsável por contar as vogais em cada palavra de um array enviado na requisição POST.

### Método `post`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VowelCountRequestSerializer
from .utils import count_vowels

class VowelCountView(APIView):
    def post(self, request):
        serializer = VowelCountRequestSerializer(data=request.data)
        if serializer.is_valid():
            words = serializer.validated_data['words']
            vowel_counts = count_vowels(words)
            return Response(vowel_counts, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
**Descrição**

- **Classe:**
 `VowelCountView` herda de `APIView`.
 - **Método `post`:**
 Recebe uma requisição POST contendo um array de palavras.
    - **Serialização:**
    Utiliza o `VowelCountRequestSerializer` para validar e desserializar os dados recebidos.
    - **Contagem de Vogais:**
    Chama a função `count_vowels(words)` para contar as vogais em cada palavra do array.
    - **Resposta:**
    Retorna um objeto JSON com as contagens de vogais ou erros de validação, com os respectivos códigos de status HTTP.




## View para ordenar

A classe `SortView` é responsável por ordenar as palavras em um array conforme especificado na requisição POST.

### Método `post`

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SortRequestSerializer
from .utils import sort_words

class SortView(APIView):
    def post(self, request):
        serializer = SortRequestSerializer(data=request.data)
        if serializer.is_valid():
            words = serializer.validated_data['words']
            order = serializer.validated_data['order']
            sorted_words = sort_words(words, order)
            return Response(sorted_words, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**Descrição**

- **Classe:**
 `SortView` herda de `APIView`.
 - **Método `post`:**
 Recebe uma requisição POST contendo um array de palavras e um parâmetro de ordenação (`order`).
    - **Serialização:**
    Utiliza o `SortRequestSerializer` para validar e desserializar os dados recebidos.
    - **Ordenação de Palavras:**
    Chama a função `sort_words(words, order)` para ordenar o array de palavras conforme especificado.
    - **Resposta:**
    Retorna um objeto JSON com as palavras ordenadas ou erros de validação, com os respectivos códigos de status HTTP.


Este documento detalha as classes `VowelCountView` e `SortView` da API `word_analyzer`, explicando como cada uma processa requisições POST, utiliza serializadores para validar dados e chama funções utilitárias (`count_vowels` e `sort_words`) para realizar operações específicas.