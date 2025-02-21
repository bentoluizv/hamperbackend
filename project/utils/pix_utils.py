from efipay import EfiPay


efi = EfiPay()

body = {
    'calendario': {
        'expiracao': 3600
    },
    'devedor': {
        'cpf': '13274958999',
        'nome': 'Vanessa Hellen de Moura'
    },
    'valor': {
        'original': '0.05'
    },
    'chave': '71cdf9ba-c695-4e3c-b010-abb521a3f1be',
    'solicitacaoPagador': 'Cobrança dos serviços prestados.'
}

response =  efi.pix_create_immediate_charge(body=body)
print(response)
