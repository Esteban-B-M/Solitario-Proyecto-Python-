from Clase_Carta import Cartas
import random

class Inglesa:

    #Creo un diccionario con los nombres especiales
    Nombres_decartas = {
        1:"As",
        11:"Jota",
        12:"Reina",
        13:"Rey",
    }

    def _nombrar_cartas(self,BarajaCualquiera):
        """
        Metodo que usa un diccionario para nombrar las cartas especiales de la baraja -como las figuras-
        y que nombra a las demas como su respectivo valor.

        Argumentos:
            Baraja (Lista): Una lista de cartas, con 52 elementos, 13 de cada palo para esta baraja inglesa

        Anotaciones: str(2) es lo mismo que "2" por ejemplo, esta parte del codigo garantiza que se devuelve un
            nombre incluso cuando el diccionario no proporciona uno
        """
        for carta in BarajaCualquiera:
            valor = carta.ver_valor()
            nombre = self.Nombres_decartas.get(valor,str(valor))
            carta.cambiar_nombre(nombre)

    def __init__ (self,vacia:bool=False):
        """Constructor de la clase que genera una baraja de 52 cartas, 13 de cada palo o una vacia si el parametro
        de entrada vacia es True.
        """
        self._Baraja = []
        if not vacia:
            
            Palos = ["Tréboles","Picas","Corazones","Diamantes"]
            for Palo in Palos:
                for n in range (1,14):
                    self._Baraja.append(Cartas(Palo,n))
            
            self._nombrar_cartas(self._Baraja)


    def agregarCarta(self,Carta):
        """Metodo que agrega una carta al final de la baraja

        Args:
            Carta: Carta a agregar
        """
        self._Baraja.append(Carta)
    

    def eliminarCarta(self,posicion):
        """Metodo que elimina una carta de la baraja en base a una posicion dada

        Args:
            posicion (int): La pocision de la baraja en la que se encuentra la carta a eliminar

        Devuelve:
            Carta: La carta eliminada
        """
        if not 0 <= posicion < len(self._Baraja):
            raise IndexError("Has tratado de acceder a una posicion que no existe, ojala nunca salga este error")
        
        return self._Baraja.pop(posicion)
    

    def Buscar(self,carta):
        """ Busca dentro de la baraja si se encuentra o no una carta

        Argumentos:
            carta : Carta que se proporciona al metodo para que busque dentro de la baraja

        Devuelve:
            Booleano, True o False

        Anotaciones: esto funciona porque dentro de Cartas se ha definido un metodo __eq__()
            return carta in self_Baraja internamente hace algo como:

            for CartaBaraja in self._Baraja:
                if CartaBaraja == carta:
                    return True
        
            return False
        """
        return carta in self._Baraja
    

    def VerCarta(self,posicion):
        """ Devuelve informacion acerca de la carta que esta en esa posicion dentro de la baraja

        Argumentos:
            posicion (Entero): Es la posicion que se desea ver en la baraja

        Devuelve:
            Palo (String) : El palo de la carta
            Valor (Entero) : El valor numerico de la carta
        """
        if not 0 <= posicion < len(self._Baraja):
            raise IndexError("Has tratado de acceder a una posicion que no existe, ojala nunca salga este error")
        Palo = self._Baraja[posicion].ver_palo()
        Valor = self._Baraja[posicion].ver_valor()
        return (Palo,Valor)


    def Barajar(self):
        """Desplaza todas las cartas de la baraja a posiciones al azar"""
        random.shuffle(self._Baraja)

    def Repartir (self,Cantidad):
        """Metodo que separa un grupo de cartas de la baraja, para un subgrupo(como una mano)

        Args:
            Cantidad (int): cuantas cartas se repartiran

        Returns:
            Repartidas (Lista): Un array con las cartas repartidas, la clase mano contendra este array en su interior
        """
        if Cantidad > len(self._Baraja):
            Cantidad = len(self._Baraja)
        Repartidas = self._Baraja[:Cantidad]
        del self._Baraja[:Cantidad]
        return Repartidas
    
    def Repartir_normal (self,Cantidad):
        """Metodo que separa un grupo de cartas de la baraja, para un subgrupo(como una mano)

        Args:
            Cantidad (int): cuantas cartas se repartiran

        Returns:
            Repartidas (Lista): Un array con las cartas repartidas, la clase mano contendra este array en su interior
        """
        if Cantidad > len(self._Baraja):
            Cantidad = len(self._Baraja)
        Repartidas = self._Baraja[-Cantidad:]
        del self._Baraja[-Cantidad:]
        return Repartidas
     
    def dar(self,cartas_a_dar, receptor):
        """
        Agrega las cartas especificadas a otra baraja y las elimina de la mano que la da.
    
        Args:
            cartas_a_dar (list[Cartas]): Cartas a agregar.
            receptor (list[Cartas]): Lista de cartas destino.
        """
        for carta in cartas_a_dar:
            receptor.agregarCarta(carta)
            self._Baraja.remove(carta)

    def Reiniciar(self):
        """Metodo que reinicia la baraja a su estado original y devuelve un resguardo por seguridad"""
        Resguardo = self._Baraja[:]
        self.__init__()

        return Resguardo

    def __len__ (self):
        """Metodo que devuelve el largo de la baraja y permite usar len(Mibaraja) fuera de la clase para mas comodidad"""
        return len(self._Baraja)
    
    def __getitem__ (self, posicion):
        """Metodo que permite usar baraja[i] fuera de la clase"""
        return self._Baraja[posicion]
    
    def __iter__(self):
        """Metodo que permite iterar fuera de la clase"""
        return iter(self._Baraja)
