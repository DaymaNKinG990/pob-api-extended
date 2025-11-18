# Stats Unit Test Cases

## Module: pobapi.stats

### Overview
Юнит-тест-кейсы для модуля stats, который содержит dataclass `Stats` для хранения статистик персонажа.

---

## Test Case: TC-STATS-001
**Title:** Stats.__init__() with defaults

**Category:** Positive

**Description:** Проверка инициализации Stats с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `Stats()`
2. Проверить значения всех полей

**Expected Result:**
- Все поля равны None (дефолтные значения)
- Объект создан успешно

---

## Test Case: TC-STATS-002
**Title:** Stats.__init__() with all parameters

**Category:** Positive

**Description:** Проверка инициализации Stats со всеми параметрами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats со всеми параметрами
2. Проверить значения всех полей

**Expected Result:**
- Все поля установлены корректно
- Значения соответствуют переданным параметрам

---

## Test Case: TC-STATS-003
**Title:** Stats.__init__() with partial parameters

**Category:** Positive

**Description:** Проверка инициализации Stats с частичными параметрами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с некоторыми параметрами
2. Проверить установленные и дефолтные значения

**Expected Result:**
- Установленные параметры имеют переданные значения
- Неустановленные параметры равны None
- Результат корректен

---

## Test Case: TC-STATS-004
**Title:** Stats damage fields

**Category:** Positive

**Description:** Проверка полей, связанных с уроном

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями урона
2. Проверить значения полей

**Expected Result:**
- average_hit, average_damage установлены
- total_dps, total_dot установлены
- bleed_dps, ignite_dps, poison_dps установлены
- Результат корректен

---

## Test Case: TC-STATS-005
**Title:** Stats attribute fields

**Category:** Positive

**Description:** Проверка полей атрибутов (strength, dexterity, intelligence)

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями атрибутов
2. Проверить значения полей

**Expected Result:**
- strength, dexterity, intelligence установлены
- strength_required, dexterity_required, intelligence_required установлены
- Результат корректен

---

## Test Case: TC-STATS-006
**Title:** Stats life fields

**Category:** Positive

**Description:** Проверка полей, связанных с жизнью

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями жизни
2. Проверить значения полей

**Expected Result:**
- life, life_increased установлены
- life_unreserved, life_unreserved_percent установлены
- life_regen, life_leech_rate_per_hit установлены
- Результат корректен

---

## Test Case: TC-STATS-007
**Title:** Stats mana fields

**Category:** Positive

**Description:** Проверка полей, связанных с манной

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями манны
2. Проверить значения полей

**Expected Result:**
- mana, mana_increased установлены
- mana_unreserved, mana_unreserved_percent установлены
- mana_regen, mana_leech_rate_per_hit установлены
- Результат корректен

---

## Test Case: TC-STATS-008
**Title:** Stats energy shield fields

**Category:** Positive

**Description:** Проверка полей, связанных с energy shield

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями energy shield
2. Проверить значения полей

**Expected Result:**
- energy_shield, energy_shield_increased установлены
- energy_shield_regen установлен
- energy_shield_leech_rate_per_hit установлен
- Результат корректен

---

## Test Case: TC-STATS-009
**Title:** Stats defense fields

**Category:** Positive

**Description:** Проверка полей защиты

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями защиты
2. Проверить значения полей

**Expected Result:**
- evasion, armour установлены
- block_chance, spell_block_chance установлены
- physical_damage_reduction установлен
- Результат корректен

---

## Test Case: TC-STATS-010
**Title:** Stats resistance fields

**Category:** Positive

**Description:** Проверка полей сопротивлений

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями сопротивлений
2. Проверить значения полей

**Expected Result:**
- fire_resistance, cold_resistance установлены
- lightning_resistance, chaos_resistance установлены
- over_cap сопротивления установлены
- Результат корректен

---

## Test Case: TC-STATS-011
**Title:** Stats charge fields

**Category:** Positive

**Description:** Проверка полей зарядов

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями зарядов
2. Проверить значения полей

**Expected Result:**
- power_charges, frenzy_charges, endurance_charges установлены
- maximum заряды установлены
- Результат корректен

---

## Test Case: TC-STATS-012
**Title:** Stats maximum hit taken fields

**Category:** Positive

**Description:** Проверка полей максимального полученного урона

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями maximum hit taken
2. Проверить значения полей

**Expected Result:**
- physical_maximum_hit_taken установлен
- fire_maximum_hit_taken, cold_maximum_hit_taken установлены
- lightning_maximum_hit_taken, chaos_maximum_hit_taken установлены
- total_effective_health_pool установлен
- Результат корректен

---

## Test Case: TC-STATS-013
**Title:** Stats speed fields

**Category:** Positive

**Description:** Проверка полей скорости

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями скорости
2. Проверить значения полей

**Expected Result:**
- attack_speed, cast_speed установлены
- trap_throwing_speed, mine_laying_speed установлены
- totem_placement_speed установлен
- Результат корректен

---

## Test Case: TC-STATS-014
**Title:** Stats critical strike fields

**Category:** Positive

**Description:** Проверка полей критического удара

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Stats с полями критического удара
2. Проверить значения полей

**Expected Result:**
- pre_effective_crit_chance, crit_chance установлены
- crit_multiplier установлен
- Результат корректен

---

## Test Case: TC-STATS-015
**Title:** Stats dataclass behavior

**Category:** Positive

**Description:** Проверка поведения dataclass (сравнение, хеширование, и т.д.)

**Preconditions:**
- Нет

**Test Steps:**
1. Создать два Stats объекта с одинаковыми значениями
2. Создать Stats объект с разными значениями
3. Проверить сравнение объектов

**Expected Result:**
- Объекты с одинаковыми значениями равны
- Объекты с разными значениями не равны
- Dataclass поведение работает корректно
