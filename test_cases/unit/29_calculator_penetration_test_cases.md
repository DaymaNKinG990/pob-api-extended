# Calculator Penetration Unit Test Cases

## Module: pobapi.calculator.penetration

### Overview
Юнит-тест-кейсы для модуля calculator.penetration, который отвечает за расчет проникновения сопротивлений.

---

## Test Case: TC-CALC-PENETRATION-001
**Title:** PenetrationCalculator.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации PenetrationCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать PenetrationCalculator
2. Проверить инициализацию

**Expected Result:**
- penetration_calculator.modifiers is not None

---

## Test Case: TC-CALC-PENETRATION-002
**Title:** PenetrationCalculator.calculate_effective_resistance() base resistance only

**Category:** Positive

**Description:** Проверка метода calculate_effective_resistance() только с базовым сопротивлением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_effective_resistance(base_res=75.0, reduction=0.0, penetration=0.0)`
2. Проверить результат

**Expected Result:**
- result == 0.75
- Базовое сопротивление возвращено без изменений

---

## Test Case: TC-CALC-PENETRATION-003
**Title:** PenetrationCalculator.calculate_effective_resistance() with reduction

**Category:** Positive

**Description:** Проверка метода calculate_effective_resistance() с reduction

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_effective_resistance(base_res=75.0, reduction=-44.0, penetration=0.0)`
2. Проверить результат

**Expected Result:**
- result == 0.31 (75% - 44% = 31%)
- Reduction применен корректно

---

## Test Case: TC-CALC-PENETRATION-004
**Title:** PenetrationCalculator.calculate_effective_resistance() with penetration

**Category:** Positive

**Description:** Проверка метода calculate_effective_resistance() с penetration

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_effective_resistance(base_res=75.0, reduction=0.0, penetration=37.0)`
2. Проверить результат

**Expected Result:**
- result == 0.38 (75% - 37% = 38%)
- Penetration применен корректно

---

## Test Case: TC-CALC-PENETRATION-005
**Title:** PenetrationCalculator.calculate_effective_resistance() with reduction and penetration

**Category:** Positive

**Description:** Проверка метода calculate_effective_resistance() с reduction и penetration

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_effective_resistance(base_res=75.0, reduction=-44.0, penetration=37.0)`
2. Проверить результат

**Expected Result:**
- result == -0.06 (75% - 44% - 37% = -6%)
- Оба модификатора применены корректно

---

## Test Case: TC-CALC-PENETRATION-006
**Title:** PenetrationCalculator.calculate_effective_resistance() zero base

**Category:** Edge Case

**Description:** Проверка метода calculate_effective_resistance() с нулевым базовым сопротивлением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_effective_resistance(base_res=0.0, reduction=0.0, penetration=0.0)`
2. Проверить результат

**Expected Result:**
- result == 0.0
- Нулевое сопротивление обработано корректно

---

## Test Case: TC-CALC-PENETRATION-007
**Title:** PenetrationCalculator.calculate_effective_resistance() over-penetration

**Category:** Edge Case

**Description:** Проверка метода calculate_effective_resistance() с over-penetration

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_effective_resistance(base_res=75.0, reduction=0.0, penetration=100.0)`
2. Проверить результат

**Expected Result:**
- result == -0.25 (75% - 100% = -25%)
- Over-penetration обработан корректно

---

## Test Case: TC-CALC-PENETRATION-008
**Title:** PenetrationCalculator.calculate_effective_resistance() minimum cap

**Category:** Edge Case

**Description:** Проверка метода calculate_effective_resistance() для минимального cap (-200%)

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_effective_resistance(base_res=0.0, reduction=-100.0, penetration=150.0)`
2. Проверить результат

**Expected Result:**
- result == -2.0 (capped at -200%)
- Минимальный cap применен корректно

---

## Test Case: TC-CALC-PENETRATION-009
**Title:** PenetrationCalculator.calculate_fire_resistance() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_fire_resistance() с модификаторами

**Preconditions:**
- Модификаторы EnemyFireResistance и FirePenetration добавлены

**Test Steps:**
1. Добавить модификаторы EnemyFireResistance и FirePenetration
2. Вызвать `calculate_fire_resistance(75.0)`
3. Проверить результат

**Expected Result:**
- result == -0.06 (75% - 44% - 37% = -6%)
- Модификаторы применены корректно

---

## Test Case: TC-CALC-PENETRATION-010
**Title:** PenetrationCalculator.calculate_cold_resistance() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_cold_resistance() с модификаторами

**Preconditions:**
- Модификаторы EnemyColdResistance и ColdPenetration добавлены

**Test Steps:**
1. Добавить модификаторы EnemyColdResistance и ColdPenetration
2. Вызвать `calculate_cold_resistance(75.0)`
3. Проверить результат

**Expected Result:**
- Результат рассчитан корректно
- Модификаторы применены

---

## Test Case: TC-CALC-PENETRATION-011
**Title:** PenetrationCalculator.calculate_lightning_resistance() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_lightning_resistance() с модификаторами

**Preconditions:**
- Модификаторы EnemyLightningResistance и LightningPenetration добавлены

**Test Steps:**
1. Добавить модификаторы EnemyLightningResistance и LightningPenetration
2. Вызвать `calculate_lightning_resistance(75.0)`
3. Проверить результат

**Expected Result:**
- Результат рассчитан корректно
- Модификаторы применены

---

## Test Case: TC-CALC-PENETRATION-012
**Title:** PenetrationCalculator.calculate_chaos_resistance() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_chaos_resistance() с модификаторами

**Preconditions:**
- Модификаторы EnemyChaosResistance и ChaosPenetration добавлены

**Test Steps:**
1. Добавить модификаторы EnemyChaosResistance и ChaosPenetration
2. Вызвать `calculate_chaos_resistance(75.0)`
3. Проверить результат

**Expected Result:**
- Результат рассчитан корректно
- Модификаторы применены

---

## Test Case: TC-CALC-PENETRATION-013
**Title:** PenetrationCalculator.calculate_fire_resistance() no modifiers

**Category:** Positive

**Description:** Проверка метода calculate_fire_resistance() без модификаторов

**Preconditions:**
- Нет модификаторов

**Test Steps:**
1. Вызвать `calculate_fire_resistance(75.0)`
2. Проверить результат

**Expected Result:**
- result == 0.75
- Базовое сопротивление возвращено
