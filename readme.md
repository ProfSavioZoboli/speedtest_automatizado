# 🚀 Automated ISP Speedtest Tracker

Este projeto é um script de automação em Python que realiza testes de velocidade de internet de forma periódica e organiza os resultados visualmente através de screenshots. Ele foi desenvolvido para monitorar instabilidades de conexão e gerar provas documentais para suporte técnico e auditorias de rede.

## 📋 Funcionalidades

* **Automação com Selenium:** Simula a interação humana real, abrindo o navegador e acionando o teste no site oficial do provedor.
* **Frequência Customizável:** Configurado para rodar a cada 5 minutos (300 segundos).
* **Organização por Horário:** Cria pastas automaticamente para cada hora do dia, facilitando a navegação pelas evidências.
* **Gestão de Diretórios:** O script verifica a existência das pastas e as cria dinamicamente, evitando erros de execução.

## 🛠️ Pré-requisitos

Para rodar este script, você precisará de:

1.  **Python 3.x** instalado.
2.  **Google Chrome** instalado.
3.  **ChromeDriver** (O Selenium geralmente gerencia isso automaticamente nas versões mais recentes, mas é bom ter o Chrome atualizado).
4.  Biblioteca Selenium:
    ```bash
    pip install selenium
    ```

## 🚀 Como usar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/ProfSavioZoboli/speedtest_automatizado.git](https://github.com/ProfSavioZoboli/speedtest_automatizado.git)
    cd speedtest_automatizado
    ```

2.  **Execução:**
    Basta rodar o arquivo principal:
    ```bash
    python main.py
    ```

3.  **Localização dos Resultados:**
    Os prints serão salvos na pasta `screenshots/` dentro do diretório do projeto.

## 📁 Estrutura de Pastas

O script organiza os arquivos da seguinte forma:

```text
/
├── speedtest_monitor.py
└── screenshots/
    ├── 07h/
    │   ├── speedtest_07-00-01.png
    │   └── speedtest_07-05-02.png
    ├── 08h/
    │   └── ...
    └── ...
```
## 🤖 Créditos e Inteligência Artificial

Este código foi gerado com o auxílio de **Inteligência Artificial (Gemini)**. A IA foi utilizada para estruturar a lógica de automação do navegador, gerenciamento de arquivos de sistema e formatação da documentação, visando criar uma ferramenta robusta para defesa dos direitos do consumidor frente a serviços de telecomunicações.

---

### ⚠️ Aviso Legal

Este script deve ser usado para fins de monitoramento pessoal e diagnóstico de rede. Certifique-se de que a frequência dos testes não viole os termos de uso do site alvo. O autor não se responsabiliza pelo uso indevido da ferramenta.
