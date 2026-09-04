# 1
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

# 2
def series_voltage_drop(voltage, resistors):
    if not resistors:
        raise ValueError("You must hand in at least one resistance")

    total_resistance = sum(resistors)
    current = voltage / total_resistance

    return [current * r for r in resistors]

# 3
def voltage_divider(voltage_1=None, resistors=None, current=None):
    if resistors is None:
        print("Resistors are required")
        return

    resistances_total = sum(resistors)
    voltages_drops = []


    if voltage_1 is not None:
        for i, r in enumerate(resistors):    
            resistances_cal = r / resistances_total
            drop = voltage_1 * resistances_cal
            voltages_drops.append(drop)
            print(f"Voltage Drop #{i+1} Output:", drop)
        

    if current is None:
        current = voltage_1 / resistances_total
        print("Current: ", current, "A")

    print("Voltage exit: ", sum(voltages_drops))

# 4
def current_divider(resistors:None, current:None):
    It =  sum(current)
    total_r = sum(resistors)

    I1 = It * (resistors[1] / total_r)
    I2 = It * (resistors[0] / total_r)

    print(f"I1 = {I1} A")
    print(f"I2 = {I2} A")
    print(f"It = {I1 + I2} A")

# 6 
def KCL(Vin, R1, *resistors):
    Vnode = Vin / (1 + sum(R1 / R for R in resistors))

    I1 = (Vin - Vnode) / R1
    currents = [Vnode / R for R in resistors]

    print(f"Vnode: {Vnode:.2f} V")
    print(f"I1: {I1:.2f} A")

    for i, current in enumerate(currents, 2):
        print(f"I{i}: {current:.2f} A")

    print(f"KCL: {I1:.2f} = {sum(currents):.2f}")
