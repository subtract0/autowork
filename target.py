def process_transactions(users, transactions):
    # Pre-size array based on max user_id seen in transactions
    n_users = len(users)
    user_totals = [0.0] * n_users
    
    # Local variable caching for speed
    totals = user_totals
    add = totals.__setitem__
    
    for t in transactions:
        uid = t['user_id']
        totals[uid] = totals[uid] + t['amount']
    
    return [{'name': u['name'], 'total': user_totals[u['id']]} for u in users]