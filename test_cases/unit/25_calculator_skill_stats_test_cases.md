# Calculator Skill Stats Unit Test Cases

## Module: pobapi.calculator.skill_stats

### Overview
Юнит-тест-кейсы для модуля calculator.skill_stats, который отвечает за расчет статистик скиллов.

---

## Test Case: TC-CALC-SKILL-STATS-001
**Title:** SkillStatsCalculator.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации SkillStatsCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать SkillStatsCalculator
2. Проверить инициализацию

**Expected Result:**
- skill_stats_calculator.modifiers is not None

---

## Test Case: TC-CALC-SKILL-STATS-002
**Title:** SkillStatsCalculator.calculate_area_of_effect_radius() with base value only

**Category:** Positive

**Description:** Проверка метода calculate_area_of_effect_radius() только с базовым значением

**Preconditions:**
- SkillStatsCalculator инициализирован

**Test Steps:**
1. Вызвать `calculate_area_of_effect_radius("TestSkill", base_radius=10.0)`
2. Проверить результат

**Expected Result:**
- result == 10.0
- Базовый радиус возвращен без изменений

---

## Test Case: TC-CALC-SKILL-STATS-003
**Title:** SkillStatsCalculator.calculate_area_of_effect_radius() with AoE modifiers

**Category:** Positive

**Description:** Проверка метода calculate_area_of_effect_radius() с модификаторами AoE

**Preconditions:**
- Модификатор AreaOfEffect добавлен

**Test Steps:**
1. Добавить модификатор AreaOfEffect
2. Вызвать `calculate_area_of_effect_radius("TestSkill", base_radius=10.0)`
3. Проверить результат

**Expected Result:**
- Радиус рассчитан с учетом AoE
- result == 14.14 для примера (sqrt(2.0) * 10)
- Формула: base_radius * sqrt(1 + increased/100)

---

## Test Case: TC-CALC-SKILL-STATS-004
**Title:** SkillStatsCalculator.calculate_projectile_count() with base count

**Category:** Positive

**Description:** Проверка метода calculate_projectile_count() с базовым количеством

**Preconditions:**
- SkillStatsCalculator инициализирован

**Test Steps:**
1. Вызвать `calculate_projectile_count("TestSkill", base_count=1)`
2. Проверить результат

**Expected Result:**
- result == 1
- Базовое количество возвращено

---

## Test Case: TC-CALC-SKILL-STATS-005
**Title:** SkillStatsCalculator.calculate_projectile_count() with additional projectiles

**Category:** Positive

**Description:** Проверка метода calculate_projectile_count() с дополнительными снарядами

**Preconditions:**
- Модификатор AdditionalProjectiles добавлен

**Test Steps:**
1. Добавить модификатор AdditionalProjectiles
2. Вызвать `calculate_projectile_count("TestSkill", base_count=1)`
3. Проверить результат

**Expected Result:**
- Количество рассчитано корректно
- result == 3 для примера (1 + 2)
- Дополнительные снаряды добавлены

---

## Test Case: TC-CALC-SKILL-STATS-006
**Title:** SkillStatsCalculator.calculate_projectile_count() with fractional additional

**Category:** Edge Case

**Description:** Проверка метода calculate_projectile_count() с дробным количеством дополнительных снарядов

**Preconditions:**
- Модификатор AdditionalProjectiles с дробным значением

**Test Steps:**
1. Добавить модификатор AdditionalProjectiles=0.5
2. Вызвать `calculate_projectile_count("TestSkill", base_count=1)`
3. Проверить результат

**Expected Result:**
- Дробная часть округляется вниз
- result == 1 (1 + 0.5 округляется до 1)

---

## Test Case: TC-CALC-SKILL-STATS-007
**Title:** SkillStatsCalculator.calculate_projectile_speed() with base value only

**Category:** Positive

**Description:** Проверка метода calculate_projectile_speed() только с базовым значением

**Preconditions:**
- SkillStatsCalculator инициализирован

**Test Steps:**
1. Вызвать `calculate_projectile_speed("TestSkill", base_speed=10.0)`
2. Проверить результат

**Expected Result:**
- result == 10.0
- Базовая скорость возвращена без изменений

---

## Test Case: TC-CALC-SKILL-STATS-008
**Title:** SkillStatsCalculator.calculate_projectile_speed() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_projectile_speed() с модификаторами

**Preconditions:**
- Модификатор ProjectileSpeed добавлен

**Test Steps:**
1. Добавить модификатор ProjectileSpeed
2. Вызвать `calculate_projectile_speed("TestSkill", base_speed=10.0)`
3. Проверить результат

**Expected Result:**
- Скорость рассчитана с учетом модификатора
- result == 25.0 для примера (10 * 2.5)
- Формула: base_speed * (ProjectileSpeed / 100.0)

---

## Test Case: TC-CALC-SKILL-STATS-009
**Title:** SkillStatsCalculator.calculate_skill_cooldown() with base cooldown

**Category:** Positive

**Description:** Проверка метода calculate_skill_cooldown() с базовым cooldown

**Preconditions:**
- SkillStatsCalculator инициализирован

**Test Steps:**
1. Вызвать `calculate_skill_cooldown("TestSkill", base_cooldown=10.0)`
2. Проверить результат

**Expected Result:**
- result == 10.0
- Базовый cooldown возвращен без изменений

---

## Test Case: TC-CALC-SKILL-STATS-010
**Title:** SkillStatsCalculator.calculate_skill_cooldown() with recovery modifiers

**Category:** Positive

**Description:** Проверка метода calculate_skill_cooldown() с модификаторами recovery

**Preconditions:**
- Модификатор CooldownRecovery добавлен

**Test Steps:**
1. Добавить модификатор CooldownRecovery
2. Вызвать `calculate_skill_cooldown("TestSkill", base_cooldown=10.0)`
3. Проверить результат

**Expected Result:**
- Cooldown рассчитан с учетом recovery
- result == 5.0 для примера (10 / 2.0)
- Формула: base_cooldown / (1 + recovery/100)

---

## Test Case: TC-CALC-SKILL-STATS-011
**Title:** SkillStatsCalculator.calculate_skill_cooldown() with zero recovery

**Category:** Edge Case

**Description:** Проверка метода calculate_skill_cooldown() с нулевым recovery

**Preconditions:**
- Нет модификаторов recovery

**Test Steps:**
1. Вызвать `calculate_skill_cooldown("TestSkill", base_cooldown=10.0)`
2. Проверить результат

**Expected Result:**
- result == 10.0
- Cooldown равен базовому при нулевом recovery

---

## Test Case: TC-CALC-SKILL-STATS-012
**Title:** SkillStatsCalculator.calculate_trap_cooldown()

**Category:** Positive

**Description:** Проверка метода calculate_trap_cooldown() для расчета cooldown ловушек

**Preconditions:**
- Модификатор CooldownRecovery добавлен

**Test Steps:**
1. Добавить модификатор CooldownRecovery
2. Вызвать `calculate_trap_cooldown()`
3. Проверить результат

**Expected Result:**
- Cooldown ловушек рассчитан корректно
- result == 1.33 для примера (4.0 / 3.0)
- Базовый cooldown ловушек = 4.0

---

## Test Case: TC-CALC-SKILL-STATS-013
**Title:** SkillStatsCalculator.calculate_mine_cooldown()

**Category:** Positive

**Description:** Проверка метода calculate_mine_cooldown() для расчета времени установки мин

**Preconditions:**
- Модификатор MineLayingSpeed добавлен

**Test Steps:**
1. Добавить модификатор MineLayingSpeed
2. Вызвать `calculate_mine_cooldown()`
3. Проверить результат

**Expected Result:**
- Время установки рассчитано корректно
- result == 0.1 для примера (0.3 / 3.0)
- Базовое время = 0.3

---

## Test Case: TC-CALC-SKILL-STATS-014
**Title:** SkillStatsCalculator.calculate_totem_placement_time()

**Category:** Positive

**Description:** Проверка метода calculate_totem_placement_time() для расчета времени установки тотема

**Preconditions:**
- Модификатор TotemPlacementSpeed добавлен

**Test Steps:**
1. Добавить модификатор TotemPlacementSpeed=150.0
2. Вызвать `calculate_totem_placement_time()`
3. Проверить результат

**Expected Result:**
- Время установки рассчитано корректно
- Базовое время размещения = 0.6 секунды
- Модификатор TotemPlacementSpeed=150.0 (итоговое значение = 100.0 + 150.0 = 250.0)
- Формула: final_time = base_time / (TotemPlacementSpeed / 100.0)
- result == 0.24 для примера (0.6 / 2.5, где 2.5 = 250.0 / 100.0)
- Вариант с нулевым модификатором: при TotemPlacementSpeed=0.0 (только базовое 100.0), speed_mult = 1.0, result == 0.6 (0.6 / 1.0)

---

## Test Case: TC-CALC-SKILL-STATS-015
**Title:** SkillStatsCalculator.calculate_skill_cooldown() with high recovery

**Category:** Edge Case

**Description:** Проверка метода calculate_skill_cooldown() с высоким recovery

**Preconditions:**
- Модификатор CooldownRecovery с высоким значением

**Test Steps:**
1. Добавить модификатор CooldownRecovery=200.0
2. Вызвать `calculate_skill_cooldown("TestSkill", base_cooldown=10.0)`
3. Проверить результат

**Expected Result:**
- Cooldown значительно уменьшен
- result == 3.33 для примера (10 / 3.0)
- Высокий recovery обработан корректно

---

## Test Case: TC-CALC-SKILL-STATS-016
**Title:** SkillStatsCalculator.calculate_area_of_effect_radius() with negative AoE

**Category:** Edge Case

**Description:** Проверка метода calculate_area_of_effect_radius() с отрицательным AoE

**Preconditions:**
- Модификатор AreaOfEffect с отрицательным значением

**Test Steps:**
1. Добавить модификатор AreaOfEffect=-50.0
2. Вызвать `calculate_area_of_effect_radius("TestSkill", base_radius=10.0)`
3. Проверить результат

**Expected Result:**
- Радиус уменьшен корректно
- result == 7.07 для примера (sqrt(0.5) * 10)
- Отрицательный AoE обработан

---

## Test Case: TC-CALC-SKILL-STATS-017
**Title:** SkillStatsCalculator.calculate_projectile_count() with multiple additions

**Category:** Positive

**Description:** Проверка метода calculate_projectile_count() с несколькими источниками дополнительных снарядов

**Preconditions:**
- Несколько модификаторов AdditionalProjectiles добавлены

**Test Steps:**
1. Добавить несколько модификаторов AdditionalProjectiles
2. Вызвать `calculate_projectile_count("TestSkill", base_count=1)`
3. Проверить результат

**Expected Result:**
- Все дополнительные снаряды учтены
- С base_count=1 и модификаторами AdditionalProjectiles +2 и +3, ожидаемый результат == 1 + (2 + 3) == 6
- result == 6

---

## Test Case: TC-CALC-SKILL-STATS-018
**Title:** SkillStatsCalculator.calculate_projectile_speed() with zero base

**Category:** Edge Case

**Description:** Проверка метода calculate_projectile_speed() с нулевой базовой скоростью

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `calculate_projectile_speed("TestSkill", base_speed=0.0)`
2. Проверить результат

**Expected Result:**
- result == 0.0
- Нулевая скорость обработана корректно
