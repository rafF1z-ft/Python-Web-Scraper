import re
import threading
import requests
from bs4 import BeautifulSoup

DOMINIO = "https://django-anuncios.solyd.com.br"
URL_AUTO = f"{DOMINIO}/automoveis/"

LINKS = []
TELEFONES = []

def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f'Erro ao fazer requisição: Status Code {resposta.status_code}')
    except Exception as error:
        print('Erro ao fazer requisição:', error)
    return None

def parsing(resposta_html):
    try:
        return BeautifulSoup(resposta_html, 'html.parser')
    except Exception as error:
        print('Erro ao fazer parsing HTML:', error)
    return None

def encontrar_links(soup):
    try:
        cards_pai = soup.find("div", class_="ui three doubling link cards")
        cards = cards_pai.find_all("a") if cards_pai else []
        return [card['href'] for card in cards]
    except Exception as error:
        print('Erro ao encontrar links:', error)
    return []

def encontrar_telefone(soup):
    try:
        descricao_divs = soup.find_all("div", class_="sixteen wide column")
        descricao = descricao_divs[2].p.get_text().strip() if len(descricao_divs) > 2 else None
    except Exception as error:
        print('Erro ao requisitar descrição:', error)
        return None

    regex = re.findall(r"\(?0?([1-9]{2})\)?[ \-\.]?(9\d{4})[ \-\.]?(\d{4})", descricao)
    return regex if regex else []

def descobrir_numeros():
    while LINKS:
        try:
            link_anuncio = LINKS.pop(0)
            resposta_anuncio = requisicao(DOMINIO + link_anuncio)
            if resposta_anuncio:
                soup_anuncio = parsing(resposta_anuncio)
                if soup_anuncio:
                    telefones = encontrar_telefone(soup_anuncio)
                    if telefones:
                        for telefone in telefones:
                            print(f'Telefone encontrado: {telefone}')
                            TELEFONES.append(telefone)
                        salvar(telefones)
        except Exception as error:
            print('Erro durante a descoberta de números:', error)

def salvar(telefones):
    try:
        with open("telefones.csv", "a") as arquivo:
            for telefone in telefones:
                arquivo.write(f'{telefone[0]}{telefone[1]}{telefone[2]}\n')
    except Exception as error:
        print("Erro ao salvar arquivo:", error)

if __name__ == "__main__":
    resposta_busca = requisicao(URL_AUTO)
    if resposta_busca:
        soup_busca = parsing(resposta_busca)
        if soup_busca:
            LINKS = encontrar_links(soup_busca)
            threads = [threading.Thread(target=descobrir_numeros) for _ in range(5)]
            for t in threads:
                t.start()
            for t in threads:
                t.join()
