# Parser ↔ Serializer Integration Test Cases

## Module: test_cases/integration/test_parser_serializer_integration.py

### Overview
Интеграционные тест-кейсы для проверки взаимодействия между парсерами и сериализаторами.

---

## Test Case: TC-INT-PARSER-SERIALIZER-001
**Title:** Parse then serialize XML

**Category:** Positive

**Integration:** DefaultBuildParser ↔ BuildXMLSerializer ↔ PathOfBuildingAPI

**Description:** Проверка парсинга XML и сериализации обратно в XML

**Preconditions:**
- Есть sample_xml fixture

**Test Steps:**
1. Парсить XML через DefaultBuildParser
2. Создать build через PathOfBuildingAPI
3. Сериализовать build в XML через build.to_xml()

**Expected Result:**
- xml is not None
- len(xml) > 0

---

## Test Case: TC-INT-PARSER-SERIALIZER-002
**Title:** Parse then generate import code

**Category:** Positive

**Integration:** DefaultBuildParser ↔ ImportCodeGenerator ↔ PathOfBuildingAPI

**Description:** Проверка парсинга XML и генерации import code

**Preconditions:**
- Есть sample_xml fixture

**Test Steps:**
1. Парсить XML через DefaultBuildParser
2. Создать build через PathOfBuildingAPI
3. Сгенерировать import code через ImportCodeGenerator.generate_from_api()

**Expected Result:**
- import_code is not None
- len(import_code) > 0

---

## Test Case: TC-INT-PARSER-SERIALIZER-003
**Title:** Import code round trip

**Category:** Positive

**Integration:** ImportCodeGenerator ↔ PathOfBuildingAPI ↔ BuildFactory

**Description:** Проверка round-trip: import code → build → import code

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Сгенерировать import code из build
2. Создать новый build из import code через BuildFactory
3. Сгенерировать import code из нового build
4. Сравнить результаты

**Expected Result:**
- Оба import code валидны
- Следующие свойства должны совпадать между исходным и восстановленным build:
  - **class_name** (character class: Witch, Ranger, Duelist, etc.)
  - **level** (character level: 1-100)
  - **ascendancy_name** (ascendancy class, если присутствует)
  - **bandit** (bandit choice: Alira, Oak, Kraityn, или None)
  - **items** (IDs, names, quantities, slots) — порядок элементов может отличаться
  - **skills** (IDs, names, ranks/levels, quality, enabled status) — порядок может отличаться
  - **trees** (passive nodes/unlocked nodes: node IDs для каждого дерева) — порядок узлов может отличаться
  - **skill_groups** (структура групп навыков: enabled, label, active skill index, abilities)
  - **item_sets** (наборы предметов и их слоты)
  - **notes** (метаданные: build notes/description)
  - **config** (конфигурация билда: enemy level, resistance penalty, stationary, и другие настройки)
  - **stats** (атрибуты/статистики: HP, MP, Energy Shield, Strength, Dexterity, Intelligence, Armour, Evasion, DPS, Average Hit, Resistances) — допускаются небольшие различия из-за округления (tolerance: ±0.01 для float значений)
- **Правила толерантности:**
  - Списки (items, skills, nodes) считаются эквивалентными, если содержат одинаковые элементы независимо от порядка
  - Вычисляемые значения (stats) могут отличаться на ±0.01 из-за округления при сериализации/десериализации
  - Опциональные поля (ascendancy_name, bandit, notes) могут отсутствовать в обоих билдах

---

## Test Case: TC-INT-PARSER-SERIALIZER-004
**Title:** XML serialize with modifications

**Category:** Positive

**Integration:** BuildModifier ↔ BuildXMLSerializer ↔ PathOfBuildingAPI

**Description:** Проверка сериализации XML после модификаций

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Модифицировать build (добавить items, skills)
2. Сериализовать в XML
3. Парсить XML обратно
4. Проверить, что модификации сохранены

**Expected Result:**
- xml is not None
- Модификации сохранены в XML

---

## Test Case: TC-INT-PARSER-SERIALIZER-005
**Title:** Build create then serialize

**Category:** Positive

**Integration:** BuildBuilder ↔ BuildXMLSerializer ↔ PathOfBuildingAPI

**Description:** Проверка создания build через builder и сериализации

**Preconditions:**
- Нет

**Test Steps:**
1. Создать build через create_build() builder
2. Настроить build (class, level, items, skills)
3. Получить API instance через builder.build()
4. Сериализовать в XML

**Expected Result:**
- xml is not None
- len(xml) > 0

---

## Test Case: TC-INT-PARSER-SERIALIZER-006
**Title:** Build modify then serialize

**Category:** Positive

**Integration:** BuildModifier ↔ BuildXMLSerializer ↔ PathOfBuildingAPI

**Description:** Проверка модификации build и сериализации

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Модифицировать build (добавить/изменить items, skills, nodes)
2. Сериализовать в XML
3. Проверить, что все модификации в XML

**Expected Result:**
- xml is not None
- Все модификации присутствуют в XML

---
