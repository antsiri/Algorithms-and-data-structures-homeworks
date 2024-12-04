def min_coins(V, n, coins):
    results = [float("inf")]*(V+1)
    results[0] = 0

    for i in range(n):
        for j in range(coins[i], V+1):
            results[j] = min(results[j], results[j-coins[i]]+1)

    return results[V]

def main():
    print("Minimum number of coins to archieve value V\n")
    print("The first value is V, the second one is the number of coins, and the others are the value of each coin\n")

    lines = []
    results = []

    while True:
        print("Insert new array: ")
        line = input().strip()

        if line == "END":
            break

        lines.append(line)
        array = list(map(int, line.split()))

        results.append(min_coins(array[0], array[1], array[2:]))

    print("\nRESULTS:\n")

    for i in range(len(lines)):
        print(lines[i], results[i], sep="\t")

if __name__ == "__main__":
    main()