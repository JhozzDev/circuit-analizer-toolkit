def ohms_law(v=None, i=None, r=None):

    dados = sum(x is not None for x in (v, i, r))
    if dados != 2:
        raise ValueError("You must provide 2 of the 3 elements (v, i, r)")

    if v is None:
        v = i * r
    elif i is None:
        if r == 0:
            raise ZeroDivisionError("R  cannot be 0")
        i = v / r
    elif r is None:
        if i == 0:
            raise ZeroDivisionError("I cannot 0")
        r = v / i

    return {"v": v, "i": i, "r": r}

def series_voltage_drop(voltage, resistors):
    if not resistors:
        raise ValueError("You must hand in at least one resistance")

    total_resistance = sum(resistors)
    current = voltage / total_resistance

    return [current * r for r in resistors]