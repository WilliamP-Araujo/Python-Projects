
# Enviar um email com os detalhes da compra online (maximo 3
# tentativas para compras confirmadas)

compra_comfirmada = True
dados_compra = "Compra no valor de R$12.50 e entrega confirmada"
for enviar in range(3):
    if compra_comfirmada:
       print(dados_compra)
       print("Detalhes enviado para o seu email")
       break
else:
    print("Falha durante sua aquisição")
