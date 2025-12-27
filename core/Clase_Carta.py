class Cartas:

    def __init__(self, palo, valor,nombre=None):
        """Este es el constructor de esta clase que tendra sus dos objetos privados 
        Argumento: String:Palo ; Int:Valor
        """
        self.__palo = palo
        self.__valor = valor 
        if nombre == None:
            self.__nombre = ""
        else:
            self.__nombre = nombre
        
    def cambiar_nombre(self, nuevo_nombre):
        """Permite que una baraja le asigne un nombre específico a una carta."""
        self.__nombre = nuevo_nombre
    
    def ver_palo(self):
        """ 
        Este metodo accede al palo de la carta que escojemos
        Argumento: 
            Carta: La carta de la que querramos encontrar informacion
            
        Devuelve:
            Un string: palo
        """         
        return self.__palo
    
    def ver_valor(self):
        """ 
        Este metodo accede al valor de la carta que escojemos
        Argumento: 
            Carta: La carta de la que querramos encontrar informacion
            
        Devuelve:
            Un int: valor 
        """         
        return self.__valor

    def ver_nombre(self):
        """ 
        Este metodo accede al nombre de la carta que escojemos
        Argumento: 
            Carta: La carta de la que querramos encontrar informacion
            
        Devuelve:
            Un string: nombre 
        """         
        return self.__nombre
    
    def caracteristicas(self):
         """ 
        Este metodo muestra todas las caracteristicas de una carta, palo, valor y nombre: 
            Carta: La carta de la que querramos encontrar informacion
            
        Devuelve:
            Una lista con el palo, el nombre y el valor como string
        """         
         Respuesta=[self.ver_nombre(), self.ver_palo(), self.ver_valor()] 
         return Respuesta      
    
    def cambiar(self, palo_nuevo=None, valor_nuevo=None):
        """ 
        Este metodo modifica el valor, palo o ambos dependiendo lo que se le de 
        Argumento: 
            string: palo_nuevo 
            int: valor_nuevo
            
        Devuelve:
            Carta: Carta modificada
        """         
        if palo_nuevo is not None:
            self.__palo = palo_nuevo
        if valor_nuevo is not None:
            self.__valor = valor_nuevo

    def MismoPalo(self, otra):
        """Metodo que compara si dos cartas tienen el mismo Palo y devuelve True o False

            Anotaciones: isinstance compara inicialmente si el objeto es una carta, asi ahorramos tiempo.
        """
        return isinstance(otra, Cartas) and self.__palo == otra.__palo

    def MismoValor(self, otra):
        """Metodo que compara si dos cartas tienen el mismo Valor y devuelve True o False
        """
        return isinstance(otra, Cartas) and self.__valor == otra.__valor

    def MismoNombre(self, otra):
        """Metodo que compara si dos cartas tienen el mismo Nombre y devuelve True o False
        """
        return isinstance(otra, Cartas) and self.__nombre == otra.__nombre
    
    @staticmethod
    def ordenar_mayor(lista):
        """
        Metodo estatico de la clase cartas, deberia ir en un sector de utilidades en el futuro
        Recibe una lista de cartas y devuelve una nueva lista ordenada de mayor a menor valor,
        sin modificar la original.
        habia hecho una version casera, pero consumia muchos mas recursos, asi que esta usa sorted().
        """
        return sorted(lista, key=lambda carta: carta.ver_valor, reverse=True)


    def __eq__(self, otra):
        """
            Metodo que compara si dos cartas son iguales y devuelve True o False

            Anotaciones, darle el nombre __eq__ permite luego usar comparadores como Carta1==Carta2
            comparando los atributos de las cartas en vez de si son identicas en memoria,
            como sucederia de no configurarse.
        """
        return self.MismoPalo(otra) and self.MismoValor(otra) and self.MismoNombre(otra)
    
    def __str__(self):
        return f"{self.__nombre} de {self.__palo} con valor {self.__valor}"