# Enter Input
name = input('Enter name: ')
hours = float(input('Enter number of hours \
worked weekly: '))
rate = float(input('Enter hourly pay rate: '))
cpf = float(input('Enter CPF contribution \
rate (%): '))


# Calculation
pay = hours*rate
total_cpf = pay*(cpf/100)
net_pay = pay - total_cpf

# Adding unit to variables
rate_w_unit = ['$', '{0:.2f}'.format(rate)]
cpf_w_unit = [int(cpf),'%']
pay_w_unit = ['$', '{0:.2f}'.format(pay)]
total_cpf_w_unit = ['$', '{0:.2f}'.format(total_cpf)]
net_pay_w_unit = ['$', '{0:.2f}'.format(net_pay)]


# Output
print('Payroll statement for', name)
print('Number of hours worked in a week:', int(hours))
print('Hourly pay rate:', ''.join(map(str, rate_w_unit)))
print('Gross pay = ', ''.join(map(str, pay_w_unit)))
print('CPF contribution at', ''.join(map(str, cpf_w_unit)),\
      '=', ''.join(map(str, total_cpf_w_unit)))
print('Net pay =', ''.join(map(str, net_pay_w_unit)))
