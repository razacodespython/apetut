# Define the version
# @version ^0.3.0

# Create a string variable that can store maximum 100 characters
greet: public(String[100])

#Define the visibility with a decorator
@external

#This is the constructor that sets the value of the variable greet 
#upon deploying the smart contract
def __init__():
    self.greet = "Hello World"