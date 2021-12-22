import sys
class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def toString(self):
        return self.name+": "+str(self.price)

def cmp(a,b):
    return a.price-b.price

class Goodies:
    def main():
        sc=sys.stdin=open("C:/Users/ADMIN/Desktop/HIGH PEAK/input.txt","r")
        no_of_employees=int(input().split(": ")[1])
        input()
        input()
        input()
        goodies=[]
        for Item in sc:
            current=input().split(": ")
            goodies.append(Item(current[0],int(current[1])))
        sc.close()
        sorted_goodies=[]
        sorted_goodies=sorted(goodies)
        min_diff=sorted_goodies[len(sorted_goodies)-1].price
        min_index=0
        i=0
        while(i<len(sorted_goodies)-no_of_employees+1):
            diff = sorted_goodies[no_of_employees+i-1].price-sorted_goodies[i].price
            if (diff <= min_diff):
                min_diff=diff
                min_index=i
            i+=1
        fw=open("C:/Users/ADMIN/Desktop/HIGH PEAK/output.txt")
        fw.write("Here the goodies that are selected for distribution are:\n")
        i = min_index
        while(i<min_index+no_of_employees):
            fw.write(sorted_goodies[i].toString()+"\n")
            i+=1
        fw.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is "+str(min_diff))
        fw.close()

if __name__=="__main__":
    Goodies.main()