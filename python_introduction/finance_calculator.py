#!/usr/bin/env python3
monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your monthly expense: "))
montly_savings = monthly_income - monthly_expense
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your annual savings: ${projected_savings:.2f}")

