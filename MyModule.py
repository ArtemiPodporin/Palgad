#11
def calculate_net_salary(gross_salary, tax_rate):
    net_salary = gross_salary * (100 - tax_rate) / 100
    return net_salary

def print_net_salaries(names, salaries, tax_rate):
    for i in range(len(names)):
        net_salary = calculate_net_salary(salaries[i], tax_rate)
        print(f"{names[i]}: netopalk = {net_salary}")

#19
from palgad import average_salary

palgad = [1200, 2500, 750, 395, 1200]
avg = average_salary(palgad)
print("Средняя зарплата:", avg)