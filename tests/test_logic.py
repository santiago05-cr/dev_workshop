import pytest
from src.logic.logic import Logica

class TestLogica:
    def setup_method(self):
        self.logica = Logica()
    
    def test_AND(self):
        # Test para todas las combinaciones de AND
        assert self.logica.AND(True, True) == True
        assert self.logica.AND(True, False) == False
        assert self.logica.AND(False, True) == False
        assert self.logica.AND(False, False) == False
    
    def test_OR(self):
        # Test para todas las combinaciones de OR
        assert self.logica.OR(True, True) == True
        assert self.logica.OR(True, False) == True
        assert self.logica.OR(False, True) == True
        assert self.logica.OR(False, False) == False
    
    def test_NOT(self):
        # Test para todas las combinaciones de NOT
        assert self.logica.NOT(True) == False
        assert self.logica.NOT(False) == True
    
    def test_XOR(self):
        # Test para todas las combinaciones de XOR
        assert self.logica.XOR(True, True) == False
        assert self.logica.XOR(True, False) == True
        assert self.logica.XOR(False, True) == True
        assert self.logica.XOR(False, False) == False
    
    def test_NAND(self):
        # Test para todas las combinaciones de NAND
        assert self.logica.NAND(True, True) == False
        assert self.logica.NAND(True, False) == True
        assert self.logica.NAND(False, True) == True
        assert self.logica.NAND(False, False) == True
    
    def test_NOR(self):
        # Test para todas las combinaciones de NOR
        assert self.logica.NOR(True, True) == False
        assert self.logica.NOR(True, False) == False
        assert self.logica.NOR(False, True) == False
        assert self.logica.NOR(False, False) == True
    
    def test_XNOR(self):
        # Test para todas las combinaciones de XNOR
        assert self.logica.XNOR(True, True) == True
        assert self.logica.XNOR(True, False) == False
        assert self.logica.XNOR(False, True) == False
        assert self.logica.XNOR(False, False) == True
    
    def test_implicacion(self):
        # Test para todas las combinaciones de implicación
        assert self.logica.implicacion(True, True) == True
        assert self.logica.implicacion(True, False) == False
        assert self.logica.implicacion(False, True) == True
        assert self.logica.implicacion(False, False) == True
    
    def test_bi_implicacion(self):
        # Test para todas las combinaciones de bi-implicación
        assert self.logica.bi_implicacion(True, True) == True
        assert self.logica.bi_implicacion(True, False) == False
        assert self.logica.bi_implicacion(False, True) == False
        assert self.logica.bi_implicacion(False, False) == True
