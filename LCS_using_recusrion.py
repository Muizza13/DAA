def lcs_recursive_length(text1, text2, m, n):
    if m == 0 or n == 0:
        return 0
    if text1[m - 1] == text2[n - 1]:
        return 1 + lcs_recursive_length(text1, text2, m - 1, n - 1)
    else:
        return max(
            lcs_recursive_length(text1, text2, m - 1, n),
            lcs_recursive_length(text1, text2, m, n - 1),
        )


def lcs_recursive_string(text1, text2, m, n):
    if m == 0 or n == 0:
        return ""
    if text1[m - 1] == text2[n - 1]:
        return lcs_recursive_string(text1, text2, m - 1, n - 1) + text1[m - 1]
    else:
        if lcs_recursive_length(text1, text2, m - 1, n) > lcs_recursive_length(
            text1, text2, m, n - 1
        ):
            return lcs_recursive_string(text1, text2, m - 1, n)
        else:
            return lcs_recursive_string(text1, text2, m, n - 1)


if __name__ == "__main__":
    text1 = input("Enter first string: ")
    text2 = input("Enter second string: ")

    length = lcs_recursive_length(text1, text2, len(text1), len(text2))
    lcs_str = lcs_recursive_string(text1, text2, len(text1), len(text2))

    print(f"\nLength of LCS: {length}")
    print(f"LCS: {lcs_str}")
