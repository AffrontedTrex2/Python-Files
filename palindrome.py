#Largest palindrome from the product of two three digit numbers
def palindrome(n):
    n = str(n)
    nArray = []
    for num in n:
        nArray.append(num)

    nArray2 = nArray.copy()
    nArray2.reverse()

    if nArray2 == nArray:
        return True
    else:
        return False

def largestPalindrome():
    num = 999
    num2 = 999
    offSet = True
    while True:
        product = num * num2
        if palindrome(product) == True:
            return product
            break
        else:
            if offSet == True:
                num = num - 1
                offSet = False
            else:
                num2 = num2 - 1
                offSet = True
print(largestPalindrome())
