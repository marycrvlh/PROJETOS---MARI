#script para permitir acesso conforme os cargos e dias

#solicitação das informações
nome=input('digite o seu nome: ') .strip() .lower()
cargo=input('insira o seu cargo(gerente, analista ou estagiario): ') .strip() .lower()
diaSemana=input('insira os dias trabalhados da semana: ') .strip() .lower()

#analise da condição
if cargo == 'gerente':
    if diaSemana == 'segunda-feira' or diaSemana == 'terça-feira'  or diaSemana == 'quarta-feira'   or diaSemana == 'quinta-feira'  or diaSemana == 'sexta-feira' or diaSemana == 'sabado':
     print(f'olá {nome}, acesso liberado para todos os dias')
     
elif cargo == 'analista':
    if diaSemana == 'segunda-feira' or diaSemana == 'terça-feira'  or diaSemana == 'quarta-feira'   or diaSemana == 'quinta-feira'  or diaSemana == 'sexta-feira':
        print(f'olá {nome}, acesso liberado.') 
    elif diaSemana == 'sabado' or diaSemana == 'domingo':
        print('acesso negado.')
            
elif cargo == 'estagiario':
    if diaSemana == 'segunda-feira' or diaSemana == 'quarta-feira'  or diaSemana == 'sexta-feira':
        print('acesso permitido')
else:
    print('cargo invalido. acesso negado.')
