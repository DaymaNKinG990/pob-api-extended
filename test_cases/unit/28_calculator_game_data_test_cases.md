# Calculator Game Data Unit Test Cases

## Module: pobapi.calculator.game_data

### Overview
Юнит-тест-кейсы для модуля calculator.game_data, который отвечает за загрузку игровых данных.

---

## Test Case: TC-CALC-GAME-DATA-001
**Title:** PassiveNode.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации PassiveNode

**Preconditions:**
- Нет

**Test Steps:**
1. Создать PassiveNode с параметрами
2. Проверить значения атрибутов

**Expected Result:**
- node.node_id == 12345
- node.name == "Test Node"
- len(node.stats) == 1
- node.is_keystone == False

---

## Test Case: TC-CALC-GAME-DATA-002
**Title:** SkillGem.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации SkillGem

**Preconditions:**
- Нет

**Test Steps:**
1. Создать SkillGem с параметрами
2. Проверить значения атрибутов

**Expected Result:**
- gem.name == "Fireball"
- gem.is_spell == True
- gem.is_attack == False
- gem.base_damage содержит Fire урон

---

## Test Case: TC-CALC-GAME-DATA-003
**Title:** UniqueItem.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации UniqueItem

**Preconditions:**
- Нет

**Test Steps:**
1. Создать UniqueItem с параметрами
2. Проверить значения атрибутов

**Expected Result:**
- unique.name == "Test Unique"
- unique.base_type == "Leather Belt"
- len(unique.special_effects) == 1

---

## Test Case: TC-CALC-GAME-DATA-004
**Title:** GameDataLoader.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации GameDataLoader

**Preconditions:**
- Нет

**Test Steps:**
1. Создать GameDataLoader()
2. Проверить инициализацию

**Expected Result:**
- loader is not None
- Loader инициализирован корректно

---

## Test Case: TC-CALC-GAME-DATA-005
**Title:** GameDataLoader.load_passive_tree_data() empty

**Category:** Edge Case

**Description:** Проверка метода load_passive_tree_data() для пустого файла

**Preconditions:**
- Нет файла данных

**Test Steps:**
1. Вызвать `loader.load_passive_tree_data()`
2. Проверить результат

**Expected Result:**
- nodes is dict
- Пустой файл обработан корректно

---

## Test Case: TC-CALC-GAME-DATA-006
**Title:** GameDataLoader.load_skill_gem_data() empty

**Category:** Edge Case

**Description:** Проверка метода load_skill_gem_data() для пустого файла

**Preconditions:**
- Нет файла данных

**Test Steps:**
1. Вызвать `loader.load_skill_gem_data()`
2. Проверить результат

**Expected Result:**
- gems is dict
- Пустой файл обработан корректно

---

## Test Case: TC-CALC-GAME-DATA-007
**Title:** GameDataLoader.load_unique_item_data() empty

**Category:** Edge Case

**Description:** Проверка метода load_unique_item_data() для пустого файла

**Preconditions:**
- Нет файла данных

**Test Steps:**
1. Вызвать `loader.load_unique_item_data()`
2. Проверить результат

**Expected Result:**
- uniques is dict
- Пустой файл обработан корректно

---

## Test Case: TC-CALC-GAME-DATA-008
**Title:** GameDataLoader.load_unique_item_data() from file

**Category:** Positive

**Description:** Проверка метода load_unique_item_data() для загрузки из JSON файла

**Preconditions:**
- Временный JSON файл создан

**Test Steps:**
1. Создать временный JSON файл с данными unique item
2. Вызвать `loader.load_unique_item_data(str(data_file))`
3. Проверить результат

**Expected Result:**
- len(uniques) >= 1
- Unique item загружен корректно
- Данные соответствуют файлу

---

## Test Case: TC-CALC-GAME-DATA-009
**Title:** GameDataLoader.get_unique_item() not found

**Category:** Negative

**Description:** Проверка метода get_unique_item() для несуществующего предмета

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `loader.get_unique_item("NonExistent Unique")`
2. Проверить результат

**Expected Result:**
- item is None
- Несуществующий предмет обработан корректно

---

## Test Case: TC-CALC-GAME-DATA-010
**Title:** GameDataLoader.get_unique_item() by name

**Category:** Positive

**Description:** Проверка метода get_unique_item() для поиска по имени

**Preconditions:**
- Unique item загружен в loader

**Test Steps:**
1. Загрузить unique item данные
2. Вызвать `loader.get_unique_item("Inpulsa's Broken Heart")`
3. Проверить результат

**Expected Result:**
- item is not None
- item.name == "Inpulsa's Broken Heart"
- item is UniqueItem

---

## Test Case: TC-CALC-GAME-DATA-011
**Title:** GameDataLoader.get_passive_node() not found

**Category:** Negative

**Description:** Проверка метода get_passive_node() для несуществующего узла

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `loader.get_passive_node(99999)`
2. Проверить результат

**Expected Result:**
- node is None
- Несуществующий узел обработан корректно

---

## Test Case: TC-CALC-GAME-DATA-012
**Title:** GameDataLoader.get_skill_gem() not found

**Category:** Negative

**Description:** Проверка метода get_skill_gem() для несуществующего гема

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `loader.get_skill_gem("NonExistent Gem")`
2. Проверить результат

**Expected Result:**
- gem is None
- Несуществующий гем обработан корректно

---

## Test Case: TC-CALC-GAME-DATA-013
**Title:** GameDataLoader.get_unique_item() with normalized name

**Category:** Positive

**Description:** Проверка метода get_unique_item() с нормализованным именем

**Preconditions:**
- Unique item загружен с нормализованным ключом

**Test Steps:**
1. Загрузить unique item с нормализованным ключом
2. Вызвать get_unique_item() с различными вариантами имени
3. Проверить результат

**Expected Result:**
- Unique item найден по нормализованному имени
- Результат корректен

---

## Test Case: TC-CALC-GAME-DATA-014
**Title:** GameDataLoader.get_unique_item() case insensitive search

**Category:** Positive

**Description:** Проверка метода get_unique_item() с case insensitive поиском

**Preconditions:**
- Unique item загружен

**Test Steps:**
1. Загрузить unique item
2. Вызвать get_unique_item() с разным регистром
3. Проверить результат

**Expected Result:**
- Unique item найден независимо от регистра
- Результат корректен

---

## Test Case: TC-CALC-GAME-DATA-015
**Title:** GameDataLoader.get_unique_item() with item name match

**Category:** Positive

**Description:** Проверка метода get_unique_item() с поиском по item name

**Preconditions:**
- Unique item загружен

**Test Steps:**
1. Загрузить unique item
2. Вызвать get_unique_item() с item name
3. Проверить результат

**Expected Result:**
- Unique item найден по item name
- Результат корректен

---

## Test Case: TC-CALC-GAME-DATA-016
**Title:** GameDataLoader.load_unique_item_data() fallback to uniques.json

**Category:** Positive

**Description:** Проверка метода load_unique_item_data() с fallback на uniques.json

**Preconditions:**
- uniques.json файл существует

**Test Steps:**
1. Создать uniques.json файл
2. Вызвать load_unique_item_data() без указания файла
3. Проверить результат

**Expected Result:**
- Данные загружены из uniques.json
- Fallback работает корректно

---

## Test Case: TC-CALC-GAME-DATA-017
**Title:** GameDataLoader.find_data_file() nonexistent

**Category:** Negative

**Description:** Проверка метода find_data_file() для несуществующего файла

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `loader.find_data_file("nonexistent.json")`
2. Проверить результат

**Expected Result:**
- file_path is None
- Несуществующий файл обработан корректно

---

## Test Case: TC-CALC-GAME-DATA-018
**Title:** GameDataLoader.load_unique_item_data() camel case

**Category:** Positive

**Description:** Проверка метода load_unique_item_data() для camelCase данных

**Preconditions:**
- JSON файл с camelCase полями

**Test Steps:**
1. Создать JSON файл с camelCase полями
2. Вызвать load_unique_item_data()
3. Проверить результат

**Expected Result:**
- Данные загружены корректно
- camelCase обработан

---

## Test Case: TC-CALC-GAME-DATA-019
**Title:** GameDataLoader.load_unique_item_data() snake case

**Category:** Positive

**Description:** Проверка метода load_unique_item_data() для snake_case данных

**Preconditions:**
- JSON файл с snake_case полями

**Test Steps:**
1. Создать JSON файл с snake_case полями
2. Вызвать load_unique_item_data()
3. Проверить результат

**Expected Result:**
- Данные загружены корректно
- snake_case обработан

---

## Test Case: TC-CALC-GAME-DATA-020
**Title:** GameDataLoader.find_data_file() existing

**Category:** Positive

**Description:** Проверка метода find_data_file() для существующего файла

**Preconditions:**
- Файл данных существует

**Test Steps:**
1. Создать файл данных
2. Вызвать find_data_file()
3. Проверить результат

**Expected Result:**
- file_path is not None
- Путь к файлу корректен

---

## Test Case: TC-CALC-GAME-DATA-021
**Title:** GameDataLoader.find_data_file() with env var

**Category:** Positive

**Description:** Проверка метода find_data_file() с переменной окружения

**Preconditions:**
- Переменная окружения установлена

**Test Steps:**
1. Установить переменную окружения
2. Вызвать find_data_file()
3. Проверить результат

**Expected Result:**
- Путь из переменной окружения учтен
- Результат корректен

---

## Test Case: TC-CALC-GAME-DATA-022
**Title:** GameDataLoader.load_passive_tree_data() from file

**Category:** Positive

**Description:** Проверка метода load_passive_tree_data() для загрузки из файла

**Preconditions:**
- JSON файл с данными passive tree

**Test Steps:**
1. Создать JSON файл с данными passive tree
2. Вызвать load_passive_tree_data()
3. Проверить результат

**Expected Result:**
- Данные загружены корректно
- nodes содержит узлы

---

## Test Case: TC-CALC-GAME-DATA-023
**Title:** GameDataLoader.load_skill_gem_data() from file

**Category:** Positive

**Description:** Проверка метода load_skill_gem_data() для загрузки из файла

**Preconditions:**
- JSON файл с данными skill gems

**Test Steps:**
1. Создать JSON файл с данными skill gems
2. Вызвать load_skill_gem_data()
3. Проверить результат

**Expected Result:**
- Данные загружены корректно
- gems содержит гемы

---

## Test Case: TC-CALC-GAME-DATA-024
**Title:** GameDataLoader.load_passive_tree_data() invalid JSON

**Category:** Negative

**Description:** Проверка метода load_passive_tree_data() для невалидного JSON

**Preconditions:**
- Файл с невалидным JSON

**Test Steps:**
1. Создать файл с невалидным JSON
2. Вызвать load_passive_tree_data()
3. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- Выбрасывается исключение или возвращается пустой dict

---

## Test Case: TC-CALC-GAME-DATA-025
**Title:** GameDataLoader.load_skill_gem_data() invalid JSON

**Category:** Negative

**Description:** Проверка метода load_skill_gem_data() для невалидного JSON

**Preconditions:**
- Файл с невалидным JSON

**Test Steps:**
1. Создать файл с невалидным JSON
2. Вызвать load_skill_gem_data()
3. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- Выбрасывается исключение или возвращается пустой dict

---

## Test Case: TC-CALC-GAME-DATA-026
**Title:** GameDataLoader.load_unique_item_data() invalid JSON

**Category:** Negative

**Description:** Проверка метода load_unique_item_data() для невалидного JSON

**Preconditions:**
- Файл с невалидным JSON

**Test Steps:**
1. Создать файл с невалидным JSON
2. Вызвать load_unique_item_data()
3. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- Выбрасывается исключение или возвращается пустой dict

---

## Test Case: TC-CALC-GAME-DATA-027
**Title:** GameDataLoader.load_passive_tree_data() wrong structure

**Category:** Negative

**Description:** Проверка метода load_passive_tree_data() для неправильной структуры данных

**Preconditions:**
- JSON файл с неправильной структурой

**Test Steps:**
1. Создать JSON файл с неправильной структурой
2. Вызвать load_passive_tree_data()
3. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- Выбрасывается исключение или возвращается пустой dict

---

## Test Case: TC-CALC-GAME-DATA-028
**Title:** GameDataLoader.load_skill_gem_data() wrong structure

**Category:** Negative

**Description:** Проверка метода load_skill_gem_data() для неправильной структуры данных

**Preconditions:**
- JSON файл с неправильной структурой

**Test Steps:**
1. Создать JSON файл с неправильной структурой
2. Вызвать load_skill_gem_data()
3. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- Выбрасывается исключение или возвращается пустой dict
