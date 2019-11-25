producto = 0
baja = 9000
alta = 0
valido = 7
numba = 0
numal = 0
rango = range(1,11)
for elemento in rango:
	numero = float(raw_input("%s ingrese calificacion" %(elemento)))
	producto = numero + producto 
	if numero < baja:
		baja = numero
	elif numero > alta:
		alta = numero
	if numero < 7:
		numba += 1;
	elif numero >= 7:
		numal += 1

print ("la calificacion mas baja es %s" %(baja))
print ("la calificacion mas alta es %s" %(alta))
print ("las calificaciones reprobadas son %s" %(numba))
print ("las calificaciones aprobadas son %s" %(numal))
promedio = producto / 10
print ("el promedio es %s" %(promedio))

if promedio >= valido:
	print ("usted esta aprovado")
else: 
	print ("usted esta reprovado")
