# Web Scraper Django Anúncios

Um web scraper desenvolvido em Python para extrair dados de anúncios de veículos do site Django Anúncios. Este scraper é projetado para realizar buscas eficientes e extração de informações de forma eficaz.

## Funcionalidades

- **Extração de Links:** Coleta todos os links dos anúncios de veículos.
- **Coleta de Telefones:** Busca e extrai números de telefone dos anúncios.
- **Persistência de Dados:** Salva os números de telefone encontrados em um arquivo CSV.

## Requisitos

- Python 3.11.2
- Arquivo `requirements.txt` com as dependências necessárias.

## Instalação

1. **Clone o repositório:**

    ```bash
    git clone git@github.com:rafF1z-ft/Python-Web-Scraper.git
    ```

2. **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

## Uso

Execute o script para iniciar a extração de dados.

### Exemplo de Comando

- **Executar o scraper:**

    ```bash
    python main.py
    ```

## Arquivos Gerados

- `telefones.csv`: Arquivo contendo os números de telefone extraídos dos anúncios.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
