# Types Unit Test Cases

## Module: pobapi.types

### Overview
Юнит-тест-кейсы для модуля types. Тесты проверяют enum классы и методы класса PassiveNodeID.

---

## Test Case: TC-TYPES-001
**Title:** CharacterClass enum WITCH value

**Category:** Positive

**Description:** Проверка значения enum CharacterClass.WITCH

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `CharacterClass.WITCH.value`
2. Проверить значение

**Expected Result:**
- CharacterClass.WITCH.value == "Witch"

---

## Test Case: TC-TYPES-002
**Title:** CharacterClass enum RANGER value

**Category:** Positive

**Description:** Проверка значения enum CharacterClass.RANGER

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `CharacterClass.RANGER.value`
2. Проверить значение

**Expected Result:**
- CharacterClass.RANGER.value == "Ranger"

---

## Test Case: TC-TYPES-003
**Title:** CharacterClass enum SCION value

**Category:** Positive

**Description:** Проверка значения enum CharacterClass.SCION

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `CharacterClass.SCION.value`
2. Проверить значение

**Expected Result:**
- CharacterClass.SCION.value == "Scion"

---

## Test Case: TC-TYPES-004
**Title:** Ascendancy enum NECROMANCER value

**Category:** Positive

**Description:** Проверка значения enum Ascendancy.NECROMANCER

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `Ascendancy.NECROMANCER.value`
2. Проверить значение

**Expected Result:**
- Ascendancy.NECROMANCER.value == "Necromancer"

---

## Test Case: TC-TYPES-005
**Title:** Ascendancy enum DEADEYE value

**Category:** Positive

**Description:** Проверка значения enum Ascendancy.DEADEYE

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `Ascendancy.DEADEYE.value`
2. Проверить значение

**Expected Result:**
- Ascendancy.DEADEYE.value == "Deadeye"

---

## Test Case: TC-TYPES-006
**Title:** ItemSlot enum BODY_ARMOUR value

**Category:** Positive

**Description:** Проверка значения enum ItemSlot.BODY_ARMOUR

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `ItemSlot.BODY_ARMOUR.value`
2. Проверить значение

**Expected Result:**
- ItemSlot.BODY_ARMOUR.value == "Body Armour"

---

## Test Case: TC-TYPES-007
**Title:** ItemSlot enum HELMET value

**Category:** Positive

**Description:** Проверка значения enum ItemSlot.HELMET

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `ItemSlot.HELMET.value`
2. Проверить значение

**Expected Result:**
- ItemSlot.HELMET.value == "Helmet"

---

## Test Case: TC-TYPES-008
**Title:** BanditChoice enum ALIRA value

**Category:** Positive

**Description:** Проверка значения enum BanditChoice.ALIRA

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `BanditChoice.ALIRA.value`
2. Проверить значение

**Expected Result:**
- BanditChoice.ALIRA.value == "Alira"

---

## Test Case: TC-TYPES-009
**Title:** BanditChoice enum OAK value

**Category:** Positive

**Description:** Проверка значения enum BanditChoice.OAK

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `BanditChoice.OAK.value`
2. Проверить значение

**Expected Result:**
- BanditChoice.OAK.value == "Oak"

---

## Test Case: TC-TYPES-010
**Title:** SkillName enum ARC value

**Category:** Positive

**Description:** Проверка значения enum SkillName.ARC

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `SkillName.ARC.value`
2. Проверить значение

**Expected Result:**
- SkillName.ARC.value == "Arc"

---

## Test Case: TC-TYPES-011
**Title:** SkillName enum FIREBALL value

**Category:** Positive

**Description:** Проверка значения enum SkillName.FIREBALL

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `SkillName.FIREBALL.value`
2. Проверить значение

**Expected Result:**
- SkillName.FIREBALL.value == "Fireball"

---

## Test Case: TC-TYPES-012
**Title:** PassiveNodeID constant ELEMENTAL_EQUILIBRIUM

**Category:** Positive

**Description:** Проверка константы PassiveNodeID.ELEMENTAL_EQUILIBRIUM

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `PassiveNodeID.ELEMENTAL_EQUILIBRIUM`
2. Проверить значение

**Expected Result:**
- PassiveNodeID.ELEMENTAL_EQUILIBRIUM == 39085

---

## Test Case: TC-TYPES-013
**Title:** PassiveNodeID constant MINION_INSTABILITY

**Category:** Positive

**Description:** Проверка константы PassiveNodeID.MINION_INSTABILITY

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `PassiveNodeID.MINION_INSTABILITY`
2. Проверить значение

**Expected Result:**
- PassiveNodeID.MINION_INSTABILITY == 55906

---

## Test Case: TC-TYPES-014
**Title:** PassiveNodeID constant ZEALOTS_OATH

**Category:** Positive

**Description:** Проверка константы PassiveNodeID.ZEALOTS_OATH

**Preconditions:**
- Нет

**Test Steps:**
1. Получить значение `PassiveNodeID.ZEALOTS_OATH`
2. Проверить значение

**Expected Result:**
- PassiveNodeID.ZEALOTS_OATH == 10490

---

## Test Case: TC-TYPES-015
**Title:** PassiveNodeID.get_name() with existing node ID

**Category:** Positive

**Description:** Проверка статического метода get_name() для существующего ID ноды

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_name(39085)`
2. Проверить возвращаемое значение

**Expected Result:**
- Метод возвращает "ELEMENTAL_EQUILIBRIUM"

---

## Test Case: TC-TYPES-016
**Title:** PassiveNodeID.get_name() with another existing node ID

**Category:** Positive

**Description:** Проверка статического метода get_name() для другого существующего ID ноды

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_name(55906)`
2. Проверить возвращаемое значение

**Expected Result:**
- Метод возвращает "MINION_INSTABILITY"

---

## Test Case: TC-TYPES-017
**Title:** PassiveNodeID.get_name() with non-existing node ID

**Category:** Edge Case

**Description:** Проверка статического метода get_name() для несуществующего ID ноды

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_name(999999)`
2. Проверить возвращаемое значение

**Expected Result:**
- Метод возвращает None

---

## Test Case: TC-TYPES-018
**Title:** PassiveNodeID.get_id() with existing name (uppercase)

**Category:** Positive

**Description:** Проверка статического метода get_id() для существующего имени в верхнем регистре

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_id("ELEMENTAL_EQUILIBRIUM")`
2. Проверить возвращаемое значение

**Expected Result:**
- Метод возвращает 39085

---

## Test Case: TC-TYPES-019
**Title:** PassiveNodeID.get_id() with existing name (lowercase)

**Category:** Positive

**Description:** Проверка статического метода get_id() для существующего имени в нижнем регистре (case-insensitive)

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_id("elemental_equilibrium")`
2. Проверить возвращаемое значение

**Expected Result:**
- Метод возвращает 39085 (case-insensitive поиск)

---

## Test Case: TC-TYPES-020
**Title:** PassiveNodeID.get_id() with another existing name

**Category:** Positive

**Description:** Проверка статического метода get_id() для другого существующего имени

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_id("MINION_INSTABILITY")`
2. Проверить возвращаемое значение

**Expected Result:**
- Метод возвращает 55906

---

## Test Case: TC-TYPES-021
**Title:** PassiveNodeID.get_id() with non-existing name

**Category:** Edge Case

**Description:** Проверка статического метода get_id() для несуществующего имени

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_id("NON_EXISTING_NODE")`
2. Проверить возвращаемое значение

**Expected Result:**
- Метод возвращает None

---

## Test Case: TC-TYPES-022
**Title:** Enum value comparison

**Category:** Positive

**Description:** Проверка сравнения enum значений на равенство

**Preconditions:**
- Нет

**Test Steps:**
1. Сравнить `CharacterClass.WITCH` с `CharacterClass.WITCH`
2. Сравнить `CharacterClass.WITCH` с `CharacterClass.RANGER`
3. Проверить результаты

**Expected Result:**
- CharacterClass.WITCH == CharacterClass.WITCH возвращает True
- CharacterClass.WITCH == CharacterClass.RANGER возвращает False
