import sys

def create_table(n, final_states, transitions):
    table = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if (i in final_states) != (j in final_states):
                table[i][j] = True
    
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                if not table[i][j]:
                    for symbol in range(len(transitions[i])):
                        if symbol >= len(transitions[j]):
                            continue
                        p = transitions[i][symbol]
                        q = transitions[j][symbol]
                        if p > q:
                            p, q = q, p
                        if table[p][q]:
                            table[i][j] = True
                            changed = True
                            break
    return table

def find_equivalent_pairs(n, table):
    equivalent_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not table[i][j]:
                equivalent_pairs.append((i, j))
    return equivalent_pairs

def main():
    c = int(input().strip())
    
    for _ in range(c):
        n = int(input().strip())
        alphabet = input().strip().split()
        final_states = list(map(int, input().strip().split())) if input().strip() else []
        transitions = [list(map(int, input().strip().split())) for _ in range(n)]

        table = create_table(n, final_states, transitions)
        equivalent_pairs = find_equivalent_pairs(n, table)

        if equivalent_pairs:
            print(" ".join(f"({i},{j})" for i, j in equivalent_pairs))
        else:
            print(None)

if __name__ == "__main__":
    main()
