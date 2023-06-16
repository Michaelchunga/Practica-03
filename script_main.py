
import random

def generate_random_numbers():
    numbers = []
    for _ in range(20):
        numbers.append(random.randint(0, 100))
    return numbers

def display_numbers(numbers):
    print("Lista de números generados:")
    print(numbers)

def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    print("Lista de números ordenados:")
    print(sorted_numbers)
