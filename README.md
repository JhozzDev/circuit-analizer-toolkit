# Circuit Toolkit

A Python toolkit that contains functions for performing basic electronical circuit calculations.

The goal of this project is to turn fundamental electronics formulas into reusable Python functions.

## Functions

### `ohms_law()`

Calculates the missing value between voltage, current, and resistance.

```text
V = I × R
I = V / R
R = V / I
```

Requires exactly two of the three values:

```python
ohms_law(v=12, r=4)
```

Returns:

```python
{
    "v": 12,
    "i": 3.0,
    "r": 4
}
```

---

### `series_voltage_drop()`

Calculates the voltage drop across each resistor in a series circuit.

For a series circuit:

```text
RT = R1 + R2 + ... + Rn
```

The current is:

```text
I = V / RT
```

And the voltage drop across each resistor is:

```text
VR = I × R
```

Example:

```python
series_voltage_drop(20, [5, 10, 5])
```

Returns:

```python
[5.0, 10.0, 5.0]
```

The sum of all voltage drops equals the source voltage:

```text
5V + 10V + 5V = 20V
```

##  Purpose

This project is part of my bio-electronics self-study.

I am using Python to implement the formulas and methods I learn while studying electronics circuits.

## Planned Functions

The toolkit will be expanded with more circuit-analysis functions, including:

* Parallel resistance
* Voltage divider
* Current divider
* Power calculations
* KCL
* KVL
* Nodal analysis
* Mesh analysis
* Unit conversions

## Technology

* Python
* NumPy 

## Status

Work in progress. New functions will be added as I progress through circuit analysis.
