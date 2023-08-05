"""
Faça um programa que leia o tempo de duração de um evento em uma fábrica expressa em segundos
e mostre-o expresso em horas, minutos e segundos.
"""

tempo_em_segundos = int(input("Digite o tempo de duração do evento em segundos: "))

horas = tempo_em_segundos // 3600
minutos = (tempo_em_segundos % 3600) // 60
segundos = tempo_em_segundos % 60

print(f"Tempo: {horas} horas, {minutos} minutos e {segundos} segundos")
