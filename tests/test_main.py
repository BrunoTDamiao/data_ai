from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API do Assistente Inteligente de Análise de Dados está rodando!"}


def test_analyze_complaint():
    complaint_data = {
        "product": "Conta Corrente",
        "issue": "Cobrança de taxas",
        "narrative": "Fui cobrado por uma taxa que não estava descrita no contrato."
    }

    response = client.post("/analyze", json=complaint_data)
    assert response.status_code == 200
    assert "insight" in response.json()
