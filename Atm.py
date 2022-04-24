class atm(object):
    def __init__(self,cardNumber,pinNumber,CashWthdrawl,BalanceEnquiry = None):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.CashWithdrawl = CashWthdrawl
        self.BalanceEnquiry = BalanceEnquiry
        pass