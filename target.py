def process_transactions(users, transactions):
    # Pre-size array based on number of users (ids are 0 to len-1)
    n_users = len(users)
    user_totals = [0.0] * n_users
    
    for t in transactions:
        user_totals[t['user_id']] += t['amount']
    
    return [{'name': u['name'], 'total': user_totals[u['id']]} for u in users]