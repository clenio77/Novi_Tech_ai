📰 TechToday - Seu Resumo Diário do Mundo da Tecnologia
Este projeto utiliza o framework CrewAI para automatizar a coleta de notícias de tecnologia, transformar as informações em um infográfico textual e enviá-las por e-mail diariamente.

🚀 Funcionalidades
🔍 Busca automatizada de notícias tech utilizando a ferramenta Serper.

🎨 Geração de infográfico textual em estilo carrossel do Instagram.

📧 Envio automático por e-mail usando conta do Gmail com autenticação segura.

🧠 Utiliza modelos da OpenAI via LangChain para raciocínio e formatação.

🧠 Arquitetura do Projeto
Este projeto utiliza 3 agentes inteligentes, orquestrados em processo sequencial:

Agente	Função	Ferramentas Utilizadas
tech_researcher	Busca as principais notícias do dia	SerperDevTool
infographic_designer	Resume e transforma as notícias em infográfico textual	LLM
email_sender	Envia o resultado por e-mail	SMTP (via Gmail)

📁 Estrutura do Projeto
bash
Copiar
Editar
techtoday_project/
├── techtoday.py           # Script principal com os agentes, tarefas e crew
├── .env.example           # Exemplo de variáveis de ambiente
├── requirements.txt       # Dependências do projeto
└── README.md              # Instruções (este arquivo)
⚙️ Como Usar
1. Clone ou crie o projeto localmente
bash
Copiar
Editar
git clone <url>
cd techtoday_project
2. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
3. Configure suas variáveis
Crie um arquivo .env baseado no .env.example:

env
Copiar
Editar
OPENAI_API_KEY=sua_openai_key
SERPER_API_KEY=sua_serper_key
GMAIL_EMAIL=seu_email@gmail.com
GMAIL_PASSWORD=sua_senha_de_aplicativo
DEST_EMAIL=destinatario@gmail.com
⚠️ Use uma senha de aplicativo criada nas configurações da sua conta Google. Como gerar

4. Execute o script
bash
Copiar
Editar
python techtoday.py
⏱️ Automatizando o Envio Diário
No Linux, edite o crontab:

bash
Copiar
Editar
crontab -e
E adicione:

cron
Copiar
Editar
0 8 * * * /usr/bin/python3 /caminho/completo/para/techtoday_project/techtoday.py
Isso roda todos os dias às 8h da manhã.

📦 Dependências
CrewAI

LangChain OpenAI

LangChain Community Tools

python-dotenv

smtplib (embutido no Python)

💡 Observações
Este projeto simula um infográfico visual em formato textual, ideal para consumo rápido em dispositivos móveis.

Pode ser facilmente estendido para gerar PDFs, imagens ou postar em redes sociais no futuro.

