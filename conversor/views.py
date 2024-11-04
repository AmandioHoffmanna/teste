from django.shortcuts import render

# Função pura para validar se um valor é numérico
def is_numeric(value):
    try:
        float(value)  # Tenta converter o valor para float
        return True
    except ValueError:
        return False

# Função pura para realizar a conversão de moeda
def converter(valor, taxa_cambio):
    return valor * taxa_cambio  # Aplica a taxa de câmbio para converter

def conversao(request):
    resultado = None
    error = None

    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        valor = request.POST.get('valor')  # Obtém o valor do formulário
        moeda_origem = request.POST.get('moeda_origem')  # Obtém a moeda de origem
        moeda_destino = request.POST.get('moeda_destino')  # Obtém a moeda de destino
        taxa_cambio = request.POST.get('taxa_cambio')  # Obtém a taxa de câmbio

        # Valida se as moedas são diferentes
        if moeda_origem == moeda_destino:
            error = "A moeda de destino deve ser diferente da moeda de origem."
        # Valida se o valor a ser convertido é fornecido e positivo
        elif not valor or not is_numeric(valor) or float(valor) < 0:
            error = "O valor a converter deve ser um número positivo e é obrigatório."
        # Valida se a taxa de câmbio é fornecida e positiva
        elif not taxa_cambio or not is_numeric(taxa_cambio) or float(taxa_cambio) <= 0:
            error = "A taxa de câmbio deve ser um número positivo e é obrigatória."
        else:
            valor = float(valor)  # Converte o valor para float
            taxa_cambio = float(taxa_cambio)  # Converte a taxa de câmbio para float
            
            # Utiliza a função de conversão
            resultado = converter(valor, taxa_cambio)  # Aplica a taxa de câmbio

    return render(request, 'conversao.html', {'resultado': resultado, 'error': error})
