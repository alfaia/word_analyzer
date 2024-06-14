# Serializers da API Word Analyzer

Aqui estão os serializers da API Word Analyzer que definem como os dados são validados e processados para contagem de vogais e ordenação de palavras.

## Serializador para Contagem

Class `VowelCountRequestSerializer` para contar vogais em uma lista de palavras.

```python
from rest_framework import serializers

class VowelCountRequestSerializer(serializers.Serializer):
    words = serializers.ListField(
        child=serializers.CharField()
    )
```
**Descrição:**

A classe `VowelCountRequestSerializer` no Django REST Framework valida uma entrada que consiste em uma lista de palavras, onde cada palavra é representada como uma string (`serializers.CharField()`) na variável `words`. Este serializador garante que os dados recebidos estejam formatados corretamente para operações subsequentes, como a contagem de vogais, assegurando a consistência e integridade dos dados manipulados pela API.

**Atributos:**

- **`words` (list):** Lista de palavras a serem analisadas para contagem de vogais.


## Serializador para ordenar

Class `SortRequestSerializer` para ordenar uma lista de palavras.

```python
from rest_framework import serializers

class SortRequestSerializer(serializers.Serializer):
    words = serializers.ListField(
        child=serializers.CharField()
    )
    order = serializers.ChoiceField(
        choices=['asc', 'desc']
    )
```
**Descrição:**

A classe `SortRequestSerializer` no Django REST Framework valida uma entrada que inclui uma lista de palavras, onde cada palavra é representada como uma string (`serializers.ListField(child=serializers.CharField())`) na variável `words`. Além disso, a classe valida uma opção de ordenação na variável order (`serializers.ChoiceField(choices=['asc', 'desc'])`), permitindo especificar se a ordenação deve ser ascendente (`asc`) ou descendente (`desc`). Esses validadores garantem que os dados recebidos estejam no formato adequado para realizar operações de ordenação dentro da API, mantendo a integridade e a consistência dos dados manipulados.

**Atributos:**

- **`words` (list):** Lista de palavras a serem ordenadas.
- **`order` (str):** Ordem de ordenação, `asc` para crescente e `desc` para decrescente.


Estes serializadores são utilizados para validar e processar dados nas operações de contagem de vogais e ordenação de palavras na API Word Analyzer do Django REST Framework. Eles garantem que os dados recebidos estejam no formato esperado antes de serem processados pelas funções correspondentes da API.