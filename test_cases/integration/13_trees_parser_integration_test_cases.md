# TreesParser Integration Test Cases

## Module: tests/integrations/test_trees_parser_integration.py

### Overview
Интеграционные тест-кейсы для проверки взаимодействия TreesParser с другими компонентами.

---

## Test Case: TC-INT-TREES-PARSER-001
**Title:** Parse trees from build

**Category:** Positive

**Integration:** TreesParser ↔ PathOfBuildingAPI

**Description:** Проверка парсинга trees из build

**Preconditions:**
- Есть build fixture с trees

**Test Steps:**
1. Получить trees из build
2. Парсить trees через TreesParser.parse_trees()

**Expected Result:**
- trees is not None
- isinstance(trees, list)

---

## Test Case: TC-INT-TREES-PARSER-002
**Title:** TreesParser with PathOfBuildingAPI

**Category:** Positive

**Integration:** TreesParser ↔ PathOfBuildingAPI

**Description:** Проверка работы TreesParser с PathOfBuildingAPI

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Получить XML из build
2. Парсить trees через TreesParser
3. Проверить результат

**Expected Result:**
- trees is not None
- len(trees) > 0

---

## Test Case: TC-INT-TREES-PARSER-003
**Title:** TreesParser with active tree

**Category:** Positive

**Integration:** TreesParser ↔ PathOfBuildingAPI

**Description:** Проверка работы TreesParser с active_skill_tree

**Preconditions:**
- Есть build fixture с active_skill_tree

**Test Steps:**
1. Получить active_skill_tree из build
2. Парсить trees через TreesParser
3. Проверить соответствие

**Expected Result:**
- trees is not None
- active_skill_tree соответствует parsed trees

---

## Test Case: TC-INT-TREES-PARSER-004
**Title:** Default parser uses TreesParser

**Category:** Positive

**Integration:** DefaultBuildParser ↔ TreesParser

**Description:** Проверка, что DefaultBuildParser использует TreesParser

**Preconditions:**
- Есть sample_xml fixture

**Test Steps:**
1. Парсить XML через DefaultBuildParser
2. Проверить, что trees парсятся через TreesParser

**Expected Result:**
- trees is not None
- trees парсятся корректно

---

## Test Case: TC-INT-TREES-PARSER-005
**Title:** Factory uses TreesParser

**Category:** Positive

**Integration:** BuildFactory ↔ TreesParser

**Description:** Проверка, что BuildFactory использует TreesParser

**Preconditions:**
- Есть sample_xml fixture

**Test Steps:**
1. Создать build через BuildFactory.from_xml_bytes()
2. Проверить, что trees парсятся через TreesParser

**Expected Result:**
- build.trees is not None
- trees парсятся корректно

---

## Test Case: TC-INT-TREES-PARSER-006
**Title:** TreesParser feeds CalculationEngine

**Category:** Positive

**Integration:** TreesParser ↔ CalculationEngine

**Description:** Проверка, что TreesParser передает данные в CalculationEngine

**Preconditions:**
- Есть build fixture с trees

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Проверить, что tree модификаторы загружены

**Expected Result:**
- engine.modifiers is not None
- engine.modifiers содержит tree модификаторы

---

## Test Case: TC-INT-TREES-PARSER-007
**Title:** TreesParser with PassiveTreeParser

**Category:** Positive

**Integration:** TreesParser ↔ PassiveTreeParser

**Description:** Проверка работы TreesParser с PassiveTreeParser

**Preconditions:**
- Есть build fixture с trees и nodes

**Test Steps:**
1. Парсить trees через TreesParser
2. Парсить nodes через PassiveTreeParser
3. Проверить соответствие

**Expected Result:**
- modifiers is not None
- isinstance(modifiers, list)

---

## Test Case: TC-INT-TREES-PARSER-008
**Title:** TreesParser jewel sockets with PassiveTreeParser

**Category:** Positive

**Integration:** TreesParser ↔ PassiveTreeParser ↔ JewelParser

**Description:** Проверка работы TreesParser с jewel sockets и PassiveTreeParser

**Preconditions:**
- Есть build fixture с trees и jewel sockets

**Test Steps:**
1. Парсить trees через TreesParser
2. Найти jewel sockets
3. Парсить jewel modifiers через PassiveTreeParser

**Expected Result:**
- modifiers is not None
- isinstance(modifiers, list)

---

## Test Case: TC-INT-TREES-PARSER-009
**Title:** TreesParser full workflow

**Category:** Positive

**Integration:** TreesParser ↔ DefaultBuildParser ↔ PathOfBuildingAPI

**Description:** Проверка полного рабочего процесса TreesParser

**Preconditions:**
- Есть sample_xml fixture

**Test Steps:**
1. Парсить XML через DefaultBuildParser
2. Создать build через PathOfBuildingAPI
3. Парсить trees через TreesParser
4. Проверить все компоненты

**Expected Result:**
- trees is not None
- tree["nodes"] == tree_serialized["nodes"]

---

## Test Case: TC-INT-TREES-PARSER-010
**Title:** TreesParser with serialization

**Category:** Positive

**Integration:** TreesParser ↔ BuildXMLSerializer ↔ PathOfBuildingAPI

**Description:** Проверка работы TreesParser с сериализацией

**Preconditions:**
- Есть build fixture с trees

**Test Steps:**
1. Парсить trees из build
2. Сериализовать build в XML
3. Парсить XML обратно
4. Проверить, что trees сохранены

**Expected Result:**
- trees сохранены в XML
- trees парсятся корректно

---
