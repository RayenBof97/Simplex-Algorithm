# Code Implemented from Scratch By Rayen Bouafif & Ismail Bouchriha 
import numpy as np 
import numpy.linalg as linalg
#FUNCTIONS : 
def divide_matrix_by_alpha(alpha, matrix_column):
    mask = alpha > 0
    result_matrix = np.zeros_like(matrix_column)
    result_matrix[:, mask] = matrix_column[:, mask] / alpha[mask]
    result_matrix[result_matrix == 0] = np.max(result_matrix) + 1
    out_vector = np.argmin(result_matrix)
    teta=np.min(result_matrix)
    return out_vector,teta



# Constraint Matrix A (Canonical Form) : 
Canonical_A = np.array([
    [1, 1],
    [2, 1],
    [1, 0],
])
# b Matrix :
B=np.array([[80,100,40]])
#Objective Matrix C : 
C=np.array([
    [3,2]
])

#Tranforming to Standard form : 
shape=Canonical_A.shape   #Shape = (m,n) (Tuple Type) where m is the number of constraint and n number of decision variables
Base= np.eye(shape[0]) # Base Matrix (Start)
print(Base)
Standard_A= np.hstack((Canonical_A,Base)) 
C_b=np.zeros((1,shape[0]))
standard_C= np.hstack((C,C_b))

#Step 0 : Initialisation 
Xn=np.zeros((1,shape[1])) #Decision Variables
Xb=B #Slope Variables
X= np.arange(1, Standard_A.shape[1]+1)
i=1
while True:
    #Step 1 
    print('------------------Iteration ',i)
    print(' ')
    y=standard_C[:, shape[1]:].dot(linalg.inv(Standard_A[:, shape[1]:]))
    print('y= ',y)
    print(' ')

    #Step 2 (Reduction Costs) :
    delta = standard_C[:, :shape[1]] - y.dot(Standard_A[:, :shape[1]])
    print('delta = ',delta)
    print(' ')
    #Step 3 (Optimum Test) : 
    if np.all(delta < 0):
        print("Optimality !")
        print(' ')
        break

    #Step 4 (In Base Vector)
    in_vector = np.argmax(delta)

    #Step 5 :
    alpha_values= linalg.inv(Standard_A[:, shape[1]:]).dot(Standard_A[:,in_vector])
    print('alpha = ',alpha_values)
    print(' ')
    if np.all(alpha_values < 0):
        print("Non bornée") 
        break
    out_vector,teta = divide_matrix_by_alpha(alpha_values, Xb)
    print('teta = ',teta)
    print(' ')
    #Step 6: 
    Xn[0,in_vector]=teta
    Xb=Xb-teta*alpha_values
    temp = np.copy(Xn[:, in_vector])
    Xn[:, in_vector] = Xb[:, out_vector]
    Xb[:, out_vector] = temp
    Standard_A[:, [in_vector, out_vector+shape[1]]] = Standard_A[:, [out_vector+shape[1], in_vector]]
    standard_C[:, [in_vector, out_vector+shape[1]]] = standard_C[:, [out_vector+shape[1], in_vector]]
    X[in_vector], X[out_vector+shape[1]] = X[out_vector+shape[1]], X[in_vector]
    print(Standard_A)
    print(' ')
    print(standard_C)
    print(' ')
    i=i+1
    
    
Xn= np.hstack((Xn,Xb)) 
Xn=Xn[0]
Solution = np.empty_like(Xn)
Solution[X - 1] = Xn

Solution = Solution.reshape(1, -1)
print('X* = ',Solution[0])
objective=Solution[:,:shape[1]].dot(C.reshape(-1,1))
print('Z* = ',objective[0,0])
