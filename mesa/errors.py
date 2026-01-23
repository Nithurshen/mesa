"""Mesa-specific exception hierarchy."""


class MesaError(Exception):
    """Base class for all Mesa-specific exceptions."""


class CellNotEmptyError(MesaError):
    """Raised when attempting to place an agent in an already occupied cell."""

    def __init__(self, pos):
        """Initialize the exception.

        Args:
            pos: The coordinate tuple that caused the error.
        """
        self.pos = pos
        super().__init__(f"Cell at position {pos} is not empty.")
