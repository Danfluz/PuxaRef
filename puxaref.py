import crossref_commons.retrieval
from random import randint

def formatador(doifinal):
    abnt = None
    try:
        publicacao = crossref_commons.retrieval.get_publication_as_json(doifinal)
        print('Sucesso.')
    except:
        print('Erro.')
        # print(f'Acesse: https://doi.org/{doifinal}')
        abnt = 'Erro-nao-ok'

    # print(publicacao)


    listautores = []

    continuar_script = True
    if abnt == 'Erro-nao-ok':
        continuar_script = False

    if continuar_script == True:
        try:
            authname = publicacao['author']
            authname = 'author'
        except KeyError:
            authname = 'editor'

        for author in publicacao[authname]:
            sobrenome = author['family'].upper() + ', '
            nome = author['given'] + '; '
            nome = sobrenome + nome
            listautores.append(nome)

        for ultimo in listautores:
            if ultimo == listautores[-1]:
                listautores.pop(-1)
                ultimo = ultimo.replace(';', '.')
                listautores.append(ultimo)

        autores = ''.join(listautores)

        for titulonome in publicacao['title']:
            titulo = titulonome + '. '
            break

        revista = False
        for revistanome in publicacao['container-title']:
            revista = revistanome + ','
            # revista = '\033[1m' + revista + '\033[0m'
            break
        if revista == False:
            revista = publicacao['publisher']

        try:
            publidata = publicacao['published-print']['date-parts']
            publidata = 'published-print'
        except KeyError:
            publidata = 'created'

        for meseano in publicacao[publidata]['date-parts']:
            try:
                mes = int(meseano[1])
            except:
                mes = randint(1, 12)
            if mes == 1:
                mes = 'jan'
            if mes == 2:
                mes = 'fev'
            if mes == 3:
                mes = 'mar'
            if mes == 4:
                mes = 'abr'
            if mes == 5:
                mes = 'mai'
            if mes == 6:
                mes = 'jun'
            if mes == 7:
                mes = 'jul'
            if mes == 8:
                mes = 'ago'
            if mes == 9:
                mes = 'set'
            if mes == 10:
                mes = 'out'
            if mes == 11:
                mes = 'nov'
            if mes == 12:
                mes = 'dez'
            ano = meseano[0]
            datapubli = mes + ', ' + str(ano) + '.'

        try:
            volume = 'v. ' + publicacao['volume'] + ', '
        except KeyError:
            volume = ''

        try:
            paginas = 'p. ' + publicacao['page'] + ', '
        except KeyError:
            paginas = ''

        try:
            edicao = 'n. ' + publicacao['issue'] + ', '
        except KeyError:
            edicao = ''

        # print(publicacao)
        ordem = autores, titulo, revista, volume, edicao, paginas, datapubli
        abnt = ''.join(ordem)

        return abnt

    elif continuar_script == False:
        return abnt

# print(crossref_commons.retrieval.get_publication_as_json('10.1590/1808-1657v77p3632010')) # Teste