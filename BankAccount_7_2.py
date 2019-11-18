class BankAccount:
    ROI=10.5;
    def __init__(self,name,Amount):
        self.name=name;
        self.Amount=Amount;
    def Deposit(self,amount):
        self.Amount+=amount;
        print("After Deposit: ",self.Amount);
    def Withdraw(self,amount):
        self.Amount-=amount;    
        print("After Withdraw: ",self.Amount);
    def Calculate_Interest(self):
        print("Amount with Interest: ",(self.Amount/100)*BankAccount.ROI+self.Amount);
    def Display(self):
        print("Name: ",self.name);       
        print("Amount: ",self.Amount);     





def main():
    c1=BankAccount("Vithal",500);
    c1. Display();
    c1.Deposit(500);
    c1.Withdraw(200);
    c1.Calculate_Interest();
    

    print("********************************************************")


    c2=BankAccount("Ankit",1000);
    c2. Display();
    c2.Deposit(500);
    c2.Withdraw(200);
    c2.Calculate_Interest();
   
if __name__=="__main__":
    main();