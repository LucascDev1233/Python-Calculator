meuaporte = float(input('Digite o valor do seu aporte mensal: R$ '))
anos = float(input('Digite por quantos anos pretende investir: '))

# Converter anos em meses
meses = int(anos * 12)

# Taxa de juros mensal (exemplo: 8% ao ano ≈ 0.64% ao mês)
taxa_mensal = 0.08 / 12  

# Cálculo do montante com juros compostos e aportes mensais
montante = 0
for i in range(meses):
    montante = (montante + meuaporte) * (1 + taxa_mensal)

total_investido = meuaporte * meses
rendimento = montante - total_investido

# Exibir resultados
print('\n--- DADOS ---')
print(f'Aporte mensal: R$ {meuaporte:,.2f}')
print(f'Tempo: {meses} meses ({anos} anos)')
print(f'Total investido: R$ {total_investido:,.2f}')
print(f'Rendimento: R$ {rendimento:,.2f}')
print(f'Montante final: R$ {montante:,.2f}')
