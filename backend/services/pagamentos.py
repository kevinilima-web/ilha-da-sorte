import requests
from settings import MERCADO_PAGO_TOKEN

def criar_pix(pedido_id, valor):
    payload = {
        "transaction_amount": valor,
        "description": f"Pedido {pedido_id}",
        "payment_method_id": "pix",
        "payer": {"email": "cliente@email.com"}
    }

    headers = {
        "Authorization": f"Bearer {MERCADO_PAGO_TOKEN}"
    }

    response = requests.post(
        "https://api.mercadopago.com/v1/payments",
        json=payload,
        headers=headers
    )

    return response.json()
