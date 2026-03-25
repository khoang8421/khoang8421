# Project 1 — Enhanced ATM Simulator with User Accounts
# Topics tested: functions, loops, conditionals, dictionaries, error handling
# Prompt:
# Write a function atm_system(users, transactions) where:
# users is a dictionary mapping username → balance.

# transactions is a list of dictionaries:
# {"user": str, "type": "deposit" or "withdraw", "amount": float}


# Apply transactions to the appropriate user.
# Withdrawals that exceed balance → skip and log "Insufficient funds for USER"
# Users not in the system → skip and log "Unknown user: USER"
# Return:
# {
#   "final_balances": {username: balance},
#   "successful": count_of_successful,
#   "failed": count_of_failed
# }

# Constraints / Skills Practiced:
# Loops, nested dicts, error handling, string formatting
# Handle empty users or empty transactions
# Avoid using sum() or other built-ins for aggregation
# Extra Challenge:
# Implement a function to return the richest user.

transactions = [{"user": "Kyle", "type": "deposit", "amount": 103230001.0},
                {"user": "Kaylee", "type": "withdraw", "amount": 1000000.0},
                {"user": "Kyle", "type": "deposit", "amount": 73203230000.0}]

users = {}

def atm_systems(users, transactions):

    successful = 0
    failed = 0

    for transaction in transactions:

        if not transaction:
            failed += 1

        user = transaction["user"]
        type = transaction["type"]
        amount = transaction["amount"]

        if user not in users:
            users[user] = 0.0
        
        if type == "withdraw":
            users[user] -= amount
            successful += 1
        
        if type == "deposit":
            users[user] += amount
            successful += 1

    return {
  "final_balances": users,
  "successful": successful,
  "failed": failed
}

print(atm_systems(users, transactions))
        

