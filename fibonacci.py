
def fibonacci(n):
    """
    Calcula el número Fibonacci en la posición n.

    Args:
        n (int): posición en la serie.

    Returns:
        int: número Fibonacci correspondiente.

    Raises:
        TypeError: si n no es entero.
        ValueError: si n es negativo.
    """
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    if n < 0:
        raise ValueError("n no puede ser negativo")

    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
