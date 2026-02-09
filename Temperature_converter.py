#CONVERSOR DE TEMPERATURA

#Grados centígrados = (grados Fahrenheit − 32) × 5/9.
#Grados Fahrenheit = (grados centígrados × 9/5) +32

#ingreso de datos. Qué variables necesito tener?
choise = input('Elige sólo con la letra \n\nQuieres obtener Fahrenheit(F) o Celsius(C)?: ').lower()

temp = float(input('Ingresa los grados de temperatura: '))

#Comportamiento - Qué voy a hacer con los datos ingresados?
if choise == 'c':
    print('A- La temperatura es: ')
    print((temp-32)*5/9,'grados centígrados')
elif choise == 'f':
    print('B- La temperatura es: ')
    print(temp*(9/5)+32,'grados farherenheit')
else:
    print('Discula, debes elegir unicamente entre Fahrenheit(F) o Celsius(C)')


#prueba de modificación
