def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

    def lcs(i, j):
        if i == m or j == n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if text1[i] == text2[j]:
            dp[i][j] = 1 + lcs(i + 1, j + 1)
        else:
            dp[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))

        return dp[i][j]

    lcs_length = lcs(0, 0)

    lcs_str = []
    i, j = 0, 0
    while i < m and j < n:
        if text1[i] == text2[j]:
            lcs_str.append(text1[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1

    return lcs_length, "".join(lcs_str)


if __name__ == "__main__":
    text1 = input("Enter first string: ")
    text2 = input("Enter second string: ")

    length, lcs_str = longest_common_subsequence(text1, text2)

    print(f"\nLength of LCS: {length}")
    print(f"LCS: {lcs_str}")
