# Calculator Passive Tree Parser Unit Test Cases

## Module: pobapi.calculator.passive_tree_parser

### Overview
Юнит-тест-кейсы для модуля calculator.passive_tree_parser, который отвечает за парсинг пассивного дерева.

---

## Test Case: TC-CALC-PASSIVE-PARSER-001
**Title:** PassiveTreeParser.parse_node() with no data

**Category:** Edge Case

**Description:** Проверка метода parse_node() для узла без данных

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveTreeParser.parse_node(12345)`
2. Проверить результат

**Expected Result:**
- modifiers == []
- Узел без данных обработан корректно

---

## Test Case: TC-CALC-PASSIVE-PARSER-002
**Title:** PassiveTreeParser.parse_node() with stats

**Category:** Positive

**Description:** Проверка метода parse_node() для узла со статами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать node_data со статами
2. Вызвать `PassiveTreeParser.parse_node(12345, node_data)`
3. Проверить результат

**Expected Result:**
- len(modifiers) == 3
- modifiers содержит модификатор с stat="Strength", value=10.0, mod_type=ModifierType.FLAT
- modifiers содержит модификатор с stat="Life", value=5.0, mod_type=ModifierType.INCREASED
- modifiers содержит модификатор с stat="maximum Life", value=20.0, mod_type=ModifierType.FLAT
- Модификаторы распознаны корректно

---

## Test Case: TC-CALC-PASSIVE-PARSER-003
**Title:** PassiveTreeParser.parse_node() keystone node

**Category:** Positive

**Description:** Проверка метода parse_node() для keystone узла

**Preconditions:**
- Известный keystone ID из constants

**Test Steps:**
1. Получить keystone ID из KEYSTONE_IDS
2. Вызвать `PassiveTreeParser.parse_node(keystone_id)`
3. Проверить результат

**Expected Result:**
- modifiers содержит модификаторы keystone
- Keystone распознан корректно

---

## Test Case: TC-CALC-PASSIVE-PARSER-004
**Title:** PassiveTreeParser.parse_tree() empty tree

**Category:** Edge Case

**Description:** Проверка метода parse_tree() для пустого дерева

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveTreeParser.parse_tree([])`
2. Проверить результат

**Expected Result:**
- modifiers == []
- Пустое дерево обработано корректно

---

## Test Case: TC-CALC-PASSIVE-PARSER-005
**Title:** PassiveTreeParser.parse_tree() with nodes

**Category:** Positive

**Description:** Проверка метода parse_tree() для дерева с узлами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать список node_ids и tree_data
2. Вызвать `PassiveTreeParser.parse_tree(node_ids, tree_data)`
3. Проверить результат

**Expected Result:**
- modifiers содержит модификаторы всех узлов
- len(modifiers) == 2
- modifiers содержит модификатор с stat="Strength", value=10.0, mod_type=ModifierType.FLAT (из node_id 12345)
- modifiers содержит модификатор с stat="Life", value=5.0, mod_type=ModifierType.INCREASED (из node_id 12346)
- Все узлы обработаны

---

## Test Case: TC-CALC-PASSIVE-PARSER-006
**Title:** PassiveTreeParser.parse_tree() without tree data

**Category:** Edge Case

**Description:** Проверка метода parse_tree() без tree_data

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveTreeParser.parse_tree(node_ids)`
2. Проверить результат

**Expected Result:**
- modifiers == [] или минимальные модификаторы
- Без tree_data обработано корректно

---

## Test Case: TC-CALC-PASSIVE-PARSER-007
**Title:** PassiveTreeParser.parse_keystone() known keystone

**Category:** Positive

**Description:** Проверка метода parse_keystone() для известного keystone

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveTreeParser.parse_keystone("Acrobatics")`
2. Проверить результат

**Expected Result:**
- modifiers содержит модификаторы Acrobatics
- len(modifiers) >= 1
- DodgeChance модификатор присутствует

---

## Test Case: TC-CALC-PASSIVE-PARSER-008
**Title:** PassiveTreeParser.parse_keystone() common keystones

**Category:** Positive

**Description:** Проверка метода parse_keystone() для распространенных keystones с конкретными ожидаемыми модификаторами

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveTreeParser.parse_keystone("Acrobatics")`
2. Вызвать `PassiveTreeParser.parse_keystone("Avatar of the Chase")`
3. Вызвать `PassiveTreeParser.parse_keystone("Chaos Inoculation")`
4. Вызвать `PassiveTreeParser.parse_keystone("Mind Over Matter")`
5. Вызвать `PassiveTreeParser.parse_keystone("Resolute Technique")`
6. Вызвать `PassiveTreeParser.parse_keystone("Point Blank")`
7. Проверить результаты для каждого keystone

**Expected Result:**
- **Acrobatics:**
  - modifiers содержит модификатор с stat="Evasion", value=30.0, mod_type=ModifierType.INCREASED, source="keystone:acrobatics"
  - modifiers содержит модификатор с stat="EnergyShield", value=-50.0, mod_type=ModifierType.INCREASED, source="keystone:acrobatics"
  - modifiers содержит модификатор с stat="DodgeChance", value=30.0, mod_type=ModifierType.FLAT, source="keystone:acrobatics"
  - len(modifiers) == 3
- **Avatar of the Chase:**
  - modifiers возвращает список (может быть пустым, если keystone не реализован)
  - Если реализован, должен содержать соответствующие модификаторы для движения/скорости
- **Chaos Inoculation:**
  - modifiers содержит модификатор с stat="Life", value=1.0, mod_type=ModifierType.BASE, source="keystone:chaos_inoculation"
  - modifiers содержит модификатор с stat="ChaosResistance", value=100.0, mod_type=ModifierType.FLAT, source="keystone:chaos_inoculation"
  - len(modifiers) == 2
- **Mind Over Matter:**
  - modifiers содержит модификатор с stat="DamageTakenFromMana", value=30.0, mod_type=ModifierType.FLAT, source="keystone:mind_over_matter"
  - len(modifiers) == 1
- **Resolute Technique:**
  - modifiers содержит модификатор с stat="HitChance", value=100.0, mod_type=ModifierType.FLAT, source="keystone:resolute_technique"
  - modifiers содержит модификатор с stat="CritChance", value=0.0, mod_type=ModifierType.BASE, source="keystone:resolute_technique"
  - len(modifiers) == 2
- **Point Blank:**
  - modifiers содержит модификатор с stat="ProjectileDamage", value=50.0, mod_type=ModifierType.MORE, source="keystone:point_blank", conditions={"projectile_distance": "close"}
  - modifiers содержит модификатор с stat="ProjectileDamage", value=-50.0, mod_type=ModifierType.MORE, source="keystone:point_blank", conditions={"projectile_distance": "far"}
  - len(modifiers) == 2

---

## Test Case: TC-CALC-PASSIVE-PARSER-009
**Title:** PassiveTreeParser.parse_keystone() unknown keystone

**Category:** Edge Case

**Description:** Проверка метода parse_keystone() для неизвестного keystone

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveTreeParser.parse_keystone("Unknown Keystone")`
2. Проверить результат

**Expected Result:**
- modifiers == [] или default модификаторы
- Неизвестный keystone обработан корректно

---

## Test Case: TC-CALC-PASSIVE-PARSER-010
**Title:** PassiveTreeParser.parse_jewel_socket() with no jewel

**Category:** Edge Case

**Description:** Проверка метода parse_jewel_socket() без джема

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveTreeParser.parse_jewel_socket(12345, None)`
2. Проверить результат

**Expected Result:**
- modifiers == []
- Отсутствие джема обработано корректно

---

## Test Case: TC-CALC-PASSIVE-PARSER-011
**Title:** PassiveTreeParser.parse_jewel_socket() with jewel

**Category:** Positive

**Description:** Проверка метода parse_jewel_socket() с джемом

**Preconditions:**
- Mock jewel создан

**Test Steps:**
1. Создать mock jewel с текстом
2. Вызвать `PassiveTreeParser.parse_jewel_socket(12345, jewel)`
3. Проверить результат

**Expected Result:**
- modifiers содержит модификаторы из джема
- Модификаторы распознаны корректно

---

## Test Case: TC-CALC-PASSIVE-PARSER-012
**Title:** PassiveTreeParser.parse_jewel_socket() different jewel types

**Category:** Positive

**Description:** Проверка метода parse_jewel_socket() для различных типов джемов

**Preconditions:**
- Mock jewels различных типов

**Test Steps:**
1. Создать различные типы джемов (Small Cluster, Thread of Hope, Glorious Vanity)
2. Вызвать parse_jewel_socket() для каждого
3. Проверить результаты

**Expected Result:**
- Все типы джемов обработаны
- Модификаторы распознаны корректно
- Результаты корректны

---

## Test Case: TC-CALC-PASSIVE-PARSER-013
**Title:** PassiveTreeParser.parse_jewel_socket() timeless jewel with seed

**Category:** Positive

**Description:** Проверка метода parse_jewel_socket() для timeless jewel с seed

**Preconditions:**
- Mock timeless jewel с seed

**Test Steps:**
1. Создать timeless jewel с seed
2. Вызвать parse_jewel_socket()
3. Проверить результат

**Expected Result:**
- Timeless jewel обработан
- Seed учтен
- Результат корректен

---

## Test Case: TC-CALC-PASSIVE-PARSER-014
**Title:** PassiveTreeParser.parse_jewel_socket() timeless jewel with properties

**Category:** Positive

**Description:** Проверка метода parse_jewel_socket() для timeless jewel с properties

**Preconditions:**
- Mock timeless jewel с properties

**Test Steps:**
1. Создать timeless jewel с properties
2. Вызвать parse_jewel_socket()
3. Проверить результат

**Expected Result:**
- Timeless jewel обработан
- Properties учтены
- Результат корректен

---

## Test Case: TC-CALC-PASSIVE-PARSER-015
**Title:** PassiveTreeParser.parse_jewel_socket() timeless jewel invalid seed

**Category:** Negative

**Description:** Проверка метода parse_jewel_socket() для timeless jewel с невалидным seed

**Preconditions:**
- Mock timeless jewel с невалидным seed

**Test Steps:**
1. Создать timeless jewel с невалидным seed
2. Вызвать parse_jewel_socket()
3. Проверить результат

**Expected Result:**
- Невалидный seed обработан
- Результат корректен или выбрасывается исключение

---

## Test Case: TC-CALC-PASSIVE-PARSER-016
**Title:** PassiveTreeParser.parse_jewel_socket() conversion jewel

**Category:** Positive

**Description:** Проверка метода parse_jewel_socket() для conversion jewel

**Preconditions:**
- Mock conversion jewel

**Test Steps:**
1. Создать conversion jewel (Thread of Hope, Impossible Escape)
2. Вызвать parse_jewel_socket()
3. Проверить результат

**Expected Result:**
- Conversion jewel обработан
- Модификаторы распознаны
- Результат корректен

---

## Test Case: TC-CALC-PASSIVE-PARSER-017
**Title:** PassiveTreeParser.parse_jewel_socket() radius jewel

**Category:** Positive

**Description:** Проверка метода parse_jewel_socket() для radius jewel

**Preconditions:**
- Mock radius jewel

**Test Steps:**
1. Создать radius jewel
2. Вызвать parse_jewel_socket()
3. Проверить результат

**Expected Result:**
- Radius jewel обработан
- Радиус учтен
- Результат корректен

---

## Test Case: TC-CALC-PASSIVE-PARSER-018
**Title:** PassiveTreeParser.parse_jewel_socket() timeless seed from properties

**Category:** Positive

**Description:** Проверка метода parse_jewel_socket() для извлечения seed из properties

**Preconditions:**
- Mock timeless jewel с seed в properties

**Test Steps:**
1. Создать timeless jewel с seed в properties
2. Вызвать parse_jewel_socket()
3. Проверить результат

**Expected Result:**
- Seed извлечен из properties
- Результат корректен

---

## Test Case: TC-CALC-PASSIVE-PARSER-019
**Title:** PassiveTreeParser.parse_jewel_socket() timeless property edge cases

**Category:** Edge Case

**Description:** Проверка метода parse_jewel_socket() для edge cases свойств timeless jewel

**Preconditions:**
- Mock timeless jewel с edge cases

**Test Steps:**
1. Создать timeless jewel без value или без name в properties
2. Вызвать parse_jewel_socket()
3. Проверить результат

**Expected Result:**
- Edge cases обработаны корректно
- Результат корректен

---

## Test Case: TC-CALC-PASSIVE-PARSER-020
**Title:** PassiveTreeParser.parse_jewel_socket() case insensitive seed

**Category:** Positive

**Description:** Проверка метода parse_jewel_socket() для case insensitive seed

**Preconditions:**
- Mock timeless jewel с seed в разных регистрах

**Test Steps:**
1. Создать timeless jewel с seed в lowercase/mixed case
2. Вызвать parse_jewel_socket()
3. Проверить результат

**Expected Result:**
- Seed распознан независимо от регистра
- Результат корректен
