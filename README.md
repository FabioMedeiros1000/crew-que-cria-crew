# CrewAI Auto Setup

Este projeto tem como objetivo **automatizar a criação de arquivos essenciais para o funcionamento de uma crew no CrewAI**, a partir de um tema definido pelo usuário.

---

## Visão Geral

O projeto gera automaticamente três arquivos principais:

- `agents.yaml` – Define os agentes, suas funções (roles), metas (goals) e histórias (backstory).
- `tasks.yaml` – Lista as tarefas que serão atribuídas aos agentes.
- `crew.py` – Cria a estrutura da crew, importando os agentes e tarefas definidos.

Tudo isso é baseado em um **tema informado pelo usuário** no arquivo `main.py`.

## Objetivo

Automatizar o processo inicial de criação de uma crew no CrewAI, tornando mais fácil:

- Prototipar ideias.
- Criar soluções orientadas a agentes com maior agilidade.
- Focar no conteúdo dos agentes e suas interações, ao invés de configurar manualmente os arquivos repetitivos.

---

## Como Funciona

1. Usuário define o tema no main.py (ex: "sustentabilidade", "educação em IA", "startup financeira").
2. O sistema utiliza esse tema para gerar dinamicamente os arquivos:
  - Cada agente terá um papel relevante ao tema.
  - As tarefas serão distribuídas entre os agentes com foco na resolução do problema.
  - O crew.py importará tudo e instanciará a crew com base nesses dados.

## Tecnologias Utilizadas

- Python 3.10+
- CrewAI
- YAML
- Funções LLM-based (dependendo de como você gera os arquivos)

## Exemplo de Uso

- No main.py, defina o tema:
- Ao executar:

```bash
python main.py
```

Serão gerados os arquivos:
- agents.yaml com especialistas em IA, educação e políticas públicas.
- tasks.yaml com tarefas como: pesquisar soluções, montar plano de ação, simular cenários.
- crew.py com tudo montado para execução da crew.

## Testes
Você pode testar a funcionalidade alterando o tema no main.py e verificando os arquivos gerados.
