class Seat:
    """Representa um assento no avião."""
    def __init__(self, seat_number: str):
        self.seat_number = seat_number
        self.is_occupied = False

    def occupy(self):
        """Marca o assento como ocupado."""
        self.is_occupied = True

    def __repr__(self):
        return self.seat_number