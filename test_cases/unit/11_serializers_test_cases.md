# Serializers Unit Test Cases

## Module: pobapi.serializers

### Overview
Юнит-тест-кейсы для модуля serializers, который отвечает за сериализацию билдов в XML и генерацию import code.

---

## Test Case: TC-SERIALIZERS-001
**Title:** BuildXMLSerializer.serialize() with basic build

**Category:** Positive

**Description:** Проверка статического метода serialize() для базового билда

**Preconditions:**
- BuildBuilder настроен с классом и уровнем

**Test Steps:**
1. Создать builder с классом и уровнем
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить XML структуру

**Expected Result:**
- xml_element.tag == "PathOfBuilding"
- build_elem.get("className") == "Witch"
- build_elem.get("ascendClassName") == "Necromancer"
- build_elem.get("level") == "90"

---

## Test Case: TC-SERIALIZERS-002
**Title:** BuildXMLSerializer.serialize() with bandit choice

**Category:** Positive

**Description:** Проверка статического метода serialize() с выбором бандита

**Preconditions:**
- BuildBuilder настроен с bandit

**Test Steps:**
1. Установить bandit
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить атрибут bandit

**Expected Result:**
- build_elem.get("bandit") == "Alira"

---

## Test Case: TC-SERIALIZERS-003
**Title:** BuildXMLSerializer.serialize() with skill groups

**Category:** Positive

**Description:** Проверка статического метода serialize() с группами скиллов

**Preconditions:**
- BuildBuilder содержит скиллы

**Test Steps:**
1. Добавить Gem в builder
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить элемент Skills

**Expected Result:**
- skills_elem найден
- skill_elem найден
- ability_elem содержит корректные атрибуты

---

## Test Case: TC-SERIALIZERS-004
**Title:** BuildXMLSerializer.serialize() with active skill

**Category:** Positive

**Description:** Проверка статического метода serialize() с активным скиллом (покрывает строку 47)

**Preconditions:**
- BuildBuilder содержит скилл с установленным active

**Test Steps:**
1. Добавить скилл
2. Установить active на skill group
3. Вызвать `BuildXMLSerializer.serialize(builder)`
4. Проверить mainActiveSkill

**Expected Result:**
- skill_elem.get("mainActiveSkill") == "0"

---

## Test Case: TC-SERIALIZERS-005
**Title:** BuildXMLSerializer.serialize() with support gem

**Category:** Positive

**Description:** Проверка статического метода serialize() с support гемом

**Preconditions:**
- BuildBuilder содержит support гем

**Test Steps:**
1. Добавить support Gem
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить атрибуты support гема

**Expected Result:**
- Support гем корректно сериализован
- Атрибуты соответствуют ожидаемым

---

## Test Case: TC-SERIALIZERS-006
**Title:** BuildXMLSerializer.serialize() with items

**Category:** Positive

**Description:** Проверка статического метода serialize() с предметами

**Preconditions:**
- BuildBuilder содержит предметы

**Test Steps:**
1. Добавить предметы в builder
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить элемент Items

**Expected Result:**
- items_elem найден
- Предметы корректно сериализованы

---

## Test Case: TC-SERIALIZERS-007
**Title:** BuildXMLSerializer.serialize() with passive tree

**Category:** Positive

**Description:** Проверка статического метода serialize() с пассивным деревом

**Preconditions:**
- BuildBuilder содержит дерево с нодами

**Test Steps:**
1. Создать дерево и добавить ноды
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить элемент Tree

**Expected Result:**
- tree_elem найден
- Ноды корректно сериализованы

---

## Test Case: TC-SERIALIZERS-008
**Title:** ImportCodeGenerator.generate() with valid build

**Category:** Positive

**Description:** Проверка статического метода generate() с валидным билдом

**Preconditions:**
- BuildBuilder настроен и собран

**Test Steps:**
1. Создать билд через builder
2. Вызвать `ImportCodeGenerator.generate(build)`
3. Проверить возвращаемый код

**Expected Result:**
- Возвращается валидный import code (строка)
- Код можно декодировать обратно в XML

---

## Test Case: TC-SERIALIZERS-009
**Title:** ImportCodeGenerator.generate() encodes correctly

**Category:** Positive

**Description:** Проверка корректности кодирования import code

**Preconditions:**
- Валидный билд создан

**Test Steps:**
1. Сгенерировать import code
2. Декодировать код обратно в XML
3. Проверить содержимое XML

**Expected Result:**
- XML соответствует исходному билду
- Все данные сохранены

---

## Test Case: TC-SERIALIZERS-010
**Title:** BuildXMLSerializer.serialize() with empty build

**Category:** Edge Case

**Description:** Проверка статического метода serialize() с пустым билдом

**Preconditions:**
- BuildBuilder инициализирован без данных

**Test Steps:**
1. Вызвать `BuildXMLSerializer.serialize(builder)`
2. Проверить XML структуру

**Expected Result:**
- XML создан
- Содержит базовую структуру PathOfBuilding

---

## Test Case: TC-SERIALIZERS-011
**Title:** BuildXMLSerializer.serialize() with multiple skill groups

**Category:** Positive

**Description:** Проверка статического метода serialize() с несколькими группами скиллов

**Preconditions:**
- BuildBuilder содержит несколько групп скиллов

**Test Steps:**
1. Добавить несколько групп скиллов
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить все группы

**Expected Result:**
- Все группы скиллов сериализованы
- Каждая группа содержит корректные данные

---

## Test Case: TC-SERIALIZERS-012
**Title:** BuildXMLSerializer.serialize() with multiple item sets

**Category:** Positive

**Description:** Проверка статического метода serialize() с несколькими наборами предметов

**Preconditions:**
- BuildBuilder содержит несколько item sets

**Test Steps:**
1. Создать несколько item sets
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить все наборы

**Expected Result:**
- Все наборы предметов сериализованы
- Каждый набор содержит корректные данные

---

## Test Case: TC-SERIALIZERS-013
**Title:** ImportCodeGenerator.generate() with complex build

**Category:** Positive

**Description:** Проверка статического метода generate() со сложным билдом

**Preconditions:**
- BuildBuilder настроен со всеми компонентами

**Test Steps:**
1. Создать сложный билд (класс, скиллы, предметы, дерево)
2. Вызвать `ImportCodeGenerator.generate(build)`
3. Проверить код

**Expected Result:**
- Import code успешно сгенерирован
- Код можно декодировать в полный билд

---

## Test Case: TC-SERIALIZERS-014
**Title:** BuildXMLSerializer.serialize() preserves all attributes

**Category:** Positive

**Description:** Проверка статического метода serialize() для сохранения всех атрибутов

**Preconditions:**
- BuildBuilder настроен со всеми возможными атрибутами

**Test Steps:**
1. Настроить все атрибуты билда
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить все атрибуты в XML

**Expected Result:**
- Все атрибуты сохранены в XML
- Значения соответствуют исходным

---

## Test Case: TC-SERIALIZERS-015
**Title:** ImportCodeGenerator.generate() produces valid base64

**Category:** Positive

**Description:** Проверка статического метода generate() для генерации валидного base64

**Preconditions:**
- Валидный билд создан

**Test Steps:**
1. Сгенерировать import code
2. Проверить, что код является валидным base64
3. Декодировать base64

**Expected Result:**
- Код является валидным base64
- Декодирование проходит успешно

---

## Test Case: TC-SERIALIZERS-016
**Title:** BuildXMLSerializer.serialize() with notes

**Category:** Positive

**Description:** Проверка статического метода serialize() с заметками

**Preconditions:**
- BuildBuilder содержит notes

**Test Steps:**
1. Установить notes
2. Вызвать `BuildXMLSerializer.serialize(builder)`
3. Проверить элемент Notes

**Expected Result:**
- Notes элемент найден
- Содержимое соответствует установленному тексту

---

## Test Case: TC-SERIALIZERS-017
**Title:** ImportCodeGenerator.generate() round-trip test

**Category:** Positive

**Description:** Проверка полного цикла: билд → import code → билд

**Preconditions:**
- Валидный билд создан

**Test Steps:**
1. Создать билд
2. Сгенерировать import code
3. Загрузить билд из import code
4. Сравнить исходный и загруженный билды

**Expected Result:**
- Билды идентичны
- Все данные сохранены
