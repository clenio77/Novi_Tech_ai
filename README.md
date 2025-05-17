<!-- Marca d'água Python -->
<div style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 0; pointer-events: none;">
  <img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo" style="width:60vw; opacity:0.07; position:absolute; top:20vh; left:20vw;"/>
</div>

<div style="position: relative; z-index: 1;">
  
# 📰 TechToday - Seu Resumo Diário do Mundo da Tecnologia

<p align="center">
  <img src="https://github.com/joaomdmoura/crewAI/raw/main/docs/logo.png" alt="CrewAI Logo" width="200"/>
</p>

Este projeto utiliza o framework CrewAI para automatizar a coleta de notícias de tecnologia, transformar as informações em um infográfico textual e enviá-las por e-mail diariamente.

## 🚀 Funcionalidades

- 🔍 Busca automatizada de notícias tech utilizando a ferramenta Serper.
- 🎨 Geração de infográfico textual em estilo carrossel do Instagram.
- 📧 Envio automático por e-mail usando conta do Gmail com autenticação segura.
- 🧠 Utiliza modelos da OpenAI via LangChain para raciocínio e formatação.

## 🧠 Arquitetura do Projeto

O projeto utiliza 3 agentes inteligentes, orquestrados em processo sequencial:

| Agente              | Função                                               | Ferramentas Utilizadas |
|---------------------|------------------------------------------------------|-----------------------|
| tech_researcher     | Busca as principais notícias do dia                  | SerperSearchTool      |
| infographic_designer| Resume e transforma as notícias em infográfico textual| LLM                  |
| email_sender        | Envia o resultado por e-mail                         | SMTP (via Gmail)      |

## 📁 Estrutura do Projeto

```
techtoday_project/
├── techtoday.py           # Script principal com os agentes, tarefas e crew
├── .env.example           # Exemplo de variáveis de ambiente
├── requirements.txt       # Dependências do projeto
└── README.md              # Instruções (este arquivo)
```

## ⚙️ Como Usar

1. Clone ou crie o projeto localmente:
   ```bash
   git clone <url-do-repositorio>
   cd techtoday_project
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure suas variáveis de ambiente:
   - Crie um arquivo `.env` baseado no `.env.example`:
     ```
     OPENAI_API_KEY=sua_openai_key
     SERPER_API_KEY=sua_serper_key
     GMAIL_EMAIL=seu_email@gmail.com
     GMAIL_PASSWORD=sua_senha_de_aplicativo
     DEST_EMAIL=destinatario@gmail.com
     ```
   ⚠️ Use uma senha de aplicativo criada nas configurações da sua conta Google.

4. Execute o script:
   ```bash
   python techtoday.py
   ```

## ⏱️ Automatizando o Envio Diário

### Linux (crontab)

Edite o crontab com o comando:

```cron
0 8 * * * /usr/bin/python3 /caminho/para/techtoday_project/techtoday.py
```
> Isso executa o script todos os dias às 8h da manhã. Substitua `/caminho/para/techtoday_project/techtoday.py` pelo caminho completo do seu arquivo.

### Windows (Agendador de Tarefas)

1. Abra o **Agendador de Tarefas** (Task Scheduler).
2. Clique em **Criar Tarefa...**.
3. Na aba **Ações**, clique em **Nova...** e configure:
   - **Ação:** Iniciar um programa
   - **Programa/script:** Caminho completo para o executável do Python (ex: `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python311\python.exe`)
   - **Adicionar argumentos:** Caminho completo para o script (ex: `C:\caminho\para\techtoday_project\techtoday.py`)
4. Na aba **Disparadores**, configure o horário desejado (ex: diariamente às 8h).
5. Salve a tarefa.

## 📦 Dependências

- CrewAI
- LangChain OpenAI
- LangChain Community Tools
- python-dotenv
- smtplib (embutido no Python)

## 💡 Observações

- Este projeto simula um infográfico visual em formato textual, ideal para consumo rápido em dispositivos móveis.
- Pode ser facilmente estendido para gerar PDFs, imagens ou postar em redes sociais no futuro.

---

<p align="center">
  <img src="https://github.com/joaomdmoura/crewAI/raw/main/docs/logo.png" alt="CrewAI Logo" width="100"/>
</p>
<p align="center">
  <sub>© 2025 Feito por Clenio Afonso de Oliveira Moura. Todos os direitos reservados.</sub>
</p>

</div>