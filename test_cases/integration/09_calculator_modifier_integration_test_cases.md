# Calculator ↔ ModifierSystem Integration Test Cases

## Module: tests/integrations/test_calculator_modifier_integration.py

### Overview
Интеграционные тест-кейсы для проверки явных интеграций между ModifierSystem и всеми калькуляторами.

---

## Test Case: TC-INT-CALC-MODIFIER-001
**Title:** ModifierSystem ↔ DamageCalculator integration

**Category:** Positive

**Integration:** ModifierSystem ↔ DamageCalculator

**Description:** Проверка явной интеграции между ModifierSystem и DamageCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ModifierSystem
2. Создать DamageCalculator с ModifierSystem
3. Добавить PhysicalDamage modifier через modifier_system.add_modifier()
4. Рассчитать базовый урон через damage_calc.calculate_base_damage()

**Expected Result:**
- damage is not None

---

## Test Case: TC-INT-CALC-MODIFIER-002
**Title:** ModifierSystem ↔ DefenseCalculator integration

**Category:** Positive

**Integration:** ModifierSystem ↔ DefenseCalculator

**Description:** Проверка явной интеграции между ModifierSystem и DefenseCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ModifierSystem
2. Создать DefenseCalculator с ModifierSystem
3. Добавить Life modifier через modifier_system.add_modifier()
4. Рассчитать все защиты через defense_calc.calculate_all_defenses()

**Expected Result:**
- defense is not None

---

## Test Case: TC-INT-CALC-MODIFIER-003
**Title:** ModifierSystem ↔ ResourceCalculator integration

**Category:** Positive

**Integration:** ModifierSystem ↔ ResourceCalculator

**Description:** Проверка явной интеграции между ModifierSystem и ResourceCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ModifierSystem
2. Создать ResourceCalculator с ModifierSystem
3. Добавить Mana modifier через modifier_system.add_modifier()
4. Рассчитать mana cost через resource_calc.calculate_mana_cost()

**Expected Result:**
- mana_cost is not None

---

## Test Case: TC-INT-CALC-MODIFIER-004
**Title:** ModifierSystem ↔ SkillStatsCalculator integration

**Category:** Positive

**Integration:** ModifierSystem ↔ SkillStatsCalculator

**Description:** Проверка явной интеграции между ModifierSystem и SkillStatsCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ModifierSystem
2. Создать SkillStatsCalculator с ModifierSystem
3. Добавить SkillDamage modifier через modifier_system.add_modifier()
4. Рассчитать area of effect radius через skill_stats_calc.calculate_area_of_effect_radius()

**Expected Result:**
- aoe_radius is not None

---

## Test Case: TC-INT-CALC-MODIFIER-005
**Title:** ModifierSystem ↔ MinionCalculator integration

**Category:** Positive

**Integration:** ModifierSystem ↔ MinionCalculator

**Description:** Проверка явной интеграции между ModifierSystem и MinionCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ModifierSystem
2. Создать MinionCalculator с ModifierSystem
3. Добавить MinionDamage modifier через modifier_system.add_modifier()
4. Рассчитать все minion stats через minion_calc.calculate_all_minion_stats()

**Expected Result:**
- minion_stats is not None

---

## Test Case: TC-INT-CALC-MODIFIER-006
**Title:** ModifierSystem ↔ PartyCalculator integration

**Category:** Positive

**Integration:** ModifierSystem ↔ PartyCalculator

**Description:** Проверка явной интеграции между ModifierSystem и PartyCalculator

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ModifierSystem
2. Создать PartyCalculator с ModifierSystem
3. Создать PartyMember с auras
4. Обработать party через party_calc.process_party()
5. Проверить, что модификаторы добавлены в систему

**Expected Result:**
- len(modifiers) > 0
- modifier_system is not None

---

## Test Case: TC-INT-CALC-MODIFIER-007
**Title:** Engine shares ModifierSystem with calculators

**Category:** Positive

**Integration:** CalculationEngine ↔ ModifierSystem ↔ All Calculators

**Description:** Проверка, что CalculationEngine делит ModifierSystem со всеми калькуляторами

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Проверить, что все калькуляторы используют тот же ModifierSystem

**Expected Result:**
- engine.modifiers is engine.damage_calc.modifiers
- engine.modifiers is engine.defense_calc.modifiers
- engine.modifiers is engine.resource_calc.modifiers
- engine.modifiers is engine.skill_stats_calc.modifiers
- engine.modifiers is engine.minion_calc.modifiers
- engine.modifiers is engine.party_calc.modifiers

---

## Test Case: TC-INT-CALC-MODIFIER-008
**Title:** Add modifier affects all calculators

**Category:** Positive

**Integration:** CalculationEngine ↔ ModifierSystem ↔ All Calculators

**Description:** Проверка, что добавление модификатора влияет на все калькуляторы

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить Life modifier через engine.modifiers.add_modifier()
4. Рассчитать защиты через engine.defense_calc.calculate_all_defenses()
5. Рассчитать все статистики через engine.calculate_all_stats()

**Expected Result:**
- defense is not None
- stats is not None

---

## Test Case: TC-INT-CALC-MODIFIER-009
**Title:** Damage and Defense calculators share modifiers

**Category:** Positive

**Integration:** ModifierSystem ↔ DamageCalculator ↔ DefenseCalculator

**Description:** Проверка, что DamageCalculator и DefenseCalculator делят модификаторы

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ModifierSystem
2. Создать DamageCalculator и DefenseCalculator с тем же ModifierSystem
3. Вычислить baseline damage и defense
4. Добавить модификаторы (skill base damage и life)
5. Вычислить damage и defense после добавления модификаторов
6. Проверить изменения
7. Проверить, что калькуляторы используют тот же ModifierSystem

**Expected Result:**
- damage_change >= 50.0
- life_change == 100.0
- damage_calc.modifiers is defense_calc.modifiers
- damage_calc.modifiers is modifier_system

---

## Test Case: TC-INT-CALC-MODIFIER-010
**Title:** All calculators through engine

**Category:** Positive

**Integration:** CalculationEngine ↔ All Calculators ↔ ModifierSystem

**Description:** Проверка работы всех калькуляторов вместе через engine

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить различные модификаторы (Damage, Life, Mana)
4. Рассчитать все статистики через engine.calculate_all_stats()

**Expected Result:**
- stats is not None
- hasattr(stats, "life")
- hasattr(stats, "mana")

---
