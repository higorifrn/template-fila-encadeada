# 1. Propósito
---
Esta tarefa tem os seguintes propósitos:
- Desenvolver as habilidades de criação e manipulação de estruturas de dados do tipo fila (queue);
- Implementar e validar os conceitos relacionados ao métodos de esturas de dados fila.

# 2. Orientações
---

As subsessões a seguir orientam sobre o uso de soluções as quais poderão auxiliar na realização dessa tarefa, bem como os aspectos gerais relativos à implementação (código fonte) da sua solução.

## 2.1. Instalação do framework pytest
---
A estrutura do código fonte está montada para ser validada com a framework pytest, o qual poderá ser instalado com o comando:

```console
$ pip install pytest
```

Você não está obrigado a instalar o pytest e rodar os testes de validação antes do envio da tarefa, entretanto pode ser bastante útil para que você consiga identificar onde estão os pontos de falhas no seu projeto.

Para realizar um teste de validação de todos os métodos da sua implementação, basta executar o seguinte comando:

```console
$ pytest test/test_fila.py -v
```

O pytest permite que você realize o teste em métodos específicos. Portanto, também é válido o comando:

```console
$ pytest test/test_fila.py -k is_empty -v --no-header
```
A opção -k is_empty avaliará apenas os métodos dentro do arquivo test/test_fila.py que contenham a string "is_empty" no nome do método. No caso de todos os testes serem aprovados, o resultado de saída no terminal deverá ser algo como mostrado em: 

```console
$ pytest test/test_fila.py -k is_empty -v --no-header
=================================== test session starts ===================================
collected 5 items / 3 deselected / 2 selected                                             

test/test_fila.py::test_is_empty_true PASSED                                        [ 50%]
test/test_fila.py::test_is_empty_false PASSED                                       [100%]

============================= 2 passed, 3 deselected in 0.01s =============================
```

No caso de algum dos testes sobre o método falhar, o resultado de saída no terminal poderá ser algo como mostrado em: 

```console
$ pytest test/test_fila.py -k is_empty -v --no-header
=================================== test session starts ===================================
collected 5 items / 3 deselected / 2 selected                                             

test/test_fila.py::test_is_empty_true PASSED                                        [ 50%]
test/test_fila.py::test_is_empty_false FAILED                                       [100%]

======================================== FAILURES =========================================
___________________________________ test_is_empty_false ___________________________________

    @mark.is_empty
    def test_is_empty_false():
    
        try:
            exists = os.path.exists("fila.py")
            assert exists == True
        except:
            sys.exit()
    
        fila = Fila(3)
        fila.enqueue(1)
        fila.enqueue(2)
    
>       assert fila.is_empty() == False and fila.size() > 0
E       assert (True == False)
E        +  where True = <bound method Fila.is_empty of <fila.Fila object at 0x10c5b3790>>()
E        +    where <bound method Fila.is_empty of <fila.Fila object at 0x10c5b3790>> = <fila.Fila object at 0x10c5b3790>.is_empty

test/test_fila.py:37: AssertionError
---------------------------------- Captured stdout call -----------------------------------
Criada EDD Fila com capacidade: 3
Item (Dado: 1) inserido na EDD Fila!
Item (Dado: 2) inserido na EDD Fila!
================================= short test summary info =================================
FAILED test/test_fila.py::test_is_empty_false - assert (True == False)
======================== 1 failed, 1 passed, 3 deselected in 0.05s ========================
```

Para mais detalhes e informações sobre o framework consultar no [link](https://docs.pytest.org/en/7.3.x/contents.html).

## 2.2. Implementação da solução
---

Você deverá implementar os **métodos da classe Fila** no arquivo **fila.py**, os quais ainda não foram implementados. Esteja atento ao tipo de retorno de cada método, pois isso irá impactar diretamente na avaliação da sua solução após você enviar o commit com as suas implementações para o repositório remoto.

Após concluir a tarefa, você deverá realizar um **git push** para entregar a sua atividade. Você poderá realizar tantos envios ao repositório remoto quanto desejar. Entretanto, esteja atento ao prazo de entreda da atividade para não realizar a entrega com atraso, pois isso irá impactar sobre a nota da atividade. 

Os testes de validação da pontuação realizados pelo GitHub-Classroom não ocorrem imediatamente após o envio do push para o servidor. Normalmente, o GitHub levará o tempo de alguns segundos para realizar o teste sobre a solução enviada por você. Você deverá atualizar a página no GitHub-Classroom a cada 10s, caso não perceba a mudança no resultado da pontuação, até que o GitHub faça o computo dos seus pontos a partir da execução dos testes sobre a sua entrega.

Esteja atento aos tipos de retorno de cada método, os quais se encontram descritos com _type hint_ no próprio método.

## 2.3. Prazo de entrega
---

O prazo de entrega encontra-se descrito no ambiente do Google Sala de Aula da turma e também do GitHub Classroom.


# 3. Tarefas
---

Segue a relação de tarefas a serem observadas na implementação de cada método e a respectiva pontuação do método destacada em parênteses. Toda a tarefa valerá **20pts**, o que corresponde a **20%** da nota da primeira etapa.

- [x] Estudar e analizar os conceitos e técnicas para implementação da estrutura de dados do tipo fila
- [ ] **(2pts)** Implementar o método **is_empty()**
  - [ ] Deve retornar um boolean True se não houver itens (Nó) na fila ou False, caso contrário
- [ ] **(2pts)** Implementar o método **is_full()**
  - [ ] Deve retornar um boolean True se houver itens (Nó) na fila ou False, caso contrário
- [ ] **(5pts)** Implementar o método **enqueue()**, o qual deve receber como entrada um valor para criar um nó que deverá ser inserido na fila
  - [ ] Criar um objeto Nó a partir do valor recebido pelo método
  - [ ] Deve retornar um boolean True se conseguir inserir um item (Nó) na fila
  - [ ] Caso a fila tenha alcançado a sua capacidade máxima deverá lançar uma Exception com uma mensagem de erro relativo ao ocorrido, senão o item (Nó) deve ser inserido na fila e método deverá retornar um boolean True
- [ ] **(5pts)** Implementar o método **dequeue()**, o qual deve retornar o primeiro item (Nó) da fila e remover esse item da fila
  - [ ] Caso a fila esteja vazia deverá lançar uma Exception com uma mensagem de erro
  - [ ] Caso a fila possua um ou mais itens, o primeiro item (Nó) da fila deve ser removido e em seguida retornado pelo método
- [ ] **(1pts)** Implementar o método **peek_first()**, o qual deve retornar o primeiro item (Nó) da fila SEM remover esse item da fila
  - [ ] Caso a fila esteja vazia deverá retornar um None
  - [ ] Caso a fila possua um ou mais itens, o primeiro item (Nó) inserido na fila deve ser retornado pelo método
- [ ] **(1pts)** Implementar o método **peek_last()**, o qual deve retornar o último item (Nó) da fila SEM remover esse item da fila
  - [ ] Caso a fila esteja vazia deverá retornar um None
  - [ ] Caso a fila possua um ou mais itens, o último item (Nó) inserido na fila deve ser retornado pelo método

- [ ] **(3pts)** Implementar o método **display()**, o qual deve retornar uma lista com os valores (atributo dado) dos itens (Nó) inseridos na fila
  - [ ] Caso a fila esteja vazia deverá retornar uma lista vazia []
  - [ ] Caso a fila possua um ou mais itens, o primeiro elemento da lista deve ser o valor do dado do primeiro item (Nó) na fila, seguido das demais valores que compõem a fila (do primeiro ao último), nessa ordem
- [ ] **(1pts)** Implementar o método **size()**, o qual deve retornar um int
  - [ ] O método deverá retornar ZERO, caso a fila esteja vazia, ou, caso possua algum item na fila, o valor relativo à quantidade de itens presentes na fila