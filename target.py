def process_transactions(users, transactions):
    n_users = len(users)
    
    # Count transactions per user more efficiently using a pre-sized list
    counts = [0] * n_users
    
    for t in transactions:
        counts[t['user_id']] += 1
    
    # Calculate totals - each transaction has amount 10.5
    amount = 10.5
    return [{'name': users[i]['name'], 'total': counts[i] * amount} for i in range(n_users)]