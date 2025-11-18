# Parser ↔ API Integration Test Cases

## Module: tests/integrations/test_parser_api_integration.py

### Overview
Интеграционные тест-кейсы для проверки взаимодействия между парсерами (ItemModifierParser, UniqueItemParser, JewelParser) и PathOfBuildingAPI.

---

## Test Case: TC-INT-PARSER-API-001
**Title:** Parse items from build

**Category:** Positive

**Integration:** ItemModifierParser ↔ PathOfBuildingAPI

**Description:** Проверка парсинга модификаторов из items build

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Парсить модификаторы из каждого item через ItemModifierParser.parse_item_text()
3. Проверить структуру модификаторов

**Expected Result:**
- len(all_modifiers) > 0
- Все модификаторы имеют правильную структуру (Modifier, stat, value, mod_type, source)

---

## Test Case: TC-INT-PARSER-API-002
**Title:** Parse item and add to modifier system

**Category:** Positive

**Integration:** ItemModifierParser ↔ CalculationEngine ↔ ModifierSystem

**Description:** Проверка парсинга item модификаторов и добавления в modifier system

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Создать CalculationEngine и загрузить build
2. Получить первый item из build
3. Парсить модификаторы через ItemModifierParser.parse_item_text()
4. Добавить модификаторы в engine.modifiers через add_modifiers()

**Expected Result:**
- engine.modifiers.count() == len(modifiers)

---

## Test Case: TC-INT-PARSER-API-003
**Title:** Parse unique items from build

**Category:** Positive

**Integration:** UniqueItemParser ↔ PathOfBuildingAPI

**Description:** Проверка парсинга unique item effects из build

**Preconditions:**
- Есть build fixture с unique items

**Test Steps:**
1. Получить items из build
2. Найти unique items (rarity == "unique")
3. Парсить unique item effects через UniqueItemParser.parse_unique_item()

**Expected Result:**
- modifiers is not None
- isinstance(modifiers, list)
- len(modifiers) >= 1  # Unique items should have at least one modifier
- For each modifier in modifiers:
  - isinstance(modifier, Modifier)
  - isinstance(modifier.stat, str) and len(modifier.stat) > 0
  - isinstance(modifier.value, (int, float))
  - isinstance(modifier.mod_type, ModifierType)
  - isinstance(modifier.source, str) and modifier.source.startswith("unique:")
- At least one modifier should have:
  - stat in common unique stats: ["Life", "Mana", "EnergyShield", "ItemQuantity", "ItemRarity", "PhysicalDamage", "ElementalDamage", "ChaosDamage", "CritChance", "AttackSpeed", "CastSpeed", "MovementSpeed", "Resist", "Strength", "Dexterity", "Intelligence"] or contains "Effect", "Convert", "Bypass"
  - value >= 0.0  # Values are typically non-negative
  - mod_type in [ModifierType.FLAT, ModifierType.INCREASED, ModifierType.MORE, ModifierType.FLAG]
- Example expected modifier structure:
  - stat: "Life" or "ItemQuantity" or "HeadhunterEffect" (or similar)
  - value: 10.0 to 100.0 (for numeric stats) or 0.0 to 1.0 (for flags)
  - mod_type: ModifierType.INCREASED or ModifierType.FLAT or ModifierType.FLAG
  - source: "unique:ItemName" (normalized, no spaces/apostrophes)

---

## Test Case: TC-INT-PARSER-API-004
**Title:** Unique item parser with modifier system

**Category:** Positive

**Integration:** UniqueItemParser ↔ CalculationEngine ↔ ModifierSystem

**Description:** Проверка работы UniqueItemParser с modifier system

**Preconditions:**
- Есть build fixture с unique items

**Test Steps:**
1. Создать CalculationEngine и загрузить build
2. Найти unique items
3. Парсить unique item effects
4. Добавить модификаторы в engine.modifiers

**Expected Result:**
- engine.modifiers.count() увеличился

---

## Test Case: TC-INT-PARSER-API-005
**Title:** Detect jewel type from build items

**Category:** Positive

**Integration:** JewelParser ↔ PathOfBuildingAPI

**Description:** Проверка определения типа jewel из build items

**Preconditions:**
- Есть build fixture с jewel items

**Test Steps:**
1. Получить items из build
2. Найти jewel items
3. Определить тип jewel через JewelParser.detect_jewel_type()

**Expected Result:**
- jewel_type is not None
- isinstance(jewel_type, JewelType)

---

## Test Case: TC-INT-PARSER-API-006
**Title:** Parse jewel socket from build

**Category:** Positive

**Integration:** JewelParser ↔ PathOfBuildingAPI

**Description:** Проверка парсинга jewel socket из build

**Preconditions:**
- Есть build fixture с jewel items

**Test Steps:**
1. Получить items из build
2. Найти jewel items
3. Парсить jewel socket через JewelParser.parse_jewel_socket()

**Expected Result:**
- jewel_modifiers is not None
- isinstance(jewel_modifiers, list)
- len(jewel_modifiers) >= 0  # Jewels may have 0 modifiers if empty socket
- For each modifier in jewel_modifiers:
  - isinstance(modifier, Modifier)
  - isinstance(modifier.stat, str) and len(modifier.stat) > 0
  - isinstance(modifier.value, (int, float))
  - isinstance(modifier.mod_type, ModifierType)
  - isinstance(modifier.source, str) and ("jewel:" in modifier.source or modifier.source in ["item", "passive"])
- If len(jewel_modifiers) > 0:
  - At least one modifier should have:
    - stat in common jewel stats: ["Life", "Mana", "EnergyShield", "PhysicalDamage", "ElementalDamage", "CritChance", "CritMultiplier", "AttackSpeed", "CastSpeed", "Resist", "Strength", "Dexterity", "Intelligence", "AccuracyRating", "Armour", "Evasion", "MovementSpeed"] or contains "Per", "Radius", "Convert"
    - value in range -100.0 to 1000.0  # Realistic jewel modifier ranges
    - mod_type in [ModifierType.FLAT, ModifierType.INCREASED, ModifierType.MORE, ModifierType.REDUCED]
  - Example expected modifier structure:
    - stat: "Life" or "PhysicalDamage" or "CritChance" (or similar)
    - value: 5.0 to 50.0 (for percentage stats) or 10.0 to 100.0 (for flat stats)
    - mod_type: ModifierType.INCREASED or ModifierType.FLAT
    - source: "jewel:socket_id" or "item" or "passive"

---

## Test Case: TC-INT-PARSER-API-007
**Title:** Jewel parser with passive tree parser

**Category:** Positive

**Integration:** JewelParser ↔ PassiveTreeParser

**Description:** Проверка работы JewelParser с PassiveTreeParser

**Preconditions:**
- Есть build fixture с jewel items и passive tree

**Test Steps:**
1. Получить jewel items и passive tree nodes
2. Парсить jewel modifiers через JewelParser
3. Использовать PassiveTreeParser для обработки nodes

**Expected Result:**
- jewel_modifiers is not None
- isinstance(jewel_modifiers, list)
- len(jewel_modifiers) >= 0  # Jewels may have 0 modifiers if empty socket
- For each modifier in jewel_modifiers:
  - isinstance(modifier, Modifier)
  - isinstance(modifier.stat, str) and len(modifier.stat) > 0
  - isinstance(modifier.value, (int, float))
  - isinstance(modifier.mod_type, ModifierType)
  - isinstance(modifier.source, str) and ("jewel:" in modifier.source or modifier.source in ["item", "passive"])
- If len(jewel_modifiers) > 0:
  - At least one modifier should have:
    - stat in common jewel stats: ["Life", "Mana", "EnergyShield", "PhysicalDamage", "ElementalDamage", "CritChance", "CritMultiplier", "AttackSpeed", "CastSpeed", "Resist", "Strength", "Dexterity", "Intelligence", "AccuracyRating", "Armour", "Evasion", "MovementSpeed"] or contains "Per", "Radius", "Convert"
    - value in range -100.0 to 1000.0  # Realistic jewel modifier ranges
    - mod_type in [ModifierType.FLAT, ModifierType.INCREASED, ModifierType.MORE, ModifierType.REDUCED]
  - Example expected modifier structure:
    - stat: "Life" or "PhysicalDamage" or "CritChance" (or similar)
    - value: 5.0 to 50.0 (for percentage stats) or 10.0 to 100.0 (for flat stats)
    - mod_type: ModifierType.INCREASED or ModifierType.FLAT
    - source: "jewel:socket_id" or "item" or "passive"

---

## Test Case: TC-INT-PARSER-API-008
**Title:** All parsers feed modifier system

**Category:** Positive

**Integration:** All Parsers ↔ CalculationEngine ↔ ModifierSystem

**Description:** Проверка, что все парсеры добавляют модификаторы в modifier system

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine и загрузить build
2. Зафиксировать начальное количество модификаторов
3. Парсить модификаторы из всех источников (items, unique items, jewels)
4. Добавить все модификаторы в engine.modifiers

**Expected Result:**
- engine.modifiers.count() >= initial_count + 15

---

## Test Case: TC-INT-PARSER-API-009
**Title:** Parser chain integration

**Category:** Positive

**Integration:** ItemModifierParser ↔ UniqueItemParser ↔ JewelParser ↔ CalculationEngine

**Description:** Проверка цепочки парсеров: Item → Unique → Jewel → Engine

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Создать CalculationEngine и загрузить build
2. Парсить модификаторы через цепочку парсеров
3. Добавить все модификаторы в engine
4. Рассчитать статистики

**Expected Result:**
- stats is not None
- "processed" in stats
- "errors" in stats
- "duration" in stats
- isinstance(stats["processed"], int) and stats["processed"] >= 0
- isinstance(stats["errors"], int) and stats["errors"] == 0
- isinstance(stats["duration"], (int, float)) and stats["duration"] > 0

---
