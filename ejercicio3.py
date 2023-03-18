amountRepetions = int( input('Type numbers of repetitios: ') )

countTwo = 0
countThree = 0


for i in range(amountRepetions):
    numero = int( input('Digite un numero: ') )

    if ( numero % 2 == 0):
        countTwo += 1

    if ( numero % 3 == 0):
        countThree += 1
print( f'The multiples of two: { countTwo }' )
print( f'The multiples of three: { countThree }' )