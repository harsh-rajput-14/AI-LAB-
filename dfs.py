def solve_8_puzzle_dfs(start, goal, max_depth=15):
    stack = [(start, [], {start})]

    while stack:
        state, path, visited = stack.pop()
        if state == goal:
            return path

        if len(path) < max_depth:
            zero = state.index(0)
            row, col = divmod(zero, 3)

            for move, dr, dc in [("Right", 0, 1), ("Left", 0, -1), ("Down", 1, 0), ("Up", -1, 0)]:
                nr, nc = row + dr, col + dc
                if 0 <= nr < 3 and 0 <= nc < 3:
                    target = nr * 3 + nc
                    nxt = list(state)
                    nxt[zero], nxt[target] = nxt[target], nxt[zero]
                    nxt_tuple = tuple(nxt)
                    if nxt_tuple not in visited:
                        stack.append((nxt_tuple, path + [move], visited | {nxt_tuple}))
    return None

print(solve_8_puzzle_dfs((1, 2, 3, 0, 4, 6, 7, 5, 8), (1, 2, 3, 4, 5, 6, 7, 8, 0)))
