print('\nOlá, sejam bem-vindes ao Easycheck ✔\numa solução organizacional para os centros cirúrgicos.\n')

login = dict()
cirurgias = dict()
cirurgias_confirmadas = list()
login['maria'] = 123456
login['joao'] = 654321

while True:
    print("Digite no usuário 'sair' para encerrar o programa.")
    usuario = input("Usuário: ")
    if usuario == 'sair':
        break
    senha = input('Senha: ')

    if usuario in login:
        if senha == str(login[usuario]):
            while True:
                print("\nEscolha uma opção:")
                print("1: Listar cirugias")
                print("2: Cadastrar uma cirugia nova")
                print("3: Consultar os detalhes de uma cirurgia")
                print("4: Editar os dados de uma cirurgia")
                print("5: Marcar uma cirurgia como confirmada e removê-la da lista de pendências")
                print("6: Exibir lista de cirurgias confirmadas ✔")
                print("-1: Encerrar o programa")

                opcao = int(input('Opção: '))
                if opcao == 1:
                    for nome_cirurgia in cirurgias:
                        print(nome_cirurgia)
                    print("\n")

                elif opcao == 2:
                    nome_cirurgia = input("Nome da cirurgia: ").title()
                    sala = int(input("Número da sala: "))
                    horario = input("Horário: ")

                    cirurgia = {'nome_cirurgia': nome_cirurgia, 'sala': sala, 'horario': horario}
                    cirurgias[nome_cirurgia] = cirurgia

                elif opcao == 3:
                    nome_cirurgia = input("Informe o nome da cirurgia: ").title()

                    cirurgia = cirurgias.get(nome_cirurgia, None)
                    if cirurgia is not None:
                        print("Nome da cirurgia:", cirurgia['nome_cirurgia'])
                        print("Número da sala da cirurgia:", cirurgia['sala'])
                        print("Horário:", cirurgia['horario'])
                    else:
                        print("Cirurgia não encontrada")

                    print()

                elif opcao == 4:
                    nome_cirurgia = input("Informe o nome da cirurgia: ").title()

                    novo_nome = input("Novo Nome: ").title()
                    nova_sala = int(input("Sala: "))
                    novo_horario = input("Horário: ")


                    cirurgia = cirurgias.pop(nome_cirurgia, None)
                    if cirurgia is None:
                        print("Cirurgia não encontrada")
                    else:
                        cirurgia['nome_cirurgia'] = novo_nome
                        cirurgia['sala'] = nova_sala
                        cirurgia['horario'] = novo_horario
                        cirurgias[novo_nome] = cirurgia

                elif opcao == 5:
                    nome_cirurgia = input("Informe o nome da cirurgia: ").title()


                    cirurgia = cirurgias.pop(nome_cirurgia, None)
                    if cirurgia is None:
                        print("Cirurgia não encontrada")
                    else:
                        print("A cirurgia {0} foi removida da lista de pendências e marcada como confirmada.".format(cirurgia['nome_cirurgia']))
                        cirurgias_confirmadas.append(nome_cirurgia)

                    print()

                elif opcao == 6:
                    if len(cirurgias_confirmadas) == 0:
                        print('Nenhuma cirurgia foi confirmada')
                    else:
                        print('Lista de cirurgias confirmadas ✔')
                        print(cirurgias_confirmadas)

                elif opcao == -1:
                    break

        else:
            print("senha incorreta")
    else:
        print('usuario incorreto')
