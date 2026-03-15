def process_transactions(users, transactions):
    n_users = len(users)
    user_totals = [0.0] * n_users
    
    for t in transactions:
        uid = t['user_id']
        # Use augmented assignment to avoid double lookup
        user_totals[uid] += t['amount']
    
    return [{'name': u['name'], 'total': user_totals[u['id']]} for u in users]