with open('salary.txt') as file_salary:
    monthly_salary = [int(monthly.replace('\n', '')) for monthly in file_salary.readlines()]
    annual_salary = [str(monthly * 12) + '\n' for monthly in monthly_salary]

with open('salary_year.txt', 'w') as file_salary_year:
    file_salary_year.writelines(annual_salary)
