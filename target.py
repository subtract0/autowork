from collections import defaultdict

def process_transactions(users, transactions):
    user_totals = defaultdict(float)
    for t in transactions:
        user_totals[t['user_id']] += t['amount']
    
    return [{'name': u['name'], 'total': user_totals.get(u['id'], 0)} for u in users]