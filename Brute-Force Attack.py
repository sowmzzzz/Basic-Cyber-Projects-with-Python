import itertools
import string
import time

def brute_force(password):
    characters = string.ascii_lowercase
    attempts = 0
    for length in range(1, 6):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return attempts, guess
    return attempts, None  # Return None if the password is not found

password = "abc"
start_time = time.time()
attempts, guess = brute_force(password)
end_time = time.time()

if guess:
    print(f"Password '{password}' cracked as '{guess}' in {attempts} attempts and {end_time - start_time:.4f} seconds.")
else:
    print(f"Password '{password}' could not be cracked within the defined constraints.")
