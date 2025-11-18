# BuildBuilder Unit Test Cases

## Module: pobapi.build_builder

### Overview
Юнит-тест-кейсы для модуля BuildBuilder, который отвечает за построение билдов программно.

---

## Test Case: TC-BUILD-BUILDER-001
**Title:** BuildBuilder.__init__() default values

**Category:** Positive

**Description:** Проверка инициализации BuildBuilder с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `create_build()`
2. Проверить все дефолтные значения

**Expected Result:**
- builder.class_name == "Scion"
- builder.ascendancy_name is None
- builder.level == 1
- builder.bandit is None
- builder.items == []
- builder.item_sets == []
- builder.trees == []
- builder.skill_groups == []
- builder.notes == ""

---

## Test Case: TC-BUILD-BUILDER-002
**Title:** BuildBuilder.set_class() with Enum types

**Category:** Positive

**Description:** Проверка метода set_class() с Enum типами

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_class(CharacterClass.WITCH, Ascendancy.NECROMANCER)`
2. Проверить значения

**Expected Result:**
- builder.class_name == "Witch"
- builder.ascendancy_name == "Necromancer"

---

## Test Case: TC-BUILD-BUILDER-003
**Title:** BuildBuilder.set_class() with string types

**Category:** Positive

**Description:** Проверка метода set_class() со строковыми типами

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_class("Ranger", "Deadeye")`
2. Проверить значения

**Expected Result:**
- builder.class_name == "Ranger"
- builder.ascendancy_name == "Deadeye"

---

## Test Case: TC-BUILD-BUILDER-004
**Title:** BuildBuilder.set_class() without ascendancy

**Category:** Edge Case

**Description:** Проверка метода set_class() без асценданси

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_class(CharacterClass.WITCH)`
2. Проверить значения

**Expected Result:**
- builder.class_name == "Witch"
- builder.ascendancy_name is None

---

## Test Case: TC-BUILD-BUILDER-005
**Title:** BuildBuilder.set_level() with valid level

**Category:** Positive

**Description:** Проверка метода set_level() с валидным уровнем

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_level(90)`
2. Проверить значение

**Expected Result:**
- builder.level == 90

---

## Test Case: TC-BUILD-BUILDER-006
**Title:** BuildBuilder.set_level() with level too low

**Category:** Negative

**Description:** Проверка метода set_level() с уровнем ниже допустимого

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_level(0)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Level must be between 1 and 100"

---

## Test Case: TC-BUILD-BUILDER-007
**Title:** BuildBuilder.set_level() with level too high

**Category:** Negative

**Description:** Проверка метода set_level() с уровнем выше допустимого

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_level(101)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Level must be between 1 and 100"

---

## Test Case: TC-BUILD-BUILDER-008
**Title:** BuildBuilder.set_bandit() with Enum type

**Category:** Positive

**Description:** Проверка метода set_bandit() с Enum типом

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_bandit(BanditChoice.ALIRA)`
2. Проверить значение

**Expected Result:**
- builder.bandit == "Alira"

---

## Test Case: TC-BUILD-BUILDER-009
**Title:** BuildBuilder.set_bandit() with string type

**Category:** Positive

**Description:** Проверка метода set_bandit() со строковым типом

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_bandit("Oak")`
2. Проверить значение

**Expected Result:**
- builder.bandit == "Oak"

---

## Test Case: TC-BUILD-BUILDER-010
**Title:** BuildBuilder.set_bandit() with None

**Category:** Edge Case

**Description:** Проверка метода set_bandit() с None

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_bandit(None)`
2. Проверить значение

**Expected Result:**
- builder.bandit is None

---

## Test Case: TC-BUILD-BUILDER-011
**Title:** BuildBuilder.set_bandit() with invalid choice

**Category:** Negative

**Description:** Проверка метода set_bandit() с невалидным выбором

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_bandit("Invalid")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Invalid bandit choice"

---

## Test Case: TC-BUILD-BUILDER-012
**Title:** BuildBuilder.add_item() with valid item

**Category:** Positive

**Description:** Проверка метода add_item() с валидным предметом

**Preconditions:**
- Валидный Item объект создан

**Test Steps:**
1. Создать валидный Item
2. Вызвать `builder.add_item(item)`
3. Проверить результат

**Expected Result:**
- index == 0
- len(builder.items) == 1
- builder.items[0] == item

---

## Test Case: TC-BUILD-BUILDER-013
**Title:** BuildBuilder.create_item_set() creates new set

**Category:** Positive

**Description:** Проверка метода create_item_set() для создания нового набора

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.create_item_set()`
2. Проверить результат

**Expected Result:**
- len(builder.item_sets) == 1
- item_set является экземпляром models.Set
- item_set.weapon1 is None
- item_set.helmet is None

---

## Test Case: TC-BUILD-BUILDER-014
**Title:** BuildBuilder.equip_item() with valid item and slot

**Category:** Positive

**Description:** Проверка метода equip_item() с валидным индексом предмета и слотом

**Preconditions:**
- Предмет добавлен в билд
- Item set создан

**Test Steps:**
1. Добавить предмет
2. Создать item set
3. Вызвать `builder.equip_item(item_index, ItemSlot.BELT)`
4. Проверить результат

**Expected Result:**
- builder.item_sets[0].belt == item_index
- Предмет экипирован

---

## Test Case: TC-BUILD-BUILDER-015
**Title:** BuildBuilder.equip_item() with string slot

**Category:** Positive

**Description:** Проверка метода equip_item() со строковым именем слота

**Preconditions:**
- Предмет добавлен
- Item set создан

**Test Steps:**
1. Вызвать `builder.equip_item(item_index, "Helmet")`
2. Проверить результат

**Expected Result:**
- builder.item_sets[0].helmet == item_index
- Предмет экипирован в слот

---

## Test Case: TC-BUILD-BUILDER-016
**Title:** BuildBuilder.equip_item() with invalid item index

**Category:** Negative

**Description:** Проверка метода equip_item() с невалидным индексом предмета

**Preconditions:**
- Item set создан
- Предметы не добавлены

**Test Steps:**
1. Вызвать `builder.equip_item(0, ItemSlot.BELT)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Invalid item index"

---

## Test Case: TC-BUILD-BUILDER-017
**Title:** BuildBuilder.equip_item() with invalid slot

**Category:** Negative

**Description:** Проверка метода equip_item() с невалидным слотом

**Preconditions:**
- Предмет добавлен
- Item set создан

**Test Steps:**
1. Вызвать `builder.equip_item(item_index, "InvalidSlot")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Invalid slot"

---

## Test Case: TC-BUILD-BUILDER-018
**Title:** BuildBuilder.create_tree() creates new tree

**Category:** Positive

**Description:** Проверка метода create_tree() для создания нового дерева

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.create_tree()`
2. Проверить результат

**Expected Result:**
- len(builder.trees) == 1
- tree является валидным объектом дерева

---

## Test Case: TC-BUILD-BUILDER-019
**Title:** BuildBuilder.add_node() with valid node ID

**Category:** Positive

**Description:** Проверка метода add_node() с валидным ID ноды

**Preconditions:**
- Дерево создано

**Test Steps:**
1. Создать дерево
2. Вызвать `builder.add_node(PassiveNodeID.ELEMENTAL_EQUILIBRIUM)`
3. Проверить результат

**Expected Result:**
- Нода добавлена в дерево
- PassiveNodeID.ELEMENTAL_EQUILIBRIUM in builder.trees[0].nodes

---

## Test Case: TC-BUILD-BUILDER-020
**Title:** BuildBuilder.add_skill() with valid gem

**Category:** Positive

**Description:** Проверка метода add_skill() с валидным гемом

**Preconditions:**
- Валидный Gem объект создан

**Test Steps:**
1. Создать валидный Gem
2. Вызвать `builder.add_skill(gem)`
3. Проверить результат

**Expected Result:**
- Gem добавлен в skill_groups
- Группа скиллов создана или обновлена

---

## Test Case: TC-BUILD-BUILDER-021
**Title:** BuildBuilder.build() creates PathOfBuildingAPI

**Category:** Positive

**Description:** Проверка метода build() для создания финального билда

**Preconditions:**
- BuildBuilder настроен с данными

**Test Steps:**
1. Настроить builder (класс, уровень, предметы и т.д.)
2. Вызвать `builder.build()`
3. Проверить результат

**Expected Result:**
- Возвращается объект PathOfBuildingAPI
- Все данные сохранены

---

## Test Case: TC-BUILD-BUILDER-022
**Title:** BuildBuilder.set_notes() with text

**Category:** Positive

**Description:** Проверка метода set_notes() с текстом

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Вызвать `builder.set_notes("Test notes")`
2. Проверить значение

**Expected Result:**
- builder.notes == "Test notes"

---

## Test Case: TC-BUILD-BUILDER-023
**Title:** BuildBuilder.add_item() returns correct index

**Category:** Positive

**Description:** Проверка метода add_item() для возврата корректного индекса

**Preconditions:**
- BuildBuilder инициализирован

**Test Steps:**
1. Добавить первый предмет
2. Добавить второй предмет
3. Проверить индексы

**Expected Result:**
- Первый предмет имеет index == 0
- Второй предмет имеет index == 1
