import json
import os

arquivo_nome = 'produtos.json'

# Carrega os produtos do arquivo JSON
def carregar_produtos():
    try:
        with open(arquivo_nome, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Salva a lista de produtos no arquivo JSON
def salvar_produtos(produtos):
    with open(arquivo_nome, 'w') as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

def atualizar_produtos():
    produtos = carregar_produtos()
    id_atualizar = input("Informe o código do produto que você deseja atualizar: ")

    
    produto_encontrado = next((p for p in produtos if p['id'] == id_atualizar), None)

    if produto_encontrado:
        novo_nome = input("Digite o novo nome do produto: ")
        novo_id = input("Digite o novo ID para o produto: ")
        novo_valor_produto = input("Digite o novo valor em R$: ")
        nova_qtd_produtos = input("Digite a nova quantidade no estoque: ")

        produto_encontrado['nome'] = novo_nome
        produto_encontrado['id'] = novo_id
        produto_encontrado['valor'] = float(novo_valor_produto)
        produto_encontrado['quantidade'] = int(nova_qtd_produtos)

        salvar_produtos(produtos)
        print(f"\nProduto '{novo_nome}' foi alterado com sucesso!")
    else:
        print("Produto não encontrado :/")

def deletar_produtos():
    produtos = carregar_produtos()
    id_produto = input("Digite o código do produto que você deseja apagar: ")
    produto_encontrado = next((p for p in produtos if p['id'] == id_produto), None)
    
    if produto_encontrado:
        produtos.remove(produto_encontrado)
        salvar_produtos(produtos)
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado :/")



