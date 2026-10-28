*# Basic Dtypes and Type Casting-Coversion*
T = 10 # int
#int -str
type(T)
str(T) # Temporaory print
T = str(T) #'10' - Permanently assigning str to T
type(T)
#str-float
float(T) # 10.0
T = float(T)
type(T)

T =None # making T as null
bool(T) # False bcz no value in T

# T =10.0 # float
# T = "Anand" # str
# T = None 
# T = True # bool

# # Sequential Dtypes
T = [120,12.5, [True, "Vamsi"], (1,2,3), 34, {34.5,3,4,32,3}] # List
# print(T)
type(T) #List
tuple(T)  # (120, 12.5, [True, 'Vamsi'], (1, 2, 3), 34, {3, 4, 32, 34.5})
type(T) #list
T = tuple(T) # permamenet assign
type(T)
# T = (120,12.5, [True, "Vamsi"], (1,2,3), 34, {34.5,3,4,32,3}) # Tuple
# print(T)
# T = {1,10,2,4,45,14,4 ,2, 53} # Set
# T = frozenset({12,213,2,3,21})
# print(T)

# # Mapping
# T = {'Key1' : "Value1", 2: "Value2"}
# print(T)
