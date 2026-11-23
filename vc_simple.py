def simple_reflex_vacuum(rooms):
    pos = "A"
    actions = []
    for _ in range(4):
        if rooms[pos] == "Dirty":
            rooms[pos] = "Clean"
            actions.append(f"Suck at {pos}")
        elif pos == "A":
            pos = "B"
            actions.append("Move Right to B")
        else:
            pos = "A"
            actions.append("Move Left to A")
    return actions

print(simple_reflex_vacuum({"A": "Dirty", "B": "Dirty"}))
