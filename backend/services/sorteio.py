"""
Sorteio baseado na Loteria Federal
"""

def calcular_numero_vencedor(resultado_loteria: int, total_numeros: int):
    vencedor = resultado_loteria % total_numeros
    if vencedor == 0:
        vencedor = total_numeros
    return str(vencedor).zfill(2)
