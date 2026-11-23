def solve_8_puzzle_ids(start, goal, max_limit=20):
    def depth_limited(state, path, limit, seen):
        if state == goal:
            return path
        if len(path) == limit:
            return None

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for move, dr, dc in [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                target = nr * 3 + nc
                nxt = list(state)
                nxt[zero], nxt[target] = nxt[target], nxt[zero]
                nxt_tuple = tuple(nxt)
                if nxt_tuple not in seen:
                    seen.add(nxt_tuple)
                    result = depth_limited(nxt_tuple, path + [move], limit, seen)
                    if result is not None:
                        return result
                    seen.remove(nxt_tuple)
        return None

    for depth in range(max_limit + 1):
        ans = depth_limited(start, [], depth, {start})
        if ans is not None:
            return ans
    return None

print(solve_8_puzzle_ids((1, 2, 3, 0, 4, 6, 7, 5, 8), (1, 2, 3, 4, 5, 6, 7, 8, 0)))
