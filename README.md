# Fast Delivery Express

## Descrição

O projeto <b>Fast Delivery Express</b> consistem em um sistema para gerenciar entregas.
Ele permite controlar os clientes cadastrados, entregadores, pedidos, tipos de entrega, status das entregas, histórico de pedidos e calcula o frete.

## Tecnologias

- Python 3
- Git
- GitHub

## Estrutura de pastas

O projeto usará a tradicional estrutura em camadas da seguinte forma:

```
fast-delivery-express
  main.py
  models/
    ...
  interfaces/
    ...
  services/
    ...
  utils/
    ...
```

### 1. main.py

Será o entry point do sistema.

### 2. models

É onde ficarão as entidades de negócio do sistema, como cliente, entregador, pedido, entrega...

### 3. interfaces

Contratos abstratos do sistema. Aqui ficam as definições de métodos que outras classes são obrigadas a seguir.

### 4. services

Aqui ficam implementadas as regras de negócio e orquestra a comunicação entre modelos, interfaces e utilitários.

### 5. utils

Funções auxiliares e genéricas. Aqui ficarão implementações genéricas, como validações simples, para fins de reutilização.

## Como executar o projeto

Primeiro verifique os requisitos, para isso [clique aqui](#tecnologias).
Para executar o projeto, execute os comandos a seguir:

```bash
git clone https://github.com/AnndreJunior/fast-delivery-express.git

cd fast-delivery-express

python main.py

python3 main.py # caso o comando "python" não seja encontrado
```
