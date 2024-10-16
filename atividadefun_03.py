# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

raio=float(input("digite o raio do seu circulo"))

pi=("o PI equivale a 3,14")
calculo= 3.14*raio**2
def area_do_circulo(raio):
    return f"a aréa do circulo é {calculo}"


altura=int(input("digite a altura do cilindro"))

def volume_cilindro (altura,areadcirculo):
    cilindro=calculo * altura
    return f"area do cilindro é: {cilindro}"

areadcirculo=area_do_circulo(raio)

areadcilindro=volume_cilindro(altura,areadcirculo)

print(areadcilindro)  

print(areadcirculo)  

    
    
    
    
