def cargar_mapa(path):
    grilla = []
    print(path)
    with open(path, 'r', encoding='utf-8') as archivo:
        for linea in archivo.readlines():
            grilla.append(linea.strip().split(' '))
    return grilla


