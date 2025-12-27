from core.Baraja_Inglesa import Inglesa
from core.Clase_Carta import Cartas
class Mano:
    """En este constructor usamos el metodo repartir para que ya obtengamos una baraja
        Para proporcionar una mano, el constructor necesita:

        una baraja: Inglesa(por ahora que solo hay una baraja)

        la cantidad de cartas que le tocan a la mano inicial:int
        """
    
    
    def __init__(self, baraja, cantidad):
        self._mano=baraja.Repartir(cantidad)
#En este constructor usamos el metodo repartir para que ya obtengamos una baraja 


    def jugar(self,cartas_a_jugar):
        """Este metodo requiere que se le de una lista de cartas(las que se van a jugar) 
        devuelve jugada (que es un array que van a ser las cartas de tu mano que se juegan)
        solo si todas las cartas jugadas se encuentran en la mano del usuario"""

        for carta in cartas_a_jugar:

            if carta not in self._mano:
                return []  
        
        jugada = []
        for carta in cartas_a_jugar:
            self._mano.remove(carta)
            jugada.append(carta)

        return jugada
     
        
     
    def descartar(self, cartas):
        """
        Recibe una lista de cartas y descarta aquellas que están en la mano.

        Args:
        cartas (list[Cartas]): Cartas a descartar.

        Returns:
        list[Cartas]: Lista con las cartas que fueron descartadas.
        """
        descartadas = []
        for carta in cartas:
            if carta in self._mano:
                self._mano.remove(carta)
                descartadas.append(carta)  # Se guarda en la lista de descartadas
        return descartadas


    def pedir(self, baraja, cantidad):
        """
        PIDE A LA BARAJA UNA CARTA Y LA GUARDA EN LA MANO DEL JUGADOR.


        Args:
            baraja:la baraja usada
            cantidad: la cantidad a pedir


        Returns:
            Cartas_pedidas: Un resguardo de las cartas
        """
        if len(baraja) == 0:
            print("La baraja está vacía, no se puede pedir.") # Esto es para el caso en el que la la baraja ya no tenga mas cartas para evitar errores en el juego
            return None
        
        Cartas_pedidas = baraja.Repartir(cantidad) 
        for carta in Cartas_pedidas:
            self._mano.append(carta)
        return Cartas_pedidas
        
           
    def pedir_y_ubicar(self, baraja, cantidad):
        """
        Metodo temporal hecho para el correcto funcionamiento de la baraja de descartes en el solitario
        pide una carta y la coloca al final de la mano, osea en la primera posicion.


        Args:
            baraja:la baraja usada
            cantidad: la cantidad a pedir


        Returns:
            Cartas_pedidas: Un resguardo de las cartas
        """
        if len(baraja) == 0:
            print("La baraja está vacía, no se puede pedir.") # Esto es para el caso en el que la la baraja ya no tenga mas cartas para evitar errores en el juego
            return []
        
        Cartas_pedidas = baraja.Repartir_normal(cantidad) 
        self._mano = Cartas_pedidas + self._mano
        return Cartas_pedidas
        
        
    def limpiar(self):
        """
   Limpia la mano completa


        Args:
            No se le da nada.


        Returns:
           No devuelve nada simplemente modifica la mano limpiandola 
        """ 
       
        self._mano.clear()
    
    def Buscar(self,carta):
        """ Busca dentro de la mano si se encuentra o no una carta

        Argumentos:
            carta : Carta que se proporciona al metodo para que busque dentro de la mano

        Devuelve:
            Booleano, True o False

        Anotaciones: esto funciona porque dentro de Cartas se ha definido un metodo __eq__()
            return carta in self_mano internamente hace algo como:

            for Cartamano in self._mano:
                if Cartamano == carta:
                    return True
        
            return False
         """
        
        return carta in self._mano
  
    
  
    def eliminarCarta_Posicion(self,posicion):
        
        """ Elimina una carta segun la posicion que le das, devuelve un resguardo

        Argumentos:
            posicion (Entero): Es la posicion que se desea ver en la mano

        Devuelve:
           Resguardo:Carta
        """
        
        if not 0 <= posicion < len(self._mano):
            raise IndexError("Has tratado de acceder a una posicion que no existe, ojala nunca salga este error")
        
        return self._mano.pop(posicion)
    
    def eliminarCarta(self,Carta):
        
        """ Elimina una carta que le has dado de la mano. Regresa un resguardo

        Argumentos:
            carta(Carta): Es la carta que desea eliminarse de la mano

        Devuelve:
           Resguardo:Carta

        """
        if Carta not in self._mano:
            raise ValueError("La carta no está en la mano")
        
        Resguardo=Carta

        self._mano.remove(Carta)

        return Resguardo
    
    
    
    
    def VerCarta(self,posicion):
        """ Devuelve informacion acerca de la carta que esta en esa posicion dentro de la mano

        Argumentos:
            posicion (Entero): Es la posicion que se desea ver en la mano

        Devuelve:
            Palo (String) : El palo de la carta
            Valor (Entero) : El valor numerico de la carta
        """
        
        
        if not 0 <= posicion < len(self._mano):
            raise IndexError("Has tratado de acceder a una posicion que no existe, ojala nunca salga este error")
        Palo = self._mano[posicion].ver_palo()
        Valor = self._mano[posicion].ver_valor()
        return (Palo,Valor)

    def dar(self,cartas_a_dar, mano_que_recibe):
        """
        Agrega las cartas especificadas a otra mano y las elimina de la mano que la da.
    
        Args:
            cartas_a_dar (list[Cartas]): Cartas a agregar.
            mano_que_recibe (list[Cartas]): Lista de cartas destino.
        """
        for carta in cartas_a_dar:
            mano_que_recibe.agregar_cartas([carta])
            self._mano.remove(carta)
    
    def agregar_cartas(self, cartas):
        for carta in cartas:
            self._mano.append(carta)


    def intercambiar(self, mano1, cartas1, mano2, cartas2):
        """
        Intercambia cartas entre dos manos.

        Args:
        mano1 (Mano): Primer jugador.
        cartas1 (list[Cartas]): Cartas que da el primer jugador.
        mano2 (Mano): Segundo jugador.
        cartas2 (list[Cartas]): Cartas que da el segundo jugador.

        Returns:
        tupla: (cartas_recibidas_por_mano1, cartas_recibidas_por_mano2)
        """
  
        
        mano1.dar(cartas1,mano2)
        mano2.dar(cartas2,mano1)
        resguardos=[cartas1,cartas2]
        return resguardos

    
    def __len__ (self):
        """Metodo que devuelve el largo de la baraja y permite usar len(Mibaraja) fuera de la clase para mas comodidad"""
        return len(self._mano)
    
    def __getitem__ (self, posicion):
        """Metodo que permite usar baraja[i] fuera de la clase"""
        return self._mano[posicion]
    
    def __iter__(self):
        """Metodo que permite iterar fuera de la clase"""

        return iter(self._mano)
