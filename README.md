# Web Scraper Django Anúncios

Um web scraper desenvolvido em Python para extrair dados de anúncios de veículos do site Django Anúncios. Este scraper é projetado para realizar buscas eficientes e extração de informações de forma eficaz.

## Funcionalidades

- **Extração de Links:** Coleta todos os links dos anúncios de veículos.
- **Coleta de Telefones:** Busca e extrai números de telefone dos anúncios.
- **Persistência de Dados:** Salva os números de telefone encontrados em um arquivo CSV.
- **Multithreading:** Utiliza múltiplas threads para acelerar o processo de coleta de dados. O número de threads pode ser configurado através do argumento `-t`.

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

Execute o script para iniciar a extração de dados. Você pode configurar o número de threads utilizando o argumento `-t` para melhorar o desempenho.

### Exemplos de Comando

- **Executar o scraper com o número padrão de threads (5):**

    ```bash
    python main.py
    ```

- **Executar o scraper com um número personalizado de threads:**

    ```bash
    python main.py -t 10
    ```

    Onde `10` é o número de threads que você deseja usar.

## Arquivos Gerados

- `telefones.csv`: Arquivo contendo os números de telefone extraídos dos anúncios.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
