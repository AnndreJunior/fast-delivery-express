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

## Conceitos de POO utilizados

### 1. Herança

As classes Cliente e Entregador são subclasses de Pessoa.

### 2. Interface

Foi definido o contrato da classe relacionada ao cálculo de frete pela interface CalculoFreteInterface. Por meio delas várias classes poderão ter implementações diferentes do mesmo método.

### 3. Polimorfismo

Como as classes Cliente e Entregador herdam de Pessoa, então elas são polimórficas pois também podem ser do tipo Pessoa (tipo genérico de usuário do sistema). Como as classes CalculoFreteComum, calculoFreteExpresso e CalculoFretePremium sãos as implementações da interface CalculoFreteInterface, elas também são do tipo CalculoFreteInterface.

### 4. Encapsulamento

Praticamente todos os atributos das entidades são encapsuladas e são acessadas apenas por métodos que usam a anotação @property, menos as propriedades que necessitam ter seu estado modificado. Cada serviço mantém uma lista de dados encapsulada - funcionando com um banco de dados, mas em memória.

## Como executar o projeto

Primeiro verifique os requisitos, para isso [clique aqui](#tecnologias).
Para executar o projeto, execute os comandos a seguir:

```bash
git clone https://github.com/AnndreJunior/fast-delivery-express.git

cd fast-delivery-express

python main.py

python3 main.py # caso o comando "python" não seja encontrado
```
