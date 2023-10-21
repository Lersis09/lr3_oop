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
  
def task1():
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
    """Зчитування матриці з файлу, підрахунок параметрів
    та виконання операції над матрицею"""
    M = N = K = 0
    with open(filename, 'r') as f:
        param_line = f.readline().split(" ")  # "3 4 3" ["3", "4", "3"]
        try:
            M = int(param_line[0])
            N = int(param_line[1])
            K = int(param_line[2])
            if K < 1 or K > M:
                raise ValueError
        except ValueError:
            print("Wrong file data")
        else:
            input = np.loadtxt(filename, skiprows=1, max_rows=M)
            print(input)
            # Підрахунок параметрів задачі
            sum_K = np.sum(input, axis=1)[K - 1]  # [[1, 2], [3, 1]] -> [3, 4]
            prod_K = np.prod(input, axis=1)[K - 1]
            ones = np.ones((M, N))
            changed_matrix = input - ones
        
            means = np.mean(input, axis=1).reshape(-1, 1)
            print(means)
            tmp_matr = np.where(input - means > 0, 1, 0)
            print(tmp_matr)
            elements_amount = np.sum(tmp_matr, axis=1)
            print(elements_amount)
        
            return sum_K, prod_K, changed_matrix
    
    return 0, 0, np.zeros((M, N))


def task2():
    """Введення імені вхідного файлу, виклик функції для зчитування
    і обробки матриці, виведення результатів"""
    filename = input("Enter filename (.txt): ")
    sum_K, prod_K, changed_matrix = matrix1(filename)
    print(f"Сума K-го рядка: {sum_K}\nДобуток K-го рядка: {prod_K}\nЗмінена матриця:\n{changed_matrix}")
