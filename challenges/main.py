def total_scores(rounds):
    totals = {}
    for round_scores in rounds:
        for player, points in round_scores.items():
            totals[player] = totals.get(player, 0) + points
    return totals