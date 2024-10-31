import json 
import os
from time import sleep 

arquivo = os.path.join(os.path.dirname(__file__), 'crud_produtos.json')

def carregar_produtos():
    if not os.path.exists(arquivo):
        with open(arquivo, 'w') as f:
            json.dump([], f, indent=4)

    with open(arquivo, 'r') as f:
        return json.load(f)

def salvar_produtos(produtos):
    with open(arquivo, 'w') as f: 
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def adicionar_produto(id, nome, quantidade, valor):
    if not all([id, nome]) or quantidade < 0 or valor < 0:
        print("Atenção! Todos os campos devem ser preenchidos corretamente.")
        return 

    produtos = carregar_produtos()
    produtos.append({'id': id, 'nome': nome, 'quantidade': quantidade, 'valor': valor})
    
    salvar_produtos(produtos)
    print("Produto adicionado!")

def listar_produtos():
    produtos = carregar_produtos()

    if produtos:
        print("~" * 50)
        print("Todos os produtos neste estoque:")
        print("~" * 50)

        for produto in produtos:
            print(f"Produto ID: {produto['id']}\nNome: {produto['nome']}\nQuantidade: {produto['quantidade']}\nValor: {produto['valor']}")
            print("*" * 50)
    else:
        print("Não há produtos cadastrados.")

def atualizar_produtos():
    produtos = carregar_produtos()
    id_atualizar = input("Informe o código do produto que você deseja atualizar: ")

    produto_encontrado = next((p for p in produtos if p['id'] == id_atualizar), None)
    
    if produto_encontrado:
        nome = input("Digite o novo nome do produto: ")
        quantidade = int(input("Informe a nova quantidade do produto: "))
        valor = float(input("Informe o novo valor do produto: R$"))

        produto_encontrado.update({'nome': nome, 'quantidade': quantidade, 'valor': valor})
        
        salvar_produtos(produtos)
        print(f"\nProduto {nome} atualizado com sucesso!\n")
    else:
        print("\nProduto não encontrado!\n")

def deletar_produtos():
    produtos = carregar_produtos()
    id_produto = input("Digite o código do produto que você deseja apagar: ")
    produto_encontrado = next((p for p in produtos if p['id'] == id_produto), None)
    
    if produto_encontrado:
        produtos.remove(produto_encontrado)
        salvar_produtos(produtos)
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado.")

def menu_inicial():
    print(" ---->>> Teste Produtos <<<---- ")
    print("          1 - Manejar Produtos")
    print("          2 - Sair ")

def exibir_menu():
    print("\nMENU:")
    print("1. Adicionar produto")
    print("2. Listar produtos cadastrados")
    print("3. Atualizar produto")
    print("4. Deletar produto")
    print("5. Retornar ao menu principal")

def main():
    while True:
        menu_inicial()
        opcao_inicial = int(input("INFORME UMA OPÇÃO: "))

        if opcao_inicial == 1:
            while True: 
                exibir_menu()
                opcao = input("Indique o que deseja:\n>>> ")

                if opcao == '1':
                    id = input("Código de identificação do produto:\n>>> ")
                    nome = input("Nome do produto:\n>>> ")
                    quantidade = int(input("Quantidade do produto:\n>>> "))
                    valor = float(input("Valor do produto: R$\n>>> "))
                    adicionar_produto(id, nome, quantidade, valor)
                elif opcao == '2':
                    listar_produtos()
                elif opcao == '3':
                    atualizar_produtos()
                elif opcao == '4':
                    deletar_produtos()
                elif opcao == '5':
                    print("Você retornará ao menu principal.")
                    sleep(3)
                    break
                else:
                    print("Opção inválida. Por favor, tente novamente.")
        elif opcao_inicial == 2:
            print("Encerrando...")
            sleep(3)
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
