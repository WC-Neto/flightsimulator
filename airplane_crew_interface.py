from abc import ABC, abstractmethod

class IAirplaneCrew(ABC):
    """
    Interface que define o contrato para todos os membros da tripulação.
    Garante que toda classe de tripulante tenha os métodos essenciais.
    """
    
    @abstractmethod
    def check_credentials(self) -> bool:
        """Verifica se as credenciais do tripulante são válidas."""
        pass

    @abstractmethod
    def report_for_duty(self):
        """Apresenta o tripulante para o serviço."""
        pass