def yearly_return(start):
    monthly_growth = 1.1
    # Assuming monthly growth is 6.5%
    return start * (pow(monthly_growth, 12))


withdraw = 0.2
gain = 0
start = float(input('Start balance: '))
for_you = 0
for i in range(int(input('Years: '))):
    new_yearly_return = yearly_return(start)
    gain += new_yearly_return - start
    start = new_yearly_return * (1 - withdraw)
    for_you = new_yearly_return * withdraw

print('Total gain: £{}'.format(round(gain, 2)))
print('Reinvestment balance: £{}'.format(round(start, 2)))
print('For you: £{}'.format(round(for_you, 2)))
