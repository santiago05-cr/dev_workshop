import re

class Strings:
    """
    Clase con métodos para manipulación y operaciones con cadenas de texto.
    Incluye funciones para manipular, validar y transformar strings.
    """
    
    def es_palindromo(self, texto):
        texto = texto.lower().replace(" ", "")
        return texto == texto[::-1]
    
    def invertir_cadena(self, texto):
        resultado = ""
        for char in texto:
            resultado = char + resultado
        return resultado
    
    def contar_vocales(self, texto):
        return sum(1 for c in texto.lower() if c in "aeiou")
    
    def contar_consonantes(self, texto):
        return sum(1 for c in texto.lower() if c.isalpha() and c not in "aeiou")
    
    def es_anagrama(self, texto1, texto2):
        return sorted(texto1.replace(" ", "").lower()) == sorted(texto2.replace(" ", "").lower())
    
    def contar_palabras(self, texto):
        return len(texto.split())
    
    def palabras_mayus(self, texto):
        return " ".join(p.capitalize() for p in texto.split())
    
    def eliminar_espacios_duplicados(self, texto):
        return " ".join(texto.split())
    
    def es_numero_entero(self, texto):
        if not texto:
            return False
        if texto[0] == "-":
            texto = texto[1:]
        return all(c in "0123456789" for c in texto)
    
    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for c in texto:
            if c.isalpha():
                base = ord("A") if c.isupper() else ord("a")
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                resultado += c
        return resultado
    
    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)
    
    def encontrar_subcadena(self, texto, subcadena):
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i + len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones
    
    def palabras_mayus(self, texto):
        return re.sub(r'(\S+)', lambda m: m.group(1).capitalize(), texto)
    
    def eliminar_espacios_duplicados(self, texto):
        return re.sub(r'\s+', ' ', texto)