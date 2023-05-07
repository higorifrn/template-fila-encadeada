##### ATENÇÃO: Não altere o código fonte desse arquivo #####

import os.path
import sys
from pytest import raises
from no import No
from fila import Fila


# ---- INÍCIO: teste método is_empty()

def test_is_empty_true():

    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    result = fila.is_empty()
    expected = True

    assert result == expected and fila.size() == 0


def test_is_empty_false():

    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila(3)
    fila.enqueue(1)
    fila.enqueue(2)

    result = fila.is_empty()
    expected = False

    assert result == expected and fila.size() == 2

# ---- FIM: teste método is_empty()


# ---- INÍCIO: teste método is_full()

def test_is_full_true():

    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila(1)
    fila.enqueue(1)

    result = fila.is_full()
    expected = True

    assert result == expected and fila.size() == 1


def test_is_full_false():

    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila(3)
    fila.enqueue(1)
    fila.enqueue(2)

    result = fila.is_full()
    expected = False

    assert result == expected and fila.size() == 2

# ---- FIM: teste método is_full()


# ---- INÍCIO: teste método enqueue() ---------------------------------------------------

def test_enqueue_em_pilha_cheia():

    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila(1)

    fila.enqueue(1)

    assert fila.peek_first().dado == 1
    with raises(Exception):
        fila.enqueue(2) # deve gerar erro


def test_enqueue_em_fila_vazia():

    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    assert fila.enqueue(2) == True and fila.peek_first().dado == 2


def test_enqueue_em_pilha_nao_cheia():

    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila(3)

    fila.enqueue(1)
    assert fila.peek_first().dado == 1
    fila.enqueue(2)
    assert fila.peek_first().dado == 1
    
# ---- FIM: teste método enqueue() -----------------------------------------------------


# ---- INÍCIO: teste método dequeue() --------------------------------------------------

def test_dequeue_sem_itens():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    with raises(Exception):
        fila.dequeue() # deve gerar erro


def test_dequeue_com_itens():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            fila.enqueue(item[:-1])

    expected = No('1')
    result = fila.dequeue()

    assert expected.dado == result.dado and fila.peek_first().dado == '2'


def test_dequeue_com_itens_ate_esvaziar():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            fila.enqueue(item[:-1])

    for x in range(5):
      fila.dequeue()

    with raises(Exception):
        fila.dequeue() # deve gerar erro

# ---- FIM: teste método dequeue() -----------------------------------------------------


# ---- INÍCIO: teste método peek_first() -----------------------------------------------

def test_peek_first_sem_itens():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    assert fila.peek_first() == None


def test_peek_first_sem_itens_apos_dequeue():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()
    fila.enqueue(1)
    fila.dequeue()

    assert fila.peek_first() == None


def test_peek_first_com_itens():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()
    fila.enqueue(1)
    fila.enqueue(2)

    expected = No(1)
    result = fila.peek_first()

    assert expected.dado == result.dado

# ---- FIM: teste método peek_first() --------------------------------------------------


# ---- INÍCIO: teste método peek_last() ------------------------------------------------

def test_peek_last_sem_itens():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    assert fila.peek_last() == None


def test_peek_last_sem_itens_apos_dequeue():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()
    fila.enqueue(1)
    fila.dequeue()

    assert fila.peek_last() == None


def test_peek_last_com_itens():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()
    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)

    expected = No(3)
    result = fila.peek_last()

    assert expected.dado == result.dado

# ---- FIM: teste método peek_last() ---------------------------------------------------


# ---- INÍCIO: teste método display() --------------------------------------------------

def test_display_com_elementos_string():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    with open('entrada_dados.txt') as reader:
        for item in reader:
            fila.enqueue(item[:-1])

    result = fila.display()
    expected = [
        "1",
        "2",
        "3",
        "4",
        "5",
    ]

    assert result == expected


def test_display_com_elementos_int():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)

    result = fila.display()
    expected = [
        1,
        2,
        3,
    ]

    assert result == expected


def test_display_sem_elementos_ao_criar_fila():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    result = fila.display()
    expected = []
    
    assert result == expected


def test_display_sem_elementos_ao_esvaziar_fila():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    fila.enqueue(1)
    fila.enqueue(2)
    fila.dequeue()
    fila.dequeue()

    result = fila.display()
    expected = []
    
    assert result == expected

# ---- FIM: teste método display() -----------------------------------------------------


# ---- INÍCIO: teste método size() -----------------------------------------------------

def test_size_ao_criar_fila():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    result = fila.size()
    expected = 0
    
    assert result == expected


def test_size_ao_inserir_itens():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    fila.enqueue(1)
    expected = 1
    assert fila.size() == expected

    fila.enqueue(1)
    expected = 2
    assert fila.size() == expected

    fila.enqueue(1)
    expected = 3
    assert fila.size() == expected


def test_size_ao_remover_itens():
    try:
        exists = os.path.exists("fila.py")
        assert exists == True
    except:
        sys.exit()

    fila = Fila()

    fila.enqueue(1)
    fila.enqueue(1)
    fila.enqueue(1)

    fila.dequeue()
    expected = 2
    assert fila.size() == expected

    fila.dequeue()
    expected = 1
    assert fila.size() == expected

    fila.dequeue()
    expected = 0
    assert fila.size() == expected

# ---- FIM: teste método size() --------------------------------------------------------
