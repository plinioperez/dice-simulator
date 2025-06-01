import dice
import time

def lanzar_dados(amount, sides):
    resultados = []
    for i in range(amount):
        resultado = dice.roll(f'd{sides}')
        resultados.append(resultado)
        print(f"Lanzamiento {i + 1} número obtenido {resultado}")
        time.sleep(5)
    return resultados

if __name__ == "__main__":
    lanzar_dados(amount=6, sides=20)
