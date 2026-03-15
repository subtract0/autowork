def process_transactions(users, transactions):
    n_users = len(users)
    user_totals = [0.0] * n_users
    
    # Process all transactions with direct indexing
    for t in transactions:
        user_totals[t['user_id']] += t['amount']
    
    # Pre-build result list more efficiently - use i directly since users[i]['id'] == i
    return [{'name': users[i]['name'], 'total': user_totals[i]} for i in range(n_users)]