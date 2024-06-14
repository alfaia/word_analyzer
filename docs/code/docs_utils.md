# Funções de Manipulação de Palavras

Essas duas funções (`sort_words`, `count_vowels`) da API Word Analyzer manipulam listas de palavras e contabilizam as vogais de cada palavra.

### Função para Contar

A função `count_vowels` conta o número de vogais em cada palavra de uma lista.

```python
def count_vowels(words):
    vowel_counts = {
        word: sum(1 for char in word if char in 'aeiouAEIOU') for word in words
    }
    return vowel_counts
```
**Descrição**

Essa função cria um dicionário `vowel_counts` onde as chaves são palavras (`word`) de uma lista (`words`), e os valores correspondentes são o número de vogais encontradas em cada palavra.

- **Argumentos:**
Recebe uma lista de palavras na variável `words`.
- **Resposta:**
Retorna o dicionário `vowel_counts` com as chaves e os valores.




### Função para Ordenar

A função `sort_words` ordena uma lista de palavras em ordem crescente ou decrescente.

```python
def sort_words(words, order):
    return sorted(words, reverse=(order == 'desc'))
```
**Descrição**

Esta função utiliza a função `sorted` do Python para ordenar a lista de palavras (`words`). A ordem da ordenação é determinada pelo argumento order, `onde` `asc` indica ordem crescente e `desc` indica ordem decrescente.

- **Argumentos:**
    - **`words` (list):**
    Lista de palavras a serem ordenadas.
    - **`order` (str):**
     Indica a ordem de ordenação, podendo ser `asc` para crescente ou `desc` para decrescente.
- **Resposta:**
Retorna a lista `words` ordenada de acordo com a ordem especificada em `order`.

Este documento oferece uma descrição concisa e informativa das funções `count_vowels` e `sort_words`, facilitando o entendimento de suas funcionalidades e modos de uso.