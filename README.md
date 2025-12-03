# `Calc.py` - Documentación de la Clase `FinancialCalculator`

Este documento proporciona una guía técnica para la clase `FinancialCalculator`, diseñada para simplificar cálculos financieros comunes como el interés compuesto, el retorno de inversión (ROI) y la simulación de conversiones de moneda.

---

## Contenido

- [Clase `FinancialCalculator`](#clase-financialcalculator)
  - [`__init__(self, base_currency: str = "USD")`](#__init__self-base_currency-str--usd)
  - [`calculate_compound_interest(self, principal: float, rate: float, time: int, compounds_per_year: int = 1) -> float`](#calculate_compound_interestself-principal-float-rate-float-time-int-compounds_per_year-int--1---float)
  - [`calculate_roi(self, investment: float, return_amount: float) -> float`](#calculate_roi-self-investment-float-return_amount-float---float)
  - [`estimate_currency_conversion(self, amount: float, target_currency: str) -> str`](#estimate_currency_conversionself-amount-float-target_currency-str---str)
- [Ejemplos de Uso](#ejemplos-de-uso)

---

## Clase `FinancialCalculator`

Una clase simple y robusta para realizar cálculos financieros comunes, proporcionando métodos para el interés compuesto, el retorno de inversión y la conversión simulada de monedas.

### `__init__(self, base_currency: str = "USD")`

Inicializa una nueva instancia de `FinancialCalculator` con una moneda base especificada.

#### Parámetros

- `base_currency` (str, opcional): La moneda base para los cálculos, por defecto es `"USD"`.

#### Ejemplo de Uso

```python
from Calc import FinancialCalculator

# Inicializar con la moneda base por defecto (USD)
calc_usd = FinancialCalculator()

# Inicializar con otra moneda base
calc_eur = FinancialCalculator(base_currency="EUR")
```

### `calculate_compound_interest(self, principal: float, rate: float, time: int, compounds_per_year: int = 1) -> float`

Calcula el monto final de una inversión con interés compuesto.

#### Fórmula

`A = P(1 + r/n)^(nt)`
Donde:
- `A` = Monto futuro de la inversión/préstamo, incluyendo el interés.
- `P` = Monto del capital inicial (principal).
- `r` = Tasa de interés anual (como decimal, pero se espera en porcentaje en el parámetro).
- `n` = Número de veces que el interés se capitaliza por año.
- `t` = Número de años que el dinero se invierte o se presta.

#### Parámetros

- `principal` (float): El monto del capital inicial.
- `rate` (float): La tasa de interés anual en porcentaje (ej. 5 para 5%).
- `time` (int): El número de años que el dinero se invierte.
- `compounds_per_year` (int, opcional): El número de veces que el interés se capitaliza por año. Por defecto es `1` (anualmente).

#### Retorna

- `float`: El monto total (capital + interés) redondeado a dos decimales.

#### Excepciones

- `ValueError`: Si `principal`, `rate` o `time` son valores negativos.

#### Ejemplo de Uso

```python
from Calc import FinancialCalculator

calc = FinancialCalculator()

# Calcular interés compuesto para $1000 a 5% anual durante 10 años, capitalizado anualmente
amount_annual = calc.calculate_compound_interest(principal=1000, rate=5, time=10)
print(f"Monto con interés compuesto (anual): {amount_annual}")
# Salida esperada: Monto con interés compuesto (anual): 1628.89

# Calcular interés compuesto para $1000 a 5% anual durante 10 años, capitalizado trimestralmente (4 veces/año)
amount_quarterly = calc.calculate_compound_interest(principal=1000, rate=5, time=10, compounds_per_year=4)
print(f"Monto con interés compuesto (trimestral): {amount_quarterly}")
# Salida esperada: Monto con interés compuesto (trimestral): 1643.62

# Intento con valores negativos (generará ValueError)
try:
    calc.calculate_compound_interest(-100, 5, 10)
except ValueError as e:
    print(f"Error: {e}")
# Salida esperada: Error: Los valores no pueden ser negativos
```

### `calculate_roi(self, investment: float, return_amount: float) -> float`

Calcula el Retorno de Inversión (ROI) en porcentaje.

#### Parámetros

- `investment` (float): El monto inicial de la inversión.
- `return_amount` (float): El monto final recibido de la inversión.

#### Retorna

- `float`: El ROI en porcentaje, redondeado a dos decimales. Si la inversión es `0`, retorna `0.0`.

#### Ejemplo de Uso

```python
from Calc import FinancialCalculator

calc = FinancialCalculator()

# Calcular ROI para una inversión de 1000 que retorna 1200
roi_positive = calc.calculate_roi(investment=1000, return_amount=1200)
print(f"ROI positivo: {roi_positive}%")
# Salida esperada: ROI positivo: 20.0%

# Calcular ROI para una inversión de 1000 que retorna 800 (pérdida)
roi_negative = calc.calculate_roi(investment=1000, return_amount=800)
print(f"ROI negativo: {roi_negative}%")
# Salida esperada: ROI negativo: -20.0%

# Calcular ROI cuando la inversión inicial es 0
roi_zero_investment = calc.calculate_roi(investment=0, return_amount=500)
print(f"ROI con inversión cero: {roi_zero_investment}%")
# Salida esperada: ROI con inversión cero: 0.0%
```

### `estimate_currency_conversion(self, amount: float, target_currency: str) -> str`

Simula una conversión de moneda desde la `base_currency` de la calculadora a una `target_currency`.
**Nota:** Las tasas de conversión están codificadas (`hardcoded`) para este ejemplo (Prueba de Concepto - POC) y no representan tasas de cambio en tiempo real.

#### Parámetros

- `amount` (float): La cantidad de dinero a convertir.
- `target_currency` (str): El código de la moneda a la que se desea convertir (ej. "EUR", "GBP", "JPY").

#### Tasas de Conversión Simuladas

| Moneda de Destino | Tasa (por 1 USD) |
| :---------------- | :--------------- |
| EUR               | 0.85             |
| GBP               | 0.75             |
| JPY               | 110.0            |

#### Retorna

- `str`: Una cadena de texto formateada que indica la conversión o un mensaje de error si la `target_currency` no está disponible.

#### Ejemplo de Uso

```python
from Calc import FinancialCalculator

calc = FinancialCalculator(base_currency="USD")

# Convertir 100 USD a EUR
conversion_eur = calc.estimate_currency_conversion(amount=100, target_currency="EUR")
print(f"Conversión a EUR: {conversion_eur}")
# Salida esperada: Conversión a EUR: 100.0 USD son aproximadamente 85.00 EUR

# Convertir 50 USD a JPY
conversion_jpy = calc.estimate_currency_conversion(amount=50, target_currency="JPY")
print(f"Conversión a JPY: {conversion_jpy}")
# Salida esperada: Conversión a JPY: 50.0 USD son aproximadamente 5500.00 JPY

# Intentar convertir a una moneda no soportada
conversion_unsupported = calc.estimate_currency_conversion(amount=100, target_currency="CAD")
print(f"Conversión no soportada: {conversion_unsupported}")
# Salida esperada: Conversión no soportada: Lo sentimos, no tenemos la tasa para CAD
```

## Ejemplos de Uso

A continuación, se muestra un ejemplo básico de cómo utilizar la clase `FinancialCalculator` y sus métodos.

```python
from Calc import FinancialCalculator

# Crear una instancia de la calculadora financiera
calc = FinancialCalculator(base_currency="USD")

print("--- Cálculos Financieros ---")

# 1. Calcular Interés Compuesto
principal_amount = 5000
interest_rate = 6.5  # 6.5% anual
years = 5
compounds = 12 # Compuesto mensualmente

final_amount = calc.calculate_compound_interest(
    principal=principal_amount,
    rate=interest_rate,
    time=years,
    compounds_per_year=compounds
)
print(f"Interés Compuesto:")
print(f"  - Capital inicial: {principal_amount} {calc.base_currency}")
print(f"  - Tasa anual: {interest_rate}%")
print(f"  - Años: {years}")
print(f"  - Compuesto: {compounds} veces al año")
print(f"  - Monto final: {final_amount} {calc.base_currency}\n")


# 2. Calcular Retorno de Inversión (ROI)
initial_investment = 15000
final_return = 18000

roi = calc.calculate_roi(investment=initial_investment, return_amount=final_return)
print(f"Retorno de Inversión (ROI):")
print(f"  - Inversión inicial: {initial_investment} {calc.base_currency}")
print(f"  - Monto de retorno: {final_return} {calc.base_currency}")
print(f"  - ROI: {roi}%\n")


# 3. Estimar Conversión de Moneda
amount_to_convert = 250
target_currency_eur = "EUR"
target_currency_jpy = "JPY"
target_currency_cad = "CAD" # Moneda no soportada por las tasas hardcoded

conversion_result_eur = calc.estimate_currency_conversion(amount=amount_to_convert, target_currency=target_currency_eur)
conversion_result_jpy = calc.estimate_currency_conversion(amount=amount_to_convert, target_currency=target_currency_jpy)
conversion_result_cad = calc.estimate_currency_conversion(amount=amount_to_convert, target_currency=target_currency_cad)

print(f"Estimación de Conversión de Moneda:")
print(f"  - {conversion_result_eur}")
print(f"  - {conversion_result_jpy}")
print(f"  - {conversion_result_cad}\n")
```