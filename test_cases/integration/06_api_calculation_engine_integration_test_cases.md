# API ↔ CalculationEngine Integration Test Cases

## Module: tests/integrations/test_api_calculation_engine_integration.py

### Overview
Интеграционные тест-кейсы для проверки взаимодействия между PathOfBuildingAPI и CalculationEngine.

---

## Test Case: TC-INT-API-ENGINE-001
**Title:** Load build from API to engine

**Category:** Positive

**Integration:** PathOfBuildingAPI ↔ CalculationEngine

**Description:** Проверка загрузки build из API в calculation engine

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine через engine.load_build(build)

**Expected Result:**
- engine.modifiers is not None
- engine.damage_calc is not None
- engine.defense_calc is not None

---

## Test Case: TC-INT-API-ENGINE-002
**Title:** Calculate stats from API build

**Category:** Positive

**Integration:** PathOfBuildingAPI ↔ CalculationEngine

**Description:** Проверка расчета статистики из build данных API

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Рассчитать статистику через engine.calculate_all_stats(build_data=build)

**Expected Result:**
- stats is not None
- hasattr(stats, "life")
- hasattr(stats, "mana")

---

## Test Case: TC-INT-API-ENGINE-003
**Title:** API items to engine modifiers conversion

**Category:** Positive

**Integration:** PathOfBuildingAPI ↔ CalculationEngine ↔ ItemModifierParser

**Description:** Проверка конвертации items из API в модификаторы в engine

**Preconditions:**
- Есть build fixture (может быть создан с items, если их нет)

**Test Steps:**
1. Убедиться, что build имеет items (создать, если нужно)
2. Создать CalculationEngine
3. Зафиксировать начальное количество модификаторов
4. Загрузить build в engine
5. Проверить, что количество модификаторов увеличилось
6. Проверить, что есть модификаторы с source, начинающимся с "item:"
7. Проверить, что источники модификаторов соответствуют именам items

**Expected Result:**
- engine.modifiers.count() > initial_count
- len(item_modifiers) > 0 (модификаторы с source.startswith("item:"))
- Источники модификаторов содержат имена items

---

## Test Case: TC-INT-API-ENGINE-004
**Title:** API skill tree to engine modifiers conversion

**Category:** Positive

**Integration:** PathOfBuildingAPI ↔ CalculationEngine ↔ PassiveTreeParser

**Description:** Проверка конвертации skill tree из API в модификаторы в engine

**Preconditions:**
- Есть build fixture (может быть создан с active_skill_tree и nodes, если их нет)

**Test Steps:**
1. Убедиться, что build имеет active_skill_tree с nodes (создать, если нужно)
2. Создать CalculationEngine
3. Зафиксировать начальное количество модификаторов
4. Загрузить build в engine
5. Проверить, что количество модификаторов увеличилось
6. Проверить, что есть модификаторы с source, начинающимся с "passive_tree:" или "keystone:"
7. Проверить, что источники модификаторов соответствуют allocated nodes

**Expected Result:**
- engine.modifiers.count() > initial_count
- len(tree_modifiers) > 0 (модификаторы с passive_tree: или keystone:)
- Источники модификаторов соответствуют allocated nodes

---

## Test Case: TC-INT-API-ENGINE-005
**Title:** API config to engine context

**Category:** Positive

**Integration:** PathOfBuildingAPI ↔ CalculationEngine

**Description:** Проверка использования config из API в расчетах engine

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Создать context из build.config (enemy_level)
4. Рассчитать статистику с context через engine.calculate_all_stats(context=context, build_data=build)

**Expected Result:**
- stats is not None

---

## Test Case: TC-INT-API-ENGINE-006
**Title:** Full build processing pipeline

**Category:** Positive

**Integration:** PathOfBuildingAPI ↔ CalculationEngine

**Description:** Проверка полного пайплайна: import code → API → Engine → Stats

**Preconditions:**
- Есть build fixture (уже загружен из import code через API)

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Проверить инициализацию engine (modifiers, damage_calc, defense_calc)
4. Рассчитать все статистики
5. Проверить, что статистики рассчитаны
6. Создать второй engine и повторить (проверка переиспользования)

**Expected Result:**
- engine.modifiers is not None
- engine.damage_calc is not None
- engine.defense_calc is not None
- stats is not None
- hasattr(stats, "life") or hasattr(stats, "mana") or hasattr(stats, "total_dps")
- stats2 is not None (для второго engine)

---

## Test Case: TC-INT-API-ENGINE-007
**Title:** Modify build then recalculate

**Category:** Positive

**Integration:** PathOfBuildingAPI ↔ BuildModifier ↔ CalculationEngine

**Description:** Проверка модификации build и пересчета статистики

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine
2. Загрузить build в engine
3. Получить начальные статистики
4. Модифицировать build (добавить item с +500 to maximum Life через build.equip_item())
5. Проверить, что item добавлен в build
6. Перезагрузить build в engine
7. Пересчитать статистики
8. Проверить, что life увеличился

**Expected Result:**
- len(build.items) > 0 после добавления item
- "Test Item" in item_names
- new_stats is not None
- new_stats.life is not None
- new_life > initial_life

---
