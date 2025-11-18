# Calculator Unique Item Parser Unit Test Cases

## Module: pobapi.calculator.unique_item_parser

### Overview
Юнит-тест-кейсы для модуля calculator.unique_item_parser, который отвечает за парсинг уникальных предметов.

---

## Test Case: TC-CALC-UNIQUE-ITEM-001
**Title:** UniqueItemParser.is_unique_item() true

**Category:** Positive

**Description:** Проверка метода is_unique_item() для уникального предмета

**Preconditions:**
- Нет

**Test Steps:**
1. Создать item_text с "Rarity: UNIQUE"
2. Вызвать `UniqueItemParser.is_unique_item(item_text)`
3. Проверить результат

**Expected Result:**
- result is True
- Уникальный предмет распознан

---

## Test Case: TC-CALC-UNIQUE-ITEM-002
**Title:** UniqueItemParser.is_unique_item() false

**Category:** Positive

**Description:** Проверка метода is_unique_item() для не-уникального предмета

**Preconditions:**
- Нет

**Test Steps:**
1. Создать item_text с "Rarity: RARE"
2. Вызвать `UniqueItemParser.is_unique_item(item_text)`
3. Проверить результат

**Expected Result:**
- result is False
- Не-уникальный предмет распознан

---

## Test Case: TC-CALC-UNIQUE-ITEM-003
**Title:** UniqueItemParser.parse_unique_item() known unique

**Category:** Positive

**Description:** Проверка метода parse_unique_item() для известного уникального предмета

**Preconditions:**
- Нет

**Test Steps:**
1. Создать item_name и item_text для известного unique
2. Вызвать `UniqueItemParser.parse_unique_item(item_name, item_text)`
3. Проверить результат

**Expected Result:**
- len(modifiers) >= 1
- Модификаторы из базы данных применены
- Результат корректен

---

## Test Case: TC-CALC-UNIQUE-ITEM-004
**Title:** UniqueItemParser.parse_unique_item() unknown unique

**Category:** Positive

**Description:** Проверка метода parse_unique_item() для неизвестного уникального предмета

**Preconditions:**
- Нет

**Test Steps:**
1. Создать item_name и item_text для неизвестного unique
2. Вызвать `UniqueItemParser.parse_unique_item(item_name, item_text)`
3. Проверить результат

**Expected Result:**
- len(modifiers) >= 1
- Модификаторы из item_text распарсены
- Regular модификаторы присутствуют

---

## Test Case: TC-CALC-UNIQUE-ITEM-005
**Title:** UniqueItemParser.parse_unique_item() from database

**Category:** Positive

**Description:** Проверка метода parse_unique_item() для предмета из базы данных

**Preconditions:**
- Нет

**Test Steps:**
1. Создать item_name и item_text
2. Вызвать `UniqueItemParser.parse_unique_item(item_name, item_text)`
3. Проверить результат

**Expected Result:**
- Модификаторы из базы данных применены
- Результат корректен

---

## Test Case: TC-CALC-UNIQUE-ITEM-006
**Title:** UniqueItemParser.parse_unique_item() with explicit mods

**Category:** Positive

**Description:** Проверка метода parse_unique_item() с explicit mods из GameDataLoader

**Preconditions:**
- Unique item в GameDataLoader

**Test Steps:**
1. Создать unique item с explicit_mods в GameDataLoader
2. Вызвать `parse_unique_item()` с skip_regular_parsing=False
3. Проверить результат

**Expected Result:**
- explicit_mods распарсены
- Нет рекурсии
- Результат корректен

---

## Test Case: TC-CALC-UNIQUE-ITEM-007
**Title:** UniqueItemParser.parse_unique_item() name normalization

**Category:** Positive

**Description:** Проверка метода parse_unique_item() для нормализации имени

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать parse_unique_item() с именем, содержащим апострофы и пробелы
2. Проверить результат

**Expected Result:**
- Имя нормализовано корректно
- Предмет найден в базе данных
- Результат корректен

---

## Test Case: TC-CALC-UNIQUE-ITEM-008
**Title:** UniqueItemParser.parse_unique_item() GameDataLoader error

**Category:** Negative

**Description:** Проверка метода parse_unique_item() при ошибке GameDataLoader

**Preconditions:**
- GameDataLoader замокан для выброса ошибки

**Test Steps:**
1. Замокать GameDataLoader для выброса ошибки
2. Вызвать parse_unique_item()
3. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- Метод не падает
- Результат корректен

---

## Test Case: TC-CALC-UNIQUE-ITEM-009
**Title:** UniqueItemParser.parse_unique_item() GameDataLoader AttributeError

**Category:** Negative

**Description:** Проверка метода parse_unique_item() при AttributeError от GameDataLoader

**Preconditions:**
- GameDataLoader замокан для выброса AttributeError

**Test Steps:**
1. Замокать GameDataLoader для выброса AttributeError
2. Вызвать parse_unique_item()
3. Проверить обработку ошибки

**Expected Result:**
- AttributeError обработан корректно
- Метод не падает
- Результат корректен

---

## Test Case: TC-CALC-UNIQUE-ITEM-010
**Title:** UniqueItemParser.parse_unique_item() skip regular parsing

**Category:** Positive

**Description:** Проверка метода parse_unique_item() с skip_regular_parsing=True

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать parse_unique_item() с skip_regular_parsing=True
2. Проверить результат

**Expected Result:**
- Regular парсинг пропущен
- Только модификаторы из базы данных
- Результат корректен
