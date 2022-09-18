from CuentaBancaria import Cuenta_bancaria

Cuenta1 = Cuenta_bancaria("Cuenta 1", 0, 0, 0, 0)
Cuenta2 = Cuenta_bancaria("Cuenta 2", 0, 0, 0, 0)

#Cuenta 1: 3 depósitos, 1 retiro, generar interés y obtener balance
Cuenta1.depositos(20000).depositos(20000).depositos(20000).retiros(10000).intereses(0.01).balance_cuenta()

#Cuenta 2: 2 depósitos, 4 retiros, generar interés y obtener balance
Cuenta2.depositos(30000).depositos(30000).retiros(5000).retiros(5000).retiros(5000).retiros(5000).intereses(0.01).balance_cuenta()

#Impresión de todas las instancias de la información de una cuenta bancaria
#Lista del total de cuentas
Cuenta_bancaria.imprime_lista()