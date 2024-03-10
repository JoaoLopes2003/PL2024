# TPC5: Máquina de Vending
## 2024-03-10

## Autor:
- A100594
- João Manuel Machado Lopes

## Resumo

O objetivo deste trabalho é construir uma máquina de vending capaz de responder aos seguintes inputs:

- **"LISTAR"** : O programa ao receber este input deverá apresentar ao cliente uma lista de todos os produtos disponíveis a serem comprados, incluindo nesta informação o id do produto, o seu nome e o seu preço.

- **"MOEDA 1e, 20c, 50c, ..."** : O programa recebe como input uma lista de valores associados a uma letra (e ou c) e adiciona a soma destes valores ao saldo do cliente. Importante salientar que este comando começa pela palavra *MOEDA* seguida de um espaço.

- **"SELECIONAR 1"** : O programa ao receber este input deverá verificar se o cliente tem saldo suficiente para comprar o produto indicado pelo mesmo através do seu id (neste caso *1*). Caso tenha devolve o saldo resultante da compra do produto e em caso de não ter saldo suficiente informa o mesmo disso. Importante salientar que este comando associado à compra de um produto começa sempre obrigatoriamente pela palavra *SELECIONAR*.

- **"SAIR"** : Este comando é utilizado pelo cliente quando já terminou a sua interação com a máquina de vending, ou seja, não deseja realizar mais nenhuma operação. Quando o cliente introduzir este input, antes de terminar a execução do programa deverá ser apresentado ao mesmo o troco.