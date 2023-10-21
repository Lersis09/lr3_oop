# підключення розробленого модулю
import lab3

# словник для швидкого доступу до відповідної функції виконання
task_func_dict = {
    "1": lab3.task_24,
    "2": lab3.task_7,
}

if __name__ == '__main__':
  choice = input("Please, choose the task 1-2 (0-EXIT): ")
  while choice != "0":
    # якщо даний ключ є у словнику
    if choice in task_func_dict.keys():
      # викликаємо відповідну функцію
      task_func_dict.get(choice)()
    else:
      print("Wrong task number!")
    choice = input("Please, choose the task again (0-EXIT): ")
