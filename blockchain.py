# Initializing blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchin value to the block blockchin

    Arguments:
      :transaction_amount: The amount that should be added
      :last_transaction: The last blockchain transaction (default [1])
    """
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float """
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to console
    for block in blockchain:
        print('Outputting block')
        print(block)


# Get first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        continue
    else:
        print('Input was invalid, please pick a value from the list!')
    print('Choice registered!')

print('Done!')
