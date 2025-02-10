def rgb_para_hexadecimal(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def main():
    print("Conversor de RGB para Hexadecimal")
    
    while True:
        try:
            r = int(input("Insira o valor de Red (0-255): "))
            g = int(input("Insira o valor de Green (0-255): "))
            b = int(input("Insira o valor de Blue (0-255): "))
            
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                hexadecimal = rgb_para_hexadecimal(r, g, b)
                print("O valor hexadecimal é:", hexadecimal)
            else:
                print("Os valores de RGB devem estar entre 0 e 255.")
        except ValueError:
            print("Por favor, insira um número válido.")
        
        continuar = input("Deseja realizar outra conversão? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
