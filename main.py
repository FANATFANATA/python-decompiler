import os
import subprocess
import json

def load_language(lang):
    """Загружает тексты на выбранном языке."""
    with open(f"lang/{lang}.json", "r", encoding="utf-8") as file:
        return json.load(file)

def ask_question(question):
    """Функция для задавания вопросов пользователю."""
    return input(question).strip()

def decompile_with_unluac(luac_file, output_file):
    """Декомпиляция с использованием unluac."""
    try:
        command = f"java -jar tools/unluac.jar {luac_file} > {output_file}"
        subprocess.run(command, shell=True, check=True)
        print(texts["decompilation_complete"].format(output_file))
    except subprocess.CalledProcessError as e:
        print(texts["decompilation_error"].format(e))

def decompile_with_luadec(luac_file, output_file):
    """Декомпиляция с использованием luadec."""
    try:
        command = f"tools/luadec {luac_file} > {output_file}"
        subprocess.run(command, shell=True, check=True)
        print(texts["decompilation_complete"].format(output_file))
    except subprocess.CalledProcessError as e:
        print(texts["decompilation_error"].format(e))

def main():
    global texts
    lang = ask_question("Choose language (en/ru): ").lower()
    if lang not in ["en", "ru"]:
        print("Invalid language choice! Using English by default.")
        lang = "en"
    
    texts = load_language(lang)
    print(texts["welcome"])
    
    luac_file = ask_question(texts["enter_luac_path"])
    if not os.path.exists(luac_file):
        print(texts["file_not_found"])
        return
    
    tool = ask_question(texts["choose_tool"]).lower()
    if tool not in ["unluac", "luadec"]:
        print(texts["invalid_tool"])
        return
    
    output_file = ask_question(texts["enter_output_path"])
    
    if tool == "unluac":
        decompile_with_unluac(luac_file, output_file)
    elif tool == "luadec":
        decompile_with_luadec(luac_file, output_file)

if __name__ == "__main__":
    main()
