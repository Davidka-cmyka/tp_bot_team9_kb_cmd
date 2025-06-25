import os
from pathlib import Path
from dotenv import load_dotenv

parent = Path(f"{os.getcwd()}").parent

def test_main_file_exists():
    main_path = Path(f"{parent}/bot_main.py")
    assert main_path.exists(), "Файл bot_main.py не найден"
    assert main_path.is_file(), "bot_main.py существует, но не является файлом"

def test_main_file_has_required_imports():
    required_imports = [
        "from aiogram import",
        "from handlers import",
        "from callbacks import"
    ]
    with open(f"{parent}/bot_main.py", "r", encoding="utf-8") as file:
        content = file.read()
        for imp in required_imports:
            assert imp in content, f"Не найден обязательный импорт: {imp}"
