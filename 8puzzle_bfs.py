from collections import deque

def solve_8_puzzle_bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for move, dr, dc in [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                target = nr * 3 + nc
                nxt = list(state)
                nxt[zero], nxt[target] = nxt[target], nxt[zero]
                nxt_tuple = tuple(nxt)
                if nxt_tuple not in visited:
                    visited.add(nxt_tuple)
                    queue.append((nxt_tuple, path + [move]))
    return None

print(solve_8_puzzle_bfs((1, 2, 3, 0, 4, 6, 7, 5, 8), (1, 2, 3, 4, 5, 6, 7, 8, 0)))
