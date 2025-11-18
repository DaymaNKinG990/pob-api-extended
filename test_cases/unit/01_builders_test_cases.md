# Builders Unit Test Cases

## Module: pobapi.builders

### Overview
Юнит-тест-кейсы для модуля builders, который содержит классы для построения объектов из XML данных. Тесты проверяют отдельные методы классов в изоляции.

---

## Test Case: TC-BUILDERS-001
**Title:** StatsBuilder.build() with valid player stats

**Category:** Positive

**Description:** Проверка метода StatsBuilder.build() при наличии валидных статистик игрока в XML

**Preconditions:**
- XML root содержит элемент Build с атрибутами life и mana

**Test Steps:**
1. Создать XML root с валидными статистиками
2. Вызвать `StatsBuilder.build(xml_root)`
3. Проверить значения stats.life и stats.mana

**Expected Result:**
- Метод возвращает объект Stats
- stats.life == 163.0
- stats.mana == 60.0

---

## Test Case: TC-BUILDERS-002
**Title:** StatsBuilder.build() with missing Build element

**Category:** Edge Case

**Description:** Проверка метода StatsBuilder.build() при отсутствии элемента Build в XML

**Preconditions:**
- XML root не содержит элемент Build

**Test Steps:**
1. Создать XML root без элемента Build
2. Вызвать `StatsBuilder.build(xml_root)`
3. Проверить значения stats.life и stats.mana

**Expected Result:**
- Метод возвращает объект Stats
- stats.life is None
- stats.mana is None

---

## Test Case: TC-BUILDERS-003
**Title:** StatsBuilder.build() with Build element but no stats

**Category:** Edge Case

**Description:** Проверка метода StatsBuilder.build() при наличии Build элемента, но без атрибутов статистик

**Preconditions:**
- XML root содержит элемент Build без атрибутов life и mana

**Test Steps:**
1. Создать XML root с Build элементом без статистик
2. Вызвать `StatsBuilder.build(xml_root)`
3. Проверить значения stats.life и stats.mana

**Expected Result:**
- Метод возвращает объект Stats
- stats.life is None
- stats.mana is None

---

## Test Case: TC-BUILDERS-004
**Title:** ConfigBuilder.build() with valid config values

**Category:** Positive

**Description:** Проверка метода ConfigBuilder.build() с валидными значениями конфигурации

**Preconditions:**
- XML root содержит элемент Config с Input элементами
- character_level предоставлен как параметр

**Test Steps:**
1. Создать XML root с валидной конфигурацией
2. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
3. Проверить значения config.enemy_level и config.is_stationary

**Expected Result:**
- Метод возвращает объект Config
- config.enemy_level == 84
- config.is_stationary is True

---

## Test Case: TC-BUILDERS-005
**Title:** ConfigBuilder.build() with empty config

**Category:** Edge Case

**Description:** Проверка метода ConfigBuilder.build() при отсутствии конфигурации в XML

**Preconditions:**
- XML root не содержит элемент Config

**Test Steps:**
1. Создать XML root без Config элемента
2. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
3. Проверить значения конфигурации

**Expected Result:**
- Метод возвращает объект Config
- Используются дефолтные значения
- config.enemy_level is not None

---

## Test Case: TC-BUILDERS-006
**Title:** ConfigBuilder.build() with boolean field type

**Category:** Positive

**Description:** Проверка метода ConfigBuilder.build() с boolean типом поля Input

**Preconditions:**
- XML root содержит Input элемент с атрибутом boolean="true"

**Test Steps:**
1. Создать XML root с Input name="conditionStationary" boolean="true"
2. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
3. Проверить значение config.is_stationary

**Expected Result:**
- Метод возвращает объект Config
- config.is_stationary is True

---

## Test Case: TC-BUILDERS-007
**Title:** ConfigBuilder.build() with number field type

**Category:** Positive

**Description:** Проверка метода ConfigBuilder.build() с числовым типом поля Input

**Preconditions:**
- XML root содержит Input элемент с атрибутом number="90"

**Test Steps:**
1. Создать XML root с Input name="enemyLevel" number="90"
2. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
3. Проверить значение config.enemy_level

**Expected Result:**
- Метод возвращает объект Config
- config.enemy_level == 90

---

## Test Case: TC-BUILDERS-008
**Title:** ConfigBuilder.build() with string field type

**Category:** Positive

**Description:** Проверка метода ConfigBuilder.build() со строковым типом поля Input

**Preconditions:**
- XML root содержит Input элемент с атрибутом string="average"

**Test Steps:**
1. Создать XML root с Input name="igniteMode" string="average"
2. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
3. Проверить значение config.ignite_mode

**Expected Result:**
- Метод возвращает объект Config
- config.ignite_mode == "Average"

---

## Test Case: TC-BUILDERS-009
**Title:** ConfigBuilder.build() with Input without field type

**Category:** Edge Case

**Description:** Проверка метода ConfigBuilder.build() с Input элементом без атрибутов boolean/number/string

**Preconditions:**
- XML root содержит Input элемент без атрибутов типа

**Test Steps:**
1. Создать XML root с Input name="enemyLevel" без атрибутов
2. Вызвать `ConfigBuilder.build(xml_root, character_level=1)`
3. Проверить наличие атрибута enemy_level

**Expected Result:**
- Метод возвращает объект Config
- hasattr(config, "enemy_level") is True

---

## Test Case: TC-BUILDERS-010
**Title:** ItemSetBuilder.build_all() with valid item sets

**Category:** Positive

**Description:** Проверка метода ItemSetBuilder.build_all() с валидными наборами предметов

**Preconditions:**
- XML root содержит элемент Items с ItemSet элементами

**Test Steps:**
1. Создать XML root с валидными наборами предметов
2. Вызвать `ItemSetBuilder.build_all(xml_root)`
3. Проверить количество и содержимое наборов

**Expected Result:**
- Метод возвращает список ItemSet объектов
- len(item_sets) == 1
- item_set.body_armour == 0
- item_set.helmet == 1

---

## Test Case: TC-BUILDERS-011
**Title:** ItemSetBuilder.build_all() with missing Items element

**Category:** Edge Case

**Description:** Проверка метода ItemSetBuilder.build_all() при отсутствии элемента Items

**Preconditions:**
- XML root не содержит элемент Items

**Test Steps:**
1. Создать XML root без Items элемента
2. Вызвать `ItemSetBuilder.build_all(xml_root)`
3. Проверить результат

**Expected Result:**
- Метод возвращает пустой список []
- len(item_sets) == 0

---

## Test Case: TC-BUILDERS-012
**Title:** ItemSetBuilder.build_all() with empty Items element

**Category:** Edge Case

**Description:** Проверка метода ItemSetBuilder.build_all() с пустым элементом Items

**Preconditions:**
- XML root содержит пустой элемент Items

**Test Steps:**
1. Создать XML root с пустым Items элементом
2. Вызвать `ItemSetBuilder.build_all(xml_root)`
3. Проверить результат

**Expected Result:**
- Метод возвращает пустой список []
- len(item_sets) == 0

---

## Test Case: TC-BUILDERS-013
**Title:** ItemSetBuilder._build_single() with empty slots

**Category:** Edge Case

**Description:** Проверка приватного метода ItemSetBuilder._build_single() с пустыми слотами

**Preconditions:**
- item_set_data является пустым словарем

**Test Steps:**
1. Создать пустой словарь item_set_data
2. Вызвать `ItemSetBuilder._build_single(item_set_data)`
3. Проверить значения слотов

**Expected Result:**
- Метод возвращает объект ItemSet
- item_set.body_armour is None
- item_set.helmet is None

---

## Test Case: TC-BUILDERS-014
**Title:** ConfigBuilder.build() with None character_level

**Category:** Edge Case

**Description:** Проверка метода ConfigBuilder.build() с None в качестве character_level

**Preconditions:**
- character_level=None передается в метод

**Test Steps:**
1. Создать XML root
2. Вызвать `ConfigBuilder.build(xml_root, character_level=None)`
3. Проверить обработку None значения

**Expected Result:**
- Метод обрабатывает None корректно
- Используется дефолтное значение или выбрасывается исключение

---

## Test Case: TC-BUILDERS-015
**Title:** StatsBuilder.build() with float stat values

**Category:** Positive

**Description:** Проверка метода StatsBuilder.build() с дробными значениями статистик

**Preconditions:**
- XML root содержит статистики с дробными значениями

**Test Steps:**
1. Создать XML root с life="163.5" и mana="60.5"
2. Вызвать `StatsBuilder.build(xml_root)`
3. Проверить типы и значения

**Expected Result:**
- Метод возвращает объект Stats
- stats.life == 163.5
- stats.mana == 60.5
