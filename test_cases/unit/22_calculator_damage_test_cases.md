# Calculator Damage Unit Test Cases

## Module: pobapi.calculator.damage

### Overview
Юнит-тест-кейсы для модуля calculator.damage, который отвечает за расчет урона.

---

## Test Case: TC-CALC-DAMAGE-001
**Title:** DamageBreakdown.__init__() with defaults

**Category:** Positive

**Description:** Проверка инициализации DamageBreakdown с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `DamageBreakdown()`
2. Проверить значения всех типов урона

**Expected Result:**
- breakdown.physical == 0.0
- breakdown.fire == 0.0
- breakdown.cold == 0.0
- breakdown.lightning == 0.0
- breakdown.chaos == 0.0

---

## Test Case: TC-CALC-DAMAGE-002
**Title:** DamageBreakdown.__init__() with custom values

**Category:** Positive

**Description:** Проверка инициализации DamageBreakdown с кастомными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `DamageBreakdown(physical=100.0, fire=50.0, cold=25.0, lightning=10.0, chaos=5.0)`
2. Проверить значения

**Expected Result:**
- Все значения установлены корректно
- breakdown.physical == 100.0
- breakdown.fire == 50.0

---

## Test Case: TC-CALC-DAMAGE-003
**Title:** DamageBreakdown.total property

**Category:** Positive

**Description:** Проверка свойства total для расчета общего урона

**Preconditions:**
- DamageBreakdown создан с значениями

**Test Steps:**
1. Создать DamageBreakdown с различными типами урона
2. Вызвать `breakdown.total`
3. Проверить результат

**Expected Result:**
- total == сумма всех типов урона
- breakdown.total == 190.0 для примера

---

## Test Case: TC-CALC-DAMAGE-004
**Title:** DamageBreakdown.elemental property

**Category:** Positive

**Description:** Проверка свойства elemental для расчета элементального урона

**Preconditions:**
- DamageBreakdown создан с элементальным уроном

**Test Steps:**
1. Создать DamageBreakdown с элементальным уроном
2. Вызвать `breakdown.elemental`
3. Проверить результат

**Expected Result:**
- elemental == fire + cold + lightning
- breakdown.elemental == 85.0 для примера

---

## Test Case: TC-CALC-DAMAGE-005
**Title:** DamageCalculator.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации DamageCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать DamageCalculator
2. Проверить инициализацию

**Expected Result:**
- damage_calculator.modifiers is not None

---

## Test Case: TC-CALC-DAMAGE-006
**Title:** DamageCalculator.calculate_base_damage() with no modifiers

**Category:** Positive

**Description:** Проверка метода calculate_base_damage() без модификаторов

**Preconditions:**
- DamageCalculator инициализирован

**Test Steps:**
1. Вызвать `damage_calculator.calculate_base_damage("TestSkill")`
2. Проверить результат

**Expected Result:**
- Все типы урона равны 0.0
- breakdown.physical == 0.0

---

## Test Case: TC-CALC-DAMAGE-007
**Title:** DamageCalculator.calculate_base_damage() with modifiers

**Category:** Positive

**Description:** Проверка метода calculate_base_damage() с модификаторами

**Preconditions:**
- Модификаторы добавлены в modifier_system

**Test Steps:**
1. Добавить модификаторы для base damage
2. Вызвать `damage_calculator.calculate_base_damage("TestSkill")`
3. Проверить результат

**Expected Result:**
- Урон рассчитан корректно
- breakdown.physical == 100.0
- breakdown.fire == 50.0

---

## Test Case: TC-CALC-DAMAGE-008
**Title:** DamageCalculator._apply_damage_conversion() physical to fire

**Category:** Positive

**Description:** Проверка метода _apply_damage_conversion() для конвертации физического урона в огненный

**Preconditions:**
- DamageBreakdown с physical уроном создан
- Модификатор конвертации добавлен

**Test Steps:**
1. Создать DamageBreakdown(physical=100.0)
2. Добавить модификатор PhysicalToFire
3. Вызвать `_apply_damage_conversion()`
4. Проверить результат

**Expected Result:**
- result.physical == 50.0 (100 - 50)
- result.fire == 50.0 (100 * 0.5)

---

## Test Case: TC-CALC-DAMAGE-009
**Title:** DamageCalculator._apply_damage_conversion() multiple conversions

**Category:** Positive

**Description:** Проверка метода _apply_damage_conversion() для множественных конвертаций

**Preconditions:**
- DamageBreakdown с physical уроном создан
- Несколько модификаторов конвертации добавлены

**Test Steps:**
1. Создать DamageBreakdown(physical=100.0)
2. Добавить модификаторы PhysicalToFire и PhysicalToCold
3. Вызвать `_apply_damage_conversion()`
4. Проверить результат

**Expected Result:**
- result.physical == 50.0 (100 - 30 - 20)
- result.fire == 30.0
- result.cold == 20.0

---

## Test Case: TC-CALC-DAMAGE-010
**Title:** DamageCalculator._apply_extra_damage() extra damage modifiers

**Category:** Positive

**Description:** Проверка метода _apply_extra_damage() для применения extra damage модификаторов

**Preconditions:**
- DamageBreakdown создан
- Extra damage модификатор добавлен

**Test Steps:**
1. Создать DamageBreakdown(physical=100.0)
2. Добавить модификатор PhysicalAsExtraFire
3. Вызвать `_apply_extra_damage()`
4. Проверить результат

**Expected Result:**
- result.physical == 100.0 (неизменен)
- result.fire == 20.0 (100 * 0.2)

---

## Test Case: TC-CALC-DAMAGE-011
**Title:** DamageCalculator._apply_damage_multipliers() more multipliers

**Category:** Positive

**Description:** Проверка метода _apply_damage_multipliers() для применения more модификаторов

**Preconditions:**
- DamageBreakdown создан
- More модификаторы добавлены

**Test Steps:**
1. Создать DamageBreakdown(physical=100.0, fire=50.0)
2. Добавить more модификаторы
3. Вызвать `_apply_damage_multipliers()`
4. Проверить результат

**Expected Result:**
- result.physical == 150.0 (100 * 1.5)
- result.fire == 65.0 (50 * 1.3)

---

## Test Case: TC-CALC-DAMAGE-012
**Title:** DamageCalculator.calculate_dps() with crits

**Category:** Positive

**Description:** Проверка метода calculate_dps() с учетом критических ударов

**Preconditions:**
- Base damage: 100.0
- Attack speed: 2.0 (attacks per second)
- Crit chance: 0.25 (25%)
- Crit multiplier: 2.0 (200%)
- DamageBreakdown создан с указанными значениями
- Модификаторы crit chance и crit multiplier добавлены

**Test Steps:**
1. Создать DamageBreakdown с base_damage = 100.0
2. Установить attack_speed = 2.0
3. Добавить модификаторы: crit_chance = 0.25, crit_multiplier = 2.0
4. Вызвать `calculate_dps()`
5. Проверить результат

**Expected Result:**
- Expected DPS: 250.0
- Formula: DPS = base_damage * attack_speed * ((1 - crit_chance) + crit_chance * crit_multiplier)
- Calculation: 100.0 * 2.0 * ((1 - 0.25) + 0.25 * 2.0) = 100.0 * 2.0 * 1.25 = 250.0
- Assert: `assert abs(calculated_dps - 250.0) < 0.01`

---

## Test Case: TC-CALC-DAMAGE-013
**Title:** DamageCalculator.calculate_dps() without crits

**Category:** Positive

**Description:** Проверка метода calculate_dps() без критических ударов

**Preconditions:**
- DamageBreakdown создан
- Нет crit модификаторов

**Test Steps:**
1. Создать DamageBreakdown
2. Вызвать `calculate_dps()` без crit
3. Проверить результат

**Expected Result:**
- DPS рассчитан без учета crit
- Результат корректен

---

## Test Case: TC-CALC-DAMAGE-014
**Title:** DamageCalculator.calculate_dot_dps() ignite

**Category:** Positive

**Description:** Проверка метода calculate_dot_dps() для ignite урона

**Preconditions:**
- Модификаторы для ignite добавлены

**Test Steps:**
1. Добавить модификаторы для ignite:
   - `TestSkillBaseFireDamage`: 100.0 (FLAT)
   - `TestSkillBasePhysicalDamage`: 50.0 (FLAT)
   - `IgniteDamage`: 40.0 (INCREASED)
2. Вызвать `calculate_dot_dps("TestSkill", "ignite", context)`
3. Проверить результат

**Expected Result:**
- **Input Parameters:**
  - Base Fire Damage: 100.0
  - Base Physical Damage: 50.0
  - IgniteDamage modifier: +40% (INCREASED)
- **Calculation Formula:**
  - `base_for_dot = fire + 0.5 * physical = 100.0 + 0.5 * 50.0 = 125.0`
  - `dot_multiplier = (100.0 + 40.0) / 100.0 = 1.4`
  - `ignite_dps = base_for_dot * dot_multiplier = 125.0 * 1.4 = 175.0`
- **Expected Ignite DPS = 175.0**
- **Tolerance: ±0.1** (for floating-point precision)
- **Units: DPS** (damage per second)
- **Rounding: None** (exact calculation expected)
- **Assertion Examples:**
  - `assert abs(actual_ignite_dps - 175.0) <= 0.1`
  - `assert 174.9 <= actual_ignite_dps <= 175.1`

---

## Test Case: TC-CALC-DAMAGE-015
**Title:** DamageCalculator.calculate_dot_dps() poison

**Category:** Positive

**Description:** Проверка метода calculate_dot_dps() для poison урона

**Preconditions:**
- Модификаторы для poison добавлены

**Test Steps:**
1. Добавить модификаторы для poison:
   - `TestSkillBasePhysicalDamage`: 100.0 (FLAT)
   - `TestSkillBaseChaosDamage`: 50.0 (FLAT)
   - `PoisonDamage`: 30.0 (INCREASED)
2. Вызвать `calculate_dot_dps("TestSkill", "poison", context)`
3. Проверить результат

**Expected Result:**
- **Input Parameters:**
  - Base Physical Damage: 100.0
  - Base Chaos Damage: 50.0
  - PoisonDamage modifier: +30% (INCREASED)
- **Calculation Formula:**
  - `base_for_dot = physical + chaos = 100.0 + 50.0 = 150.0`
  - `dot_multiplier = (100.0 + 30.0) / 100.0 = 1.3`
  - `poison_dps = base_for_dot * dot_multiplier = 150.0 * 1.3 = 195.0`
- **Expected Poison DPS = 195.0**
- **Tolerance: ±0.1** (for floating-point precision)
- **Assertion:** `assert abs(actual_poison_dps - 195.0) <= 0.1`

---

## Test Case: TC-CALC-DAMAGE-016
**Title:** DamageCalculator.calculate_dot_dps() bleed

**Category:** Positive

**Description:** Проверка метода calculate_dot_dps() для bleed урона

**Preconditions:**
- Модификаторы для bleed добавлены

**Test Steps:**
1. Добавить модификаторы для bleed:
   - `TestSkillBasePhysicalDamage`: 100.0 (FLAT)
   - `BleedDamage`: 40.0 (INCREASED)
2. Вызвать `calculate_dot_dps("TestSkill", "bleed", context)`
3. Проверить результат

**Expected Result:**
- **Input Parameters:**
  - Base Physical Damage: 100.0
  - BleedDamage modifier: +40% (INCREASED)
- **Calculation Formula:**
  - `base_for_dot = physical = 100.0` (bleed scales only from physical damage)
  - `dot_multiplier = (100.0 + 40.0) / 100.0 = 1.4`
  - `bleed_dps = base_for_dot * dot_multiplier = 100.0 * 1.4 = 140.0`
- **Expected Bleed DPS = 140.0**
- **Tolerance: ±0.1** (for floating-point precision)
- **Assertion:** `assert abs(actual_bleed_dps - 140.0) <= 0.1`

---

## Test Case: TC-CALC-DAMAGE-017
**Title:** DamageCalculator.calculate_damage_against_enemy() with resistances

**Category:** Positive

**Description:** Проверка метода calculate_damage_against_enemy() с учетом сопротивлений врага

**Preconditions:**
- Модификаторы базового урона добавлены
- Контекст с конкретными сопротивлениями врага:
  - `enemy_fire_resist`: 25.0 (25%)
  - `enemy_cold_resist`: 40.0 (40%)
  - `enemy_lightning_resist`: 0.0 (0%)
  - `enemy_chaos_resist`: 0.0 (0%)

**Test Steps:**
1. Добавить модификаторы базового урона:
   - `TestSkillBasePhysicalDamage`: 100.0 (FLAT)
   - `TestSkillBaseFireDamage`: 200.0 (FLAT)
   - `TestSkillBaseColdDamage`: 150.0 (FLAT)
   - `TestSkillBaseLightningDamage`: 80.0 (FLAT)
2. Создать контекст с сопротивлениями врага:
   - `context = {"enemy_fire_resist": 25.0, "enemy_cold_resist": 40.0, "enemy_lightning_resist": 0.0, "enemy_chaos_resist": 0.0}`
3. Вызвать `calculate_damage_against_enemy("TestSkill", context)`
4. Проверить результат с конкретными числовыми утверждениями

**Expected Result:**
- **Input Parameters:**
  - Base Physical Damage: 100.0
  - Base Fire Damage: 200.0
  - Base Cold Damage: 150.0
  - Base Lightning Damage: 80.0
  - Enemy Fire Resistance: 25.0% (0.25 as fraction)
  - Enemy Cold Resistance: 40.0% (0.40 as fraction)
  - Enemy Lightning Resistance: 0.0% (0.00 as fraction)
- **Calculation Formula:**
  - Physical damage is not affected by elemental resistances: `physical_after = 100.0`
  - Fire damage reduction: `effective_fire_res = 25.0 / 100.0 = 0.25`
  - Fire damage after resistance: `fire_after = 200.0 * (1.0 - 0.25) = 200.0 * 0.75 = 150.0`
  - Cold damage reduction: `effective_cold_res = 40.0 / 100.0 = 0.40`
  - Cold damage after resistance: `cold_after = 150.0 * (1.0 - 0.40) = 150.0 * 0.60 = 90.0`
  - Lightning damage reduction: `effective_lightning_res = 0.0 / 100.0 = 0.0`
  - Lightning damage after resistance: `lightning_after = 80.0 * (1.0 - 0.0) = 80.0 * 1.0 = 80.0`
  - Total damage: `total = 100.0 + 150.0 + 90.0 + 80.0 = 420.0`
- **Expected Damage Values:**
  - Physical: 100.0 (unchanged)
  - Fire: 150.0 (reduced by 25%)
  - Cold: 90.0 (reduced by 40%)
  - Lightning: 80.0 (unchanged, 0% resistance)
  - Total: 420.0
- **Tolerance: ±0.1** (for floating-point precision)
- **Assertion Examples:**
  - `assert abs(breakdown.physical - 100.0) <= 0.1`
  - `assert abs(breakdown.fire - 150.0) <= 0.1`
  - `assert abs(breakdown.cold - 90.0) <= 0.1`
  - `assert abs(breakdown.lightning - 80.0) <= 0.1`
  - `assert abs(breakdown.total - 420.0) <= 0.1`

---

## Test Case: TC-CALC-DAMAGE-018
**Title:** DamageCalculator.calculate_average_hit() with None context

**Category:** Edge Case

**Description:** Проверка метода calculate_average_hit() с None контекстом

**Preconditions:**
- DamageCalculator инициализирован
- Нет модификаторов урона для тестового скилла

**Test Steps:**
1. Вызвать `calculate_average_hit("TestSkill", None)`
2. Проверить, что метод не выбрасывает исключение
3. Проверить тип и значение результата

**Expected Result:**
- Метод НЕ выбрасывает исключение (None контекст преобразуется в пустой словарь `{}`)
- Метод возвращает значение типа `float`
- Если нет модификаторов урона для скилла, результат равен `0.0`
- **Assertion:** `assert isinstance(result, float) and result == 0.0`

---

## Test Case: TC-CALC-DAMAGE-019
**Title:** DamageCalculator.calculate_dps() with None context

**Category:** Edge Case

**Description:** Проверка метода calculate_dps() с None контекстом

**Preconditions:**
- DamageCalculator инициализирован

**Test Steps:**
1. Вызвать `calculate_dps("TestSkill", None)`
2. Проверить, что метод возвращает float значение (DPS)
3. Проверить, что исключение не выбрасывается

**Expected Result:**
- Метод возвращает float значение (DPS) при передаче None контекста
- Метод не выбрасывает исключение, а обрабатывает None как пустой словарь
