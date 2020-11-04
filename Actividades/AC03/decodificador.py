from itertools import chain


def decodificar(string):
    #lista= {'0':'a','1':'r','2':'q','3':'u','4':'e','5':'t','6':'i','7':'p','8':'o','9':'s',}
    s1='arquetipos'
    s2='0123456789'

    str3 = dict(list(zip(s1,s2)))
    str3.update(list(zip(s2,s1)))

    str2 = [str3[x]  if x in str3 else x for x in string]

    string = ''.join(str2) 
    return string


if __name__ == "__main__":
    tests = [
        "66cqquu", 
        "P18g10m0c68n 0v0nz0d0 qaro-q",
        "E950 49 3n0 7134b0 d4l d4c8d6f6c0d81",
        "S6 734d49 l441 4958, 58d8 h0 90l6d8 m3y b64n!!"]


    print("  ---  PRUEBA DE DECODIFICADO ---  ")
    for test in tests:
        print(decodificar(test), "\n")