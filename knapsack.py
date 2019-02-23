import knapsack as knapSack
# A naive recursive implementation of 0-1 Knapsack Problem 

# Returns the maximum value that can be put in a knapsack of 
# capacity M 
def knapSack(M, W, P, n): 
    K = [[0 for x in range(M + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for m in range(M + 1): 
            if i == 0 or m == 0: 
                K[i][m] = 0
            elif W[i-1] <= m: 
                K[i][m] = max(P[i-1] + K[i-1][m-W[i-1]],  K[i-1][m]) 
            else: 
                K[i][m] = K[i-1][m] 
  
    return K[n][M] 
  
# Driver program to test above function 
M = 15
W = [5, 7, 9, 6]
P = [10, 15, 17, 12] 
n = len(P) 
print(knapSack(M, W, P, n)) 
