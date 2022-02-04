def palindromo(palabra):
    p = palabra.replace(' ', '').lower()
    p_inv = p[::-1]
    if p == p_inv:
        return True
    else:
        return False


def main():
    word = input('Ingresa la palabra a verificar: ')
    es_palindromo = palindromo(word)
    if es_palindromo == True:
        print('La palabra es palindromo')
    else:
        print('La palabra no es palindromo')


if __name__ == '__main__':
    main()
