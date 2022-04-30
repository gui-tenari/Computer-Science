# Entrada e saída de dados

### Estrutura de dados

* **Módulos**: Todo arquivo que contém definições e instruções em Python (com extensão **.py**). As funções criadas dentro de um módulo podem ser reultilizadas em outros arquivos atraves da declaração `import`

* **Pacotes**: são módulos Python que contêm outros **módulos** e/ou **pacotes**. Na prática, um **pacote** é um diretório que pode conter vários **módulos** (arquivos de extensão `.py` ) e/ou outros **pacotes** .

```python
import http  # importa o pacote http como um módulo

from http import client  # importa o módulo client do pacote http

from http.client import HTTP_PORT  # importa a constante HTTP_POST do módulo client do pacote http
```

### Ambiente virtual

* **venv** - módulo, já embutido na linguagem, que serve para isolar ambientes entre projetos. (*mesma ideia do npm*)

  ```bash
  python3 -m venv .venv
  ```

* **Ativação do ambiente:** 

  ```bash
  source .venv/bin/activate // source => utilizado para rodar script  
  which python3
  ```

## Entrada de dados

* **Input**: recebe valores <u>apenas</u> do tipo <u>*string*</u>:

  ```python
  my_number = input("Digite um numbero:")
  print(my_number)
  ```

* **sys**: o módulo sys recebe parametros quando executamos o script, guardando-os dentro de uma variavel chamada `sys.argv`

  ```python
  import sys
  
  
  if __name__ == "__main__":
      for argument in sys.argv:
          print("Received -> ", argument)
  ```

  ```bash
   python3 arquivo.py 2 4 "teste"
  ```

  ```bash
  >>> 
  Received ->  arquivo.py
  Received ->  2
  Received ->  4
  Received ->  teste
  ```

  

## Saída de dados

* **Múltiplos:** 

  ```python
  print("Os resultado são", 6, 23, 42)  # saída: Os resultados são 6 23 42
  ```

* **Valor do fim de linha**: 

  ```python
  print("Em duas ")  #Padrão
  print("linhas.")
  
  >> Em duas
  linhas.
  
  
  print("Na mesma", end="")
  print("linha.")
  
  >> Na mesma linha.
  ```

* **Sáida de erros**: 

  ```python
  import sys
  
  
  err = "Arquivo não encontrado"
  print(f"Erro aconteceu: {err}", file=sys.stderr)
  ```

  > *💡 Em **Python** , podemos fazer interpolação de variáveis e expressões utilizando [f-string ](https://pyformat.info/). Adicionamos um `f` antes das aspas e o valor de saída entre chaves. Essa dica é importante, pois é a maneira mais eficiente de formatar strings.*

```python
x = 5
y = 3
print(f"{x} / {y} = {x / y:.2f}")  # saída: 5 / 2 = 1.67
# {x} é substituído por 5
# {y} é substituído por 3
# {x / y:.2f} O que vem após os dois pontos são formatadores, como nesse exemplo, duas casas decimais (.2f).
print(f"{x:.^3}")  # saída: ".5."
# . é o caractere utilizado para preencher
# ^ indica que o valor será centralizado
# 3 são o número de caracteres exibidos
```

## Manipulação de arquivos

* **open**: a função `open` requer o parametro arquivo e o modo (read=r, write=w, create=*x*, update=+  )

  ```python
  file = open("arquivo.txt", mode="w")
  ```

* **write** : 

  ```python
  file.write("nome idade\n") ##\n quebra linha
  ```

  > 💡 Podemos escrever em um arquivo apenas após abrirmos ele.

* **print** : 

```python
# Não precisa da quebra de linha, pois esse é um comportamento padrão do print
print("Túlio 22", file=file) ##segundo parametro do print (arquivo)
```

* **writelines**: 

  ```python
  LINES = ["Alberto 35\n", "Betina 22\n", "João 42\n", "Victor 19\n"]
  file.writelines(LINES)
  ```

* **close**: 

  ```python
  file.close()
  ```

> 💡 ***IMPORTANTE NÃO ESQUECER DE FECHAR O ARQUIVO APÓS ABRI-LO***

## Erros e Exceções

* **Erros de sintaxe:** erros presente na semantica do código

  ```python
  print{"Olá, mundo!"} 
  print("Olá, mundo!") .
  ```

* **Exceções** : caso o erro disparado seja previsto no  `except` , o código não encerrará, e executará a linha do escopo previsto:

  ```python
  while True:
      try:
          x = int(input("Please enter a number: "))
          break
      except ValueError:
          print("Oops!  That was no valid number.  Try again...")
  ```

  **TRY**

  * **else** : executado caso as operações do try tenham sido bem sucedidas
  * **finally**: ações de finalização, executadas independente se há erro ou nao.

  ```python
  try:
      arquivo = open("arquivo.txt", "w")
  except OSError:
      # será executado caso haja uma exceção
      print("arquivo inexistente")
  else:
      # será executado se tudo ocorrer bem no try
      print("arquivo manipulado e fechado com sucesso")
      arquivo.close()
  finally:
      # será sempre executado, independentemente de erro
      print("Tentativa de abrir arquivo")
  ```

  **WITH** - cria um contexto, que aloca um espaço no processamento que é liberado assim que o bloco de código se encerra;

  ```python
  # Criamos um contexto, limitando o escopo onde o arquivo está aberto.
  # O uso do "as" aqui é somente para atribuir o valor utilizado no contexto à variável file
  with open("arquivo.txt", "w") as file:
      file.write("Michelle 27\n")
  # como estamos fora do contexto, o arquivo foi fechado
  print(file.closed)
  ```

  

## JSON 

Utilizado para arquivos com grande quantidade de dados. 

> Métodos: load` , `loads` , `dump` , `dumps

* **LOADS** : carrega o `JSON` a partir de um texto

```python
import json  # json é um modulo que vem embutido, porém precisamos importá-lo


with open("pokemons.json") as file:
    content = file.read()  # leitura do arquivo
    pokemons = json.loads(content)["results"]  # o conteúdo é transformado em estrutura python equivalente, dicionário neste caso.
    # acessamos a chave results que é onde contém nossa lista de pokemons

print(pokemons[0])  # imprime o primeiro pokemon da lista
```

* **LOAD**: carrega o `JSON` a partir de um arquivo.

  ```python
  import json
  
  
  with open("pokemons.json") as file:
      pokemons = json.load(file)["results"]
  
  print(pokemons[0])  # imprime o primeiro pokemon da lista
  ```

* **DUMPS** : converte para `JSON`

  ```python
  import json
  
  # Leitura de todos os pokemons
  with open("pokemons.json") as file:
      pokemons = json.load(file)["results"]
  
  # Separamos somente os do tipo grama
  grass_type_pokemons = [
      pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
  ]
  
  # Abre o arquivo para escrevermos apenas o pokemons do tipo grama
  with open("grass_pokemons.json", "w") as file:
      json_to_write = json.dumps(
          grass_type_pokemons
      )  # conversão de Python para o formato json (str)
      file.write(json_to_write)
  ```

* **DUMP**: Escreve direto no arquivo em `JSON`

  ```python
  import json
  
  # leitura de todos os pokemons
  with open("pokemons.json") as file:
      pokemons = json.load(file)["results"]
  
  # separamos somente os do tipo grama
  grass_type_pokemons = [
      pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
  ]
  
  # abre o arquivo para escrita
  with open("grass_pokemons.json", "w") as file:
      # escreve no arquivo já transformando em formato json a estrutura
      json.dump(grass_type_pokemons, file)
  ```

  > 💡 Arquivos JSON não seguem a nomenclatura habitual de leitura e escrita ( `write` e `read` ), pois são considerados formatos de serialização de dados. Seguem então as mesmas nomenclaturas utilizadas em módulos como [`marshal` ](https://docs.python.org/3/library/marshal.html#module-marshal)e [`pickle` ](https://docs.python.org/3/library/pickle.html#module-pickle), que também são formatos de serialização.

## CSV

- `reader` :  nos ajuda a ler o conteúdo, já fazendo as transformações dos valores para Python;

-  `writer` :   facilita a escrita.

  ```python
  import csv
  
  with open("balneabilidade.csv") as file:
      beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
      header, *data = beach_status_reader #Truque para separar os dados
  
  print(data)
  ```

  ​				

  ```python
  a, b = "cd"
  print(a)  # saída: c
  print(b)  # saída: d
  
  head, *tail = [1,2,3] # Quando um * está presente no desempacotamento, os valores são desempacotados em formato de lista.
  print(head)  # saída: 1
  print(tail)  # saída: [2, 3]
  ```

  

