from ape import accounts, project

def main(): 
      # Initialize deployer account and print balance 
    dev_account = accounts.load("anvil2") 
    print(f'The account balance is: {dev_account.balance / 1e18} ETH')  
     # Deploy the smart contract and print a message 
    # kw = {
    #     'type': 0
    # }
    dev_account.deploy(project.hello) 
    print("Contract deployed!")