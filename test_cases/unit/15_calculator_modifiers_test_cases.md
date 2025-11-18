# Calculator Modifiers Unit Test Cases

## Module: pobapi.calculator.modifiers

### Overview
Юнит-тест-кейсы для модуля modifiers, который содержит систему модификаторов.

---

## Test Case: TC-CALC-MODIFIERS-001
**Title:** ModifierSystem.__init__() default initialization

**Category:** Positive

**Description:** Проверка инициализации ModifierSystem с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModifierSystem()`
2. Проверить инициализацию

**Expected Result:**
- modifier_system._modifiers == []

---

## Test Case: TC-CALC-MODIFIERS-002
**Title:** ModifierSystem.add_modifier() with single modifier

**Category:** Positive

**Description:** Проверка метода add_modifier() для добавления одного модификатора

**Preconditions:**
- ModifierSystem инициализирован
- Валидный Modifier создан

**Test Steps:**
1. Создать валидный Modifier
2. Вызвать `modifier_system.add_modifier(mod)`
3. Проверить добавление

**Expected Result:**
- len(modifier_system._modifiers) == 1
- modifier_system._modifiers[0] == mod

---

## Test Case: TC-CALC-MODIFIERS-003
**Title:** ModifierSystem.add_modifiers() with multiple modifiers

**Category:** Positive

**Description:** Проверка метода add_modifiers() для добавления нескольких модификаторов

**Preconditions:**
- ModifierSystem инициализирован
- Список модификаторов создан

**Test Steps:**
1. Создать список модификаторов
2. Вызвать `modifier_system.add_modifiers(modifiers)`
3. Проверить добавление

**Expected Result:**
- len(modifier_system._modifiers) == len(modifiers)
- Все модификаторы добавлены

---

## Test Case: TC-CALC-MODIFIERS-004
**Title:** ModifierSystem.get_modifiers() with empty system

**Category:** Edge Case

**Description:** Проверка метода get_modifiers() при отсутствии модификаторов

**Preconditions:**
- ModifierSystem инициализирован

**Test Steps:**
1. Вызвать `modifier_system.get_modifiers("Life")`
2. Проверить результат

**Expected Result:**
- Возвращается пустой список
- mods == []

---

## Test Case: TC-CALC-MODIFIERS-005
**Title:** ModifierSystem.get_modifiers() by stat name

**Category:** Positive

**Description:** Проверка метода get_modifiers() для получения модификаторов по имени стата

**Preconditions:**
- ModifierSystem содержит модификаторы для разных статов

**Test Steps:**
1. Добавить модификаторы для "Life" и "Mana"
2. Вызвать `modifier_system.get_modifiers("Life")`
3. Проверить результат

**Expected Result:**
- Возвращаются только модификаторы для "Life"
- len(mods) == количество модификаторов для "Life"
- all(m.stat == "Life" for m in mods)

---

## Test Case: TC-CALC-MODIFIERS-006
**Title:** ModifierSystem.get_modifiers() with conditions

**Category:** Positive

**Description:** Проверка метода get_modifiers() с условиями

**Preconditions:**
- ModifierSystem содержит модификатор с условиями

**Test Steps:**
1. Добавить модификатор с условием on_full_life
2. Вызвать `modifier_system.get_modifiers("Life", {"current_life": 100.0, "max_life": 100.0})`
3. Проверить результат

**Expected Result:**
- Модификатор возвращается когда условие выполнено
- len(mods) == 1 когда условие выполнено
- len(mods) == 0 когда условие не выполнено

---

## Test Case: TC-CALC-MODIFIERS-007
**Title:** ModifierSystem.calculate_stat() with flat modifiers

**Category:** Positive

**Description:** Проверка метода calculate_stat() с flat модификаторами

**Preconditions:**
- ModifierSystem содержит flat модификатор

**Test Steps:**
1. Добавить flat модификатор
2. Вызвать `modifier_system.calculate_stat("Life", base_value)`
3. Проверить результат

**Expected Result:**
- result == base_value + flat_value
- Расчет корректен

---

## Test Case: TC-CALC-MODIFIERS-008
**Title:** ModifierSystem.calculate_stat() with increased modifiers

**Category:** Positive

**Description:** Проверка метода calculate_stat() с increased модификаторами

**Preconditions:**
- ModifierSystem содержит increased модификатор

**Test Steps:**
1. Добавить increased модификатор
2. Вызвать `modifier_system.calculate_stat("Life", base_value)`
3. Проверить результат

**Expected Result:**
- result == base_value * (1 + increased/100)
- Расчет корректен

---

## Test Case: TC-CALC-MODIFIERS-009
**Title:** ModifierSystem.calculate_stat() with more modifiers

**Category:** Positive

**Description:** Проверка метода calculate_stat() с more модификаторами

**Preconditions:**
- ModifierSystem содержит more модификатор

**Test Steps:**
1. Добавить more модификатор
2. Вызвать `modifier_system.calculate_stat("Life", base_value)`
3. Проверить результат

**Expected Result:**
- result == base_value * (1 + more/100)
- Расчет корректен

---

## Test Case: TC-CALC-MODIFIERS-010
**Title:** ModifierSystem.calculate_stat() with less modifiers

**Category:** Positive

**Description:** Проверка метода calculate_stat() с less модификаторами

**Preconditions:**
- ModifierSystem содержит less модификатор

**Test Steps:**
1. Добавить less модификатор
2. Вызвать `modifier_system.calculate_stat("Life", base_value)`
3. Проверить результат

**Expected Result:**
- result == base_value * (1 - less/100)
- Расчет корректен

---

## Test Case: TC-CALC-MODIFIERS-011
**Title:** Modifier.applies() without conditions

**Category:** Positive

**Description:** Проверка метода applies() для модификатора без условий (покрывает строку 100)

**Preconditions:**
- Modifier без условий создан

**Test Steps:**
1. Создать Modifier без conditions
2. Вызвать `modifier.applies({})`
3. Проверить результат

**Expected Result:**
- Метод возвращает True
- Модификатор всегда применяется

---

## Test Case: TC-CALC-MODIFIERS-012
**Title:** Modifier.applies() with conditions using ConditionEvaluator

**Category:** Positive

**Description:** Проверка метода applies() для модификатора с условиями через ConditionEvaluator (покрывает строки 111-113)

**Preconditions:**
- Modifier с условиями создан

**Test Steps:**
1. Создать Modifier с условиями
2. Вызвать `modifier.applies(context)`
3. Проверить использование ConditionEvaluator

**Expected Result:**
- ConditionEvaluator используется для проверки условий
- Результат зависит от выполнения условий

---

## Test Case: TC-CALC-MODIFIERS-013
**Title:** ModifierSystem.calculate_stat() removes per-attribute modifier from applicable

**Category:** Positive

**Description:** Проверка метода calculate_stat() для удаления per-attribute модификатора из applicable (покрывает строку 203)

**Preconditions:**
- ModifierSystem содержит per-attribute модификатор

**Test Steps:**
1. Добавить per-attribute модификатор (например, LifePerStrength)
2. Вызвать `modifier_system.calculate_stat("Life", base_value)`
3. Проверить удаление из applicable_mods

**Expected Result:**
- Per-attribute модификатор удален из applicable_mods при расчете производного стата
- Расчет корректен

---

## Test Case: TC-CALC-MODIFIERS-014
**Title:** ModifierSystem.calculate_stat() with multiple modifier types

**Category:** Positive

**Description:** Проверка метода calculate_stat() с несколькими типами модификаторов

**Preconditions:**
- ModifierSystem содержит модификаторы разных типов

**Test Steps:**
1. Добавить flat, increased и more модификаторы
2. Вызвать `modifier_system.calculate_stat("Life", base_value)`
3. Проверить результат

**Expected Result:**
- Все типы модификаторов применены корректно
- Порядок применения: flat → increased → more
- Результат корректен

---

## Test Case: TC-CALC-MODIFIERS-015
**Title:** ModifierSystem.get_modifiers() excludes non-applicable modifiers

**Category:** Positive

**Description:** Проверка метода get_modifiers() для исключения неприменимых модификаторов

**Preconditions:**
- ModifierSystem содержит модификаторы с условиями

**Test Steps:**
1. Добавить модификатор с условием
2. Вызвать `get_modifiers()` с контекстом, где условие не выполнено
3. Проверить результат

**Expected Result:**
- Неприменимые модификаторы не возвращаются
- Только применимые модификаторы в результате

---

## Test Case: TC-CALC-MODIFIERS-016
**Title:** ModifierSystem.calculate_stat() with zero base value

**Category:** Edge Case

**Description:** Проверка метода calculate_stat() с нулевым базовым значением

**Preconditions:**
- ModifierSystem содержит модификаторы

**Test Steps:**
1. Вызвать `modifier_system.calculate_stat("Life", 0.0)`
2. Проверить результат

**Expected Result:**
- Результат корректен
- Flat модификаторы применяются к нулю

---

## Test Case: TC-CALC-MODIFIERS-017
**Title:** ModifierSystem.calculate_stat() with negative modifiers

**Category:** Edge Case

**Description:** Проверка метода calculate_stat() с отрицательными модификаторами

**Preconditions:**
- ModifierSystem содержит отрицательные модификаторы

**Test Steps:**
1. Добавить отрицательный increased модификатор
2. Вызвать `modifier_system.calculate_stat("Life", base_value)`
3. Проверить результат

**Expected Result:**
- Отрицательные модификаторы обработаны корректно
- Результат может быть меньше базового значения

---

## Test Case: TC-CALC-MODIFIERS-018
**Title:** ModifierSystem with complex condition evaluation

**Category:** Positive

**Description:** Проверка ModifierSystem со сложной оценкой условий

**Preconditions:**
- ModifierSystem содержит модификаторы с множественными условиями

**Test Steps:**
1. Добавить модификаторы с несколькими условиями
2. Вызвать `get_modifiers()` с различными контекстами
3. Проверить результаты

**Expected Result:**
- Сложные условия оценены корректно
- Только применимые модификаторы возвращаются
