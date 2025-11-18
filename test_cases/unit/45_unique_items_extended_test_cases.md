# Unique Items Extended Unit Test Cases

## Module: pobapi.calculator.unique_items_extended

### Overview
Юнит-тест-кейсы для модуля calculator.unique_items_extended, который содержит расширенную базу данных уникальных предметов.

---

## Test Case: TC-UNIQUE-ITEMS-EXT-001
**Title:** EXTENDED_UNIQUE_EFFECTS structure

**Category:** Positive

**Description:** Проверка структуры словаря EXTENDED_UNIQUE_EFFECTS

**Preconditions:**
- Нет

**Test Steps:**
1. Импортировать EXTENDED_UNIQUE_EFFECTS
2. Проверить структуру

**Expected Result:**
- EXTENDED_UNIQUE_EFFECTS имеет тип dict[str, list[Modifier]]
- isinstance(EXTENDED_UNIQUE_EFFECTS, dict) == True
- len(EXTENDED_UNIQUE_EFFECTS) > 0 (словарь не пустой)
- Все ключи имеют тип str (например: "Bisco's Collar", "Bisco's Leash", "Perandus Blazon", "Soulthirst", "The Nomad", и т.д.)
- Все значения имеют тип list (например: isinstance(EXTENDED_UNIQUE_EFFECTS["Bisco's Collar"], list) == True)
- Все элементы в списках имеют тип Modifier (например: isinstance(EXTENDED_UNIQUE_EFFECTS["Bisco's Collar"][0], Modifier) == True)

---

## Test Case: TC-UNIQUE-ITEMS-EXT-002
**Title:** EXTENDED_UNIQUE_EFFECTS modifier structure

**Category:** Positive

**Description:** Проверка структуры модификаторов в EXTENDED_UNIQUE_EFFECTS

**Preconditions:**
- Нет

**Test Steps:**
1. Взять первый предмет из EXTENDED_UNIQUE_EFFECTS
2. Проверить структуру модификаторов

**Expected Result:**
- Первый предмет из EXTENDED_UNIQUE_EFFECTS имеет тип str (имя предмета)
- Список модификаторов первого предмета имеет тип list[Modifier]
- len(список_модификаторов) >= 1 (список не пустой)
- Все элементы списка имеют тип Modifier (isinstance(modifier, Modifier) == True для каждого элемента)
- Каждый Modifier имеет атрибут stat (тип: str, например: "ItemQuantity", "ItemRarity", "SoulEater", "Life", "Mana")
- Каждый Modifier имеет атрибут value (тип: float | int, например: 50.0, 20.0, 1.0, 30.0)
- Каждый Modifier имеет атрибут mod_type (тип: ModifierType, например: ModifierType.INCREASED, ModifierType.FLAT, ModifierType.FLAG)
- Каждый Modifier имеет атрибут source (тип: str, начинается с "unique:", например: "unique:BiscosCollar", "unique:BiscosLeash")

---

## Test Case: TC-UNIQUE-ITEMS-EXT-003
**Title:** EXTENDED_UNIQUE_EFFECTS specific items

**Category:** Positive

**Description:** Проверка наличия конкретных уникальных предметов

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить наличие известных предметов
2. Проверить их модификаторы

**Expected Result:**
- "Bisco's Collar" in EXTENDED_UNIQUE_EFFECTS == True
- len(EXTENDED_UNIQUE_EFFECTS["Bisco's Collar"]) >= 1 (модификаторы присутствуют)
- EXTENDED_UNIQUE_EFFECTS["Bisco's Collar"][0].stat == "ItemQuantity" (тип: str)
- EXTENDED_UNIQUE_EFFECTS["Bisco's Collar"][0].value == 50.0 (тип: float)
- EXTENDED_UNIQUE_EFFECTS["Bisco's Collar"][0].mod_type == ModifierType.INCREASED (тип: ModifierType)
- EXTENDED_UNIQUE_EFFECTS["Bisco's Collar"][0].source == "unique:BiscosCollar" (тип: str)
- Аналогичные проверки для других известных предметов (если указаны в тесте)
- Все модификаторы имеют корректную структуру

---

## Test Case: TC-UNIQUE-ITEMS-EXT-004
**Title:** EXTENDED_UNIQUE_EFFECTS modifier types

**Category:** Positive

**Description:** Проверка типов модификаторов в EXTENDED_UNIQUE_EFFECTS

**Preconditions:**
- Нет

**Test Steps:**
1. Пройтись по всем предметам
2. Проверить типы модификаторов

**Expected Result:**
- Все mod_type являются валидными ModifierType
- Типы корректны
- Результат корректен

---

## Test Case: TC-UNIQUE-ITEMS-EXT-005
**Title:** EXTENDED_UNIQUE_EFFECTS source format

**Category:** Positive

**Description:** Проверка формата source в модификаторах

**Preconditions:**
- Нет

**Test Steps:**
1. Пройтись по всем предметам
2. Проверить формат source

**Expected Result:**
- Все source начинаются с "unique:"
- Формат соответствует ожидаемому
- Результат корректен

---

## Test Case: TC-UNIQUE-ITEMS-EXT-006
**Title:** EXTENDED_UNIQUE_EFFECTS unique item names

**Category:** Positive

**Description:** Проверка уникальности имен предметов

**Preconditions:**
- Нет

**Test Steps:**
1. Получить все ключи EXTENDED_UNIQUE_EFFECTS
2. Проверить уникальность

**Expected Result:**
- Все имена уникальны
- Нет дубликатов
- Результат корректен

---

## Test Case: TC-UNIQUE-ITEMS-EXT-007
**Title:** EXTENDED_UNIQUE_EFFECTS empty modifiers list

**Category:** Edge Case

**Description:** Проверка предметов с пустым списком модификаторов (если есть)

**Preconditions:**
- Нет

**Test Steps:**
1. Найти предметы с пустым списком модификаторов
2. Проверить обработку

**Expected Result:**
- Пустые списки обработаны корректно
- Результат корректен

---

## Test Case: TC-UNIQUE-ITEMS-EXT-008
**Title:** EXTENDED_UNIQUE_EFFECTS modifier values

**Category:** Positive

**Description:** Проверка значений модификаторов

**Preconditions:**
- Нет

**Test Steps:**
1. Пройтись по всем модификаторам
2. Проверить, что values являются числами

**Expected Result:**
- Все values являются float или int
- Значения корректны
- Результат корректен

---

## Test Case: TC-UNIQUE-ITEMS-EXT-009
**Title:** EXTENDED_UNIQUE_EFFECTS integration with UniqueItemParser

**Category:** Positive

**Description:** Проверка интеграции с UniqueItemParser

**Preconditions:**
- UniqueItemParser доступен

**Test Steps:**
1. Использовать предмет из EXTENDED_UNIQUE_EFFECTS
2. Проверить, что UniqueItemParser может его использовать
3. Проверить результат

**Expected Result:**
- Предмет распознан UniqueItemParser
- Модификаторы применены
- Результат корректен

---

## Test Case: TC-UNIQUE-ITEMS-EXT-010
**Title:** EXTENDED_UNIQUE_EFFECTS coverage

**Category:** Positive

**Description:** Проверка покрытия различных категорий предметов

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить наличие предметов разных категорий
2. Проверить распределение

**Expected Result:**
- Различные категории представлены
- Покрытие достаточное
- Результат корректен
