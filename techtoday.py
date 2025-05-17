from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do .env
load_dotenv()

# Ferramenta de busca com Serper
search_tool = SerperDevTool()

# Modelo LLM da OpenAI via LangChain
llm = ChatOpenAI(model="gpt-4", temperature=0.5)

# Agente 1: Pesquisador de notícias
tech_researcher = Agent(
    role="Especialista em notícias de tecnologia",
    goal="Encontrar as novidades mais relevantes do mundo sobre inteligencia artificial hoje",
    backstory="Você é um analista de tendências de tecnologia.",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool],
    llm=llm
)

# Agente 2: Designer de Infográficos
infographic_designer = Agent(
    role="Designer de Infográficos",
    goal="Transformar as notícias em um infográfico textual atrativo e moderno",
    backstory="Você é especialista em apresentar dados em formato carrossel visual e impactante.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Função para enviar o e-mail
def enviar_email(assunto, corpo_html):
    msg = MIMEText(corpo_html, 'html')  # <-- tipo HTML
    msg['Subject'] = assunto
    msg['From'] = os.getenv("GMAIL_EMAIL")
    msg['To'] = os.getenv("DEST_EMAIL")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(os.getenv("GMAIL_EMAIL"), os.getenv("GMAIL_PASSWORD"))
        server.send_message(msg)


# Task 1: Buscar notícias
task1 = Task(
    description="Buscar as 5 principais novidades em tecnologia no mundo hoje.",
    expected_output="Uma lista com 5 manchetes e resumos breves das notícias mais relevantes de hoje no mundo da tecnologia.",
    agent=tech_researcher
)

# Task 2: Criar infográfico textual
task2 = Task(
    description="Transforme as notícias recebidas em um infográfico textual, com título chamativo, resumo e tópicos organizados visualmente como um carrossel para redes sociais.",
    expected_output="Um infográfico textual no formato HTML. Para cada notícia, inclua o título em negrito, o resumo e um link clicável para a notícia. Se possível, inclua uma imagem (URL da thumbnail) com tag <img>.",
    agent=infographic_designer,
    depends_on=[task1]
)

# Task 3: Enviar por e-mail
def email_callback(output):
    corpo = str(output)  # Corrige erro de tipo
    enviar_email("Tech Today - Novidades em Tecnologia", corpo)

task3 = Task(
    description="Envie o infográfico final para o usuário via e-mail.",
    expected_output="Confirmação de que o e-mail foi enviado com sucesso contendo o infográfico textual.",
    agent=infographic_designer,
    depends_on=[task2],
    output_file="tech_today_output.txt",
    callback=email_callback
)

# Definindo a crew e o processo
crew = Crew(
    agents=[tech_researcher, infographic_designer],
    tasks=[task1, task2, task3],
    verbose=True,
    process=Process.sequential
)

# Execução
if __name__ == "__main__":
    crew.kickoff()