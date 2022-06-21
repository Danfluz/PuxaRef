import pdfplumber


def encdoi(caminhopdf):
    naoencontroudoi = True
    with pdfplumber.open(caminhopdf) as temp:

        # doi = []
        # idx = 0
        pagdoi = 'xyz'
        if 'DOI:' in temp.pages[0].extract_text() or 'doi:' in temp.pages[0].extract_text() or 'doi.org' in temp.pages[0].extract_text():
            pagdoi = str(temp.pages[0].extract_text())
        else:
            for page in temp.pages:
                if 'DOI:' in page.extract_text() or 'doi:' in page.extract_text() or 'doi.org' in page.extract_text():
                    pagdoi = str(page.extract_text())
        if pagdoi == 'xyz':
            pagdoi = 'naoencontroudoi'
        temp.close()
        texto2 = None
        textodoi = ''
        for inhon in pagdoi.splitlines():
            if textodoi.startswith('10.'):
                break
            if 'DOI:' in inhon or 'doi:' in inhon or '10.' in inhon and '/' in inhon:
                textodoi = str(inhon)
                if not textodoi.startswith(('DOI:', 'doi:', 'https', 'doi.org', 'http:')):
                    textodoi = textodoi.split()
                    for texto in textodoi:
                        if '10.' in texto and '/' in texto:
                            texto2 = texto
                    if texto2 != None:
                        textodoi = texto2
                if type(textodoi) != str:
                    textodoi = f'Erro ao encontrar o DOI: {textodoi}'
                if textodoi.startswith('DOI: '):
                    textodoi = textodoi.strip('DOI: ')
                if textodoi.startswith('https://doi.org/'):
                    textodoi = textodoi.strip('https://doi.org/')
                if textodoi.startswith('http://doi.org/'):
                    textodoi = textodoi.strip('http://doi.org/')
                if textodoi.startswith('doi.org/'):
                    textodoi = textodoi.strip('doi.org/')
                if textodoi.startswith('doi:'):
                    textodoi = textodoi.strip('doi:')
                if textodoi.startswith('DOI:'):
                    textodoi = textodoi.strip('DOI:')
                if ' ' in textodoi:
                    textodoi = textodoi.strip(' ')
                if '	' in textodoi:
                    textodoi = textodoi.strip('	')
                if '‑' in textodoi:
                    textodoi = textodoi.replace('‑', '-')

                naoencontroudoi = False

            else:
                pass
    if naoencontroudoi is True:
        textodoi = 'Erro. Não encontrou DOI.'

    return textodoi
    #     textotemp = open("output.txt", "w+")
    #     textotemp.write(textodoi)
    #     textotemp.close()
    #
    #     textotemp = open("output.txt", "r")
    #     linhas = textotemp.readlines()
    #
    #     for linha in linhas:
    #
    #         if 'DOI:' in linha:
    #             doi.insert(idx, linha)
    #             idx += 1
    #             break
    #         elif '10.' in linha and '/' in linha:
    #             doi.insert(idx, linha)
    #             idx += 1
    #             break
    #
    #     textotemp.close()
    #     textotemp = open("output.txt", "w+")
    #     textotemp.write('')
    #     textotemp.close()
    #
    #     if len(doi) == 0:
    #         print('Erro.')
    #     else:
    #         tamanho_linha = len(doi)
    #
    #         for i in range(tamanho_linha):
    #             doifinal = doi[i]
    #
    #
    # print(f'Doi encontrado: {doifinal}')

# print(encdoi(r"C:\Users\steff\Downloads\Chen2021_Article_OnTheSporeOrnamentationOfTheMi.pdf")) # Teste