class BookStore:
    noOfBooks=0;
    def __init__(self,name,Author):
        self.name=name;
        self.Author=Author;
        BookStore.noOfBooks+=1;
    def display(self):
        print("Name: ",self.name);
        print("Author: ",self.Author);
        print("Copies: ",BookStore.noOfBooks);    




def main():
    o1=BookStore("Linux System programming","Robert Love");
    o1.display();

    
    o2=BookStore("C Programming","Dennis Ritchie");
    o1.display();


if __name__=="__main__":
    main();