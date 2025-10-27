biblioteca = []
proximo_id = 1

def menu():
    print('\n')
    print('*'*30)
    print('      SISTEMA BIBLIOTECA')
    print('*'*30)
    print('1 - Cadastrar Livro')
    print('2 - Listar Livros')
    print('3 - Buscar Livro')
    print('4 - Atualizar Livro')
    print("5 - Remover Livro")
    print('6 - Estatisticas')
    print('0 - Sair')
    print('*'*30)
    print('8 - Livros Predefinidos')#Livros Predefinidos para teste de codigo

    while True:
        opcao = input('Escolha a opção: ')
        if opcao.isdigit():
            return int(opcao)
        else:
            print('ERRO: Opção invalido')

def livro_pred():
    '''
    Adiciona livros Pré-definidos à biblioteca
    '''
    autores_tit = ["Machado de assis", "William Shakespeare","Clarice Lispector","Monteiro Lobato", "Stephen King"]
    livros_tit = ["Dom Casmurro", "Romeu e Julieta","A Hora da Estrela", "O Saci", "It, A coisa"]
    ano_tit = [1899, 1597, 1977, 1921, 1986]
    preco_tit = [15, 35, 25, 56, 70]
    global proximo_id

    for i in range(0, len(livros_tit)):
        novo_livro = {
            'id': proximo_id,
            'titulo': livros_tit[i],
            'autor': autores_tit[i],
            'ano': int(ano_tit[i]),
            'preco': preco_tit[i],
        }

        biblioteca.append(novo_livro)
        proximo_id += 1
def cadastrar_livro():
    global proximo_id

    print('\n--- CADASTRAR LIVRO ---')

    while True:
        titulo = input('Informe o Titulo do Livro: ').strip().capitalize()
        if titulo:
            break
        print('ERRO: Titulo não pode ficar vazio!')

    autor = input('Informe o Autor(DEIXAR VAZIO SERÁ CONSIDERADO AUTOR DESCONHECIDO): ').strip().capitalize()
    if not autor:
        autor = 'Autor Desconhecido'

    while True:
        ano = input("Informe o Ano de Publicação: ").strip()
        if ano.isdigit() and len(ano) <= 4:
            break
        print('ERRO: Informe uma Data Válida(4 digitos)!')

    while True:
        preco_input = input('Informe o Preço do Livro R$: ').strip()
        try:
            preco = float(preco_input)
            if preco >= 0:
                break
            else:
                print('ERRO: O PREÇO NÃO PODE SER NEGATIVO!')
        except ValueError:
            print("ERRO: Digite um valor válido(Ex: 35,98)!")

    for livro in biblioteca:
        if (livro['titulo'].lower() == titulo.lower() and
            livro['autor'].lower() == autor.lower()):
            print('ERRO: Este Livro já está Cadastrado!!')
            return False

    novo_livro = {
        'id': proximo_id,
        'titulo': titulo,
        'autor': autor,
        'ano': int(ano),
        'preco': preco
    }

    biblioteca.append(novo_livro)
    proximo_id += 1

    print("SUCESSO!: Livro {} Cadastrado com sucesso! ID: {}".format(titulo,novo_livro['id']))
    return True

def listar_livros():
    print("\n --- TODOS OS LIVROS CADASTRADOS ---")

    if not biblioteca:
        print('\n--- NENHUM LIVRO ENCONTRADO ---')
        return

    entrada = input('\n******************************\nInforme como quer Listrar os Livros:\n1 - ID\n2 - Título\n3 - Autor\n4 - Ano\n5 - Preço\n******************************\nInforme a Opção Desejada: ').strip()
    if entrada == '1' or entrada == 'id':
        entrada = 'id'
    elif entrada == '2' or entrada == 'titulo':
        entrada = 'titulo'
    elif entrada == '3' or entrada == 'autor':
        entrada = 'autor'
    elif entrada == '4' or entrada == 'ano':
        entrada = 'ano'
    elif entrada == '5' or entrada == 'preco' or entrada == 'preço':
        entrada = 'preco'
    else:
        print('ERRO: Opção Invalida!')
        return

    livros_ordenados = sorted(biblioteca, key=lambda x: x[entrada])

    for livro in livros_ordenados:
        print(f'ID: {livro["id"]} | {livro["titulo"]} | {livro["autor"]} | {livro["ano"]} | {livro["preco"]:.2f}')

    print(f'\nTotal de Livros: {len(biblioteca)}')

def buscar_livro():
    print('\n--- BUSCAR LIVRO ---')

    if not biblioteca:
        print('\n--- NENHUM LIVRO ENCONTRADO ---')
        return

    termo = input('Informe o Título ou Autor do Livro para Buscar: ').strip().lower()

    if not termo:
        print('ERRO: Digite algo para Buscar!')
        return

    livros_encontrados = []
    for livro in biblioteca:
        if (termo in livro['titulo'].lower() or
            termo in livro['autor'].lower()):
            livros_encontrados.append(livro)

    if livros_encontrados:
        print(f'Encontrados: {len(livros_encontrados)} livro(s):')
        for livro in livros_encontrados:
            print(f'ID: {livro['id']} | {livro['titulo']} | {livro['autor']} | {livro['ano']} | {livro['preco']:.2f}')
    else:
        print('Nenhum livro encontrado com a Informação {}'.format(termo))

def atualizar_livro():
    print('\n--- ATUALIZAR LIVRO ---')

    if not biblioteca:
        print('\n--- NENHUM LIVRO ENCONTRADO ---')
        return

    while True:
        id_input = input('\nInforme o ID do Livro para Atualizar: ').strip()
        if id_input.isdigit():
            id_livro = int(id_input)
            break
        print('ERRO: INFORME UM ID VALIDO!')

    livro_encontrado = None
    for livro in biblioteca:
        if livro['id'] == id_livro:
            livro_encontrado = livro
            break

    if not livro_encontrado:
        print('ERRO: Nenhum livro encontrado!')
        return

    print(f'Livro Encontrado: {livro_encontrado}')
    print('************************************************************\nDEIXE EM BRANCO AS INFORMAÇÕES QUE DESEJA MANTER!')

    novo_titulo = input(f'Novo titulo [{livro_encontrado["titulo"]}]:').strip().capitalize()
    if novo_titulo:
        livro_encontrado['titulo'] = novo_titulo

    novo_autor = input(f'Novo Autor [{livro_encontrado["autor"]}]:').strip().lower()
    if novo_autor:
        livro_encontrado['autor'] = novo_autor

    while True:
        novo_ano = input(f'Novo Ano [{livro_encontrado["ano"]}]:').strip().lower()
        if not novo_ano:
            break

        if novo_ano.isdigit() and len(novo_ano) >= 4:
            livro_encontrado['ano'] = int(novo_ano)
            break
        print('ERRO: Digite o Ano valido!')

    while True:
        novo_preco = input(f'Novo Preço [{livro_encontrado["preco"]:.2f}]:').strip().lower()
        if not novo_preco:
            break
        try:
            preco = float(novo_preco)
            if preco >= 0:
                livro_encontrado['preco'] = preco
                break
            else:
                print('ERRO: O PREÇO NÃO PODE SER NEGATIVO!')
        except ValueError:
            print('ERRO: Digite um valor Válido!')

def remover_livro():
    print('\n--- REMOVER LIVRO ---')

    if not biblioteca:
        print('\n--- NENHUM LIVRO ENCONTRADO ---')
        return

    while True:
        id_input = input('Informe o ID do Livro para Remover: ')
        if id_input.isdigit():
            id_livro = int(id_input)
            break
        print('ERRO: INFORME UM ID VALIDO!')

    for i, livro in enumerate(biblioteca):
        if livro['id'] == id_livro:
            confirmacao = input(f'TEM CERTEZA QUE DESEJA REMOVER [{livro["titulo"]}]? (S/N)').strip().lower()
            if confirmacao == 's':
                livro_removido = biblioteca.pop(i)
                print(f'SUCESSO: Livro[{livro_removido}] removido com sucesso!')
                return True
            else:
                print('--- REMOÇÃO CANCELADA ---')
                return False

    print('ERRO: LIVRO NÃO ENCONTRADO!')
    return False

def mostrar_estatisticas():
    print('\n--- ESTATISTICAS DA BIBLIOTECA ---')

    if not biblioteca:
        print('\n--- NENHUM LIVRO ENCONTRADO ---')
        return

    total_livros = len(biblioteca)
    precos = [livro['preco'] for livro in biblioteca]
    anos = [livro['ano'] for livro in biblioteca]

    print(f'Total de Livros: {total_livros}')
    print(f'Livro mais Caro: R${max(precos)}')
    print(f'Livro mais Barato: R${min(precos)}')
    print(f'Livro mais Antigo: {min(anos)}')
    print(f'Livro mais Recente: {max(anos)}')

    autores = {}
    for livro in biblioteca:
        autor = livro['autor']
        autores[autor] = autores.get(autor, 0) + 1

    if autores:
        autor_mais_livros = max(autores, key=autores.get)
        print(f'Autor com mais Livros: {autor_mais_livros} ({autores[autor_mais_livros]} Livros)')

def main():
    print('SISTEMA DE BIBLIOTECA')

    while True:
        opcao = menu()

        if opcao == 1:
            cadastrar_livro()
        elif opcao == 2:
            listar_livros()
        elif opcao == 3:
            buscar_livro()
        elif opcao == 4:
            atualizar_livro()
        elif opcao == 5:
            remover_livro()
        elif opcao == 6:
            mostrar_estatisticas()
        elif opcao == 8:
            livro_pred()
        elif opcao == 0:
            print('Obrigado por usar meu programa! (ASS: Otaviano)')
            print('ENCERRANDO PROGRAMA!')
            print('Até Logo!')
            break
        else:
            print('ERRO: OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')

if __name__ == '__main__':
    main()
