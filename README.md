## Organização do projeto vestibular UERJ
projeto-vestibular/
│
├── data/
│   ├── raw/
│   │   ├── candidato_vaga/
│   │   ├── classificados/
│   │   └── max_min/
│   │
│   ├── processed/
│   │   ├── candidato_vaga/
│   │   ├── classificados/
│   │   └── max_min/
│   │
│   └── curated/
│
├── notebooks/
│   ├── 01_etl_candidato_vaga.ipynb
│   ├── 02_etl_classificados.ipynb
│   ├── 03_etl_max_min.ipynb
│   └── 04_analise_exploratoria.ipynb
│
├── src/
│   └── vestibular/
│       ├── extraction/
│       │   ├── candidato_vaga.py
│       │   ├── classificados.py
│       │   └── max_min.py
│       │
│       ├── transformation/
│       │   └── limpeza.py
│       │
│       ├── validation/
│       │   └── qualidade.py
│       │
│       └── loading/
│           └── supabase.py
│
├── tests/
│   ├── test_candidato_vaga.py
│   ├── test_classificados.py
│   └── test_max_min.py
│
├── .env
├── .gitignore
├── .python-version
├── pyproject.toml
└── README.md

## Fonte dos dados e privacidade

Os dados utilizados neste projeto foram obtidos a partir de informações
publicamente disponibilizadas pela Universidade do Estado do Rio de Janeiro
(UERJ), por meio do portal oficial do Vestibular UERJ:

https://www.vestibular.uerj.br/?page_id=8456

Os dados são utilizados exclusivamente para fins acadêmicos e de estudo,
com o objetivo de realizar análises estatísticas e explorar técnicas de
Engenharia e Análise de Dados.

### Tratamento de dados pessoais

Embora os dados de origem sejam disponibilizados publicamente pela fonte
oficial, este projeto adota o princípio de minimização de dados, evitando
a exposição de informações pessoais que não sejam necessárias para as
análises realizadas.

Dados pessoais presentes nos documentos originais, como nome do candidato
e número de inscrição, não são utilizados como variáveis analíticas e não
devem ser disponibilizados publicamente no dataset final do projeto.

As análises são realizadas de forma agregada, principalmente por curso,
ano, turno, unidade, modalidade de ingresso e demais características
relevantes para o estudo.

Este projeto não possui finalidade comercial nem pretende identificar,
classificar ou avaliar individualmente candidatos.

### Referência da fonte

Universidade do Estado do Rio de Janeiro (UERJ) – Vestibular UERJ.
Disponível em:
https://www.vestibular.uerj.br/?page_id=8456

Acesso em: [14/09/2026].

