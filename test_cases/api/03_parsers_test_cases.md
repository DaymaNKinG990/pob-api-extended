# Parsers Test Cases

## Module: pobapi.parsers

### Overview
Тест-кейсы для модуля parsers, который отвечает за парсинг XML данных в структурированные объекты.

---

## Test Case: TC-PARSERS-001
**Title:** Parse valid build info

**Category:** Positive

**Description:** Проверка парсинга валидной информации о билде

**Preconditions:**
- XML содержит валидные данные Build элемента

**Test Steps:**
1. Вызвать `BuildInfoParser.parse(xml_root)`
2. Проверить все поля результата

**Expected Result:**
- Результат содержит корректные значения:
  - class_name соответствует XML
  - ascendancy_name соответствует XML
  - level соответствует XML
  - bandit соответствует XML
  - main_socket_group соответствует XML

---

## Test Case: TC-PARSERS-002
**Title:** Parse build info with missing Build element

**Category:** Negative

**Description:** Проверка обработки ошибки при отсутствии Build элемента

**Preconditions:**
- XML не содержит элемент Build

**Test Steps:**
1. Вызвать `BuildInfoParser.parse(xml_root)` с XML без Build элемента
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ParsingError` с сообщением "Build element not found"

---

## Test Case: TC-PARSERS-003
**Title:** Parse build info with optional fields missing

**Category:** Edge Case

**Description:** Проверка парсинга при отсутствии опциональных полей

**Preconditions:**
- XML содержит только обязательные поля Build элемента

**Test Steps:**
1. Вызвать `BuildInfoParser.parse(xml_root)`
2. Проверить опциональные поля

**Expected Result:**
- Обязательные поля заполнены корректно
- Опциональные поля (ascendancy_name, bandit) равны None

---

## Test Case: TC-PARSERS-004
**Title:** Parse valid skill groups

**Category:** Positive

**Description:** Проверка парсинга валидных групп скиллов

**Preconditions:**
- XML содержит валидные данные Skills элемента

**Test Steps:**
1. Вызвать `SkillsParser.parse_skill_groups(xml_root)`
2. Проверить структуру групп скиллов

**Expected Result:**
- Результат содержит корректные группы скиллов
- Каждая группа содержит: enabled, label, main_active_skill, abilities

---

## Test Case: TC-PARSERS-005
**Title:** Parse multiple skill groups

**Category:** Positive

**Description:** Проверка парсинга нескольких групп скиллов

**Preconditions:**
- XML содержит несколько Skill элементов

**Test Steps:**
1. Вызвать `SkillsParser.parse_skill_groups(xml_root)`
2. Проверить все группы

**Expected Result:**
- Все группы корректно обработаны
- Каждая группа содержит корректные данные

---

## Test Case: TC-PARSERS-006
**Title:** Parse skill groups with empty Skills element

**Category:** Edge Case

**Description:** Проверка парсинга при отсутствии Skills элемента

**Preconditions:**
- XML не содержит элемент Skills

**Test Steps:**
1. Вызвать `SkillsParser.parse_skill_groups(xml_root)`
2. Проверить результат

**Expected Result:**
- Возвращается пустой список []

---

## Test Case: TC-PARSERS-007
**Title:** Parse skill groups with nil mainActiveSkill

**Category:** Edge Case

**Description:** Проверка парсинга группы скиллов с nil mainActiveSkill

**Preconditions:**
- XML содержит Skill с mainActiveSkill="nil"

**Test Steps:**
1. Вызвать `SkillsParser.parse_skill_groups(xml_root)`
2. Проверить значение main_active_skill

**Expected Result:**
- main_active_skill равен None

---

## Test Case: TC-PARSERS-008
**Title:** Parse valid items

**Category:** Positive

**Description:** Проверка парсинга валидных предметов

**Preconditions:**
- XML содержит валидные данные Items элемента

**Test Steps:**
1. Вызвать `ItemsParser.parse_items(xml_root)`
2. Проверить структуру предметов

**Expected Result:**
- Результат содержит корректные предметы
- Каждый предмет содержит корректные данные

---

## Test Case: TC-PARSERS-009
**Title:** Parse items with empty Items element

**Category:** Edge Case

**Description:** Проверка парсинга при отсутствии Items элемента

**Preconditions:**
- XML не содержит элемент Items

**Test Steps:**
1. Вызвать `ItemsParser.parse_items(xml_root)`
2. Проверить результат

**Expected Result:**
- Возвращается пустой список []

---

## Test Case: TC-PARSERS-010
**Title:** Parse valid passive trees

**Category:** Positive

**Description:** Проверка парсинга валидных пассивных деревьев

**Preconditions:**
- XML содержит валидные данные Trees элемента

**Test Steps:**
1. Вызвать `TreesParser.parse_trees(xml_root)`
2. Проверить структуру деревьев

**Expected Result:**
- Результат содержит корректные деревья
- Каждое дерево содержит корректные данные

---

## Test Case: TC-PARSERS-011
**Title:** Parse trees with empty Trees element

**Category:** Edge Case

**Description:** Проверка парсинга при отсутствии Trees элемента

**Preconditions:**
- XML не содержит элемент Trees

**Test Steps:**
1. Вызвать `TreesParser.parse_trees(xml_root)`
2. Проверить результат

**Expected Result:**
- Возвращается пустой список []

---

## Test Case: TC-PARSERS-012
**Title:** Parse build with DefaultBuildParser

**Category:** Positive

**Description:** Проверка парсинга полного билда через DefaultBuildParser

**Preconditions:**
- XML содержит полные данные билда

**Test Steps:**
1. Вызвать `DefaultBuildParser.parse(xml_root)`
2. Проверить все компоненты билда

**Expected Result:**
- Все компоненты билда корректно обработаны
- Билд содержит все необходимые данные

---

## Test Case: TC-PARSERS-013
**Title:** Parse skill group with multiple abilities

**Category:** Positive

**Description:** Проверка парсинга группы скиллов с несколькими способностями

**Preconditions:**
- XML содержит Skill с несколькими Ability элементами

**Test Steps:**
1. Вызвать `SkillsParser.parse_skill_groups(xml_root)`
2. Проверить список abilities

**Expected Result:**
- Все abilities корректно обработаны
- Каждая ability содержит: name, enabled, level, gemId

---

## Test Case: TC-PARSERS-014
**Title:** Parse item with all attributes

**Category:** Positive

**Description:** Проверка парсинга предмета со всеми атрибутами

**Preconditions:**
- XML содержит Item со всеми возможными атрибутами

**Test Steps:**
1. Вызвать `ItemsParser.parse_items(xml_root)`
2. Проверить все атрибуты предмета

**Expected Result:**
- Все атрибуты предмета корректно обработаны
- Значения соответствуют XML данным

---

## Test Case: TC-PARSERS-015
**Title:** Parse tree with multiple nodes

**Category:** Positive

**Description:** Проверка парсинга дерева с несколькими нодами

**Preconditions:**
- XML содержит Tree с несколькими Node элементами

**Test Steps:**
1. Вызвать `TreesParser.parse_trees(xml_root)`
2. Проверить список нод

**Expected Result:**
- Все ноды корректно обработаны
- Каждая нода содержит корректные данные

---

## Test Case: TC-PARSERS-016
**Title:** Handle malformed XML structure

**Category:** Negative

**Description:** Проверка обработки некорректной XML структуры

**Preconditions:**
- XML имеет некорректную структуру

**Test Steps:**
1. Вызвать любой парсер с некорректным XML
2. Проверить обработку ошибки

**Expected Result:**
- Выбрасывается `ParsingError` с соответствующим сообщением

---

## Test Case: TC-PARSERS-017
**Title:** Parse build info with special characters

**Category:** Edge Case

**Description:** Проверка парсинга с специальными символами в данных

**Preconditions:**
- XML содержит специальные символы в значениях

**Test Steps:**
1. Вызвать `BuildInfoParser.parse(xml_root)`
2. Проверить обработку специальных символов

**Expected Result:**
- Специальные символы корректно обработаны
- Значения соответствуют ожидаемым

---

## Test Case: TC-PARSERS-018
**Title:** Parse skill group with disabled abilities

**Category:** Edge Case

**Description:** Проверка парсинга группы скиллов с отключенными способностями

**Preconditions:**
- XML содержит Ability с enabled="false"

**Test Steps:**
1. Вызвать `SkillsParser.parse_skill_groups(xml_root)`
2. Проверить значение enabled для abilities

**Expected Result:**
- enabled корректно установлен в False для отключенных способностей
