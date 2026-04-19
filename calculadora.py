# Tabela A - ANTT (Portaria SUROC nº 4/2026)
# Tipo: Contêiner | Operação completa (veículo + implemento)
# Fórmula: (distância × CCD) + CC

TABELA_CONTEINER = {
    3: {"ccd": 51.397, "cc": 526.13},
    4: {"ccd": 57.767, "cc": 557.42},
    5: {"ccd": 66.765, "cc": 625.16},
    6: {"ccd": 73.776, "cc": 639.38},
    7: {"ccd": 80.832, "cc": 791.67},
    9: {"ccd": 91.859, "cc": 855.76},
}

def calcular_frete(distancia_km, eixos, percentual=0):
    if distancia_km <= 0:
        raise ValueError("Distância deve ser maior que zero.")
    if eixos not in TABELA_CONTEINER:
        raise ValueError(f"Eixos inválido. Opções: {list(TABELA_CONTEINER.keys())}")
    if percentual < 0:
        raise ValueError("Percentual não pode ser negativo.")

    ccd = TABELA_CONTEINER[eixos]["ccd"]
    cc  = TABELA_CONTEINER[eixos]["cc"]

    frete_base = (distancia_km * ccd) + cc
    adicional  = frete_base * (percentual / 100)
    frete_final = frete_base + adicional

    return {
        "eixos":       eixos,
        "frete_base":  round(frete_base, 2),
        "adicional":   round(adicional, 2),
        "frete_final": round(frete_final, 2),
    }