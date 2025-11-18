# Calculator Engine Unit Test Cases

## Module: pobapi.calculator.engine

### Overview
Юнит-тест-кейсы для модуля CalculationEngine, который является основным движком расчетов.

---

## Test Case: TC-CALC-ENGINE-001
**Title:** CalculationEngine.__init__() default initialization

**Category:** Positive

**Description:** Проверка инициализации CalculationEngine с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `CalculationEngine()`
2. Проверить инициализацию всех компонентов

**Expected Result:**
- engine.modifiers is not None
- engine.damage_calc is not None
- engine.defense_calc is not None
- engine.resource_calc is not None
- engine.skill_stats_calc is not None
- engine.minion_calc is not None
- engine.party_calc is not None

---

## Test Case: TC-CALC-ENGINE-002
**Title:** CalculationEngine.__init__() with custom ModifierSystem

**Category:** Positive

**Description:** Проверка инициализации CalculationEngine с кастомным ModifierSystem (покрывает строки 106-121)

**Preconditions:**
- Кастомный ModifierSystem создан

**Test Steps:**
1. Создать кастомный ModifierSystem
2. Вызвать `CalculationEngine(modifier_system=custom_system)`
3. Проверить, что все калькуляторы используют кастомный ModifierSystem

**Expected Result:**
- engine.modifiers == custom_system
- Все калькуляторы используют один и тот же ModifierSystem

---

## Test Case: TC-CALC-ENGINE-003
**Title:** CalculationEngine.load_build() with empty build

**Category:** Positive

**Description:** Проверка метода load_build() с пустым билдом

**Preconditions:**
- Пустой билд создан

**Test Steps:**
1. Создать пустой билд
2. Вызвать `engine.load_build(build)`
3. Проверить состояние

**Expected Result:**
- Исключение не выбрасывается
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-004
**Title:** CalculationEngine.load_build() with passive tree

**Category:** Positive

**Description:** Проверка метода load_build() с пассивным деревом

**Preconditions:**
- Билд содержит дерево с нодами

**Test Steps:**
1. Создать билд с деревом
2. Вызвать `engine.load_build(build)`
3. Проверить загрузку модификаторов дерева

**Expected Result:**
- Модификаторы дерева загружены
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-005
**Title:** CalculationEngine.load_build() with items

**Category:** Positive

**Description:** Проверка метода load_build() с предметами

**Preconditions:**
- Билд содержит предметы

**Test Steps:**
1. Создать билд с предметами
2. Вызвать `engine.load_build(build)`
3. Проверить загрузку модификаторов предметов

**Expected Result:**
- Модификаторы предметов загружены
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-006
**Title:** CalculationEngine.load_build() with skills

**Category:** Positive

**Description:** Проверка метода load_build() со скиллами

**Preconditions:**
- Билд содержит группы скиллов

**Test Steps:**
1. Создать билд со скиллами
2. Вызвать `engine.load_build(build)`
3. Проверить загрузку модификаторов скиллов

**Expected Result:**
- Модификаторы скиллов загружены
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-007
**Title:** CalculationEngine.load_build() with config

**Category:** Positive

**Description:** Проверка метода load_build() с конфигурацией

**Preconditions:**
- Билд содержит конфигурацию

**Test Steps:**
1. Создать билд с конфигом
2. Вызвать `engine.load_build(build)`
3. Проверить загрузку модификаторов конфига

**Expected Result:**
- Модификаторы конфига загружены
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-008
**Title:** CalculationEngine.load_build() with invalid jewel socket indices

**Category:** Edge Case

**Description:** Проверка метода load_build() с невалидными индексами сокетов джемов

**Preconditions:**
- Дерево содержит невалидные индексы сокетов

**Test Steps:**
1. Создать дерево с невалидным положительным индексом
2. Вызвать `engine.load_build(build)`
3. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-009
**Title:** CalculationEngine.load_build() with negative jewel socket index

**Category:** Edge Case

**Description:** Проверка метода load_build() с отрицательным индексом сокета джема

**Preconditions:**
- Дерево содержит отрицательный индекс сокета

**Test Steps:**
1. Создать дерево с отрицательным индексом
2. Вызвать `engine.load_build(build)`
3. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-010
**Title:** CalculationEngine.load_build() with TypeError in jewel socket

**Category:** Edge Case

**Description:** Проверка метода load_build() с TypeError в парсинге сокета джема

**Preconditions:**
- Дерево содержит сокет с неверным типом

**Test Steps:**
1. Создать дерево с сокетом типа string
2. Вызвать `engine.load_build(build)`
3. Проверить обработку TypeError

**Expected Result:**
- TypeError обработан корректно
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-011
**Title:** CalculationEngine.load_build() aggregates modifiers from multiple trees

**Category:** Positive

**Description:** Проверка метода load_build() для агрегации модификаторов из нескольких деревьев

**Preconditions:**
- Билд содержит несколько деревьев

**Test Steps:**
1. Создать билд с несколькими деревьями
2. Вызвать `engine.load_build(build)`
3. Проверить агрегацию модификаторов

**Expected Result:**
- Модификаторы из всех деревьев загружены
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-012
**Title:** CalculationEngine.load_build() with trees containing jewel sockets

**Category:** Positive

**Description:** Проверка метода load_build() с деревьями, содержащими сокеты джемов

**Preconditions:**
- Дерево содержит сокеты джемов

**Test Steps:**
1. Создать дерево с сокетами джемов
2. Создать предметы-джемы
3. Вызвать `engine.load_build(build)`
4. Проверить парсинг сокетов

**Expected Result:**
- Сокеты джемов обработаны
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-013
**Title:** CalculationEngine.load_build() handles invalid skill groups

**Category:** Edge Case

**Description:** Проверка метода load_build() для обработки невалидных групп скиллов (покрывает строки 620-621)

**Preconditions:**
- Билд содержит некорректные данные в skill_groups

**Test Steps:**
1. Создать билд с некорректными skill_groups
2. Вызвать `engine.load_build(build)`
3. Проверить обработку ошибок

**Expected Result:**
- Ошибки обработаны корректно
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-014
**Title:** CalculationEngine.load_build() with keystones

**Category:** Positive

**Description:** Проверка метода load_build() с кистоунами

**Preconditions:**
- Билд содержит кистоуны

**Test Steps:**
1. Создать билд с кистоунами
2. Вызвать `engine.load_build(build)`
3. Проверить загрузку модификаторов кистоунов

**Expected Result:**
- Модификаторы кистоунов загружены
- parse_keystone вызван для каждого кистоуна

---

## Test Case: TC-CALC-ENGINE-015
**Title:** CalculationEngine.load_build() with missing attributes

**Category:** Edge Case

**Description:** Проверка метода load_build() с билдом без ожидаемых атрибутов

**Preconditions:**
- Билд не содержит ожидаемых атрибутов

**Test Steps:**
1. Создать объект без атрибутов
2. Вызвать `engine.load_build(build)`
3. Проверить обработку отсутствующих атрибутов

**Expected Result:**
- Отсутствующие атрибуты обработаны корректно
- engine.modifiers is not None

---

## Test Case: TC-CALC-ENGINE-016
**Title:** CalculationEngine.calculate_all_stats() with valid build

**Category:** Positive

**Description:** Проверка метода calculate_all_stats() с валидным билдом

**Preconditions:**
- Билд загружен в engine

**Test Steps:**
1. Загрузить билд в engine
2. Вызвать `engine.calculate_all_stats()`
3. Проверить результаты расчетов

**Expected Result:**
- Все статистики рассчитаны
- Результаты валидны

---

## Test Case: TC-CALC-ENGINE-017
**Title:** CalculationEngine.calculate_all_stats() handles missing skill_groups attribute

**Category:** Edge Case

**Description:** Проверка метода calculate_all_stats() для обработки отсутствующего атрибута skill_groups

**Preconditions:**
- Билд не содержит атрибут skill_groups

**Test Steps:**
1. Создать билд без skill_groups
2. Загрузить билд
3. Вызвать `engine.calculate_all_stats()`
4. Проверить обработку

**Expected Result:**
- Отсутствующий атрибут обработан корректно
- Расчеты выполнены

---

## Test Case: TC-CALC-ENGINE-018
**Title:** CalculationEngine with party members

**Category:** Positive

**Description:** Проверка CalculationEngine с членами партии

**Preconditions:**
- Билд содержит party_members

**Test Steps:**
1. Создать билд с party_members
2. Вызвать `engine.load_build(build)`
3. Проверить загрузку партийных модификаторов

**Expected Result:**
- Партийные модификаторы загружены
- engine.modifiers is not None
