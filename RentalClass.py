class RoiCalc():

    incomeDict = {}
    expensesDict = {}

    def __init__(self):
        self.purchasePrice = 0
        self.income = 0
        self.expenses = 0
        self.annualCashFlow = 0
        self.totalInvest = 0
        self.roi = 0

    def incomeToDict(self):
        itemNum = int(input("How many income items do you have?: "))
        for i in range(0,itemNum):
            what = input("Item Description: ")
            howMuch = float(input("$?: "))
            self.incomeDict[what] = howMuch
        
        v = self.incomeDict.values()
        self.income = sum(v)

    def expenseToDict(self):
            itemNum = int(input("How many expenses do you have?: "))
            for i in range(0,itemNum):
                what = input("Item Description: ")
                howMuch = float(input("$?: "))
                self.expensesDict[what] = howMuch
            
            v = self.expensesDict.values()
            self.expenses = sum(v)

    def cashFlowCalc(self):
        self.annualCashFlow = (self.income - self.expenses)*12

    def roiCalc(self):
        self.totalInvest = float(input('Total value of investments?$: '))
        self.roi = float((self.annualCashFlow/self.totalInvest)*100)

    def cashOnCashReturn(self):
        self.incomeToDict()
        self.expenseToDict()
        self.cashFlowCalc()        
        self.roiCalc()
        print(f"Total Income: ${self.income:.2f}")
        print(f"Total Expenses: ${self.expenses:.2f}")
        print(f"Total Investments: ${self.totalInvest:.2f}")
        print(f"Roi: {self.roi:.2f}%")
        
