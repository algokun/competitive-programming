def sum(array):
    total = 0
    for i in array:
        total += i
    return total
    
    
def main():
    T = int(input())
    outputs = []
    
    for i in range(T):
        N, C  = input().split()
        numbers = [int(n) for n in input().split()]
        total = sum(numbers)
        C = int(C)
        
        if(total <= C):
            outputs[i] = True        
        
        else:
            outputs[i] = False
    
    for op in outputs:
        if op:
            print("Yes")
        else:
            print("No")


    
if __name__=='__main__': 
    main()