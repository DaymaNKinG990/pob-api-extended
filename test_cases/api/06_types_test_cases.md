# Types Test Cases

## Module: pobapi.types

### Overview
Тест-кейсы для модуля types, который содержит типы данных и перечисления (enums).

---

## Test Case: TC-TYPES-001
**Title:** Verify CharacterClass enum values

**Category:** Positive

**Description:** Проверка значений enum CharacterClass

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить значение `CharacterClass.WITCH.value`
2. Проверить значение `CharacterClass.RANGER.value`
3. Проверить значение `CharacterClass.SCION.value`

**Expected Result:**
- WITCH.value == "Witch"
- RANGER.value == "Ranger"
- SCION.value == "Scion"

---

## Test Case: TC-TYPES-002
**Title:** Verify Ascendancy enum values

**Category:** Positive

**Description:** Проверка значений enum Ascendancy

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить значение `Ascendancy.NECROMANCER.value`
2. Проверить значение `Ascendancy.DEADEYE.value`

**Expected Result:**
- NECROMANCER.value == "Necromancer"
- DEADEYE.value == "Deadeye"

---

## Test Case: TC-TYPES-003
**Title:** Verify ItemSlot enum values

**Category:** Positive

**Description:** Проверка значений enum ItemSlot

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить значение `ItemSlot.BODY_ARMOUR.value`
2. Проверить значение `ItemSlot.HELMET.value`

**Expected Result:**
- BODY_ARMOUR.value == "Body Armour"
- HELMET.value == "Helmet"

---

## Test Case: TC-TYPES-004
**Title:** Verify BanditChoice enum values

**Category:** Positive

**Description:** Проверка значений enum BanditChoice

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить значение `BanditChoice.ALIRA.value`
2. Проверить значение `BanditChoice.OAK.value`

**Expected Result:**
- ALIRA.value == "Alira"
- OAK.value == "Oak"

---

## Test Case: TC-TYPES-005
**Title:** Verify SkillName enum values

**Category:** Positive

**Description:** Проверка значений enum SkillName

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить значение `SkillName.ARC.value`
2. Проверить значение `SkillName.FIREBALL.value`

**Expected Result:**
- ARC.value == "Arc"
- FIREBALL.value == "Fireball"

---

## Test Case: TC-TYPES-006
**Title:** Verify PassiveNodeID constants

**Category:** Positive

**Description:** Проверка констант PassiveNodeID

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить значение `PassiveNodeID.ELEMENTAL_EQUILIBRIUM`
2. Проверить значение `PassiveNodeID.MINION_INSTABILITY`
3. Проверить значение `PassiveNodeID.ZEALOTS_OATH`

**Expected Result:**
- ELEMENTAL_EQUILIBRIUM == 39085
- MINION_INSTABILITY == 55906
- ZEALOTS_OATH == 10490

---

## Test Case: TC-TYPES-007
**Title:** Get name for existing PassiveNodeID

**Category:** Positive

**Description:** Проверка метода get_name для существующего ID ноды

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_name(39085)` (ELEMENTAL_EQUILIBRIUM)
2. Вызвать `PassiveNodeID.get_name(55906)` (MINION_INSTABILITY)
3. Проверить возвращаемые значения

**Expected Result:**
- get_name(39085) возвращает "ELEMENTAL_EQUILIBRIUM"
- get_name(55906) возвращает "MINION_INSTABILITY"

---

## Test Case: TC-TYPES-008
**Title:** Get name for non-existing PassiveNodeID

**Category:** Edge Case

**Description:** Проверка метода get_name для несуществующего ID ноды

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_name(999999)`
2. Убедиться, что возвращаемое значение равно None

**Expected Result:**
- get_name(999999) возвращает None

---

## Test Case: TC-TYPES-009
**Title:** Use CharacterClass enum in comparison

**Category:** Positive

**Description:** Проверка использования CharacterClass enum в сравнениях

**Preconditions:**
- Нет

**Test Steps:**
1. Выполнить сравнение `CharacterClass.WITCH == CharacterClass.WITCH`
2. Выполнить сравнение `CharacterClass.WITCH != CharacterClass.TEMPLAR`
3. Опционально: выполнить проверку идентичности `CharacterClass.WITCH is CharacterClass.WITCH`
4. Опционально: выполнить проверку идентичности `CharacterClass.WITCH is not CharacterClass.TEMPLAR`

**Expected Result:**
- `CharacterClass.WITCH == CharacterClass.WITCH` возвращает `True`
- `CharacterClass.WITCH != CharacterClass.TEMPLAR` возвращает `True`
- `CharacterClass.WITCH is CharacterClass.WITCH` возвращает `True` (если язык поддерживает проверку идентичности)
- `CharacterClass.WITCH is not CharacterClass.TEMPLAR` возвращает `True` (если язык поддерживает проверку идентичности)

---

## Test Case: TC-TYPES-010
**Title:** Use Ascendancy enum in comparison

**Category:** Positive

**Description:** Проверка использования Ascendancy enum в сравнениях

**Preconditions:**
- Нет

**Test Steps:**
1. Выполнить сравнение `Ascendancy.NECROMANCER == Ascendancy.NECROMANCER`
2. Выполнить сравнение `Ascendancy.NECROMANCER != Ascendancy.SCOURGE`

**Expected Result:**
- `Ascendancy.NECROMANCER == Ascendancy.NECROMANCER` возвращает `True`
- `Ascendancy.NECROMANCER != Ascendancy.SCOURGE` возвращает `True`

---

## Test Case: TC-TYPES-011
**Title:** Iterate over CharacterClass enum

**Category:** Positive

**Description:** Проверка итерации по всем значениям CharacterClass enum

**Preconditions:**
- Нет

**Test Steps:**
1. Итерироваться по всем значениям CharacterClass
2. Проверить, что все значения доступны

**Expected Result:**
- Все значения enum доступны при итерации
- Количество значений соответствует ожидаемому

---

## Test Case: TC-TYPES-012
**Title:** Get enum value by string

**Category:** Positive

**Description:** Проверка получения enum значения по строке через конструктор enum'а. Этот тест использует CharacterClass, но API работает для всех enum'ов, наследуемых от `str, Enum` (CharacterClass, Ascendancy, ItemSlot, BanditChoice, SkillName, DamageType, ResistanceType, SocketColor, ItemRarity, ItemType, FlaskType, ChargeType, InfluenceType, ModType, SkillType, DefenseType).

**API Method:** `CharacterClass(value: str) -> CharacterClass`

**Scope:** Все enum'ы, наследуемые от `str, Enum` поддерживают получение значения по строке через конструктор. При невалидной строке выбрасывается `ValueError`.

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `CharacterClass("Witch")` и сохранить результат
2. Проверить, что результат равен `CharacterClass.WITCH`
3. Вызвать `CharacterClass("InvalidClass")` и проверить, что выбрасывается `ValueError`

**Expected Result:**
- `CharacterClass("Witch") == CharacterClass.WITCH` возвращает `True`
- `CharacterClass("InvalidClass")` выбрасывает `ValueError` с сообщением, содержащим невалидное значение

---

## Test Case: TC-TYPES-013
**Title:** Verify all CharacterClass values exist

**Category:** Positive

**Description:** Проверка наличия всех ожидаемых значений CharacterClass

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить наличие всех основных классов (Witch, Ranger, Scion, и т.д.)
2. Проверить их значения

**Expected Result:**
- Все основные классы присутствуют
- Значения соответствуют ожидаемым

---

## Test Case: TC-TYPES-014
**Title:** Verify PassiveNodeID get_name with edge cases

**Category:** Edge Case

**Description:** Проверка метода get_name с граничными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_name(0)`
2. Вызвать `PassiveNodeID.get_name(-1)`
3. Проверить возвращаемые значения

**Expected Result:**
- `PassiveNodeID.get_name(0)` возвращает None (так как нет константы со значением 0)
- `PassiveNodeID.get_name(-1)` возвращает None (так как нет константы со значением -1)
- Метод не выбрасывает исключения для граничных значений, а возвращает None для несуществующих ID

---

## Test Case: TC-TYPES-015
**Title:** Compare enum values for equality

**Category:** Positive

**Description:** Проверка сравнения enum значений на равенство

**Preconditions:**
- Нет

**Test Steps:**
1. Выполнить сравнение `CharacterClass.WITCH == CharacterClass.WITCH`
2. Выполнить сравнение `CharacterClass.WITCH != CharacterClass.RANGER`
3. Выполнить сравнение `CharacterClass.WITCH == CharacterClass.RANGER`

**Expected Result:**
- `CharacterClass.WITCH == CharacterClass.WITCH` возвращает `True`
- `CharacterClass.WITCH != CharacterClass.RANGER` возвращает `True`
- `CharacterClass.WITCH == CharacterClass.RANGER` возвращает `False`

---

## Test Case: TC-TYPES-016
**Title:** Use enum value as dictionary key

**Category:** Positive

**Description:** Проверка использования enum значения как ключа словаря

**Preconditions:**
- Нет

**Test Steps:**
1. Создать словарь с enum значением как ключом
2. Получить значение по ключу

**Expected Result:**
- Enum значение можно использовать как ключ словаря
- Значение получено корректно

---

## Test Case: TC-TYPES-017
**Title:** Convert enum to string

**Category:** Positive

**Description:** Проверка преобразования enum в строку

**Preconditions:**
- Нет

**Test Steps:**
1. Преобразовать enum значение в строку
2. Проверить результат

**Expected Result:**
- Enum значение преобразовано в строку корректно
- Строка содержит ожидаемое значение

---

## Test Case: TC-TYPES-018
**Title:** Verify PassiveNodeID.get_id() reverse lookup method

**Category:** Positive

**Description:** Проверка статического метода get_id() для обратного поиска PassiveNodeID по имени константы. Метод сигнатура: `PassiveNodeID.get_id(name: str) -> int | None`

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PassiveNodeID.get_id("ELEMENTAL_EQUILIBRIUM")` с существующим именем в верхнем регистре
2. Вызвать `PassiveNodeID.get_id("elemental_equilibrium")` с существующим именем в нижнем регистре (case-insensitive)
3. Вызвать `PassiveNodeID.get_id("MINION_INSTABILITY")` с другим существующим именем
4. Вызвать `PassiveNodeID.get_id("NON_EXISTING_NODE")` с несуществующим именем
5. Вызвать `PassiveNodeID.get_id("")` с пустой строкой
6. Проверить возвращаемые значения

**Expected Result:**
- `PassiveNodeID.get_id("ELEMENTAL_EQUILIBRIUM")` возвращает `39085` (int)
- `PassiveNodeID.get_id("elemental_equilibrium")` возвращает `39085` (int, case-insensitive поиск)
- `PassiveNodeID.get_id("MINION_INSTABILITY")` возвращает `55906` (int)
- `PassiveNodeID.get_id("NON_EXISTING_NODE")` возвращает `None` (несуществующее имя)
- `PassiveNodeID.get_id("")` возвращает `None` (пустая строка)
- Метод всегда возвращает `int | None`, никогда не выбрасывает исключения
