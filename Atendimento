from collections import deque

fila_de_atendimento = deque()

def adicionar_cliente(nome):
    """ Adiciona um cliente ao final da fila. """
    fila_de_atendimento.append(nome)
    print(f"Cliente {nome} adicionado ao final da fila.")

def atender_cliente():
    """ Remove e retorna o cliente que está no início da fila. """
    if fila_de_atendimento:
        cliente = fila_de_atendimento.popleft()
        print(f"Cliente {cliente} foi atendido.")
        return cliente
    else:
        print("Não há clientes para atender.")

# Exemplo de utilização:
adicionar_cliente("João")
adicionar_cliente("Maria")
adicionar_cliente("José")

atender_cliente()
atender_cliente()
atender_cliente()
atender_cliente()
