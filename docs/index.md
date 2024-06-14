# Documentação da API word analyzer

## Introdução

A API `word_analyzer` oferece duas rotas para operações simples em palavras dentro de um array: contar vogais em cada palavra e ordenar as palavras.

Certifique-se de que a API `word_analyzer` está em execução no endereço `https://agile-shore-49592-142c0eafee41.herokuapp.com/api/` para poder realizar as requisições.

## Rota 1: Contagem de Vogais

Esta rota permite contar as vogais em cada palavra de um array.

- **Método**: POST
- **URL**: `https://agile-shore-49592-142c0eafee41.herokuapp.com/api/vowel_count/`
- **Exemplo de Requisição**:
```json
  {
    "words": ["batman", "robin", "coringa"]
  }
```

- **Exemplo de Resposta**:
```json
  {
    "batman": 2,
    "robin": 2,
    "coringa": 3
  }
```

Para contar as vogais em cada palavra fornecida no array `words`, envie uma requisição POST para a URL especificada. O corpo da requisição deve conter um objeto JSON com a chave `words` contendo um array de strings.


## Rota 2: Ordenação de Palavras

Esta rota permite ordenar as palavras em um array, com a opção de ordenação reversa.

- **Método**: POST
- **URL**: `https://agile-shore-49592-142c0eafee41.herokuapp.com/api/sort/`
- **Exemplo de Requisição para Ordenação Crescente**:
```json
{
  "words": ["batman", "robin", "coringa"],
  "order": "asc"
}
```

- **Exemplo de Resposta para Ordenação Crescente**:
```json
[
    "batman", 
    "coringa", 
    "robin"
]
```
- **Requisição para Ordenação Decrescente**:
```json
{
  "words": ["batman", "robin", "coringa"],
  "order": "desc"
}
```

- **Exemplo de Resposta para Ordenação Decrescente**:
```json
[
    "robin", 
    "coringa", 
    "batman"
]
```

Para ordenar as palavras fornecidas no array `words`, envie uma requisição POST para a URL especificada. O corpo da requisição deve conter um objeto JSON com as chaves `words` (array de strings) e `order` (string com valor `asc` para ordem crescente ou `desc` para ordem decrescente).


## Exemplos de Uso

**Exemplo Completo de Uso das Rotas**

Aqui estão exemplos completos de como usar as duas rotas da API `word_analyzer`:


**Contagem de Vogais:**
```bash
curl -X POST "https://agile-shore-49592-142c0eafee41.herokuapp.com/api/vowel_count/" -H "Content-Type: application/json" -d '{ "words": ["batman", "robin", "coringa"]}'
```
**Resposta Esperada:**
```json
{
  "batman": 2,
  "robin": 2,
  "coringa": 3
}
```



**Ordenação de Palavras:**

- **Ordenação Crescente:**
```bash
curl -X POST "https://agile-shore-49592-142c0eafee41.herokuapp.com/api/sort/" -H "Content-Type: application/json" -d "{\"words\": [\"batman\", \"robin\", \"coringa\"], \"order\": \"asc\"}"
```

**Resposta Esperada:**
```json
[
    "batman", 
    "coringa", 
    "robin"
]
```

- **Ordenação Decrescente:**
```bash
curl -X POST "https://agile-shore-49592-142c0eafee41.herokuapp.com/api/sort/" -H "Content-Type: application/json" -d "{\"words\": [\"batman\", \"robin\", \"coringa\"], \"order\": \"desc\"}"
```

**Resposta Esperada:**
```json
[
    "robin", 
    "coringa", 
    "batman"
]
```



Esta documentação fornece uma visão abrangente de como utilizar as duas rotas da API `word_analyzer` para contar vogais em palavras e ordenar palavras em um array. Certifique-se de adaptar os exemplos e os comandos CURL conforme necessário para o ambiente específico em que você está trabalhando.