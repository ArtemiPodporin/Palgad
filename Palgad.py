#11
def calculate_salary(gross_salary, tax_rate):
    net_salary = gross_salary - (gross_salary * tax_rate / 100)
    return net_salary
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]
tax_rate = 13 
for i in range(len(palgad)):
    net_salary = calculate_salary(palgad[i], tax_rate)
    print(f"{inimesed[i]}: netopalk = {net_salary}")

#19
from palgad import salary_increase

palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

print("Изначальный список зарплат:", palgad)

percent = int(input("Введите процент увеличения зарплаты: "))
new_palga = salary_increase(palgad, inimesed, percent)

print("Обновленный список зарплат:", new_palga)