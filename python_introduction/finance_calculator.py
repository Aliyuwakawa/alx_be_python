#!/usr/bin/env python3
monthly_income = input("Enter your monthly income: ")
monthly_expense = input("Enter your monthly expense: ")
monthly_savings = float(monthly_income) - float(monthly_expense)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f"Your annual savings: ${projected_savings:.2f}")

