def process_transactions(users, transactions):
    # Build a dictionary of user_id -> total amount (O(M) instead of O(N*M))
    user_totals = {}
    for t in transactions:
        uid = t['user_id']
        user_totals[uid] = user_totals.get(uid, 0) + t['amount']
    
    # Now iterate through users and get the total (O(N))
    result = []
    for u in users:
        result.append({'name': u['name'], 'total': user_totals.get(u['id'], 0)})
    return result