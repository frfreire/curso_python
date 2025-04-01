# Sistema de Lista de Tarefas

# Lista para armazenar as tarefas
# Cada tarefa será um dicionário com 'descricao', 'concluida' e 'prioridade'
tarefas = []


# Fase bônus - leitura de um arquivo de texto
def carregar_tarefas():
    """Tenta carregar tarefas de um arquivo, se existir."""
    try:
        with open("tarefas.txt", "r") as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                partes = linha.strip().split("|")
                if len(partes) >= 3:
                    tarefa = {
                        "descricao": partes[0],
                        "concluida": partes[1] == "True",
                        "prioridade": partes[2]
                    }
                    tarefas.append(tarefa)

            print(f"{len(tarefas)} tarefas carregadas do arquivo.")
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrado. Iniciando com lista vazia.")
    except Exception as e:
        print(f"Erro ao carregar tarefas: {e}")

# Funcionalidade bônus - gravação um arquivo de texto
def salvar_tarefas():
    """Salva as tarefas em um arquivo de texto."""
    try:
        with open("tarefas.txt", "w") as arquivo:
            for tarefa in tarefas:
                linha = f"{tarefa['descricao']}|{tarefa['concluida']}|{tarefa['prioridade']}\n"
                arquivo.write(linha)
        print("Tarefas salvas com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")


# Fase 1: Adicionar Tarefas
def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista."""
    print("\n=== Adicionar Nova Tarefa ===")
    descricao = input("Digite a descrição da tarefa: ").strip()

    # Validação simples: não permitir tarefas vazias
    if descricao == "":
        print("Erro: A descrição da tarefa não pode estar vazia.")
        return

    # Selecionar prioridade
    print("\nPrioridade:")
    print("1. Alta")
    print("2. Média")
    print("3. Baixa")

    prioridade_escolhida = ""
    while prioridade_escolhida == "":
        opcao = input("Escolha a prioridade (1-3): ")
        if opcao == "1":
            prioridade_escolhida = "Alta"
        elif opcao == "2":
            prioridade_escolhida = "Média"
        elif opcao == "3":
            prioridade_escolhida = "Baixa"
        else:
            print("Opção inválida. Escolha entre 1 e 3.")

    prioridade = prioridade_escolhida

    # Criar um dicionário para a nova tarefa
    nova_tarefa = {
        "descricao": descricao,
        "concluida": False,
        "prioridade": prioridade
    }

    # Adicionar à lista de tarefas
    tarefas.append(nova_tarefa)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

    # Salvar tarefas após a adição
    salvar_tarefas()
# Fase 2: Visualizar Tarefas
def ver_tarefas():
    """Mostra todas as tarefas na lista."""
    print("\n=== Lista de Tarefas ===")

    # Verificar se a lista está vazia
    if not tarefas:
        print("Não há tarefas cadastradas.")
        return

    # Mostrar todas as tarefas com seu status e prioridade
    for i, tarefa in enumerate(tarefas, 1):
        status = "✓" if tarefa["concluida"] else " "
        # Cores para as prioridades (funciona em terminais que suportam ANSI)
        cor_inicio = ""
        cor_fim = "\033[0m"

        if tarefa["prioridade"] == "Alta":
            cor_inicio = "\033[91m"  # Vermelho
        elif tarefa["prioridade"] == "Média":
            cor_inicio = "\033[93m"  # Amarelo
        elif tarefa["prioridade"] == "Baixa":
            cor_inicio = "\033[92m"  # Verde

        print(f"{i}. [{status}] {cor_inicio}[{tarefa['prioridade']}]{cor_fim} {tarefa['descricao']}")

# Fase 3: Marcar Tarefas como Concluídas
def marcar_como_concluida():
    """Marca uma tarefa como concluída."""
    # Primeiro, mostrar as tarefas para o usuário
    ver_tarefas()

    # Verificar se existem tarefas para marcar
    if not tarefas:
        return

    print("\n=== Marcar Tarefa como Concluída ===")
    try:
        numero = int(input("Digite o número da tarefa a ser concluída: "))

        # Verificar se o número é válido
        if numero < 1 or numero > len(tarefas):
            print(f"Erro: Digite um número entre 1 e {len(tarefas)}.")
            return

        # Marcar a tarefa como concluída
        indice = numero - 1
        if tarefas[indice]["concluida"]:
            print(f"A tarefa '{tarefas[indice]['descricao']}' já está concluída.")
        else:
            tarefas[indice]["concluida"] = True
            print(f"Tarefa '{tarefas[indice]['descricao']}' marcada como concluída!")

            # Salvar tarefas após a modificação
            salvar_tarefas()

    except ValueError:
        print("Erro: Por favor, digite um número válido.")

# Funcionalidade bônus - remover tarefa da lista
def remover_tarefa():
    """Remove uma tarefa da lista."""
    # Primeiro, mostrar as tarefas para o usuário
    ver_tarefas()

    # Verificar se existem tarefas para remover
    if not tarefas:
        return

    print("\n=== Remover Tarefa ===")
    try:
        numero = int(input("Digite o número da tarefa a ser removida: "))

        # Verificar se o número é válido
        if numero < 1 or numero > len(tarefas):
            print(f"Erro: Digite um número entre 1 e {len(tarefas)}.")
            return

        # Remover a tarefa
        indice = numero - 1
        tarefa_removida = tarefas.pop(indice)
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso!")

        # Salvar tarefas após a remoção
        salvar_tarefas()

    except ValueError:
        print("Erro: Por favor, digite um número válido.")

# Funcionalidade bônus - mostrar tarefas filtradas por prioridade
def filtrar_por_prioridade():
    """Mostra tarefas filtradas por prioridade."""
    print("\n=== Filtrar por Prioridade ===")
    print("1. Alta")
    print("2. Média")
    print("3. Baixa")
    print("4. Todas")

    opcao = input("Escolha a prioridade a filtrar (1-4): ")

    prioridade_filtro = None
    if opcao == "1":
        prioridade_filtro = "Alta"
    elif opcao == "2":
        prioridade_filtro = "Média"
    elif opcao == "3":
        prioridade_filtro = "Baixa"
    elif opcao == "4":
        ver_tarefas()
        return
    else:
        print("Opção inválida.")
        return

    print(f"\n=== Tarefas com Prioridade {prioridade_filtro} ===")
    encontrou = False

    for i, tarefa in enumerate(tarefas, 1):
        if tarefa["prioridade"] == prioridade_filtro:
            encontrou = True
            status = "✓" if tarefa["concluida"] else " "
            print(f"{i}. [{status}] {tarefa['descricao']}")

    if not encontrou:
        print(f"Não há tarefas com prioridade {prioridade_filtro}.")


# Fase 4: Menu Interativo
def menu_principal():
    """Exibe o menu principal e processa a escolha do usuário."""
    # Carregar tarefas ao iniciar
    carregar_tarefas()

    while True:
        print("\n===== LISTA DE TAREFAS =====")
        print("1. Adicionar nova tarefa")
        print("2. Ver todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Filtrar por prioridade")
        print("6. Sair")

        opcao = input("\nEscolha uma opção (1-6): ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            ver_tarefas()
        elif opcao == "3":
            marcar_como_concluida()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            filtrar_por_prioridade()
        elif opcao == "6":
            print("Obrigado por usar o sistema de Lista de Tarefas!")
            # Garantir que as tarefas são salvas antes de sair
            salvar_tarefas()
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção entre 1 e 6.")


# Iniciar o programa
if __name__ == "__main__":
    print("Bem-vindo ao Sistema de Lista de Tarefas Avançado!")
    menu_principal()