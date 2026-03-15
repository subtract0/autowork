def process_transactions(users, transactions):
    n_users = len(users)
    user_totals = [0.0] * n_users
    
    for t in transactions:
        user_totals[t['user_id']] += t['amount']
    
    return [{'name': users[i]['name'], 'total': user_totals[i]} for i in range(n_users)]