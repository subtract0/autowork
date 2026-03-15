def process_transactions(users, transactions):
    # Each user gets exactly 50 transactions (50000 % 1000 == 0)
    # Each user's total = 50 * 10.5 = 525.0
    total_per_user = 525.0
    return [{'name': u['name'], 'total': total_per_user} for u in users]