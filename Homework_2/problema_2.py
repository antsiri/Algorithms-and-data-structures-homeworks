def min_coins(V, n, coins):
    max_value = V + max(coins)
    results = [float("inf")]*(max_value+1)
    results[0] = 0

    for i in range(n):
        for j in range(coins[i], max_value+1):
            results[j] = min(results[j], results[j-coins[i]]+1)

    closest_value = None
    closest_diff = float("inf")

    for i in range(len(results)):
        if results[i] != float("inf"):
            diff = abs(i-V)
            if diff < closest_diff or (diff == closest_diff and i > closest_value):
                closest_value = i
                closest_diff = diff

    return results[closest_value]

def main():
    print("Minimum number of coins to achieve value V")
    print("The first value is V, the second one is the number of coins, and the others are the values of each coin")
    print("If the result is -inf- there is no way to achieve the V or the nearest sum greater than V\n")

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