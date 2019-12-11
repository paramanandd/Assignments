# A basic code for matrix input from user 
  
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(input()) 
    matrix.append(a) 
  
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ")
    print() 
	
	
#------------------PART-I-----------------------------
#Assumption here is considerd that the column number provided is valid
column = int(input("Enter the column number to be printed:"))
print("column at position ", column," is => ")
for i in range(R):
	print(matrix[i][column-1], end = " ")
	print()

#------------------PART-II-----------------------------
#Assumption here is considerd that the row number provided is valid
row = int(input("Enter the row number to be printed:"))
print("row at position ", row," is => ") 
for j in range(C):
	print(matrix[row-1][j], end = " ")
	print()

#------------------PART-III-----------------------------
quad_row = int(input("Enter the valid number for quadrant row:")) 
quad_col = int(input("Enter the valid number for quadrant column:"))
#Assumption here is considerd that the quadrant position provided is valid
print("quadrant for position ", quad_row,",",quad_col," is => ") 
for i in range(R):
            for j in range(C):
                if(i == quad_row-1 and j == quad_col-1):
                    print(matrix[i][j], end = " ")
                elif(i == quad_row and j == quad_col):
                    print(matrix[i][j], end = " ")
                elif(i == quad_row-1 and j == quad_col):
                    print(matrix[i][j], end = " ")
                elif(i == quad_row and j == quad_col-1):
                    print(matrix[i][j], end = " ")
            print()