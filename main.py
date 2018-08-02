#Global Variables:
change_after_set_all = False
value_holder = 0
set_all_counter = 0
bit_limit=255
balance_account_map = dict()


#The pairs in balance_account_map are like this:    < account: [balance_index , setAllIndex] >

balance_index = 0 
set_all_index = 1


def getAccountBalance(account):
    global balance_account_map
    if account not in balance_account_map:
        balance_account_map[account]=[balance_index,set_all_counter]
        return balance_account_map[account][balance_index]

    #account exists in balance_account_map

    if change_after_set_all == False:
        return value_holder

    #operation was made after the setAll

    if balance_account_map[account][set_all_index]<set_all_counter:
        return value_holder
    
    return balance_account_map[account][balance_index]


def setAccount(account, value):
    global balance_account_map
    global change_after_set_all

    change_after_set_all = True
    balance_account_map[account] = [value,set_all_counter]


def resetAllAccountsSetAllCounter():
    global balance_account_map
    for account,balance in balance_account_map.items():
        balance_account_map[account][balance_index] = value_holder
        balance_account_map[account][set_all_index] = set_all_counter


def setAllBalancesWith(value):
    global value_holder
    global change_after_set_all
    global set_all_counter

    value_holder = value
    change_after_set_all = False

    set_all_counter = (set_all_counter+1)%bit_limit

    if(set_all_counter==0):
        resetAllAccountsSetAllCounter()

    #so to keep the 8 bit restriction we're "paying" with O(n) after 256 iterations.

def main():
    global balance_account_map
    global bit_limit

    #can't be zero
    bit_limit = 255

    print("Start program----\n")
    print("Get account 1 balance: ---" + str(getAccountBalance(1)) + "--- (desierd: 0)\n")
    print("Get account 2 balance: ---" + str(getAccountBalance(2)) + "--- (desierd: 0)\n")
    setAllBalancesWith(3)
    print("Get account 2 balance after setAll(3): ---" + str(getAccountBalance(2)) + "--- (desierd: 3)\n")
    setAccount(3,5)
    print("Get account 3 balance after setAccount(3,5): ---" + str(getAccountBalance(3)) + "--- (desierd: 5)\n")    
    setAllBalancesWith(7)
    print("Get account 3 balance after setAll(7): ---" + str(getAccountBalance(3)) + "--- (desierd: 7)\n")
    setAllBalancesWith(11)
    print("Get account 1 balance after setAll(11): ---" + str(getAccountBalance(1)) + "--- (desierd: 11)\n")
    print("End program----\n")

main()