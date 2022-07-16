import PySimpleGUI as sg
from encontrardoi import encdoi
from puxaref import formatador

#Menu principal

def menu():
    sg.theme('lightgreen')
    layout = [
        [sg.Text('', size=(35, 5)), sg.Text('Criador de Referencias',size=(25,1),font=('Arial, 20')), sg.T('PuxaRef  ver. 1.1', font=('Arial, 10'))],
        [sg.Text('', size=(48, 5)), sg.Image(r"img\iconpaper.png",size=(75,75),subsample=(5))],
        [sg.Text('', size=(30, 1)), sg.Text('', size=(35, 1)), sg.Text('', size=(41, 1))],
        [sg.Text('', size=(35, 1)), sg.Text('Escolha o PDF:', size=(15, 1), font='Arial, 15'), sg.FilesBrowse('Selecione', file_types=(("PDFs de Artigos", "*.pdf"),), size=(15, 1), key='arquivopdf')],
        [sg.Text('', size=(48, 5)), sg.Submit('Formatar', size=(8, 1),key='format'), sg.Text('', size=(41, 1))],
        [sg.Text('', size=(35, 2)), sg.Text('Referências (ABNT)', size=(36, 1), font='Arial, 18'), sg.Text('', size=(41, 1))],
        [sg.Text('', size=(15, 5)), sg.Multiline('', size=(80, 10), key='referenciapronta'), sg.Text('', size=(41, 1))]
    ]

    return sg.Window('PuxaRef - Criador de Referencias', layout, size=(900,600), resizable=True, finalize=True, icon=r"img\iconpaper.ico")

programa = menu()


organizaref = []


while True:
    event, values = programa.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'format':
        arquivospdfs = values['arquivopdf'].split('.pdf')
        for arqpdf in arquivospdfs:

            if arqpdf == '':
                pass
            else:
                arqpdf = arqpdf + '.pdf'
                if arqpdf[0] == ';':
                    arqpdf = arqpdf[1:]
                caminhodoarquivo = encdoi(arqpdf)
                arqpdfcopy = arqpdf
                try:
                    ref1 = str(formatador(caminhodoarquivo))
                    if ref1 == "Erro-nao-ok":
                        ref1 = f'>{arqpdfcopy}: Erro ao criar referencia'
                    organizaref.append(ref1 + '\n\n')
                except:
                    ref1 = f'>{arqpdfcopy}: Erro1 ao criar referencia\n\n'
                    organizaref.append(ref1)

        organizaref.sort()
        referenciapronta = ''.join(organizaref)
        organizaref = []

        programa['referenciapronta'].update(referenciapronta)
        referenciapronta = ''




programa.close()