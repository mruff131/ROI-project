class Rental():
    def totalIncome(self):
        while True:
            self.income = get_input("Enter Monthly Rental Income:")
            if self.income == 0:
                print('You must enter an amount greater than 0.')
                continue
            else:
                break         

    def totalExpenses(self):
        print('Enter your monthly Expenses, if not applicable hit enter or 0\n')
        self.morgage = get_input('Morgage: ')
        self.taxes = get_input('Taxes:')
        self.the_HOA = get_input('Home Owner Association Fees: ')
        self.vacancy = get_input('Vacancy: ')
        self.repairs = get_input('Repairs: ')
        self.cap = get_input('CapEx: ')
        self.management = get_input('Property Management: ')
        while True:
            response = input('Utilities? (Enter Y/N): ')
            if response.lower() == 'y':
                elec = get_input('Electric: ')
                water = get_input('Water: ')
                sewer = get_input('Sewer: ')
                garbage = get_input('Garbage: ')
                gas = get_input('Gas: ')
                other_util = get_input('Other (if applicable): ')
                self.total_util = elec + water + sewer + garbage + gas + other_util
                break
            elif response.lower() == 'n':
                self.total_util = 0
                break
            else:
                print('Invalid Response')
                continue
        print(f'Total Utilties: {self.total_util}')
        other = get_input('Other Miscellaneous Expenses (monthly total): ')
        self.total_exp = (self.morgage + self.taxes + self.the_HOA + self.vacancy + self.repairs +
                      self.cap + self.management + self.total_util + other)
        print('=====================================')
        print(f'Total Monthly Expenses: {self.total_exp}')

    def cashFlow(self):
        pass
        self.flow = (self.income - self.total_exp) # monthly
        return round(self.flow,2)

    def cashOnCashROI(self):
        print('To calculate ROI, enter total investments on property. If not applicable hit enter or 0\n')
        payment = get_input('Cash or Down Payment Amount: ')
        c_costs = get_input('Closing Costs:')
        rehab = get_input('Rehab Costs: ')
        misc = get_input('Other Miscellaneous:')
        total_investment = payment + c_costs + rehab + misc
        print('Calculating Total Investments.............')
        print('..................................')
        print('.......................')
        print(f'Total Investments: {total_investment}')
        print('Calculating Return On Investments.............')
        print('..................................')
        print('.......................')
        roi = ((self.flow * 12) / total_investment) * 100
        return round(roi,2)


def get_input(prompt, default=0):
    while True:
        try:
            value = input(prompt).strip()
            if not value:  # User just hit enter causing empty ''
                return default # zero
            return int(value)
        except ValueError:
            print("Invalid Entry, Enter a number.")


calculator = Rental()

def run():
    while True:
        print('===========================================================================')
        print('===========================================================================')
        print("Welcome to Bigger Pockets's Automated Rental Calculator!")
        print("Calculate Return on Investment for rental properties in just 3 easy steps!")
        print('===========================================================================')
        user_input = input("Enter 'yes' to continue or 'no' to exit....\n")
        if user_input.lower() =='yes':
            print('=====================================')
            print('Step One, Entering Income\n')
            calculator.totalIncome()
            print('=====================================')
            print('Step Two, Tracking Expenses\n')
            calculator.totalExpenses()
            your_cashflow = calculator.cashFlow()
            print(f'Based on your entries, your total Cash flow is ${your_cashflow}/month.')
            print('=====================================')
            print('Step Three, Calculating Investments\n')
            your_return = calculator.cashOnCashROI()
            print(f'Return On Investments: % {your_return}')
            print('===========================================================================')    
        elif user_input.lower() == 'n':
            break
        else:
            print('=====================================')
            print('Invalid Response, try again.')
            print('=====================================')
        while True:
            another = input('Would you like to do another calculation? (Enter Y/N): ')
            if another.upper() == 'Y':
                run()
            
            elif another.upper() != 'N':
                print('Invalid Response, try again.')    
            else:
                break
        break
        
            
run()
