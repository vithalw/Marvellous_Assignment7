class Numbers:
    def __init__(self,value):
        self.value=value;



    def ChkPrime(self):
        flag=0;
        if (self.value==0 or self.value==1 or self.value==2 ):
            print("Number is Prime");
        else:
            for i in range(1,self.value,1):
                if((self.value%i)==0):
                    flag=1;
        if(flag==1):
            print("Number not prime");
        if(flag==0):
            print("Number  prime");        
            
    @classmethod        
    def sumOfFactors(cls,arr):
        sum=int(0);
        for i in range(0,len(arr),1):
            sum=sum+arr[i];
        print("Sum is: ",sum);    
        return sum;                      

    def ChkPerfect(self,arr):
        #sum=sumOfFactors(arr);
        if(self.value==(Numbers.sumOfFactors(arr))):
            print("Perfect");
        else:
            print("Not Perfect")    

    def Factors(self):
        arr=list();
        for i in range(1,self.value,1):
            if((self.value%i)==0):
                arr.append(i);
        print("Factors: ",arr);
        return arr;  

   

def main():

    n1=Numbers(7);
    n1.ChkPrime();
    brr=n1.Factors();        
    n1.ChkPerfect(brr);    
   
if __name__=="__main__":
    main();