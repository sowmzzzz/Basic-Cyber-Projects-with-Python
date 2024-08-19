import re

def check_password_strength(password):
    length = len(password)
    score = 0

    if length >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    strength = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    return strength[score]

password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
