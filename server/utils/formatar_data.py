from datetime import datetime

# Função para formatar a data no padrão brasileiro
def formatar_data(data):
    try:
        data_formatada = datetime.strptime(data, '%a, %d %b %Y %H:%M:%S GMT')
        return data_formatada.strftime('%d/%m/%Y')
    except ValueError:
        return data