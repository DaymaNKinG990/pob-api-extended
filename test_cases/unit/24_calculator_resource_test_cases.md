# Calculator Resource Unit Test Cases

## Module: pobapi.calculator.resource

### Overview
Юнит-тест-кейсы для модуля calculator.resource, который отвечает за расчет ресурсов (мана, резервации и т.д.).

---

## Test Case: TC-CALC-RESOURCE-001
**Title:** ResourceCalculator.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации ResourceCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ResourceCalculator
2. Проверить инициализацию

**Expected Result:**
- resource_calculator.modifiers is not None

---

## Test Case: TC-CALC-RESOURCE-002
**Title:** ResourceCalculator.calculate_mana_cost() with no modifiers

**Category:** Positive

**Description:** Проверка метода calculate_mana_cost() без модификаторов

**Preconditions:**
- ResourceCalculator инициализирован

**Test Steps:**
1. Вызвать `resource_calculator.calculate_mana_cost("TestSkill")`
2. Проверить результат

**Expected Result:**
- result == 0.0
- Нет стоимости без модификаторов

---

## Test Case: TC-CALC-RESOURCE-003
**Title:** ResourceCalculator.calculate_mana_cost() with base cost

**Category:** Positive

**Description:** Проверка метода calculate_mana_cost() с базовой стоимостью

**Preconditions:**
- Модификатор базовой стоимости добавлен

**Test Steps:**
1. Добавить модификатор TestSkillManaCost
2. Вызвать `calculate_mana_cost("TestSkill")`
3. Проверить результат

**Expected Result:**
- result == 50.0 для примера
- Базовая стоимость применена

---

## Test Case: TC-CALC-RESOURCE-004
**Title:** ResourceCalculator.calculate_mana_cost() with multiplier

**Category:** Positive

**Description:** Проверка метода calculate_mana_cost() с множителем стоимости

**Preconditions:**
- Модификаторы базовой стоимости и множителя добавлены

**Test Steps:**
1. Добавить модификаторы TestSkillManaCost и ManaCost
2. Вызвать `calculate_mana_cost("TestSkill")`
3. Проверить результат

**Expected Result:**
- Стоимость рассчитана с учетом множителя
- result == 125.0 для примера (50 * 2.5)

---

## Test Case: TC-CALC-RESOURCE-005
**Title:** ResourceCalculator.calculate_mana_cost_per_second() for attack

**Category:** Positive

**Description:** Проверка метода calculate_mana_cost_per_second() для атакующего скилла

**Preconditions:**
- Модификаторы для attack skill добавлены

**Test Steps:**
1. Добавить модификаторы TestSkillManaCost, TestSkillIsAttack, AttackSpeed
2. Вызвать `calculate_mana_cost_per_second("TestSkill")`
3. Проверить результат

**Expected Result:**
- Mana cost per second рассчитан корректно
- result == 30.0 для примера (10 * 3.0)

---

## Test Case: TC-CALC-RESOURCE-006
**Title:** ResourceCalculator.calculate_mana_cost_per_second() for spell

**Category:** Positive

**Description:** Проверка метода calculate_mana_cost_per_second() для заклинания

**Preconditions:**
- Модификаторы для spell skill добавлены

**Test Steps:**
1. Добавить модификаторы TestSkillManaCost, CastSpeed
2. Вызвать `calculate_mana_cost_per_second("TestSkill")`
3. Проверить результат

**Expected Result:**
- Mana cost per second рассчитан корректно
- result == 80.0 для примера (20 * 4.0)

---

## Test Case: TC-CALC-RESOURCE-007
**Title:** ResourceCalculator.calculate_life_reservation()

**Category:** Positive

**Description:** Проверка метода calculate_life_reservation() для расчета резервации жизни

**Preconditions:**
- Модификатор LifeReservation добавлен

**Test Steps:**
1. Добавить модификатор LifeReservation
2. Вызвать `calculate_life_reservation()`
3. Проверить результат

**Expected Result:**
- result == 30.0 для примера
- Резервация жизни рассчитана корректно

---

## Test Case: TC-CALC-RESOURCE-008
**Title:** ResourceCalculator.calculate_mana_reservation()

**Category:** Positive

**Description:** Проверка метода calculate_mana_reservation() для расчета резервации маны

**Preconditions:**
- Модификатор ManaReservation добавлен

**Test Steps:**
1. Добавить модификатор ManaReservation
2. Вызвать `calculate_mana_reservation()`
3. Проверить результат

**Expected Result:**
- result == 50.0 для примера
- Резервация маны рассчитана корректно

---

## Test Case: TC-CALC-RESOURCE-009
**Title:** ResourceCalculator.calculate_unreserved_life() with no reservation

**Category:** Positive

**Description:** Проверка метода calculate_unreserved_life() без резервации

**Preconditions:**
- Нет резервации жизни

**Test Steps:**
1. Вызвать `calculate_unreserved_life(total_life=100.0)`
2. Проверить результат

**Expected Result:**
- result == 100.0
- Вся жизнь доступна

---

## Test Case: TC-CALC-RESOURCE-010
**Title:** ResourceCalculator.calculate_unreserved_life() with reservation

**Category:** Positive

**Description:** Проверка метода calculate_unreserved_life() с резервацией

**Preconditions:**
- Модификатор LifeReservation добавлен

**Test Steps:**
1. Добавить модификатор LifeReservation
2. Вызвать `calculate_unreserved_life(total_life=100.0)`
3. Проверить результат

**Expected Result:**
- result == 70.0 для примера (100 - 30)
- Нерезервированная жизнь рассчитана корректно

---

## Test Case: TC-CALC-RESOURCE-011
**Title:** ResourceCalculator.calculate_unreserved_life() over reservation

**Category:** Edge Case

**Description:** Проверка метода calculate_unreserved_life() при превышении резервации

**Preconditions:**
- Резервация больше total_life

**Test Steps:**
1. Добавить модификатор LifeReservation > total_life
2. Вызвать `calculate_unreserved_life(total_life=100.0)`
3. Проверить результат

**Expected Result:**
- result == 0.0
- Не может быть отрицательным

---

## Test Case: TC-CALC-RESOURCE-012
**Title:** ResourceCalculator.calculate_unreserved_mana() with no reservation

**Category:** Positive

**Description:** Проверка метода calculate_unreserved_mana() без резервации

**Preconditions:**
- Нет резервации маны

**Test Steps:**
1. Вызвать `calculate_unreserved_mana(total_mana=100.0)`
2. Проверить результат

**Expected Result:**
- result == 100.0
- Вся мана доступна

---

## Test Case: TC-CALC-RESOURCE-013
**Title:** ResourceCalculator.calculate_unreserved_mana() with reservation

**Category:** Positive

**Description:** Проверка метода calculate_unreserved_mana() с резервацией

**Preconditions:**
- Модификатор ManaReservation добавлен

**Test Steps:**
1. Добавить модификатор ManaReservation
2. Вызвать `calculate_unreserved_mana(total_mana=100.0)`
3. Проверить результат

**Expected Result:**
- result == 50.0 для примера (100 - 50)
- Нерезервированная мана рассчитана корректно

---

## Test Case: TC-CALC-RESOURCE-014
**Title:** ResourceCalculator.calculate_net_life_recovery()

**Category:** Positive

**Description:** Проверка метода calculate_net_life_recovery() для расчета чистого восстановления жизни

**Preconditions:**
- Модификаторы recovery и degen добавлены

**Test Steps:**
1. Добавить модификаторы LifeRecovery и LifeDegen
2. Вызвать `calculate_net_life_recovery()`
3. Проверить результат

**Expected Result:**
- Чистое восстановление рассчитано корректно
- result = recovery - degen

---

## Test Case: TC-CALC-RESOURCE-015
**Title:** ResourceCalculator.calculate_net_mana_recovery()

**Category:** Positive

**Description:** Проверка метода calculate_net_mana_recovery() для расчета чистого восстановления маны

**Preconditions:**
- Модификаторы recovery и degen добавлены

**Test Steps:**
1. Добавить модификаторы ManaRecovery и ManaDegen
2. Вызвать `calculate_net_mana_recovery()`
3. Проверить результат

**Expected Result:**
- Чистое восстановление рассчитано корректно
- result = recovery - degen

---

## Test Case: TC-CALC-RESOURCE-016
**Title:** ResourceCalculator.calculate_mana_cost() with reduced cost

**Category:** Positive

**Description:** Проверка метода calculate_mana_cost() с reduced cost модификаторами

**Preconditions:**
- Модификаторы reduced cost добавлены

**Test Steps:**
1. Добавить модификаторы базовой стоимости и reduced cost
2. Вызвать `calculate_mana_cost("TestSkill")`
3. Проверить результат

**Expected Result:**
- Стоимость уменьшена корректно
- Reduced cost применен

---

## Test Case: TC-CALC-RESOURCE-017
**Title:** ResourceCalculator.calculate_mana_cost() with increased cost

**Category:** Positive

**Description:** Проверка метода calculate_mana_cost() с increased cost модификаторами

**Preconditions:**
- Модификаторы increased cost добавлены

**Test Steps:**
1. Добавить модификаторы базовой стоимости и increased cost
2. Вызвать `calculate_mana_cost("TestSkill")`
3. Проверить результат

**Expected Result:**
- Стоимость увеличена корректно
- Increased cost применен

---

## Test Case: TC-CALC-RESOURCE-018
**Title:** ResourceCalculator.calculate_unreserved_life() with zero total

**Category:** Edge Case

**Description:** Проверка метода calculate_unreserved_life() с нулевым total_life

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_unreserved_life(total_life=0.0)`
2. Проверить результат

**Expected Result:**
- result == 0.0
- Нулевое значение обработано корректно
