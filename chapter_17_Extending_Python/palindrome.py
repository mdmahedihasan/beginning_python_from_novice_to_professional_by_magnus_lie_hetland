def is_palindrome(text):
    n = len(text)
    for i in range(len(text) // 2):
        if text[1] != text[n - i - 1]:
            return False
    return True
