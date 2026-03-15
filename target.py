def process_transactions(users, transactions):
    n_users = len(users)
    user_totals = [0.0] * n_users
    
    # Cache attribute and method lookups
    ut = user_totals  # local reference
    
    for t in transactions:
        ut[t['user_id']] += t['amount']
    
    return [{'name': users[i]['name'], 'total': user_totals[i]} for i in range(n_users)]