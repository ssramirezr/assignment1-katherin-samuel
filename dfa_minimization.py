import sys

def read_input():
    lines = []
    while True:
        try:
            line = input()
            if line:
                lines.append(line)
            else:
                break
        except EOFError:
            break
    
    index = 0
    c = int(lines[index])
    index += 1
    cases = []
    
    for _ in range(c):
        n = int(lines[index])
        index += 1
        alphabet = lines[index].split()
        index += 1
        final_states = set(map(int, lines[index].split()))
        index += 1
        transitions = []
        
        for _ in range(n):
            transitions.append(list(map(int, lines[index].split())))
            index += 1
        
        cases.append((n, alphabet, final_states, transitions))
    
    return cases

def minimize_dfa(n, alphabet, final_states, transitions):
    table = [[False for _ in range(n)] for _ in range(n)]
    
    # Step 1: Mark pairs where one is final and the other is not
    for i in range(n):
        for j in range(i + 1, n):
            if (i in final_states) != (j in final_states):
                table[i][j] = True
    
    # Step 2: Iteratively mark pairs based on transitions
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                if not table[i][j]:
                    for symbol_index in range(len(alphabet)):
                        p = transitions[i][symbol_index]
                        q = transitions[j][symbol_index]
                        if p > q:  # Always work with (smaller, larger)
                            p, q = q, p
                        if table[p][q]:
                            table[i][j] = True
                            changed = True
                            break
    
    # Step 3: Collect equivalent pairs
    equivalent_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not table[i][j]:
                equivalent_pairs.append((i, j))
    
    return equivalent_pairs

def main():
    cases = read_input()
    results = []
    
    for n, alphabet, final_states, transitions in cases:
        equivalent_pairs = minimize_dfa(n, alphabet, final_states, transitions)
        equivalent_pairs.sort()
        results.append(" ".join(f"({i},{j})" for i, j in equivalent_pairs))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
