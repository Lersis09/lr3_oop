# підключення необхідних бібліотек
import numpy as np


def Even(K):
    """Функция, которая проверяет, является ли число K четным"""
    return K % 2 == 0

def Even_for_list(list_of_K):
    """Функція для обробки списку вхідних даних відповідно до функції за варіантом"""
    out_data = []
    for K in list_of_K:  # Для кожного елемента вхідного списку
        out_data.append(Even(K))
    return out_data

def count_even_numbers(numbers):
    """Функція для підрахунку кількості парних чисел в наборі"""
    count = 0
    for num in numbers:
        if Even(num):
            count += 1
    return count
  
def task_1():
    """Введення вхідних даних, виклик функції для підрахунку кількості 
     парних чисел,виведення результату"""
    try:
        numbers = list(map(int, input("Enter 5 numbers: ").split()))
    except ValueError:
        print("Помилка при введенні вхідних даних!")
    else:
        count = count_even_numbers(numbers)
        print("Кількість парних чисел: ", count)
      
def matrix1(filename):
    """Зчитування матриці з файлу, підрахунок параметрів та виконання операції над 
    матрицею"""
    M = N = 0
    with open(filename, 'r') as f:
        param_line = f.readline().split(" ")  # "3 4" ["3", "4"]
        try:
            M = int(param_line[0])
            N = int(param_line[1])
        except ValueError:
            print("Wrong file data")
        else:
            input = np.loadtxt(filename, skiprows=1, max_rows=M)
            print(input)
            
            # Пошук мінімального і максимального елементів в кожному рядку
            min_vals = np.min(input, axis=1)
            max_vals = np.max(input, axis=1)
            print(min_vals)
            print(max_vals)
            
            # Знаходження рядка з найбільшим максимальним і мінімальним елементами
            min_row = np.argmin(min_vals)
            max_row = np.argmax(max_vals)
            print("Min:",min_row)
            print("Max:",max_row)
            
            # Поміняти місцями рядки матриці
            changed_matrix = np.copy(input)
            changed_matrix[[min_row, max_row]] = changed_matrix[[max_row, min_row]]
            print(changed_matrix)
            
            return changed_matrix
    
    return np.zeros((M, N))


def task_2():
    """Введення імені вхідного файлу, виклик функції для зчитування і обробки 
       матриці, виведення результатів"""
    filename = input("Enter filename (.txt): ")
    changed_matrix = matrix1(filename)
    print(f"Змінена матриця:\n{changed_matrix}")