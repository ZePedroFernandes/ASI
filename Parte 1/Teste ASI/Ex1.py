import re

test_str = ("{\n"
            "	authID: bGVpMTIzCg==\n"
            "	ContaOrigem: PT50 0010 1234 12345678901 01\n"
            "	ContaDestino: PT50 0018 4334 62245778183 19\n"
            "	Montante: 5010.10€\n"
            "}")

jsonPattern = re.compile('^\{\n'
                         '\tauthID: [a-zA-Z]+==\n'
                         '\tContaOrigem: PT50 \d{4} \d{4} \d{11} \d{2}\n'
                         '\tContaDestino: PT50 \d{4} \d{4} \d{11} \d{2}\n'
                         '\tMontante: (?P<montante>(\d{0,10}).\d{2})€\n}$')

resultado = jsonPattern.search(test_str)
if resultado:
    print("Expressão OK", end="")
    montante = float(resultado.group("montante"))
    if montante > 5000.00:
        print(" Alerta: Transferencia superior a 5000€")
