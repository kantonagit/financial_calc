import math

class FinancialCalculator:
    """
    Una clase simple para realizar calculos financieros comunes.
    """

    def __init__(self, base_currency: str = "USD"):
        self.base_currency = base_currency

    def calculate_compound_interest(self, principal: float, rate: float, time: int, compounds_per_year: int = 1) -> float:
        """
        Calcula el interés compuesto.
        
        Formula: A = P(1 + r/n)^(nt)
        """
        if principal < 0 or rate < 0 or time < 0:
             raise ValueError("Los valores no pueden ser negativos")

        # Convertir tasa porcentual a decimal
        decimal_rate = rate / 100
        
        amount = principal * math.pow((1 + decimal_rate / compounds_per_year), (compounds_per_year * time))
        return round(amount, 2)

    def calculate_roi(self, investment: float, return_amount: float) -> float:
        """
        Calcula el Retorno de Inversión (ROI) en porcentaje.
        """
        if investment == 0:
            return 0.0
            
        roi = ((return_amount - investment) / investment) * 100
        return round(roi, 2)

    def estimate_currency_conversion(self, amount: float, target_currency: str) -> str:
        """
        Simula una conversión de moneda (Hardcoded para la POC).
        """
        # Tasas simuladas
        rates = {
            "EUR": 0.85,
            "GBP": 0.75,
            "JPY": 110.0
        }
        
        if target_currency not in rates:
            return f"Lo sentimos, no tenemos la tasa para {target_currency}"
            
        converted = amount * rates[target_currency]
        return f"{amount} {self.base_currency} son aproximadamente {converted:.2f} {target_currency}"

if __name__ == "__main__":
    # Prueba rápida
    calc = FinancialCalculator()
    print(f"Interés Compuesto: {calc.calculate_compound_interest(1000, 5, 10)}")