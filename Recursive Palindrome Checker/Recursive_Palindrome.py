# Portfolio Task 2 - Recursive Palindrome Checker

def PalindromeChecker(String):
    # Removing empty spaces and converting string to lowercase
    str = String.replace(" ", "").lower()
    if len(str) < 2:
        return True
    if str[0] != str[-1]:
        return False
    return PalindromeChecker(str[1:-1])

# Testing
# Test 1 - Was It A Rat I Saw
Ans1 = PalindromeChecker("Was It A Rat I Saw")
print("Is this a palindrome: Was it a Rat I Saw: " + str(Ans1))

# Test 2 - I do not like green eggs and ham. I do not like them, Sam-I-Am
Ans2 = PalindromeChecker("I do not like green eggs and ham. I do not like them, Sam-I-Am")
print("I do not like green eggs and ham I do not like them Sam-I-Am: " + str(Ans2))

# Test 3 - Racecar
Ans3 = PalindromeChecker("Racecar")
print("Is this a palindrome: Racecar: " + str(Ans3))

# Test 4 - George
Ans4 = PalindromeChecker("George")
print("Is this a palindrome: George: " + str(Ans4))

# Test 5 - Was it a car or a cat I saw
Ans5 = PalindromeChecker("Was it a car or a cat I saw")
print("Is this a palindrome: Was it a car or a cat I saw: " + str(Ans5))