cards_given = input().split()

team_a = []
team_b = []
players_a = 11
players_b = 11
low_players = False

for el in cards_given:
    card = el.split("-")
    letter = card[0]
    number = card[1]
    if letter == "A":
        if number in team_a:
            continue
        else:
            players_a -= 1
            team_a.append(number)
    else:
        if number in team_b:
            continue
        else:
            players_b -= 1
            team_b.append(number)
    if len(team_a) > 4 or len(team_b) > 4:
        low_players = True
        break
print(f"Team A - {players_a}; Team B - {players_b}")
if low_players:
    print("Game was terminated")


