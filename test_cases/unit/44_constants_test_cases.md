# Constants Unit Test Cases

## Module: pobapi.constants

### Overview
Юнит-тест-кейсы для модуля constants, который содержит константы игры (KEYSTONE_IDS, MONSTER_DAMAGE_TABLE, и др.).

---

## Test Case: TC-CONSTANTS-001
**Title:** TREE_OFFSET constant

**Category:** Positive

**Description:** Проверка константы TREE_OFFSET

**Preconditions:**
- Нет

**Test Steps:**
1. Импортировать TREE_OFFSET
2. Проверить значение

**Expected Result:**
- TREE_OFFSET == 7
- Тип int
- Значение корректно

---

## Test Case: TC-CONSTANTS-002
**Title:** KEYSTONE_IDS structure

**Category:** Positive

**Description:** Проверка структуры словаря KEYSTONE_IDS

**Preconditions:**
- Нет

**Test Steps:**
1. Импортировать KEYSTONE_IDS
2. Проверить структуру

**Expected Result:**
- KEYSTONE_IDS имеет тип dict[str, int]
- isinstance(KEYSTONE_IDS, dict) == True
- len(KEYSTONE_IDS) > 0 (словарь не пустой, содержит 27 элементов)
- Все ключи имеют тип str (например: "acrobatics", "ancestral_bond", "arrow_dancing", "avatar_of_fire", "blood_magic", "chaos_inoculation", и т.д.)
- Все значения имеют тип int (например: 54307, 41970, 54922, 44941, 57279, 11455, и т.д.)
- Все значения > 0 (положительные целые числа)

---

## Test Case: TC-CONSTANTS-003
**Title:** KEYSTONE_IDS specific keystones

**Category:** Positive

**Description:** Проверка наличия конкретных кистоунов в KEYSTONE_IDS

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить наличие известных кистоунов
2. Проверить их ID

**Expected Result:**
- "chaos_inoculation" in KEYSTONE_IDS == True
- KEYSTONE_IDS["chaos_inoculation"] == 11455 (тип: int)
- "blood_magic" in KEYSTONE_IDS == True
- KEYSTONE_IDS["blood_magic"] == 57279 (тип: int)
- "mind_over_matter" in KEYSTONE_IDS == True
- KEYSTONE_IDS["mind_over_matter"] == 34098 (тип: int)
- Все три ID являются положительными целыми числами
- Все три значения установлены корректно

---

## Test Case: TC-CONSTANTS-004
**Title:** MONSTER_DAMAGE_TABLE structure

**Category:** Positive

**Description:** Проверка структуры MONSTER_DAMAGE_TABLE

**Preconditions:**
- Нет

**Test Steps:**
1. Импортировать MONSTER_DAMAGE_TABLE
2. Проверить структуру

**Expected Result:**
- MONSTER_DAMAGE_TABLE имеет тип list[int]
- isinstance(MONSTER_DAMAGE_TABLE, list) == True
- len(MONSTER_DAMAGE_TABLE) == 100 (список содержит 100 элементов)
- Все элементы имеют тип int (например: 5, 6, 6, 7, 7, 8, 9, 10, и т.д.)
- MONSTER_DAMAGE_TABLE[0] == 5 (первый элемент, тип: int)
- MONSTER_DAMAGE_TABLE[99] > 0 (последний элемент, тип: int, значение > 0)
- Все элементы >= 0 (неотрицательные целые числа)

---

## Test Case: TC-CONSTANTS-005
**Title:** MONSTER_DAMAGE_TABLE values range

**Category:** Positive

**Description:** Проверка диапазона значений MONSTER_DAMAGE_TABLE

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить минимальное значение
2. Проверить максимальное значение
3. Проверить, что значения возрастают

**Expected Result:**
- Минимальное значение >= 0
- Максимальное значение > 0
- Значения монотонно возрастают (или не убывают)

---

## Test Case: TC-CONSTANTS-006
**Title:** MONSTER_LIFE_TABLE structure

**Category:** Positive

**Description:** Проверка структуры MONSTER_LIFE_TABLE

**Preconditions:**
- Нет

**Test Steps:**
1. Импортировать MONSTER_LIFE_TABLE
2. Проверить структуру

**Expected Result:**
- MONSTER_LIFE_TABLE is list
- Все элементы - int
- Список не пустой
- Длина соответствует ожидаемой (100 элементов)

---

## Test Case: TC-CONSTANTS-007
**Title:** MONSTER_LIFE_TABLE values range

**Category:** Positive

**Description:** Проверка диапазона значений MONSTER_LIFE_TABLE

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить минимальное значение
2. Проверить максимальное значение
3. Проверить, что значения возрастают

**Expected Result:**
- Минимальное значение >= 0
- Максимальное значение > 0
- Значения монотонно возрастают (или не убывают)

---

## Test Case: TC-CONSTANTS-008
**Title:** VAAL_SKILL_MAP structure

**Category:** Positive

**Description:** Проверка структуры VAAL_SKILL_MAP

**Preconditions:**
- Нет

**Test Steps:**
1. Импортировать VAAL_SKILL_MAP
2. Проверить структуру

**Expected Result:**
- VAAL_SKILL_MAP is dict
- Все ключи - строки
- Все значения - строки
- Словарь не пустой

---

## Test Case: TC-CONSTANTS-009
**Title:** VAAL_SKILL_MAP specific mappings

**Category:** Positive

**Description:** Проверка конкретных маппингов в VAAL_SKILL_MAP

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить наличие известных маппингов
2. Проверить их значения

**Expected Result:**
- "Vaal Breach" -> "Portal"
- "Vaal Impurity of Fire" -> "Purity of Fire"
- Маппинги корректны

---

## Test Case: TC-CONSTANTS-010
**Title:** SKILL_MAP structure

**Category:** Positive

**Description:** Проверка структуры SKILL_MAP

**Preconditions:**
- Нет

**Test Steps:**
1. Импортировать SKILL_MAP
2. Проверить структуру

**Expected Result:**
- SKILL_MAP is dict
- Все ключи - строки
- Все значения - строки
- Словарь не пустой

---

## Test Case: TC-CONSTANTS-011
**Title:** SKILL_MAP specific mappings

**Category:** Positive

**Description:** Проверка конкретных маппингов в SKILL_MAP

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить наличие известных маппингов
2. Проверить их значения

**Expected Result:**
- "Melee" -> "Default Attack"
- "Portal" -> "Portal"
- Маппинги корректны

---

## Test Case: TC-CONSTANTS-012
**Title:** Constants immutability

**Category:** Positive

**Description:** Проверка, что константы не изменяются (концептуально)

**Preconditions:**
- Нет

**Test Steps:**
1. Импортировать константы
2. Проверить, что они доступны
3. Проверить их значения

**Expected Result:**
- Константы доступны
- Значения соответствуют ожидаемым
- Константы определены корректно
