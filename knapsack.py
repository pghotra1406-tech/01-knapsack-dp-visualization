
def solve_knapsack(weights, values, n, W):
    # Make an empty DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    print("\nCapacity:", " ".join(f"{c:3}" for c in range(W + 1)))

    # Fill the table one item at a time
    for i in range(1, n + 1):
        wt = weights[i - 1]
        val = values[i - 1]

        for capacity in range(W + 1):
            # Option 1: Do not take this item
            dp[i][capacity] = dp[i - 1][capacity]

            # Option 2: Take this item if it fits
            if wt <= capacity:
                take = val + dp[i - 1][capacity - wt]
                dp[i][capacity] = max(
                    dp[i][capacity], take
                )

        # Show the table after each item
        print(f"\nAfter item {i} (weight={wt}, value={val}):")
        for row in dp[:i + 1]:
            print(" ".join(f"{x:3}" for x in row))

    return dp[n][W]


def main():
    # Read all the test cases from input.txt
    with open("input.txt", "r") as file:
        lines = file.readlines()

    test_cases = []
    current_case = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("#Test"):
            if current_case:
                test_cases.append(current_case)
            current_case = []
        else:
            current_case.append(list(map(int, line.split())))

    if current_case:
        test_cases.append(current_case)

    # Save answers in result.txt
    with open("result.txt", "w") as output:
        for number, case in enumerate(test_cases, start=1):
            n, W = case[0]
            items = case[1:n + 1]

            weights = [item[0] for item in items]
            values = [item[1] for item in items]

            print("\n" + "=" * 40)
            print(f"TEST CASE {number}: n={n}, capacity={W}")

            answer = solve_knapsack(weights, values, n, W)

            output.write(f"#Test {number}\n")
            output.write(f"Input: {n} {W}\n")

            for wt, val in items:
                output.write(f"{wt} {val}\n")

            output.write(f"Maximum value: {answer}\n\n")

            print(f"\nMaximum value = {answer}")

    print("\nAll results have been saved in result.txt")


if __name__ == "__main__":
    main()
