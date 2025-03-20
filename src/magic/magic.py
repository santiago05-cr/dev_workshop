class Magic:
    """
    Clase con métodos para juegos matemáticos
    """
    
    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)
    
    def secuencia_fibonacci(self, n):
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
    
    def es_primo(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]
    
    def es_numero_perfecto(self, n):
        if n < 2:  # Ningún número menor a 2 puede ser perfecto
            return False  

        suma_divisores = sum(i for i in range(1, n) if n % i == 0)
        return suma_divisores == n
    
    def triangulo_pascal(self, filas):
        pascal = [[1] * (i + 1) for i in range(filas)]
        for i in range(2, filas):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal
    
    def factorial(self, n):
        return 1 if n == 0 else n * self.factorial(n - 1)
    
    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def mcm(self, a, b):
        return abs(a * b) // self.mcd(a, b)
    
    def suma_digitos(self, n):
        return sum(int(digit) for digit in str(n))
    
    def es_numero_armstrong(self, n):
        num_str = str(n)
        num_digitos = len(num_str)
        return sum(int(digit) ** num_digitos for digit in num_str) == n
    
    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        suma_ref = sum(matriz[0])
        
        for fila in matriz:
            if sum(fila) != suma_ref:
                return False
        
        for col in range(n):
            if sum(matriz[fila][col] for fila in range(n)) != suma_ref:
                return False
        
        if sum(matriz[i][i] for i in range(n)) != suma_ref:
            return False
        
        if sum(matriz[i][n - i - 1] for i in range(n)) != suma_ref:
            return False
        
        return True