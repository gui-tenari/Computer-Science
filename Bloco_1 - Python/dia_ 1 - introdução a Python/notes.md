# Introdução à Python

**CONVENÇÕES**:

* snake_case
* CONST_IN_UPPER_CASE

### Operações Básicas:

* Divisão sem numero decimal : **//**			ex: 3 // 2 = 1
* Potencia: ****** 	ex: 2 ** 10 = 1024
* comparação: **A and B; A or B**

#### Tipos de dados:

*  **Inteiros (int)**

  ```python
  a = 5
  type(a)
  >>> <class 'int'>
  ```

*  **Float** **(flutuantes)**

  ```python
  a = 5.0
  type(a)
  >>> <class 'float'>
  ```

* **Complex** 

  ```python
  a = 5.0
  type(a)
  >>> <class 'complex'>
  ```

* **String**

* **Boolean**

* **List** (o que seria os arrays no JavaScript)

  * List.Append('item') - adiciona um novo item na lista
  * List.remove('item') - remove item da lista
  * List.extend('outraLista') - acopla uma lista na outra

* **Tupla** (duas informações complementares)

  ```python
  [('Name1', 1), (Name2, 2)]
  ```

* **Dicionário** (objeto no JavaScript) *type dict*

* **Conjuntos** - *type set*

  ```python
  admin_user = { "guilherme", "gabriel" }
  users = { "guilherme", "gabriel", "barbara", "jess" }
  ```

  * Intersection - busca elementos iguais de dois conjuntos:

    ```python
    users.intersection(admin_users)
    >>> { "guilherme", "gabriel" }
    ```

  * Difference - busca elementos diferentes de dois conjuntos

    ```python
    users.difference(admin_users)
    >>> {'barbara', 'jess'} 
    ```

  * Union - une dois conjuntos

    ```python
    admin_user = { "guilherme", "gabriel" }
    users = { "jorge", "gabriel", "barbara", "bruno" }
    
    admin_user.union(users)
    >>> { "jorge", "gabriel", "barbara", "bruno", "guilherme", "gabriel" }
    ```

    

### Estruturas condicionais: 

```python
position = ""
if salary <= 2000:
    position = "estagiário"
elif 2000 < salary <= 5800:
    position = "júnior"
elif 5800 < salary <= 7500:
    position = "pleno"
elif 7500 < salary <= 10500:
    position = "senior"
else:
    position = "líder"
```

### Estruturas de repetição: 

* **FOR** : ForEach do JavaScript

```python
min_rating = 3.0
filtered_restaurants = [restaurant["name"]
                         for restaurant in restaurants
                         if restaurant["nota"] > min_rating]
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D
```

*obs: Isto é equivalente às operações de `map` e `filter` em JavaScript.*

* **WHILE**: 

  ```python
  n = 10
  last, next = 0, 1
  while last < n:
      print(last)
      last, next = next, last + next
  ```



### Funções:

* Paramentros posicionais e nomeados:

```python
def soma(x, y):
    return x + y

soma(2, 2)  # os parâmetros aqui são posicionais

soma(x=2, y=2)  # aqui estamos nomeando os parâmetros
```

* 