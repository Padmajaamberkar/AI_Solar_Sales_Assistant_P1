
import math

class SolarCalculator:

    def __init__(self):
        self.cost_per_kw = 70000
        self.panel_power = 550
        self.unit_rate = 12

    def get_system_size(self, bill):

        if bill <= 1100:
            return 1
        elif bill <= 2200:
            return 2
        elif bill <= 3300:
            return 3
        elif bill <= 4400:
            return 4
        elif bill <= 5500:
            return 5
        elif bill <= 6600:
            return 6
        elif bill <= 7700:
            return 7
        elif bill <= 8800:
            return 8
        elif bill <= 9900:
            return 9
        else:
            return 10

    def calculate(self, bill, roof):

        system_kw = self.get_system_size(bill)

        panels = math.ceil((system_kw * 1000) / self.panel_power)

        roof_required = panels * 30

        installation_cost = system_kw * self.cost_per_kw

        if system_kw == 1:
            subsidy = 30000
        elif system_kw == 2:
            subsidy = 60000
        else:
            subsidy = 78000

        final_cost = installation_cost - subsidy

        monthly_generation = system_kw * 120

        monthly_savings = monthly_generation * self.unit_rate

        yearly_savings = monthly_savings * 12

        payback = round(final_cost / yearly_savings, 1)

        return {
            "system_kw": system_kw,
            "panels": panels,
            "roof_required": roof_required,
            "installation_cost": installation_cost,
            "subsidy": subsidy,
            "final_cost": final_cost,
            "monthly_generation": monthly_generation,
            "monthly_savings": monthly_savings,
            "yearly_savings": yearly_savings,
            "payback": payback
        }
