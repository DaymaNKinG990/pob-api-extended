# Calculator Config Parser Unit Test Cases

## Module: pobapi.calculator.config_modifier_parser

### Overview
Юнит-тест-кейсы для модуля calculator.config_modifier_parser, который отвечает за парсинг конфигурации билда.

---

## Test Case: TC-CALC-CONFIG-001
**Title:** ConfigModifierParser.parse_config() empty config

**Category:** Edge Case

**Description:** Проверка метода parse_config() для пустого конфига

**Preconditions:**
- Mock config создан

**Test Steps:**
1. Создать пустой mock config
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- modifiers == []
- Пустой конфиг обработан корректно

---

## Test Case: TC-CALC-CONFIG-002
**Title:** ConfigModifierParser.parse_config() onslaught buff

**Category:** Positive

**Description:** Проверка метода parse_config() для onslaught баффа

**Preconditions:**
- Mock config с onslaught=True

**Test Steps:**
1. Создать mock config с onslaught=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- len(modifiers) == 3
- AttackSpeed, CastSpeed, MovementSpeed модификаторы присутствуют
- Все значения == 20.0, mod_type == INCREASED

---

## Test Case: TC-CALC-CONFIG-003
**Title:** ConfigModifierParser.parse_config() fortify buff

**Category:** Positive

**Description:** Проверка метода parse_config() для fortify баффа

**Preconditions:**
- Mock config с fortify=True

**Test Steps:**
1. Создать mock config с fortify=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- len(modifiers) == 1
- mod.stat == "DamageTaken"
- mod.value == -20.0
- mod.mod_type == INCREASED
- mod.source == "config:fortify"

---

## Test Case: TC-CALC-CONFIG-004
**Title:** ConfigModifierParser.parse_config() tailwind buff

**Category:** Positive

**Description:** Проверка метода parse_config() для tailwind баффа

**Preconditions:**
- Mock config с tailwind=True

**Test Steps:**
1. Создать mock config с tailwind=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- len(modifiers) == 1
- mod.stat == "ActionSpeed"
- mod.value == 10.0
- mod.mod_type == INCREASED
- mod.source == "config:tailwind"

---

## Test Case: TC-CALC-CONFIG-005
**Title:** ConfigModifierParser.parse_config() adrenaline buff

**Category:** Positive

**Description:** Проверка метода parse_config() для adrenaline баффа

**Preconditions:**
- Mock config с adrenaline=True

**Test Steps:**
1. Создать mock config с adrenaline=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- len(modifiers) == 4
- Damage, AttackSpeed, CastSpeed, MovementSpeed модификаторы присутствуют
- Значения корректны

---

## Test Case: TC-CALC-CONFIG-006
**Title:** ConfigModifierParser.parse_config() power charges

**Category:** Positive

**Description:** Проверка метода parse_config() для power charges

**Preconditions:**
- Mock config с use_power_charges=True и max_power_charges

**Test Steps:**
1. Создать mock config с power charges
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- len(modifiers) == 1
- mod.stat == "CritChance"
- mod.value зависит от количества charges
- mod.mod_type == INCREASED
- mod.source == "config:power_charges"

---

## Test Case: TC-CALC-CONFIG-007
**Title:** ConfigModifierParser.parse_config() frenzy charges

**Category:** Positive

**Description:** Проверка метода parse_config() для frenzy charges

**Preconditions:**
- Mock config с use_frenzy_charges=True и max_frenzy_charges

**Test Steps:**
1. Создать mock config с frenzy charges
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для AttackSpeed, CastSpeed, Damage присутствуют
- Значения зависят от количества charges
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-008
**Title:** ConfigModifierParser.parse_config() endurance charges

**Category:** Positive

**Description:** Проверка метода parse_config() для endurance charges

**Preconditions:**
- Mock config с use_endurance_charges=True и max_endurance_charges

**Test Steps:**
1. Создать mock config с endurance charges
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для PhysicalDamageReduction, FireResistance, ColdResistance, LightningResistance присутствуют
- Значения зависят от количества charges
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-009
**Title:** ConfigModifierParser.parse_config() hatred aura

**Category:** Positive

**Description:** Проверка метода parse_config() для hatred ауры

**Preconditions:**
- Mock config с hatred=True

**Test Steps:**
1. Создать mock config с hatred=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для ColdDamage присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-010
**Title:** ConfigModifierParser.parse_config() anger aura

**Category:** Positive

**Description:** Проверка метода parse_config() для anger ауры

**Preconditions:**
- Mock config с anger=True

**Test Steps:**
1. Создать mock config с anger=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для FireDamage присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-011
**Title:** ConfigModifierParser.parse_config() wrath aura

**Category:** Positive

**Description:** Проверка метода parse_config() для wrath ауры

**Preconditions:**
- Mock config с wrath=True

**Test Steps:**
1. Создать mock config с wrath=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для LightningDamage присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-012
**Title:** ConfigModifierParser.parse_config() haste aura

**Category:** Positive

**Description:** Проверка метода parse_config() для haste ауры

**Preconditions:**
- Mock config с haste=True

**Test Steps:**
1. Создать mock config с haste=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для AttackSpeed, CastSpeed, MovementSpeed присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-013
**Title:** ConfigModifierParser.parse_config() grace aura

**Category:** Positive

**Description:** Проверка метода parse_config() для grace ауры

**Preconditions:**
- Mock config с grace=True

**Test Steps:**
1. Создать mock config с grace=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для Evasion присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-014
**Title:** ConfigModifierParser.parse_config() determination aura

**Category:** Positive

**Description:** Проверка метода parse_config() для determination ауры

**Preconditions:**
- Mock config с determination=True

**Test Steps:**
1. Создать mock config с determination=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для Armour присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-015
**Title:** ConfigModifierParser.parse_config() discipline aura

**Category:** Positive

**Description:** Проверка метода parse_config() для discipline ауры

**Preconditions:**
- Mock config с discipline=True

**Test Steps:**
1. Создать mock config с discipline=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для EnergyShield присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-016
**Title:** ConfigModifierParser.parse_config() elemental curses

**Category:** Positive

**Description:** Проверка метода parse_config() для элементальных проклятий

**Preconditions:**
- Mock config с elemental curses

**Test Steps:**
1. Создать mock config с elemental curses
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для EnemyResistance присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-017
**Title:** ConfigModifierParser.parse_config() enfeeble curse

**Category:** Positive

**Description:** Проверка метода parse_config() для enfeeble проклятия

**Preconditions:**
- Mock config с enfeeble=True

**Test Steps:**
1. Создать mock config с enfeeble=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для EnemyDamage присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-018
**Title:** ConfigModifierParser.parse_config() vulnerability curse

**Category:** Positive

**Description:** Проверка метода parse_config() для vulnerability проклятия

**Preconditions:**
- Mock config с vulnerability=True

**Test Steps:**
1. Создать mock config с vulnerability=True
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Модификаторы для EnemyPhysicalDamageTaken присутствуют
- Результат корректен

---

## Test Case: TC-CALC-CONFIG-019
**Title:** ConfigModifierParser.parse_config() conditions

**Category:** Positive

**Description:** Проверка метода parse_config() для условий

**Preconditions:**
- Mock config с условиями

**Test Steps:**
1. Создать mock config с условиями
2. Вызвать `ConfigModifierParser.parse_config(config)`
3. Проверить результат

**Expected Result:**
- Условия обработаны
- Результат корректен
