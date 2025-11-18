# Builders Test Cases

## Module: pobapi.builders

### Overview
Тест-кейсы для модуля builders, который отвечает за построение объектов из XML данных.

---

## Test Case: TC-BUILDERS-001
**Title:** Build Stats with valid player stats

**Category:** Positive

**Description:** Проверка построения объекта Stats с валидными статистиками игрока

**Preconditions:**
- XML содержит валидные данные о статистиках

**Test Steps:**
1. Вызвать `StatsBuilder.build(xml_root)`
2. Проверить значения life и mana

**Expected Result:**
- Stats объект создан успешно
- life и mana содержат корректные числовые значения

---

## Test Case: TC-BUILDERS-002
**Title:** Build Stats with empty or missing Build element

**Category:** Edge Case

**Description:** Проверка построения Stats при отсутствии данных о статистиках

**Preconditions:**
- XML не содержит данных о статистиках или элемент Build отсутствует

**Test Steps:**
1. Вызвать `StatsBuilder.build(xml_root)` с XML без статистик
2. Проверить значения life и mana

**Expected Result:**
- Stats объект создан успешно
- life и mana равны None (дефолтные значения)

---

## Test Case: TC-BUILDERS-003
**Title:** Build Config with valid config values

**Category:** Positive

**Description:** Проверка построения объекта Config с валидными значениями конфигурации

**Preconditions:**
- XML содержит валидные данные конфигурации

**Test Steps:**
1. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
2. Проверить значения enemy_level и is_stationary

**Expected Result:**
- Config объект создан успешно
- enemy_level установлен на основе character_level
- is_stationary содержит корректное значение

---

## Test Case: TC-BUILDERS-004
**Title:** Build Config with empty config

**Category:** Edge Case

**Description:** Проверка построения Config при отсутствии данных конфигурации

**Preconditions:**
- XML не содержит данных конфигурации

**Test Steps:**
1. Вызвать `ConfigBuilder.build(xml_root, character_level=1)` с XML без конфигурации
2. Проверить значения конфигурации

**Expected Result:**
- Config объект создан успешно
- Используются дефолтные значения конфигурации

---

## Test Case: TC-BUILDERS-005
**Title:** Build Config with boolean field type

**Category:** Positive

**Description:** Проверка построения Config с boolean полем

**Preconditions:**
- XML содержит boolean поле (например, conditionStationary)

**Test Steps:**
1. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
2. Проверить, что boolean поле корректно преобразовано

**Expected Result:**
- Boolean поле содержит True или False
- Значение соответствует XML данным

---

## Test Case: TC-BUILDERS-006
**Title:** Build Config with number field type

**Category:** Positive

**Description:** Проверка построения Config с числовым полем

**Preconditions:**
- XML содержит числовое поле (например, enemyLevel)

**Test Steps:**
1. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
2. Проверить, что числовое поле корректно преобразовано

**Expected Result:**
- Числовое поле содержит корректное значение
- Значение соответствует XML данным

---

## Test Case: TC-BUILDERS-007
**Title:** Build Config with string field type

**Category:** Positive

**Description:** Проверка построения Config со строковым полем

**Preconditions:**
- XML содержит строковое поле (например, igniteMode)

**Test Steps:**
1. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
2. Проверить, что строковое поле корректно преобразовано

**Expected Result:**
- Строковое поле содержит корректное значение
- Значение соответствует XML данным

---

## Test Case: TC-BUILDERS-008
**Title:** Build Config with no field type

**Category:** Edge Case

**Description:** Проверка построения Config с полем без указанного типа

**Preconditions:**
- XML содержит поле без атрибута типа

**Test Steps:**
1. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
2. Проверить обработку поля

**Expected Result:**
- Config объект создан успешно
- Поле обработано с дефолтным поведением

---

## Test Case: TC-BUILDERS-009
**Title:** Build ItemSet with valid items

**Category:** Positive

**Description:** Проверка построения ItemSet с валидными предметами

**Preconditions:**
- XML содержит валидные данные о предметах

**Test Steps:**
1. Вызвать `ItemSetBuilder.build(xml_root)`
2. Проверить структуру ItemSet

**Expected Result:**
- ItemSet объект создан успешно
- Предметы корректно обработаны

---

## Test Case: TC-BUILDERS-010
**Title:** Build ItemSet with empty items

**Category:** Edge Case

**Description:** Проверка построения ItemSet при отсутствии предметов

**Preconditions:**
- XML не содержит данных о предметах

**Test Steps:**
1. Вызвать `ItemSetBuilder.build(xml_root)` с XML без предметов
2. Проверить структуру ItemSet

**Expected Result:**
- ItemSet объект создан успешно
- ItemSet содержит пустые или дефолтные значения

---

## Test Case: TC-BUILDERS-011
**Title:** Build Stats with missing life attribute

**Category:** Edge Case

**Description:** Проверка построения Stats при отсутствии атрибута life

**Preconditions:**
- XML не содержит атрибут life

**Test Steps:**
1. Вызвать `StatsBuilder.build(xml_root)`
2. Проверить значение life

**Expected Result:**
- Stats объект создан успешно
- life равен None

---

## Test Case: TC-BUILDERS-012
**Title:** Build Stats with missing mana attribute

**Category:** Edge Case

**Description:** Проверка построения Stats при отсутствии атрибута mana

**Preconditions:**
- XML не содержит атрибут mana

**Test Steps:**
1. Вызвать `StatsBuilder.build(xml_root)`
2. Проверить значение mana

**Expected Result:**
- Stats объект создан успешно
- mana равен None

---

## Test Case: TC-BUILDERS-013
**Title:** Build Config with multiple input fields

**Category:** Positive

**Description:** Проверка построения Config с несколькими полями ввода

**Preconditions:**
- XML содержит несколько Input элементов

**Test Steps:**
1. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
2. Проверить все поля конфигурации

**Expected Result:**
- Config объект создан успешно
- Все поля корректно обработаны

---

## Test Case: TC-BUILDERS-014
**Title:** Build Config with invalid character_level

**Category:** Negative

**Description:** Проверка обработки невалидного character_level

**Preconditions:**
- character_level имеет невалидное значение

**Test Steps:**
1. Вызвать `ConfigBuilder.build(xml_root, character_level=invalid_value)`
2. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- Используется дефолтное значение или выбрасывается исключение

---

## Test Case: TC-BUILDERS-015
**Title:** Build ItemSet with multiple item sets

**Category:** Positive

**Description:** Проверка построения нескольких наборов предметов

**Preconditions:**
- XML содержит несколько наборов предметов

**Test Steps:**
1. Вызвать `ItemSetBuilder.build(xml_root)`
2. Проверить все наборы предметов

**Expected Result:**
- Все наборы предметов корректно обработаны
- Каждый набор содержит корректные данные
