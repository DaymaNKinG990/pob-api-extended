# Calculator Defense Unit Test Cases

## Module: pobapi.calculator.defense

### Overview
Юнит-тест-кейсы для модуля calculator.defense, который отвечает за расчет защиты.

---

## Test Case: TC-CALC-DEFENSE-001
**Title:** DefenseStats.__init__() with defaults

**Category:** Positive

**Description:** Проверка инициализации DefenseStats с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `DefenseStats()`
2. Проверить значения всех статов

**Expected Result:**
- stats.life == 0.0
- stats.mana == 0.0
- stats.energy_shield == 0.0
- stats.armour == 0.0
- stats.evasion == 0.0

---

## Test Case: TC-CALC-DEFENSE-002
**Title:** DefenseCalculator.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации DefenseCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать DefenseCalculator
2. Проверить инициализацию

**Expected Result:**
- defense_calculator.modifiers is not None

---

## Test Case: TC-CALC-DEFENSE-003
**Title:** DefenseCalculator.calculate_life() with base value only

**Category:** Positive

**Description:** Проверка метода calculate_life() только с базовым значением

**Preconditions:**
- DefenseCalculator инициализирован

**Test Steps:**
1. Создать контекст с base_life
2. Вызвать `defense_calculator.calculate_life(context)`
3. Проверить результат

**Expected Result:**
- result == base_life
- result == 100.0 для примера

---

## Test Case: TC-CALC-DEFENSE-004
**Title:** DefenseCalculator.calculate_life() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_life() с модификаторами

**Preconditions:**
- Модификаторы добавлены в modifier_system

**Test Steps:**
1. Добавить flat и increased модификаторы для Life
2. Создать контекст с base_life
3. Вызвать `defense_calculator.calculate_life(context)`
4. Проверить результат

**Expected Result:**
- Результат рассчитан корректно
- Порядок: flat → increased
- result == 180.0 для примера (100 + 50) * 1.2

---

## Test Case: TC-CALC-DEFENSE-005
**Title:** DefenseCalculator.calculate_mana() with base value only

**Category:** Positive

**Description:** Проверка метода calculate_mana() только с базовым значением

**Preconditions:**
- DefenseCalculator инициализирован

**Test Steps:**
1. Создать контекст с base_mana
2. Вызвать `defense_calculator.calculate_mana(context)`
3. Проверить результат

**Expected Result:**
- result == base_mana
- result == 50.0 для примера

---

## Test Case: TC-CALC-DEFENSE-006
**Title:** DefenseCalculator.calculate_energy_shield() with base value only

**Category:** Positive

**Description:** Проверка метода calculate_energy_shield() только с базовым значением

**Preconditions:**
- DefenseCalculator инициализирован

**Test Steps:**
1. Создать контекст с base_energy_shield
2. Вызвать `defense_calculator.calculate_energy_shield(context)`
3. Проверить результат

**Expected Result:**
- result == base_energy_shield
- result == 0.0 для примера

---

## Test Case: TC-CALC-DEFENSE-007
**Title:** DefenseCalculator.calculate_energy_shield() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_energy_shield() с модификаторами

**Preconditions:**
- Модификаторы добавлены в modifier_system

**Test Steps:**
1. Добавить flat модификатор для EnergyShield
2. Вызвать `defense_calculator.calculate_energy_shield(context)`
3. Проверить результат

**Expected Result:**
- result == 100.0 для примера
- Модификаторы применены корректно

---

## Test Case: TC-CALC-DEFENSE-008
**Title:** DefenseCalculator.calculate_physical_damage_reduction() with no armour

**Category:** Positive

**Description:** Проверка метода calculate_physical_damage_reduction() без брони

**Preconditions:**
- Нет модификаторов Armour

**Test Steps:**
1. Вызвать `calculate_physical_damage_reduction(hit_damage, context)`
2. Проверить результат

**Expected Result:**
- result == 0.0
- Нет редукции без брони

---

## Test Case: TC-CALC-DEFENSE-009
**Title:** DefenseCalculator.calculate_physical_damage_reduction() with armour

**Category:** Positive

**Description:** Проверка метода calculate_physical_damage_reduction() с броней

**Preconditions:**
- Модификатор Armour добавлен

**Test Steps:**
1. Добавить модификатор Armour
2. Вызвать `calculate_physical_damage_reduction(hit_damage, context)`
3. Проверить результат

**Expected Result:**
- Редукция рассчитана корректно
- result >= 0.0 и result <= 0.9
- Формула: armour / (armour + hit_damage * 10)

---

## Test Case: TC-CALC-DEFENSE-010
**Title:** DefenseCalculator.calculate_evade_chance()

**Category:** Positive

**Description:** Проверка метода calculate_evade_chance() для расчета шанса уклонения

**Preconditions:**
- Модификатор Evasion добавлен

**Test Steps:**
1. Добавить модификатор Evasion
2. Вызвать `calculate_evade_chance(enemy_accuracy, context)`
3. Проверить результат

**Expected Result:**
- result >= 0.0
- result <= 0.95 (максимум 95%)
- Шанс уклонения рассчитан корректно

---

## Test Case: TC-CALC-DEFENSE-011
**Title:** DefenseCalculator.calculate_resistances() with base values

**Category:** Positive

**Description:** Проверка метода calculate_resistances() с базовыми значениями

**Preconditions:**
- DefenseCalculator инициализирован

**Test Steps:**
1. Вызвать calculate_stat для каждого типа сопротивления
2. Проверить результаты

**Expected Result:**
- Все сопротивления равны 0.0 по умолчанию
- fire_res == 0.0
- cold_res == 0.0

---

## Test Case: TC-CALC-DEFENSE-012
**Title:** DefenseCalculator.calculate_resistances() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_resistances() с модификаторами

**Preconditions:**
- Модификаторы сопротивлений добавлены

**Test Steps:**
1. Добавить модификаторы для сопротивлений
2. Вызвать calculate_stat для каждого типа
3. Проверить результаты

**Expected Result:**
- Сопротивления рассчитаны корректно
- fire_res == 75.0 для примера

---

## Test Case: TC-CALC-DEFENSE-013
**Title:** DefenseCalculator.calculate_block_chance()

**Category:** Positive

**Description:** Проверка метода calculate_block_chance() для расчета шанса блока

**Preconditions:**
- Модификаторы блока добавлены

**Test Steps:**
1. Добавить модификаторы для блока
2. Вызвать `calculate_block_chance(context)`
3. Проверить результат

**Expected Result:**
- Шанс блока рассчитан корректно
- result >= 0.0 и result <= 0.75 (максимум 75%)

---

## Test Case: TC-CALC-DEFENSE-014
**Title:** DefenseCalculator.calculate_maximum_hit_taken() physical

**Category:** Positive

**Description:** Проверка метода calculate_maximum_hit_taken() для физического урона

**Preconditions:**
- Life и Armour рассчитаны

**Test Steps:**
1. Установить life и armour в контексте
2. Вызвать `calculate_maximum_hit_taken("physical", context)`
3. Проверить результат

**Expected Result:**
- Максимальный удар рассчитан корректно
- Учитывается life и physical damage reduction

---

## Test Case: TC-CALC-DEFENSE-015
**Title:** DefenseCalculator.calculate_maximum_hit_taken() fire

**Category:** Positive

**Description:** Проверка метода calculate_maximum_hit_taken() для огненного урона

**Preconditions:**
- Life и FireResistance рассчитаны

**Test Steps:**
1. Установить life и fire resistance в контексте
2. Вызвать `calculate_maximum_hit_taken("fire", context)`
3. Проверить результат

**Expected Result:**
- Максимальный удар рассчитан корректно
- Учитывается life и fire resistance

---

## Test Case: TC-CALC-DEFENSE-016
**Title:** DefenseCalculator.calculate_maximum_hit_taken() no resistance

**Category:** Edge Case

**Description:** Проверка метода calculate_maximum_hit_taken() без сопротивления

**Preconditions:**
- Life рассчитан, сопротивление отсутствует

**Test Steps:**
1. Установить life в контексте
2. Вызвать `calculate_maximum_hit_taken()` без сопротивления
3. Проверить результат

**Expected Result:**
- Максимальный удар рассчитан без учета сопротивления
- Результат корректен

---

## Test Case: TC-CALC-DEFENSE-017
**Title:** DefenseCalculator.calculate_effective_health_pool()

**Category:** Positive

**Description:** Проверка метода calculate_effective_health_pool() для расчета эффективного пула здоровья

**Preconditions:**
- Life и сопротивления рассчитаны

**Test Steps:**
1. Установить life и сопротивления в контексте
2. Вызвать `calculate_effective_health_pool(context)`
3. Проверить результат

**Expected Result:**
- Эффективный пул здоровья рассчитан корректно
- Учитываются все сопротивления

---

## Test Case: TC-CALC-DEFENSE-018
**Title:** DefenseCalculator.calculate_effective_health_pool() no resistance

**Category:** Edge Case

**Description:** Проверка метода calculate_effective_health_pool() без сопротивлений

**Preconditions:**
- Life рассчитан, сопротивления отсутствуют

**Test Steps:**
1. Установить life в контексте
2. Вызвать `calculate_effective_health_pool()` без сопротивлений
3. Проверить результат

**Expected Result:**
- Эффективный пул равен life
- Результат корректен

---

## Test Case: TC-CALC-DEFENSE-019
**Title:** DefenseCalculator.calculate_life() with base modifier

**Category:** Positive

**Description:** Проверка метода calculate_life() с базовым модификатором

**Preconditions:**
- Модификатор base_life добавлен

**Test Steps:**
1. Добавить модификатор base_life
2. Вызвать `calculate_life(context)`
3. Проверить результат

**Expected Result:**
- Life рассчитан с учетом base_life
- Результат корректен

---

## Test Case: TC-CALC-DEFENSE-020
**Title:** DefenseCalculator.calculate_mana() with base modifier

**Category:** Positive

**Description:** Проверка метода calculate_mana() с базовым модификатором

**Preconditions:**
- Модификатор base_mana добавлен

**Test Steps:**
1. Добавить модификатор base_mana
2. Вызвать `calculate_mana(context)`
3. Проверить результат

**Expected Result:**
- Mana рассчитан с учетом base_mana
- Результат корректен
