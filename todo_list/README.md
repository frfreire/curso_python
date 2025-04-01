# Desafio de Programação: Lista de Tarefas

## Introdução

Este repositório contém um desafio de programação em Python projetado para praticar conceitos fundamentais como variáveis, estruturas condicionais, loops e funções. O objetivo é desenvolver um sistema simples de lista de tarefas (to-do list) usando a metodologia Coding Dojo.

## O que é um Coding Dojo?

Um Coding Dojo é uma metodologia de aprendizagem colaborativa onde os participantes se reúnem para resolver um desafio de programação em pares, alternando funções periodicamente. O formato típico inclui:

- **Piloto**: Pessoa que está codificando
- **Copiloto**: Pessoa que está orientando o piloto
- **Plateia**: Restante dos participantes, que observam e podem contribuir

A cada intervalo definido (geralmente 5-7 minutos), os papéis são alterados: o piloto volta para a plateia, o copiloto se torna piloto, e alguém da plateia se torna o novo copiloto.

## Descrição do Desafio

O desafio consiste em construir um sistema de lista de tarefas com as seguintes funcionalidades:

1. Adicionar novas tarefas
2. Visualizar todas as tarefas
3. Marcar tarefas como concluídas
4. Interface de menu interativa

O sistema utiliza conceitos como:
- Listas e dicionários para armazenamento de dados
- Funções para organizar o código
- Estruturas condicionais para tomada de decisões
- Loops para repetições e interação com o usuário

## Estrutura do Projeto

O projeto está dividido em fases progressivas:

### Fase 1: Adicionar Tarefas (15 minutos)
- Implementar uma lista para armazenar as tarefas
- Criar função para adicionar novas tarefas
- Validar entrada do usuário

### Fase 2: Visualizar Tarefas (15 minutos)
- Implementar função para exibir todas as tarefas
- Tratar caso de lista vazia
- Exibir numeração e formatação adequadas

### Fase 3: Marcar Tarefas como Concluídas (20 minutos)
- Modificar estrutura para armazenar status da tarefa
- Implementar função para atualizar status
- Melhorar visualização para mostrar tarefas concluídas

### Fase 4: Menu Interativo (20 minutos)
- Criar interface de menu usando loop
- Integrar todas as funções anteriores
- Implementar opção de saída

## Código Inicial

```python
# Sistema de Lista de Tarefas
# Código inicial

# Lista para armazenar as tarefas
tarefas = []

def menu_principal():
    """Exibe o menu principal e processa a escolha do usuário."""
    while True:
        print("\n===== LISTA DE TAREFAS =====")
        print("1. Adicionar nova tarefa")
        print("2. Ver todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")
        
        opcao = input("\nEscolha uma opção (1-4): ")
        
        # Seu código aqui para processar a opção escolhida

# Funções a serem implementadas:
# adicionar_tarefa()
# ver_tarefas()
# marcar_como_concluida()

# Iniciar o programa
if __name__ == "__main__":
    menu_principal()
```

## Funcionalidades Extras (Bônus)

Caso o grupo conclua o desafio básico antes do tempo previsto, sugerimos implementar recursos adicionais:

- Sistema de prioridades para as tarefas (alta, média, baixa)
- Função para remover tarefas
- Filtrar tarefas por status ou prioridade
- Salvar/carregar tarefas em um arquivo

## Sistema de Avaliação

A avaliação será baseada nos seguintes critérios:

### Por Fase (80 pontos)
- **Fase 1**: 20 pontos
- **Fase 2**: 15 pontos
- **Fase 3**: 20 pontos
- **Fase 4**: 25 pontos

### Colaboração (20 pontos)
- Participação ativa: 5 pontos
- Comunicação efetiva: 5 pontos
- Contribuições relevantes: 5 pontos
- Respeito às regras do Dojo: 5 pontos

### Bônus (até 10 pontos extras)
- Implementação de funcionalidades adicionais: 5 pontos
- Código bem organizado e comentado: 5 pontos

## Como Executar

1. Clone este repositório
2. Execute o script Python:
   ```
   python todo.py
   ```

## Requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa é necessária

## Dicas para os Participantes

1. Comece com funcionalidades simples e teste-as frequentemente
2. Use comentários para documentar seu código
3. Pense na experiência do usuário: mensagens claras, validações adequadas
4. Não se preocupe em implementar todos os recursos avançados de uma vez
5. Lembre-se que o objetivo não é apenas concluir o desafio, mas aprender e colaborar

---

Boa sorte e bom coding!