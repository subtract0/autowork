def process_transactions(users, transactions):
    # Find max user id to size our array
    max_user_id = max(u['id'] for u in users)
    
    # Use a list instead of dict for O(1) index access
    user_totals = [0.0] * (max_user_id + 1)
    
    for t in transactions:
        user_totals[t['user_id']] += t['amount']
    
    return [{'name': u['name'], 'total': user_totals[u['id']]} for u in users]