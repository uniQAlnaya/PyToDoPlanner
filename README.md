Консольное приложение для ведения списка задач ToDo.  
Приложение сохраняет задачи в файле todo.txt в той же папке, где находится исполняемый модуль приложения.

Поддерживаются следующие команды:  
* todo.py - показать незавершенные задачи  
* todo.py all - показать все задачи (включая завершенные)  
* todo.py add <task description> [due:<date>] - добавить задачу с описание <task description> (и дополнительно можно добавить срок выполнения <date>)  
* todo.py remove <n> - удалить задачу с номером <n>  
* todo.py edit <n> <new task description> - редактировать задачу с номером <n>: установить новое описание <new task description>  
* todo.py due <n> <date> - установить срок выполнения <date> для задачи <n>  
* todo.py done <n> - пометить задачу как выполненную  
* todo.py undo <n> - снять отметку о выполнении  
* todo.py search <sting> - поиск задач по тексту <string>  

Приложение было реализовано в рамках учебного проекта при обучении основам программирования на python от сообщества PyLadies Kazan.

