# Calculator Conditional Unit Test Cases

## Module: pobapi.calculator.conditional

### Overview
Юнит-тест-кейсы для модуля calculator.conditional, который отвечает за оценку условных модификаторов.

---

## Test Case: TC-CALC-CONDITIONAL-001
**Title:** ConditionEvaluator.evaluate_condition() on_full_life true

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_full_life при полной жизни

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_life=100.0, max_life=100.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_full_life", context)`
3. Проверить результат

**Expected Result:**
- result == True
- Условие выполнено

---

## Test Case: TC-CALC-CONDITIONAL-002
**Title:** ConditionEvaluator.evaluate_condition() on_full_life threshold

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_full_life с порогом 99%

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_life=99.0, max_life=100.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_full_life", context)`
3. Проверить результат

**Expected Result:**
- result == True (99% threshold)
- Порог учтен

---

## Test Case: TC-CALC-CONDITIONAL-003
**Title:** ConditionEvaluator.evaluate_condition() on_full_life false

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_full_life при неполной жизни

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_life=98.0, max_life=100.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_full_life", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено

---

## Test Case: TC-CALC-CONDITIONAL-004
**Title:** ConditionEvaluator.evaluate_condition() on_low_life true

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_low_life при низкой жизни

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_life=35.0, max_life=100.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_low_life", context)`
3. Проверить результат

**Expected Result:**
- result == True (35% threshold)
- Условие выполнено

---

## Test Case: TC-CALC-CONDITIONAL-005
**Title:** ConditionEvaluator.evaluate_condition() on_low_life false

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_low_life при высокой жизни

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_life=36.0, max_life=100.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_low_life", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено

---

## Test Case: TC-CALC-CONDITIONAL-006
**Title:** ConditionEvaluator.evaluate_condition() on_full_mana

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_full_mana с конкретными числовыми значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_mana=100.0, max_mana=100.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_full_mana", context)`
3. Проверить, что результат равен True
4. Создать контекст с current_mana=50.0, max_mana=100.0
5. Вызвать `ConditionEvaluator.evaluate_condition("on_full_mana", context)`
6. Проверить, что результат равен False

**Expected Result:**
- При current_mana=100.0 и max_mana=100.0 метод возвращает True
- При current_mana=50.0 и max_mana=100.0 метод возвращает False
- Условие оценено правильно для обоих случаев

---

## Test Case: TC-CALC-CONDITIONAL-007
**Title:** ConditionEvaluator.evaluate_condition() on_low_mana

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_low_mana с конкретными числовыми значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_mana=50.0, max_mana=100.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_low_mana", context)`
3. Проверить, что результат равен True
4. Создать контекст с current_mana=100.0, max_mana=100.0
5. Вызвать `ConditionEvaluator.evaluate_condition("on_low_mana", context)`
6. Проверить, что результат равен False

**Expected Result:**
- При current_mana=50.0 и max_mana=100.0 метод возвращает True
- При current_mana=100.0 и max_mana=100.0 метод возвращает False
- Условие оценено правильно для обоих случаев

---

## Test Case: TC-CALC-CONDITIONAL-008
**Title:** ConditionEvaluator.evaluate_condition() on_full_energy_shield

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_full_energy_shield с конкретными числовыми значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_energy_shield=50.0, max_energy_shield=50.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_full_energy_shield", context)`
3. Проверить, что результат равен True
4. Создать контекст с current_energy_shield=0.0, max_energy_shield=50.0
5. Вызвать `ConditionEvaluator.evaluate_condition("on_full_energy_shield", context)`
6. Проверить, что результат равен False

**Expected Result:**
- При current_energy_shield=50.0 и max_energy_shield=50.0 метод возвращает True
- При current_energy_shield=0.0 и max_energy_shield=50.0 метод возвращает False
- Условие оценено правильно для обоих случаев

---

## Test Case: TC-CALC-CONDITIONAL-009
**Title:** ConditionEvaluator.evaluate_condition() on_low_energy_shield

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условия on_low_energy_shield с конкретными числовыми значениями и явным порогом

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с current_energy_shield=0.0, max_energy_shield=50.0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_low_energy_shield", context)`
3. Проверить, что результат равен True
4. Создать контекст с current_energy_shield=50.0, max_energy_shield=50.0
5. Вызвать `ConditionEvaluator.evaluate_condition("on_low_energy_shield", context)`
6. Проверить, что результат равен False

**Expected Result:**
- При current_energy_shield=0.0 и max_energy_shield=50.0 метод возвращает True
- При current_energy_shield=50.0 и max_energy_shield=50.0 метод возвращает False
- Условие оценено правильно для обоих случаев

---

## Test Case: TC-CALC-CONDITIONAL-010
**Title:** ConditionEvaluator.evaluate_condition() life/mana conditions with flags

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для life/mana условий с флагами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с флагом условия (без значений)
2. Вызвать `ConditionEvaluator.evaluate_condition(condition, context)`
3. Проверить результат

**Expected Result:**
- Результат корректен
- Флаги учтены

---

## Test Case: TC-CALC-CONDITIONAL-011
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_bleeding

**Category:** Positive

**Description:** Проверка условия on_enemy_bleeding: true если enemy.statuses включает "bleeding" и bleeding_duration >= 1

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["bleeding"], enemy.bleeding_duration=2
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_bleeding", context)`
3. Проверить результат

**Expected Result:**
- result == True
- Условие выполнено при наличии статуса и длительности >= 1

---

## Test Case: TC-CALC-CONDITIONAL-011a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_bleeding duration threshold >=3

**Category:** Positive

**Description:** Проверка условия on_enemy_bleeding с порогом длительности >=3

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["bleeding"], enemy.bleeding_duration=3
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_bleeding", context, threshold=3)`
3. Проверить результат

**Expected Result:**
- result == True (bleeding_duration >= 3)
- Порог длительности учтен

---

## Test Case: TC-CALC-CONDITIONAL-011b
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_bleeding false

**Category:** Negative

**Description:** Проверка условия on_enemy_bleeding: false когда статус отсутствует или длительность < 1

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=[], enemy.bleeding_duration=0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_bleeding", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при отсутствии статуса или нулевой длительности

---

## Test Case: TC-CALC-CONDITIONAL-011c
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_bleeding edge case missing status

**Category:** Edge Case

**Description:** Проверка условия on_enemy_bleeding при отсутствии поля statuses

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст без enemy.statuses поля
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_bleeding", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Отсутствие поля обработано корректно

---

## Test Case: TC-CALC-CONDITIONAL-012
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_burning

**Category:** Positive

**Description:** Проверка условия on_enemy_burning: true если enemy.statuses включает "burning" и burn_ticks >= 1

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["burning"], enemy.burn_ticks=1
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_burning", context)`
3. Проверить результат

**Expected Result:**
- result == True
- Условие выполнено при наличии статуса и burn_ticks >= 1

---

## Test Case: TC-CALC-CONDITIONAL-012a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_burning threshold >=2

**Category:** Positive

**Description:** Проверка условия on_enemy_burning с порогом burn_ticks >=2

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["burning"], enemy.burn_ticks=2
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_burning", context, threshold=2)`
3. Проверить результат

**Expected Result:**
- result == True (burn_ticks >= 2)
- Порог тиков учтен

---

## Test Case: TC-CALC-CONDITIONAL-012b
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_burning false

**Category:** Negative

**Description:** Проверка условия on_enemy_burning: false когда статус отсутствует или burn_ticks < 1

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=[], enemy.burn_ticks=0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_burning", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при отсутствии статуса или нулевых тиках

---

## Test Case: TC-CALC-CONDITIONAL-013
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_cursed

**Category:** Positive

**Description:** Проверка условия on_enemy_cursed: true если enemy.statuses включает "cursed"

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["cursed"]
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_cursed", context)`
3. Проверить результат

**Expected Result:**
- result == True
- Условие выполнено при наличии статуса "cursed"

---

## Test Case: TC-CALC-CONDITIONAL-013a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_cursed false

**Category:** Negative

**Description:** Проверка условия on_enemy_cursed: false когда статус отсутствует

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=[]
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_cursed", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при отсутствии статуса

---

## Test Case: TC-CALC-CONDITIONAL-014
**Title:** ConditionEvaluator.evaluate_all_conditions() multiple conditions all true

**Category:** Positive

**Description:** Проверка метода evaluate_all_conditions() с множественными условиями, когда все условия выполняются

**Preconditions:**
- Нет

**Test Steps:**
1. Создать словарь условий:
   - `conditions = {"on_full_life": True, "enemy_is_shocked": True, "enemy_is_frozen": True, "on_full_mana": True}`
2. Создать контекст:
   - `context = {"current_life": 1000, "max_life": 1000, "current_mana": 500, "max_mana": 500, "enemy_is_shocked": True, "enemy_is_frozen": True}`
3. Вызвать `ConditionEvaluator.evaluate_all_conditions(conditions, context)`
4. Проверить результат и результаты каждого условия отдельно

**Expected Result:**
- `evaluate_all_conditions()` возвращает `True` (все условия выполнены)
- `evaluate_condition("on_full_life", context)` == `True` (current_life >= max_life * 0.99)
- `evaluate_condition("enemy_is_shocked", context)` == `True` (enemy_is_shocked == True)
- `evaluate_condition("enemy_is_frozen", context)` == `True` (enemy_is_frozen == True)
- `evaluate_condition("on_full_mana", context)` == `True` (current_mana >= max_mana * 0.99)
- Все условия оценены корректно и независимо

---

## Test Case: TC-CALC-CONDITIONAL-014a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_stunned duration threshold >=2

**Category:** Positive

**Description:** Проверка условия on_enemy_stunned с порогом stun_duration >=2

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["stunned"], enemy.stun_duration=2
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_stunned", context, threshold=2)`
3. Проверить результат

**Expected Result:**
- result == True (stun_duration >= 2)
- Порог длительности учтен

---

## Test Case: TC-CALC-CONDITIONAL-014b
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_stunned false

**Category:** Negative

**Description:** Проверка условия on_enemy_stunned: false когда статус отсутствует или stun_duration < 1

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=[], enemy.stun_duration=0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_stunned", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при отсутствии статуса или нулевой длительности

---

## Test Case: TC-CALC-CONDITIONAL-015
**Title:** ConditionEvaluator.evaluate_all_conditions() multiple conditions one false

**Category:** Negative

**Description:** Проверка метода evaluate_all_conditions() с множественными условиями, когда одно условие не выполняется

**Preconditions:**
- Нет

**Test Steps:**
1. Создать словарь условий:
   - `conditions = {"on_full_life": True, "enemy_is_shocked": True, "enemy_is_frozen": True, "on_full_mana": True}`
2. Создать контекст где одно условие false:
   - `context = {"current_life": 1000, "max_life": 1000, "current_mana": 200, "max_mana": 500, "enemy_is_shocked": True, "enemy_is_frozen": True}`
   - Примечание: `on_full_mana` будет False (200 < 500 * 0.99 = 495)
3. Вызвать `ConditionEvaluator.evaluate_all_conditions(conditions, context)`
4. Проверить результат и результаты каждого условия отдельно

**Expected Result:**
- `evaluate_all_conditions()` возвращает `False` (не все условия выполнены)
- `evaluate_condition("on_full_life", context)` == `True` (current_life >= max_life * 0.99)
- `evaluate_condition("enemy_is_shocked", context)` == `True` (enemy_is_shocked == True)
- `evaluate_condition("enemy_is_frozen", context)` == `True` (enemy_is_frozen == True)
- `evaluate_condition("on_full_mana", context)` == `False` (current_mana=200 < max_mana * 0.99=495) - **это условие не выполнено**
- Метод корректно возвращает False при первом невыполненном условии

---

## Test Case: TC-CALC-CONDITIONAL-015a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_poisoned stack threshold >3

**Category:** Positive

**Description:** Проверка условия on_enemy_poisoned с порогом poison_stack >3

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["poisoned"], enemy.poison_stack=4
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_poisoned", context, threshold=3)`
3. Проверить результат

**Expected Result:**
- result == True (poison_stack > 3)
- Порог стаков учтен

---

## Test Case: TC-CALC-CONDITIONAL-015b
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_poisoned false

**Category:** Negative

**Description:** Проверка условия on_enemy_poisoned: false когда статус отсутствует или poison_stack < 1

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=[], enemy.poison_stack=0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_poisoned", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при отсутствии статуса или нулевых стаках

---

## Test Case: TC-CALC-CONDITIONAL-016
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_shielded true

**Category:** Positive

**Description:** Проверка условия on_enemy_shielded: true если enemy.shield_value > 0

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.shield_value=100
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_shielded", context)`
3. Проверить результат

**Expected Result:**
- result == True
- Условие выполнено при shield_value > 0

---

## Test Case: TC-CALC-CONDITIONAL-016a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_shielded false

**Category:** Negative

**Description:** Проверка условия on_enemy_shielded: false когда enemy.shield_value == 0

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.shield_value=0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_shielded", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при нулевом значении щита

---

## Test Case: TC-CALC-CONDITIONAL-016b
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_shielded edge case negative value

**Category:** Edge Case

**Description:** Проверка условия on_enemy_shielded при отрицательном значении shield_value

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.shield_value=-10
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_shielded", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Отрицательное значение обработано корректно

---

## Test Case: TC-CALC-CONDITIONAL-017
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_enraged status

**Category:** Positive

**Description:** Проверка условия on_enemy_enraged: true если enemy.statuses включает "enraged"

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["enraged"]
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_enraged", context)`
3. Проверить результат

**Expected Result:**
- result == True
- Условие выполнено при наличии статуса "enraged"

---

## Test Case: TC-CALC-CONDITIONAL-017a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_enraged rage_level threshold

**Category:** Positive

**Description:** Проверка условия on_enemy_enraged: true если enemy.rage_level >= threshold

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.rage_level=50, threshold=30
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_enraged", context, threshold=30)`
3. Проверить результат

**Expected Result:**
- result == True (rage_level >= threshold)
- Порог уровня ярости учтен

---

## Test Case: TC-CALC-CONDITIONAL-017b
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_enraged false

**Category:** Negative

**Description:** Проверка условия on_enemy_enraged: false когда статус отсутствует и rage_level < threshold

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=[], enemy.rage_level=20, threshold=30
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_enraged", context, threshold=30)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при отсутствии статуса и низком уровне ярости

---

## Test Case: TC-CALC-CONDITIONAL-018
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_slowed true

**Category:** Positive

**Description:** Проверка условия on_enemy_slowed: true если enemy.slow_percentage > 0

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.slow_percentage=15
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_slowed", context)`
3. Проверить результат

**Expected Result:**
- result == True
- Условие выполнено при slow_percentage > 0

---

## Test Case: TC-CALC-CONDITIONAL-018a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_slowed threshold >=30%

**Category:** Positive

**Description:** Проверка условия on_enemy_slowed с порогом slow_percentage >=30%

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.slow_percentage=30
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_slowed", context, threshold=30)`
3. Проверить результат

**Expected Result:**
- result == True (slow_percentage >= 30%)
- Порог замедления учтен

---

## Test Case: TC-CALC-CONDITIONAL-018b
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_slowed false

**Category:** Negative

**Description:** Проверка условия on_enemy_slowed: false когда slow_percentage == 0

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.slow_percentage=0
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_slowed", context)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при нулевом замедлении

---

## Test Case: TC-CALC-CONDITIONAL-019
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_health_percent_below(50)

**Category:** Positive

**Description:** Проверка параметризованного условия on_enemy_health_percent_below(X) для X=50

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.health_percent=40
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_health_percent_below", context, threshold=50)`
3. Проверить результат

**Expected Result:**
- result == True (health_percent < 50)
- Условие выполнено при здоровье ниже 50%

---

## Test Case: TC-CALC-CONDITIONAL-019a
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_health_percent_below(25)

**Category:** Positive

**Description:** Проверка параметризованного условия on_enemy_health_percent_below(X) для X=25

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.health_percent=20
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_health_percent_below", context, threshold=25)`
3. Проверить результат

**Expected Result:**
- result == True (health_percent < 25)
- Условие выполнено при здоровье ниже 25%

---

## Test Case: TC-CALC-CONDITIONAL-019b
**Title:** ConditionEvaluator.evaluate_condition() on_enemy_health_percent_below false

**Category:** Negative

**Description:** Проверка условия on_enemy_health_percent_below: false когда health_percent >= threshold

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.health_percent=60, threshold=50
2. Вызвать `ConditionEvaluator.evaluate_condition("on_enemy_health_percent_below", context, threshold=50)`
3. Проверить результат

**Expected Result:**
- result == False
- Условие не выполнено при здоровье >= порога

---

## Test Case: TC-CALC-CONDITIONAL-020
**Title:** ConditionEvaluator.evaluate_condition() multiple enemy statuses combined

**Category:** Positive

**Description:** Проверка комбинированного случая: несколько статусов одновременно для проверки правильного приоритета и независимости условий

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy.statuses=["bleeding", "burning", "cursed", "poisoned"], enemy.bleeding_duration=2, enemy.burn_ticks=3, enemy.poison_stack=5
2. Вызвать `ConditionEvaluator.evaluate_condition()` для каждого условия отдельно
3. Проверить результаты всех условий

**Expected Result:**
- on_enemy_bleeding == True
- on_enemy_burning == True
- on_enemy_cursed == True
- on_enemy_poisoned == True
- Все условия оценены независимо и корректно
- Приоритет и логика работы сохранены

---

## Test Case: TC-CALC-CONDITIONAL-021
**Title:** ConditionEvaluator.evaluate_condition() enemy conditions edge case missing fields

**Category:** Edge Case

**Description:** Проверка всех enemy условий при отсутствии обязательных полей (statuses, shield_value, slow_percentage и т.д.)

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с enemy объектом без полей statuses, shield_value, slow_percentage, health_percent
2. Вызвать `ConditionEvaluator.evaluate_condition()` для всех enemy условий
3. Проверить результаты

**Expected Result:**
- Все условия возвращают False
- Отсутствие полей обработано корректно без исключений
- Edge-case проверки пройдены

---

## Test Case: TC-CALC-CONDITIONAL-022
**Title:** ConditionEvaluator.evaluate_condition() projectile distance conditions

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для условий расстояния снаряда с граничными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст с projectile_distance = 0
2. Вызвать `ConditionEvaluator.evaluate_condition()` для условия "<10"
3. Проверить результат = True
4. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=10 and <30"
5. Проверить результат = False
6. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=30"
7. Проверить результат = False
8. Создать контекст с projectile_distance = 9.99
9. Вызвать `ConditionEvaluator.evaluate_condition()` для условия "<10"
10. Проверить результат = True
11. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=10 and <30"
12. Проверить результат = False
13. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=30"
14. Проверить результат = False
15. Создать контекст с projectile_distance = 10
16. Вызвать `ConditionEvaluator.evaluate_condition()` для условия "<10"
17. Проверить результат = False
18. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=10 and <30"
19. Проверить результат = True
20. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=30"
21. Проверить результат = False
22. Создать контекст с projectile_distance = 29.99
23. Вызвать `ConditionEvaluator.evaluate_condition()` для условия "<10"
24. Проверить результат = False
25. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=10 and <30"
26. Проверить результат = True
27. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=30"
28. Проверить результат = False
29. Создать контекст с projectile_distance = 30
30. Вызвать `ConditionEvaluator.evaluate_condition()` для условия "<10"
31. Проверить результат = False
32. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=10 and <30"
33. Проверить результат = False
34. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=30"
35. Проверить результат = True
36. Создать контекст с projectile_distance = 100
37. Вызвать `ConditionEvaluator.evaluate_condition()` для условия "<10"
38. Проверить результат = False
39. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=10 and <30"
40. Проверить результат = False
41. Вызвать `ConditionEvaluator.evaluate_condition()` для условия ">=30"
42. Проверить результат = True

**Expected Result:**
- distance = 0: "<10" = True, ">=10 and <30" = False, ">=30" = False
- distance = 9.99: "<10" = True, ">=10 and <30" = False, ">=30" = False
- distance = 10: "<10" = False, ">=10 and <30" = True, ">=30" = False
- distance = 29.99: "<10" = False, ">=10 and <30" = True, ">=30" = False
- distance = 30: "<10" = False, ">=10 and <30" = False, ">=30" = True
- distance = 100: "<10" = False, ">=10 and <30" = False, ">=30" = True

---

## Test Case: TC-CALC-CONDITIONAL-023
**Title:** ConditionEvaluator.evaluate_condition() default condition

**Category:** Edge Case

**Description:** Проверка метода evaluate_condition() для неизвестного условия

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ConditionEvaluator.evaluate_condition("unknown_condition", {})`
2. Проверить результат

**Expected Result:**
- result == False (default)
- Неизвестное условие обработано корректно

---

## Test Case: TC-CALC-CONDITIONAL-024
**Title:** ConditionEvaluator.evaluate_all_conditions() all true

**Category:** Positive

**Description:** Проверка метода evaluate_all_conditions() когда все условия true

**Preconditions:**
- Нет

**Test Steps:**
1. Создать список условий и контекст
2. Вызвать `ConditionEvaluator.evaluate_all_conditions(conditions, context)`
3. Проверить результат

**Expected Result:**
- Все условия оценены
- Результат корректен

---

## Test Case: TC-CALC-CONDITIONAL-025
**Title:** ConditionEvaluator.evaluate_all_conditions() one false

**Category:** Positive

**Description:** Проверка метода evaluate_all_conditions() когда одно условие false

**Preconditions:**
- Нет

**Test Steps:**
1. Создать список условий с одним false
2. Вызвать `ConditionEvaluator.evaluate_all_conditions(conditions, context)`
3. Проверить результат

**Expected Result:**
- Результат отражает false условие
- Оценка корректна

---

## Test Case: TC-CALC-CONDITIONAL-026
**Title:** ConditionEvaluator.evaluate_all_conditions() empty list

**Category:** Edge Case

**Description:** Проверка метода evaluate_all_conditions() с пустым списком

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ConditionEvaluator.evaluate_all_conditions([], context)`
2. Проверить результат

**Expected Result:**
- result == True (empty list)
- Пустой список обработан корректно

---

## Test Case: TC-CALC-CONDITIONAL-027
**Title:** ConditionEvaluator.evaluate_condition() case insensitive

**Category:** Positive

**Description:** Проверка метода evaluate_condition() для case insensitive условий

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать evaluate_condition() с разным регистром ("OnFullLife", "on_full_life")
2. Проверить результаты

**Expected Result:**
- Оба варианта работают корректно
- Case insensitive обработка работает

---

## Test Case: TC-CALC-CONDITIONAL-028
**Title:** ConditionEvaluator.evaluate_condition() energy shield without values

**Category:** Edge Case

**Description:** Проверка метода evaluate_condition() для energy shield условий без значений

**Preconditions:**
- Нет

**Test Steps:**
1. Создать контекст без current_energy_shield и max_energy_shield
2. Вызвать evaluate_condition() для energy shield условий
3. Проверить результат

**Expected Result:**
- Условия обработаны корректно
- Отсутствие значений учтено
