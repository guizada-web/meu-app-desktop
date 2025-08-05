# Meu App Desktop

Este projeto é uma aplicação desktop desenvolvida em Python que consome APIs públicas, como TheCatAPI e TheDogAPI, para exibir, filtrar e manipular dados relacionados a gatos e cães. A aplicação possui uma interface gráfica que permite interações do usuário e inclui tratamento de erros.

## Estrutura do Projeto

```
meu-app-desktop
├── src
│   ├── main.py          # Ponto de entrada da aplicação
│   ├── gui.py           # Definição da interface gráfica do usuário
│   ├── api_client.py    # Gerenciamento das requisições à API pública
│   ├── utils.py         # Funções utilitárias
│   └── types
│       └── __init__.py  # Tipos e interfaces utilizados no projeto
├── requirements.txt      # Dependências do projeto
└── README.md             # Documentação do projeto
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Uso

Para iniciar a aplicação, execute o arquivo `main.py`:

```
python src/main.py
```

## APIs Consumidas

- **TheCatAPI**: API pública para obter imagens e informações sobre gatos.
- **TheDogAPI**: API pública para obter imagens e informações sobre cães.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.