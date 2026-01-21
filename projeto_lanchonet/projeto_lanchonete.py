#listas
pedidos = []


#função
def listar():
    produtos = []
    arquivo = open("produtos.txt", "r", encoding="utf-8")
    linhas = arquivo.readlines()
    for linha in linhas:
        dados = linha.strip().split(";")
        codigo = int(dados[0])
        nome = dados[1]
        preco = float(dados[2].replace(',', '.'))
        produtos.append([codigo, nome, preco])
    arquivo.close()
    return produtos

def usuario ():
    print("Qual o seu tipo de usúario ")
    print("1 - Administrador \n 2 - Cliente \n 0 - Sair")
    escolha_usuario = int(input("Digite: \n"))
    while(escolha_usuario == "" and escolha_usuario != 1 and escolha_usuario != 2 and escolha_usuario != 0):
        print("Tipo de usúario invalido, porfavor selecione um tipo válido \n")
        escolha_usuario = int(input("Digite: \n"))
    return escolha_usuario

def fazer_pedido(produtos):
    compra = 1
    nome = input("Digite seu nome: ")
    print("Olá, {}! Bem-vindo.".format(nome))
    produtos = listar()
    while(compra == 1):
        mostrar_cardapio(produtos)
        produto = int(input("Qual pedido você gostaria de comprar: \n"))
        for i in range(len(produtos)):
            if (produtos[i][0] == produto):
                print("Produto atual: {}".format(produtos[i]))
                conf_pedido = int(input("Tem certeza que quer selecionar esse produto? \n 1 para Sim \n 2 para não \n"))
                if(conf_pedido != 1 and conf_pedido != 2):
                    print("Opção invalida porfavor selecione corretamente")
                    conf_pedido = input("Tem certeza que quer selecionar esse produto? \n 1 para Sim \n 2 para não \n")
                elif(conf_pedido == 1):
                    print("Qual a quantidade que você gostaria de comprar? \n")
                    quantidade = int(input("Digite a quantidade: \n"))
                    pedidos.append((nome, produtos[i][1], produtos[i][2], quantidade))
                    print("Gostaria de efetuar mais um programa? \n")
                    continuar = int(input("1 - SIM \n 2 - Não \n Escolha: "))
                    if(continuar != 1 and continuar != 2):
                        print("Opção invalida porfavor selecione corretamente")
                        continuar = input("1 - SIM \n 2 - Não \n Escolha: \n")
                    if(continuar == 1):
                        print("Compra em processo")
                    elif(continuar == 2):
                        print("Obrigado pela compra! finalize sua compra digitando 0")
                        compra = 2
                elif(conf_pedido == 2):
                    print("Pedido não selecionado \n")     
        return pedidos

def finalizar_pedido(pedidos):
    valor_total = 0
    print("\n--- RESUMO DO SEU PEDIDO ---")
    if not pedidos:
        print("Nenhum item no pedido.")
        return

    for item in pedidos:
        subtotal_item = item[2] * item[3]
        print("{} x {} - R$ {:.2f} (Subtotal: R$ {:.2f})".format(item[3], item[1], item[2], subtotal_item))
        valor_total += subtotal_item
        
    print("Valor total do pedido: R$ {:.2f}".format(valor_total))


def mostrar_cardapio(produtos):
    print("\n---- CARDÁPIO ----")
    for p in produtos:
        print("Código: {} | Nome: {} | Preço: R${:.2f}".format(p[0], p[1], p[2]))
    print("-------------------\n")

def menu_usuario(produtos):
    produtos = listar()
    mostrar_cardapio(produtos)
    
    print("----MENU----")
    print("1 - Efetuar Pedido")
    print("0 - Finalizar pedido")
    op = int(input("Escolha uma opção: "))

    if(op == 1):
        fazer_pedido(produtos)
    elif(op == 0):
        print("Obrigado!!!")
    else:
        print("Opção indisponivel escolha novamente")
        op = int(input("Escolha uma opção: "))
    return op

def menu_adm(produtos):
    print("----MENU----")
    print("1 - Cadastrar novo produto")
    print("2 - Ver cardápio")
    print("3 - Alterar Produto")
    print("4 - Apagar produto")
    print("0 - Sair")
    op = int(input("Escolha uma opção: "))

    if(op == 1):
        cadastrar(produtos)
    elif(op == 2):
        mostrar_cardapio(produtos)
    elif(op == 3):
        alterar(produtos)
    elif(op == 4):
        apagar(produtos)
    elif(op == 0):
        print("Obrigado!!!")
    else:
        print("Número de escolha incorretp tente novamente")
        op = int(input("Escolha uma opção: "))
    return op

def cadastrar(produtos):
    loop =1
    while(loop == 1):
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        if len(produtos) == 0:
            codigo = 1
        else:
            codigo = produtos[-1][0] + 1
        produtos.append([codigo, nome, preco])
        salvar_produtos(produtos)
        print("gostaria de cadastrar mais um produto? \n")
        escolha = int(input("Digite 1 para sim e 2 para não: \n"))
        if(escolha == 1):
            print("Novo pedido em andamento")
        elif(escolha == 2):
            print("Processo de cadastro finalizado")
            loop = 0
        else:
            print("Opção inválida porfavor digite novamente")

    return codigo

def salvar_produtos(produtos):
    arquivo = open("produtos.txt", "w", encoding="utf-8")
    for p in produtos:
        linha = str(p[0]) + ";" + p[1] + ";" + str(p[2]) + "\n"
        arquivo.write(linha)
    arquivo.close()

def alterar(produtos):
    loop = 1
    while(loop == 1):
        altera = int(input("Qual o código do produto que você deseja alterar: \n"))
        for i in range(len(produtos)):
            if (produtos[i][0] == altera):
                print("Produto atual")
                novo_nome = input("Novo nome do produto: ")
                novo_preco = float(input("Novo preço do produto: "))
                produtos[i][1] = novo_nome
                produtos[i][2] = novo_preco
                salvar_produtos(produtos)
                print("Produto alterado com sucesso.")
                loop = 0
            elif(produtos[i][0] != altera):
                print("O seu código é invalido porfavor digite novamente")
            else:
                print("O seu código é invalido porfavor digite novamentea")

def apagar(produtos):
    loop = 1
    while(loop == 1):
        codigo = int(input("Digite o código do produto que deseja apagar: "))
        for i in range(len(produtos)):
            if (produtos[i][0] == codigo):
                print("Produto removido")
                produtos.pop(i)
                salvar_produtos(produtos)
                loop = 0
            elif (produtos[i][0] != codigo):
                print("O código digitado é inválido, porfavor digite novamente")


#codigo principal
inicio = 0
usuario_tipo = usuario()
produtos = listar()
while(inicio == 0):
    if(usuario_tipo == 1):
        op = menu_adm(produtos)
        if op == 0:
            escolha = input("Gostaria de finalizar: s ou n \n")
            if(escolha == "s" or escolha == "S"):
                inicio = 1
            elif(escolha == "n" or escolha == "N"):
                print("Processo ira continuar! \n")
            else:
                print("Opção inválida, porfavor digite novamente")
    elif(usuario_tipo == 2):
        op = menu_usuario(produtos)
        if op == 0:
            escolha_usu = input("Gostaria de finalizar: s ou n \n")
            if(escolha_usu == "s" or escolha_usu == "S"):
                finalizar_pedido(pedidos)
                inicio = 1
            elif(escolha_usu == "n" or escolha_usu == "N"):
                print("Processo ira continuar! \n")
            else:
                print("Opção inválida, porfavor digite novamente")
    elif(usuario_tipo == 0):
        print("Obrigado por usar nosso sistema!")
        inicio == 1
    else:
        print("Usuário inválido, porfavor tente novamente")
        usuario_tipo = usuario()


