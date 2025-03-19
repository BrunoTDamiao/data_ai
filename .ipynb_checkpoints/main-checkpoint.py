# Importação das bibliotecas necessárias
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage

# Carregar variáveis de ambiente (API Key do Groq)
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Inicializar FastAPI
app = FastAPI()

# Inicializar o modelo de IA Groq
llm = ChatGroq(model_name="mixtral-8x7b-32768", api_key=groq_api_key)


# Criar um modelo de entrada para requisições
class ComplaintRequest(BaseModel):
    product: str
    issue: str
    narrative: str


# Criar endpoint para análise de reclamações
@app.post("/analyze")
def analyze_complaint(complaint: ComplaintRequest):
    """
    Recebe uma reclamação e retorna insights gerados pela IA do Groq.
    """
    prompt = f"""
    Produto: {complaint.product}
    Problema: {complaint.issue}
    Reclamação: {complaint.narrative}

    Analise esta reclamação e forneça insights sobre padrões comuns e possíveis melhorias.
    """

    response = llm.invoke([HumanMessage(content=prompt)])
    return {"insight": response.content}


# Criar um endpoint de teste para verificar se a API está rodando
@app.get("/")
def home():
    return {"message": "API do Assistente Inteligente de Análise de Dados está rodando!"}
