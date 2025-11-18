# Calculator Jewel Parser Unit Test Cases

## Module: pobapi.calculator.jewel_parser

### Overview
Юнит-тест-кейсы для модуля calculator.jewel_parser, который отвечает за парсинг джемов.

---

## Test Case: TC-CALC-JEWEL-001
**Title:** JewelParser.detect_jewel_type() radius jewel

**Category:** Positive

**Description:** Проверка метода detect_jewel_type() для radius jewel

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `JewelParser.detect_jewel_type("Small Cluster Jewel")`
2. Проверить результат

**Expected Result:**
- result == JewelType.RADIUS
- Тип джема распознан корректно

---

## Test Case: TC-CALC-JEWEL-002
**Title:** JewelParser.detect_jewel_type() conversion jewel

**Category:** Positive

**Description:** Проверка метода detect_jewel_type() для conversion jewel

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `JewelParser.detect_jewel_type("Thread of Hope")`
2. Проверить результат

**Expected Result:**
- result == JewelType.CONVERSION
- Тип джема распознан корректно

---

## Test Case: TC-CALC-JEWEL-003
**Title:** JewelParser.detect_jewel_type() timeless jewel

**Category:** Positive

**Description:** Проверка метода detect_jewel_type() для timeless jewel

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `JewelParser.detect_jewel_type("Glorious Vanity")`
2. Проверить результат

**Expected Result:**
- result == JewelType.TIMELESS
- Тип джема распознан корректно

---

## Test Case: TC-CALC-JEWEL-004
**Title:** JewelParser.detect_jewel_type() normal jewel

**Category:** Positive

**Description:** Проверка метода detect_jewel_type() для обычного джема

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `JewelParser.detect_jewel_type("Crimson Jewel")`
2. Проверить результат

**Expected Result:**
- result == JewelType.NORMAL
- Тип джема распознан корректно

---

## Test Case: TC-CALC-JEWEL-005
**Title:** JewelParser.detect_jewel_type() case insensitive

**Category:** Positive

**Description:** Проверка метода detect_jewel_type() для case insensitive определения

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать detect_jewel_type() с разным регистром
2. Проверить результаты

**Expected Result:**
- Оба варианта возвращают одинаковый тип
- Case insensitive работает

---

## Test Case: TC-CALC-JEWEL-006
**Title:** JewelParser.parse_radius_jewel() with allocated nodes

**Category:** Positive

**Description:** Проверка метода parse_radius_jewel() с allocated nodes

**Preconditions:**
- Mock jewel создан со следующей структурой:
  - `name` (str): имя джема, например "Small Cluster Jewel"
  - `text` (str): полный текст джема, содержащий модификаторы и описание радиуса, например "Small Cluster Jewel\nAdds 2 Passive Skills\nPassives in radius have +10% to Fire Resistance"
  - Парсер читает атрибут `text` через `hasattr(jewel_item, "text")` и `jewel_item.text`
- `allocated_nodes` (list[int]): список ID выделенных нодов для расчета радиуса, например [67890, 67891, 67892], размер списка: 2-3 элемента
- Параметр `12345` (int): origin node_id (socket_id) - ID нода сокета джема, относительно которого рассчитывается радиус

**Test Steps:**
1. Создать mock radius jewel
2. Вызвать `JewelParser.parse_radius_jewel(12345, jewel, allocated_nodes)`
3. Проверить результат

**Expected Result:**
- assert isinstance(modifiers, list)
- assert len(modifiers) >= 0  # Может быть пустым, если нет модификаторов в тексте
- Если jewel.text содержит модификаторы (например, "+10 to Strength"), то:
  - assert len(modifiers) >= 1
  - assert all(isinstance(m, Modifier) for m in modifiers)
  - assert all(m.source.startswith("jewel:radius:socket_") for m in modifiers)
  - assert any(m.mod_type in (ModifierType.FLAT, ModifierType.INCREASED, ModifierType.MORE) for m in modifiers)
- Если jewel.text содержит "Passives in radius have", то:
  - assert len(modifiers) >= 1
  - assert any("nodes_in_radius" in m.source for m in modifiers)
- Если jewel.name содержит "Small Cluster Jewel", то:
  - assert any("radius" in m.source.lower() for m in modifiers) or len(modifiers) == 0
- Boundary check: если jewel.text пустой или не содержит модификаторов, то assert len(modifiers) == 0

---

## Test Case: TC-CALC-JEWEL-007
**Title:** JewelParser.parse_radius_jewel() empty allocated nodes

**Category:** Edge Case

**Description:** Проверка метода parse_radius_jewel() с пустым списком allocated nodes

**Preconditions:**
- Mock jewel создан со следующей структурой:
  - `name` (str): имя джема, например "Small Cluster Jewel"
  - `text` (str): полный текст джема, например "Small Cluster Jewel\nAdds 2 Passive Skills"
  - Парсер читает атрибут `text` через `hasattr(jewel_item, "text")` и `jewel_item.text`
- `allocated_nodes` (list[int]): пустой список [], тип: list/array, размер: 0 элементов
- Параметр `12345` (int): origin node_id (socket_id) - ID нода сокета джема

**Test Steps:**
1. Создать mock radius jewel
2. Вызвать parse_radius_jewel() с allocated_nodes=[]
3. Проверить результат

**Expected Result:**
- assert isinstance(modifiers, list)
- assert len(modifiers) >= 0  # Может быть пустым, если нет модификаторов в тексте
- Boundary check: если allocated_nodes пустой, метод все равно должен обработать jewel.text и вернуть модификаторы из текста джема (если они есть)
- Если jewel.text содержит модификаторы, то:
  - assert len(modifiers) >= 1
  - assert all(isinstance(m, Modifier) for m in modifiers)
  - assert all(hasattr(m, "stat") and hasattr(m, "value") and hasattr(m, "mod_type") for m in modifiers)
- Если jewel.text не содержит модификаторов, то assert len(modifiers) == 0

---

## Test Case: TC-CALC-JEWEL-008
**Title:** JewelParser.parse_conversion_jewel() Thread of Hope

**Category:** Positive

**Description:** Проверка метода parse_conversion_jewel() для Thread of Hope

**Preconditions:**
- Mock jewel создан со следующей структурой:
  - `name` (str): имя джема, например "Thread of Hope"
  - `text` (str): полный текст джема, содержащий описание конверсии, например "Thread of Hope\nAllocates 2 Notable Passive Skills in radius\n+10% to all Resistances"
  - Парсер читает атрибут `text` через `hasattr(jewel_item, "text")` и `jewel_item.text`
- `allocated_nodes` (list[int]): список ID выделенных нодов, например [67890, 67891, 67892], размер списка: 2-3 элемента
- Параметр `12345` (int): origin node_id (socket_id) - ID нода сокета джема, относительно которого применяется конверсия

**Test Steps:**
1. Создать mock Thread of Hope jewel
2. Вызвать `JewelParser.parse_conversion_jewel(12345, jewel, allocated_nodes)`
3. Проверить результат

**Expected Result:**
- assert isinstance(modifiers, list)
- assert len(modifiers) >= 0  # Может быть пустым, если нет модификаторов в тексте
- Если jewel.text содержит модификаторы (например, "+10 to Strength"), то:
  - assert len(modifiers) >= 1
  - assert all(isinstance(m, Modifier) for m in modifiers)
  - assert all(m.source.startswith("jewel:conversion:socket_") for m in modifiers)
  - assert all(hasattr(m, "stat") and isinstance(m.stat, str) for m in modifiers)
  - assert all(hasattr(m, "value") and isinstance(m.value, (int, float)) for m in modifiers)
  - assert all(hasattr(m, "mod_type") and isinstance(m.mod_type, ModifierType) for m in modifiers)
- Если jewel.text содержит "Allocates X Notable Passive Skills in radius" или "Allocates X Keystone Passive Skills in radius", то:
  - assert len(modifiers) >= 1
  - assert any(m.stat == "CanAllocateNodesInRadius" for m in modifiers)
  - assert any(m.mod_type == ModifierType.FLAG for m in modifiers if m.stat == "CanAllocateNodesInRadius")
  - assert any(m.value == 1.0 for m in modifiers if m.stat == "CanAllocateNodesInRadius")
- Boundary check: если jewel.text пустой или не содержит модификаторов, то assert len(modifiers) == 0

---

## Test Case: TC-CALC-JEWEL-009
**Title:** JewelParser.parse_conversion_jewel() with match pattern

**Category:** Positive

**Description:** Проверка метода parse_conversion_jewel() с matching pattern

**Preconditions:**
- Mock jewel создан со следующей структурой:
  - `name` (str): имя джема, например "Thread of Hope"
  - `text` (str): полный текст джема, содержащий matching pattern для конверсии, например "Thread of Hope\nAllocates 2 Notable Passive Skills in radius" (паттерн: "Allocates X Notable Passive Skills in radius" или "Allocates X Keystone Passive Skills in radius")
  - Парсер читает атрибут `text` через `hasattr(jewel_item, "text")` и `jewel_item.text` и ищет паттерны через regex
- `allocated_nodes` (list[int]): список ID выделенных нодов, например [67890, 67891], размер списка: 2 элемента
- Параметр `12345` (int): origin node_id (socket_id) - ID нода сокета джема

**Test Steps:**
1. Создать mock jewel с текстом, содержащим matching pattern
2. Вызвать parse_conversion_jewel()
3. Проверить результат

**Expected Result:**
- assert isinstance(modifiers, list)
- assert len(modifiers) >= 1  # Должен содержать хотя бы CanAllocateNodesInRadius модификатор
- assert any(m.stat == "CanAllocateNodesInRadius" for m in modifiers)
- assert any(m.mod_type == ModifierType.FLAG for m in modifiers if m.stat == "CanAllocateNodesInRadius")
- assert any(m.value == 1.0 for m in modifiers if m.stat == "CanAllocateNodesInRadius")
- assert any(m.source.startswith("jewel:conversion:socket_") for m in modifiers if m.stat == "CanAllocateNodesInRadius")
- Если jewel.text содержит дополнительные модификаторы, то:
  - assert len(modifiers) >= 2
  - assert all(isinstance(m, Modifier) for m in modifiers)
  - assert all(hasattr(m, "stat") and isinstance(m.stat, str) for m in modifiers)
- Boundary check: если jewel.text не содержит matching pattern, то assert len(modifiers) == 0 или assert all(m.stat != "CanAllocateNodesInRadius" for m in modifiers)

---

## Test Case: TC-CALC-JEWEL-010
**Title:** JewelParser.parse_timeless_jewel() Glorious Vanity

**Category:** Positive

**Description:** Проверка метода parse_timeless_jewel() для Glorious Vanity

**Preconditions:**
- Mock jewel создан со следующей структурой:
  - `name` (str): имя джема, например "Glorious Vanity"
  - `text` (str): полный текст джема, содержащий описание timeless jewel, например "Glorious Vanity\nBathed in the blood of # sacrificed in the name of\n+10% to all Resistances"
  - `seed` (int, optional): seed значение для timeless jewel, например 54321 (может быть извлечено из text через regex или передано явно)
  - `properties` (list, optional): список свойств джема, каждое свойство может иметь `name` и `value` для извлечения seed
  - Парсер читает атрибут `text` через `hasattr(jewel_item, "text")` и `jewel_item.text`, атрибут `seed` через `hasattr(jewel_item, "seed")` и `jewel_item.seed`
- `allocated_nodes` (list[int]): список ID выделенных нодов, например [67890, 67891, 67892], размер списка: 2-3 элемента
- Параметр `12345` (int): origin node_id (socket_id) - ID нода сокета джема, относительно которого применяются модификаторы timeless jewel

**Test Steps:**
1. Создать mock Glorious Vanity jewel
2. Вызвать `JewelParser.parse_timeless_jewel(12345, jewel, allocated_nodes)`
3. Проверить результат

**Expected Result:**
- assert isinstance(modifiers, list)
- assert len(modifiers) >= 0  # Может быть пустым, если нет модификаторов в тексте
- Если jewel.text содержит модификаторы (например, "+10 to Strength"), то:
  - assert len(modifiers) >= 1
  - assert all(isinstance(m, Modifier) for m in modifiers)
  - assert all(m.source.startswith("jewel:timeless:socket_") for m in modifiers)
  - assert all(hasattr(m, "stat") and isinstance(m.stat, str) for m in modifiers)
  - assert all(hasattr(m, "value") and isinstance(m.value, (int, float)) for m in modifiers)
  - assert all(hasattr(m, "mod_type") and isinstance(m.mod_type, ModifierType) for m in modifiers)
- Если seed предоставлен или извлечен из текста, то:
  - assert any("seed" in m.source.lower() for m in modifiers) or len(modifiers) == 0
  - assert any("timeless" in m.source.lower() for m in modifiers) or len(modifiers) == 0
- Boundary check: если jewel.text пустой или не содержит модификаторов, то assert len(modifiers) == 0
- Boundary check: если seed is None и не может быть извлечен из текста, то assert len(modifiers) >= 0 (могут быть только базовые модификаторы из jewel.text)

---

## Test Case: TC-CALC-JEWEL-011
**Title:** JewelParser.parse_radius_jewel() invalid

**Category:** Negative

**Description:** Проверка метода parse_radius_jewel() для невалидного джема

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `JewelParser.parse_radius_jewel(12345, None, [])` с невалидными данными (jewel_item=None)
2. Проверить возвращаемое значение
3. Убедиться, что исключение не выбрасывается

**Expected Result:**
- Метод возвращает пустой список `[]`
- `isinstance(result, list) == True`
- `len(result) == 0`
- Исключение не выбрасывается
- Метод обрабатывает невалидные данные gracefully, возвращая пустой список модификаторов

---

## Test Case: TC-CALC-JEWEL-012
**Title:** JewelParser.parse_conversion_jewel() invalid

**Category:** Negative

**Description:** Проверка метода parse_conversion_jewel() для невалидного джема

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `JewelParser.parse_conversion_jewel(12345, None, [])` с невалидными данными (jewel_item=None)
2. Проверить возвращаемое значение
3. Убедиться, что исключение не выбрасывается

**Expected Result:**
- Метод возвращает пустой список `[]`
- `isinstance(result, list) == True`
- `len(result) == 0`
- Исключение не выбрасывается
- Метод обрабатывает невалидные данные gracefully, возвращая пустой список модификаторов

---

## Test Case: TC-CALC-JEWEL-013
**Title:** JewelParser.parse_timeless_jewel() invalid

**Category:** Negative

**Description:** Проверка метода parse_timeless_jewel() для невалидного джема

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `JewelParser.parse_timeless_jewel(12345, None, [])` с невалидными данными (jewel_item=None)
2. Проверить возвращаемое значение
3. Убедиться, что исключение не выбрасывается

**Expected Result:**
- Метод возвращает пустой список `[]`
- `isinstance(result, list) == True`
- `len(result) == 0`
- Исключение не выбрасывается
- Метод обрабатывает невалидные данные gracefully, возвращая пустой список модификаторов

---

## Test Case: TC-CALC-JEWEL-014
**Title:** JewelParser.extract_radius_from_text() valid match

**Category:** Positive

**Description:** Проверка метода extract_radius_from_text() для валидного match

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать extract_radius_from_text() с текстом, содержащим радиус
2. Проверить результат

**Expected Result:**
- Радиус извлечен корректно
- Результат корректен

---

## Test Case: TC-CALC-JEWEL-015
**Title:** JewelParser.extract_radius_from_text() invalid match

**Category:** Edge Case

**Description:** Проверка метода extract_radius_from_text() для невалидного match

**Preconditions:**
- Regex match замокан для возврата невалидных данных

**Test Steps:**
1. Замокать regex match для возврата невалидных данных
2. Вызвать extract_radius_from_text()
3. Проверить обработку

**Expected Result:**
- Невалидный match обработан корректно
- Результат корректен

---

## Test Case: TC-CALC-JEWEL-016
**Title:** JewelParser.extract_radius_from_text() cluster jewel

**Category:** Positive

**Description:** Проверка метода extract_radius_from_text() для cluster jewel

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать extract_radius_from_text() для cluster jewel текста
2. Проверить результат

**Expected Result:**
- Радиус извлечен из cluster jewel
- Результат корректен

---

## Test Case: TC-CALC-JEWEL-017
**Title:** JewelParser.extract_radius_from_text() default

**Category:** Edge Case

**Description:** Проверка метода extract_radius_from_text() для default значения

**Preconditions:**
- Нет match

**Test Steps:**
1. Вызвать extract_radius_from_text() без match
2. Проверить результат

**Expected Result:**
- Default значение возвращено
- Результат корректен

---

## Test Case: TC-CALC-JEWEL-018
**Title:** JewelParser.extract_seed_from_text() valid match

**Category:** Positive

**Description:** Проверка метода extract_seed_from_text() для валидного match

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать extract_seed_from_text() с текстом, содержащим seed
2. Проверить результат

**Expected Result:**
- Seed извлечен корректно
- Результат корректен

---

## Test Case: TC-CALC-JEWEL-019
**Title:** JewelParser.extract_seed_from_text() no match

**Category:** Edge Case

**Description:** Проверка метода extract_seed_from_text() без match

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать extract_seed_from_text() без seed в тексте
2. Проверить результат

**Expected Result:**
- None возвращен
- Отсутствие seed обработано корректно

---

## Test Case: TC-CALC-JEWEL-020
**Title:** JewelParser.extract_timeless_modifiers() with seed

**Category:** Positive

**Description:** Проверка метода extract_timeless_modifiers() с seed

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать extract_timeless_modifiers() с seed
2. Проверить результат

**Expected Result:**
- Модификаторы извлечены с учетом seed
- Результат корректен


**Title:** JewelParser.extract_timeless_modifiers() with seed

**Category:** Positive

**Description:** Проверка метода extract_timeless_modifiers() с seed

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать extract_timeless_modifiers() с seed
2. Проверить результат

**Expected Result:**
- Модификаторы извлечены с учетом seed
- Результат корректен
