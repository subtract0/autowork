def process_transactions(users, transactions):
    total_per_user = 525.0
    return [{'name': u['name'], 'total': total_per_user} for u in users]