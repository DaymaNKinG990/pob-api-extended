# Calculator Components Integration Test Cases

## Module: tests/integrations/test_calculator_components_integration.py

### Overview
Интеграционные тест-кейсы для проверки взаимодействия между различными компонентами калькулятора.

---

## Test Case: TC-INT-CALC-COMPONENTS-001
**Title:** ModifierSystem to DamageCalculator

**Category:** Positive

**Integration:** ModifierSystem ↔ DamageCalculator ↔ CalculationEngine

**Description:** Проверка передачи модификаторов из ModifierSystem в DamageCalculator

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить damage modifier через engine.modifiers.add_modifier()
4. Рассчитать статистики через engine.calculate_all_stats()

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-002
**Title:** ModifierSystem to DefenseCalculator

**Category:** Positive

**Integration:** ModifierSystem ↔ DefenseCalculator ↔ CalculationEngine

**Description:** Проверка передачи модификаторов из ModifierSystem в DefenseCalculator

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить Life и Armour modifiers через engine.modifiers.add_modifier()
4. Рассчитать статистики
5. Проверить наличие life атрибута

**Expected Result:**
- stats is not None
- hasattr(stats, "life")

---

## Test Case: TC-INT-CALC-COMPONENTS-003
**Title:** ModifierSystem to ResourceCalculator

**Category:** Positive

**Integration:** ModifierSystem ↔ ResourceCalculator ↔ CalculationEngine

**Description:** Проверка передачи модификаторов из ModifierSystem в ResourceCalculator

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить Mana и ManaRegen modifiers через engine.modifiers.add_modifier()
4. Рассчитать статистики
5. Проверить наличие mana атрибута

**Expected Result:**
- stats is not None
- hasattr(stats, "mana")

---

## Test Case: TC-INT-CALC-COMPONENTS-004
**Title:** Damage and Defense calculators together

**Category:** Positive

**Integration:** ModifierSystem ↔ DamageCalculator ↔ DefenseCalculator ↔ CalculationEngine

**Description:** Проверка работы Damage и Defense калькуляторов вместе

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить Damage и Life modifiers
4. Рассчитать все статистики
5. Проверить наличие life атрибута

**Expected Result:**
- stats is not None
- hasattr(stats, "life")

---

## Test Case: TC-INT-CALC-COMPONENTS-005
**Title:** SkillStatsCalculator with ModifierSystem

**Category:** Positive

**Integration:** ModifierSystem ↔ SkillStatsCalculator ↔ CalculationEngine

**Description:** Проверка работы SkillStatsCalculator с ModifierSystem

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить SkillDamage modifier
4. Рассчитать статистики

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-006
**Title:** MinionCalculator with ModifierSystem

**Category:** Positive

**Integration:** ModifierSystem ↔ MinionCalculator ↔ CalculationEngine

**Description:** Проверка работы MinionCalculator с ModifierSystem

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить MinionDamage modifier
4. Рассчитать статистики

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-007
**Title:** PartyCalculator with ModifierSystem

**Category:** Positive

**Integration:** ModifierSystem ↔ PartyCalculator ↔ CalculationEngine

**Description:** Проверка работы PartyCalculator с ModifierSystem

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить Party modifiers
4. Рассчитать статистики

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-008
**Title:** GameDataLoader with PassiveTreeParser

**Category:** Positive

**Integration:** GameDataLoader ↔ PassiveTreeParser

**Description:** Проверка работы GameDataLoader с PassiveTreeParser

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Получить passive tree nodes через GameDataLoader
2. Парсить modifiers через PassiveTreeParser
3. Проверить результат

**Expected Result:**
- modifiers is not None
- isinstance(modifiers, list)

---

## Test Case: TC-INT-CALC-COMPONENTS-009
**Title:** GameDataLoader with ItemModifierParser

**Category:** Positive

**Integration:** GameDataLoader ↔ ItemModifierParser

**Description:** Проверка работы GameDataLoader с ItemModifierParser

**Preconditions:**
- Нет

**Test Steps:**
1. Получить unique items через GameDataLoader
2. Парсить modifiers через ItemModifierParser
3. Проверить результат

**Expected Result:**
- modifiers is not None
- isinstance(modifiers, list)

---

## Test Case: TC-INT-CALC-COMPONENTS-010
**Title:** MirageCalculator with ModifierSystem

**Category:** Positive

**Integration:** ModifierSystem ↔ MirageCalculator ↔ CalculationEngine

**Description:** Проверка работы MirageCalculator с ModifierSystem

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить Mirage modifiers
4. Рассчитать статистики

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-011
**Title:** PantheonTools with ModifierSystem

**Category:** Positive

**Integration:** ModifierSystem ↔ PantheonTools ↔ CalculationEngine

**Description:** Проверка работы PantheonTools с ModifierSystem

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить Pantheon modifiers
4. Рассчитать статистики

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-012
**Title:** ConfigModifierParser with Engine

**Category:** Positive

**Integration:** ConfigModifierParser ↔ CalculationEngine

**Description:** Проверка работы ConfigModifierParser с CalculationEngine

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Парсить config modifiers через ConfigModifierParser
4. Добавить модификаторы в engine
5. Рассчитать статистики

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-013
**Title:** SkillModifierParser with Engine

**Category:** Positive

**Integration:** SkillModifierParser ↔ CalculationEngine

**Description:** Проверка работы SkillModifierParser с CalculationEngine

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Парсить skill modifiers через SkillModifierParser
4. Добавить модификаторы в engine
5. Рассчитать статистики

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-014
**Title:** PenetrationCalculator with DamageCalculator

**Category:** Positive

**Integration:** PenetrationCalculator ↔ DamageCalculator ↔ CalculationEngine

**Description:** Проверка работы PenetrationCalculator с DamageCalculator

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить penetration modifiers
4. Рассчитать статистики

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-CALC-COMPONENTS-015
**Title:** All calculators together

**Category:** Positive

**Integration:** All Calculator Components ↔ CalculationEngine

**Description:** Проверка работы всех калькуляторов вместе

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Добавить модификаторы для всех типов калькуляторов
4. Рассчитать все статистики
5. Проверить наличие основных атрибутов

**Expected Result:**
- stats is not None
- hasattr(stats, "life") or hasattr(stats, "mana")

---
