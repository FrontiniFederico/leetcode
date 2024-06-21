# https://leetcode.com/problems/grumpy-bookstore-owner/description/


def satisfiedCustomer(customers: list, grumpy: list) -> int:
    """Senza curars della sliding window, calcola i clienti soddisfatti."""
    total: int = 0
    for index, elem in enumerate(customers):
        if not grumpy[index]:
            total += customers[index]
    return total

def secretGrumpiness(customers, grumpy, minutes) -> int:
    """Modifica la lista grumpy con i minuti di tecnica segreta 
    e calcola i clienti soddisfatti."""
    max: int = 0
    for index in range(len(customers)-minutes+1):
        grumpy_copy: list = grumpy.copy()
        for mod in range(minutes):
            grumpy_copy[index+mod] = 0
        esito = satisfiedCustomer(customers, grumpy_copy)
        if esito>max:
            max = esito
    return max

def optimizedSecretGrumpiness(customers, grumpy, minutes) -> int:
    """Non ricalcola i clienti soddisfatti in toto, ma quando fai sliding
    vede se aggiungere al minimo massimo qualcosa. Più efficiente. """
    max: int = 0
    low_max: int = satisfiedCustomer(customers, grumpy)
    for index in range(len(customers)-minutes+1):
        low_max_copy = low_max
        for mod in range(minutes):
            if grumpy[index+mod] == 1:
                low_max_copy += customers[index+mod]
        if low_max_copy>max:
            max = low_max_copy
    return max