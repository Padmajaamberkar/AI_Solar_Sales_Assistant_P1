
import os
import pandas as pd

FILE = "data/customers.xlsx"

def save_customer(customer, mobile, email, city, bill, roof, result):

    os.makedirs("data", exist_ok=True)

    new_data = pd.DataFrame([{
        "Customer": customer,
        "Mobile": mobile,
        "Email": email,
        "City": city,
        "Monthly Bill": bill,
        "Roof Area": roof,
        "System Size (kW)": result["system_kw"],
        "Panels": result["panels"],
        "Installation Cost": result["installation_cost"],
        "Subsidy": result["subsidy"],
        "Final Cost": result["final_cost"],
        "Monthly Savings": result["monthly_savings"],
        "Yearly Savings": result["yearly_savings"],
        "Payback": result["payback"]
    }])

    if os.path.exists(FILE):
        old = pd.read_excel(FILE)
        old = pd.concat([old, new_data], ignore_index=True)
        old.to_excel(FILE, index=False)
    else:
        new_data.to_excel(FILE, index=False)
