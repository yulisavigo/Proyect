from abc import abstractmethod, ABC


class ServicioMensaje(ABC):
    @abstractmethod
    def enviar(self, msg): pass
class ServicioSMS(ServicioMensaje):
    def enviar(self, msg): print(f"SMS: {msg}")
class ServicioEmail(ServicioMensaje):
    def enviar(self, msg): print(f"Email: {msg}")
class Notificador:
    def __init__(self, servicio: ServicioMensaje): # Inyección de dependencia
        self.servicio = servicio
    def enviar_alerta(self, msg):
        self.servicio.enviar(msg)