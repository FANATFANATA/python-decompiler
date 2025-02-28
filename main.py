import os
import subprocess

def ask_question(question):
    """Функция для задавания вопросов пользователю."""
    return input(question).strip()

def decompile_with_unluac(luac_file, output_file):
    """Декомпиляция с использованием unluac."""
    try:
        command = f"java -jar unluac.jar {luac_file} > {output_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Декомпиляция завершена. Результат сохранен в {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при декомпиляции: {e}")

def decompile_with_luadec(luac_file, output_file):
    """Декомпиляция с использованием luadec."""
    try:
        command = f"luadec {luac_file} > {output_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Декомпиляция завершена. Результат сохранен в {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при декомпиляции: {e}")

def main():
    print("=== Декомпилятор Lua-скриптов ===")
    
    # Запрашиваем путь к файлу .luac
    luac_file = ask_question("Введите путь к файлу .luac: ")
    if not os.path.exists(luac_file):
        print("Файл не найден!")
        return
    
    # Запрашиваем инструмент для декомпиляции
    tool = ask_question("Выберите инструмент (unluac/luadec): ").lower()
    if tool not in ["unluac", "luadec"]:
        print("Неверный выбор инструмента!")
        return
    
    # Запрашиваем путь для сохранения результата
    output_file = ask_question("Введите путь для сохранения результата: ")
    
    # Выполняем декомпиляцию
    if tool == "unluac":
        decompile_with_unluac(luac_file, output_file)
    elif tool == "luadec":
        decompile_with_luadec(luac_file, output_file)

if __name__ == "__main__":
    main()
