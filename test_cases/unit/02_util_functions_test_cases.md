# Util Functions Unit Test Cases

## Module: pobapi.util

### Overview
Юнит-тест-кейсы для утилитарных функций модуля util. Тесты проверяют отдельные функции в изоляции с различными входными данными.

---

## Test Case: TC-UTIL-FUNC-001
**Title:** _get_stat() with matching prefix

**Category:** Positive

**Description:** Проверка функции _get_stat() при наличии строки с совпадающим префиксом

**Preconditions:**
- Список text содержит строку с нужным префиксом

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique", "Quality: 20"], "Rarity: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает "Unique"

---

## Test Case: TC-UTIL-FUNC-002
**Title:** _get_stat() with different prefix

**Category:** Positive

**Description:** Проверка функции _get_stat() с другим префиксом

**Preconditions:**
- Список text содержит строку с другим префиксом

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique", "Quality: 20"], "Quality: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает "20"

---

## Test Case: TC-UTIL-FUNC-003
**Title:** _get_stat() with exact match (boolean)

**Category:** Positive

**Description:** Проверка функции _get_stat() для точного совпадения строки (возвращает boolean)

**Preconditions:**
- Список text содержит точное совпадение

**Test Steps:**
1. Вызвать `_get_stat(["Shaper Item", "Elder Item"], "Shaper Item")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает True

---

## Test Case: TC-UTIL-FUNC-004
**Title:** _get_stat() with exact match for different item

**Category:** Positive

**Description:** Проверка функции _get_stat() для точного совпадения другой строки

**Preconditions:**
- Список text содержит другое точное совпадение

**Test Steps:**
1. Вызвать `_get_stat(["Shaper Item", "Elder Item"], "Elder Item")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает True

---

## Test Case: TC-UTIL-FUNC-005
**Title:** _get_stat() when stat not found

**Category:** Edge Case

**Description:** Проверка функции _get_stat() когда статистика не найдена

**Preconditions:**
- Список text не содержит нужную статистику

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique"], "Quality: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает пустую строку ""

---

## Test Case: TC-UTIL-FUNC-006
**Title:** _get_stat() with empty text list

**Category:** Edge Case

**Description:** Проверка функции _get_stat() с пустым списком

**Preconditions:**
- Список text пуст

**Test Steps:**
1. Вызвать `_get_stat([], "Rarity: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает пустую строку ""

---

## Test Case: TC-UTIL-FUNC-007
**Title:** _item_text() with Implicits marker

**Category:** Positive

**Description:** Проверка функции _item_text() при наличии маркера Implicits

**Preconditions:**
- Список text содержит маркер "Implicits: N"

**Test Steps:**
1. Вызвать `_item_text(["Rarity: Unique", "Test Item", "Implicits: 2", "+10 to maximum Life", "+20 to maximum Mana"])`
2. Преобразовать результат в список
3. Проверить содержимое

**Expected Result:**
- Результат содержит "+10 to maximum Life"
- Результат содержит "+20 to maximum Mana"
- Результат не содержит "Rarity: Unique"

---

## Test Case: TC-UTIL-FUNC-008
**Title:** _item_text() without Implicits marker

**Category:** Edge Case

**Description:** Проверка функции _item_text() без маркера Implicits

**Preconditions:**
- Список text не содержит маркер Implicits

**Test Steps:**
1. Вызвать `_item_text(["Rarity: Unique", "Test Item"])`
2. Преобразовать результат в список
3. Проверить содержимое

**Expected Result:**
- Результат пустой или содержит все элементы

---

## Test Case: TC-UTIL-FUNC-009
**Title:** _item_text() with Implicits: 1 but no items

**Category:** Edge Case

**Description:** Проверка функции _item_text() с Implicits: 1, но без элементов после маркера

**Preconditions:**
- Список text содержит "Implicits: 1", но нет элементов после него

**Test Steps:**
1. Вызвать `_item_text(["Rarity: Unique", "Test Item", "Implicits: 1"])`
2. Преобразовать результат в список
3. Проверить содержимое

**Expected Result:**
- Результат пустой список []

---

## Test Case: TC-UTIL-FUNC-010
**Title:** _get_pos() with existing stat

**Category:** Positive

**Description:** Проверка функции _get_pos() для существующей статистики

**Preconditions:**
- Список text содержит нужную статистику

**Test Steps:**
1. Вызвать `_get_pos(["Rarity: Unique", "Quality: 20", "LevelReq: 68"], "Quality: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает 1 (индекс элемента)

---

## Test Case: TC-UTIL-FUNC-011
**Title:** _get_pos() with different stat

**Category:** Positive

**Description:** Проверка функции _get_pos() для другой статистики

**Preconditions:**
- Список text содержит другую статистику

**Test Steps:**
1. Вызвать `_get_pos(["Rarity: Unique", "Quality: 20", "LevelReq: 68"], "LevelReq: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает 2 (индекс элемента)

---

## Test Case: TC-UTIL-FUNC-012
**Title:** _get_pos() when stat not found

**Category:** Edge Case

**Description:** Проверка функции _get_pos() когда статистика не найдена

**Preconditions:**
- Список text не содержит нужную статистику

**Test Steps:**
1. Вызвать `_get_pos(["Rarity: Unique"], "Quality: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает None

---

## Test Case: TC-UTIL-FUNC-013
**Title:** _get_stat() with multiple matching prefixes

**Category:** Edge Case

**Description:** Проверка функции _get_stat() когда несколько строк имеют совпадающий префикс

**Preconditions:**
- Список text содержит несколько строк с одинаковым префиксом

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique", "Rarity: Rare"], "Rarity: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает значение первой найденной строки

---

## Test Case: TC-UTIL-FUNC-014
**Title:** _get_stat() with prefix at start of string

**Category:** Positive

**Description:** Проверка функции _get_stat() когда префикс находится в начале строки

**Preconditions:**
- Список text содержит строку, начинающуюся с префикса

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique", "Some other text"], "Rarity: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает "Unique"

---

## Test Case: TC-UTIL-FUNC-015
**Title:** _item_text() with multiple Implicits items

**Category:** Positive

**Description:** Проверка функции _item_text() с несколькими элементами после маркера Implicits

**Preconditions:**
- Список text содержит "Implicits: N" с несколькими элементами после него

**Test Steps:**
1. Вызвать `_item_text(["Rarity: Unique", "Implicits: 3", "Item1", "Item2", "Item3"])`
2. Преобразовать результат в список
3. Проверить количество элементов

**Expected Result:**
- Результат содержит 3 элемента
- Все элементы после маркера присутствуют

---

## Test Case: TC-UTIL-FUNC-016
**Title:** _get_pos() with empty text list

**Category:** Edge Case

**Description:** Проверка функции _get_pos() с пустым списком

**Preconditions:**
- Список text пуст

**Test Steps:**
1. Вызвать `_get_pos([], "Quality: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает None

---

## Test Case: TC-UTIL-FUNC-017
**Title:** _get_stat() with trailing whitespace in prefix (exact match required)

**Category:** Edge Case

**Description:** Проверка функции _get_stat() с дополнительными пробелами в конце префикса. Функция требует точного совпадения префикса, поэтому префикс с лишними пробелами не должен совпадать со строкой без этих пробелов.

**Preconditions:**
- Список text содержит строку "Rarity: Unique"
- Префикс содержит дополнительные пробелы в конце ("Rarity:  ")

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique"], "Rarity:  ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Функция возвращает "" (пустую строку), так как "Rarity: Unique" не начинается с "Rarity:  " (префикс требует точного совпадения)

---

## Test Case: TC-UTIL-FUNC-018
**Title:** _item_text() with Implicits: 0

**Category:** Edge Case

**Description:** Проверка функции _item_text() с Implicits: 0

**Preconditions:**
- Список text содержит "Implicits: 0"

**Test Steps:**
1. Вызвать `_item_text(["Rarity: Unique", "Implicits: 0", "Some text"])`
2. Преобразовать результат в список
3. Проверить содержимое

**Expected Result:**
- Функция возвращает список `["Some text"]`
- Результат содержит элемент "Some text"
- Результат не содержит "Rarity: Unique"
- Результат не содержит "Implicits: 0"

---

## Test Case: TC-UTIL-FUNC-019
**Title:** _item_text() handles KeyError when slicing

**Category:** Edge Case

**Description:** Проверка функции _item_text() для обработки KeyError при срезе (покрывает строки 140-141)

**Preconditions:**
- Кастомный объект, который выбрасывает KeyError при срезе

**Test Steps:**
1. Создать KeyErrorList объект
2. Вызвать `list(_item_text(text))`
3. Проверить обработку KeyError

**Expected Result:**
- KeyError обработан корректно
- Возвращается пустой список

---

## Test Case: TC-UTIL-FUNC-020
**Title:** _item_text() handles IndexError when slicing

**Category:** Edge Case

**Description:** Проверка функции _item_text() для обработки IndexError при срезе (покрывает строки 140-141)

**Preconditions:**
- Кастомный объект, который выбрасывает IndexError при срезе

**Test Steps:**
1. Создать IndexErrorList объект
2. Вызвать `list(_item_text(text))`
3. Проверить обработку IndexError

**Expected Result:**
- IndexError обработан корректно
- Возвращается пустой список

---

## Test Case: TC-UTIL-FUNC-021
**Title:** _get_default_http_client() raises ImportError when requests unavailable

**Category:** Negative

**Description:** Проверка функции _get_default_http_client() для выброса ImportError когда requests недоступен (покрывает строки 87-88)

**Preconditions:**
- requests удален из sys.modules
- __import__ замокан для выброса ImportError

**Test Steps:**
1. Удалить requests из sys.modules
2. Замокать __import__ для выброса ImportError
3. Вызвать `_get_default_http_client()`
4. Перехватить исключение

**Expected Result:**
- Выбрасывается ImportError
- Сообщение содержит "requests library is required"

---

## Test Case: TC-UTIL-FUNC-022
**Title:** _skill_tree_nodes() with invalid base64

**Category:** Negative

**Description:** Проверка функции _skill_tree_nodes() с невалидным base64

**Preconditions:**
- URL содержит невалидный base64

**Test Steps:**
1. Вызвать `_skill_tree_nodes("https://www.pathofexile.com/passive-skill-tree/AAA!!!")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValueError
- Сообщение содержит "Invalid skill tree URL format"

---

## Test Case: TC-UTIL-FUNC-023
**Title:** _skill_tree_nodes() with too short binary data

**Category:** Negative

**Description:** Проверка функции _skill_tree_nodes() с слишком короткими бинарными данными

**Preconditions:**
- URL содержит base64 данные короче TREE_OFFSET

**Test Steps:**
1. Создать URL с короткими base64 данными
2. Вызвать `_skill_tree_nodes(url)`
3. Перехватить исключение

**Expected Result:**
- Выбрасывается ValueError
- Сообщение содержит "Skill tree data too short"

---

## Test Case: TC-UTIL-FUNC-024
**Title:** _fetch_xml_from_import_code() with empty string

**Category:** Negative

**Description:** Проверка функции _fetch_xml_from_import_code() с пустой строкой

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `_fetch_xml_from_import_code("")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidImportCodeError

---

## Test Case: TC-UTIL-FUNC-025
**Title:** _fetch_xml_from_import_code() with None value

**Category:** Negative

**Description:** Проверка функции _fetch_xml_from_import_code() с None значением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `_fetch_xml_from_import_code(None)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidImportCodeError
