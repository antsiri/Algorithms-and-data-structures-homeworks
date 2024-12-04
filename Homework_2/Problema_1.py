def max_sub_sum(arr):
    max_sum = float('-inf')                             # si imposta come valore iniziale della somma massima valore -inf
    current_sum = 0                                     # valore della somma corrente

    for elem in arr:
        current_sum = max(elem, current_sum+elem)          
        max_sum = max(max_sum, current_sum)

    return max_sum

def main():
    print("Max SubArray Sum\n")

    lines = []
    results = []

    while True:
        print("Insert new array: ")
        line = input().strip()

        if line == "END":
            break

        lines.append(line)
        array = list(map(int, line.split()))

        results.append(max_sub_sum(array))

    print("\nRESULTS:\n")

    for i in range(len(lines)):
        print(lines[i], results[i], sep="\t")

if __name__ == "__main__":
    main()