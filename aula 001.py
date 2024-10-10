def soma_dois_num(funcao_decorada):
  def nova_funcao(*args, **kwargs):
    return funcao_decorada(*args, **kwargs)
  return nova_funcao

@soma_dois_num
# instancia a função soma_dois_num( ) passando como parâmetro a função soma( )
def soma(num1, num2):
  return num1 + num2

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print(soma_dois_num(soma))

