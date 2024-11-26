import matplotlib.pyplot as plt

def collatz(n):
    sequence = [n]
    
    while n != 1:
        
        if n % 2 == 0:
            n = n // 2
            
        else:
            n = 3 * n + 1
            
        sequence.append(n)
    
    return sequence

def main():
    
    num = int(input("Enter a number: "))
    
    if num < 1:
        print("Please enter a positive integer.")
        
    else:
        result = collatz(num)
        steps = len(result) - 1
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Collatz Conjecture")
        plt.plot(result, marker='o', linestyle='-', color='blue', markerfacecolor='red', markeredgecolor='red')
        plt.show()
    

main()
    

    


        
    