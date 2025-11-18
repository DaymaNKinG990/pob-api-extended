# BuildModifier Unit Test Cases

## Module: pobapi.build_modifier

### Overview
Юнит-тест-кейсы для модуля BuildModifier, который отвечает за модификацию существующих билдов.

---

## Test Case: TC-BUILD-MODIFIER-001
**Title:** BuildModifier.__init__() with valid build

**Category:** Positive

**Description:** Проверка инициализации BuildModifier с валидным билдом

**Preconditions:**
- Валидный объект PathOfBuildingAPI предоставлен

**Test Steps:**
1. Создать BuildModifier с валидным билдом
2. Проверить, что _api установлен

**Expected Result:**
- BuildModifier успешно инициализирован
- modifier._api == simple_build

---

## Test Case: TC-BUILD-MODIFIER-002
**Title:** BuildModifier.add_node() with valid node ID

**Category:** Positive

**Description:** Проверка метода add_node() с валидным ID ноды

**Preconditions:**
- BuildModifier инициализирован
- Билд содержит дерево

**Test Steps:**
1. Вызвать `modifier.add_node(PassiveNodeID.ELEMENTAL_EQUILIBRIUM)`
2. Проверить, что нода добавлена в дерево

**Expected Result:**
- Нода добавлена в список nodes
- simple_build._is_mutable is True

---

## Test Case: TC-BUILD-MODIFIER-003
**Title:** BuildModifier.add_node() with duplicate node ID

**Category:** Edge Case

**Description:** Проверка метода add_node() с дублирующимся ID ноды

**Preconditions:**
- Нода уже добавлена в дерево

**Test Steps:**
1. Добавить ноду первый раз
2. Вызвать `modifier.add_node()` с тем же ID
3. Проверить, что нода не добавлена дважды

**Expected Result:**
- Количество нод не изменилось
- Нода присутствует только один раз

---

## Test Case: TC-BUILD-MODIFIER-004
**Title:** BuildModifier.add_node() with invalid tree index

**Category:** Negative

**Description:** Проверка метода add_node() с невалидным индексом дерева

**Preconditions:**
- BuildModifier инициализирован

**Test Steps:**
1. Вызвать `modifier.add_node(PassiveNodeID.ELEMENTAL_EQUILIBRIUM, tree_index=999)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Invalid tree index"

---

## Test Case: TC-BUILD-MODIFIER-005
**Title:** BuildModifier.remove_node() with existing node

**Category:** Positive

**Description:** Проверка метода remove_node() для существующей ноды

**Preconditions:**
- Нода добавлена в дерево

**Test Steps:**
1. Добавить ноду
2. Вызвать `modifier.remove_node(node_id)`
3. Проверить, что нода удалена

**Expected Result:**
- Нода удалена из списка nodes
- simple_build._is_mutable is True

---

## Test Case: TC-BUILD-MODIFIER-006
**Title:** BuildModifier.remove_node() with non-existent node

**Category:** Edge Case

**Description:** Проверка метода remove_node() для несуществующей ноды

**Preconditions:**
- Нода не присутствует в дереве

**Test Steps:**
1. Запомнить начальное количество нод
2. Вызвать `modifier.remove_node(99999)`
3. Проверить количество нод

**Expected Result:**
- Количество нод не изменилось
- Исключение не выбрасывается

---

## Test Case: TC-BUILD-MODIFIER-007
**Title:** BuildModifier.equip_item() with valid item and slot

**Category:** Positive

**Description:** Проверка метода equip_item() с валидным предметом и слотом

**Preconditions:**
- Валидный Item объект создан
- Валидный ItemSlot предоставлен

**Test Steps:**
1. Создать валидный Item
2. Вызвать `modifier.equip_item(item, ItemSlot.HELMET)`
3. Проверить результат

**Expected Result:**
- item_index >= 0
- simple_build._is_mutable is True
- item в списке _pending_items

---

## Test Case: TC-BUILD-MODIFIER-008
**Title:** BuildModifier.equip_item() with invalid slot

**Category:** Negative

**Description:** Проверка метода equip_item() с невалидным слотом

**Preconditions:**
- Валидный Item создан

**Test Steps:**
1. Вызвать `modifier.equip_item(item, "InvalidSlot")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Invalid slot name"

---

## Test Case: TC-BUILD-MODIFIER-009
**Title:** BuildModifier.equip_item() with string slot name

**Category:** Positive

**Description:** Проверка метода equip_item() со строковым именем слота

**Preconditions:**
- Валидный Item создан

**Test Steps:**
1. Вызвать `modifier.equip_item(item, "Body Armour")`
2. Проверить результат

**Expected Result:**
- Предмет успешно экипирован
- item_index >= 0

---

## Test Case: TC-BUILD-MODIFIER-010
**Title:** BuildModifier.add_skill() with valid gem

**Category:** Positive

**Description:** Проверка метода add_skill() с валидным гемом

**Preconditions:**
- Валидный Gem объект создан

**Test Steps:**
1. Создать валидный Gem
2. Вызвать `modifier.add_skill(gem, "Main")`
3. Проверить результат

**Expected Result:**
- simple_build._is_mutable is True
- Gem добавлен в группу скиллов
- Группа найдена по label

---

## Test Case: TC-BUILD-MODIFIER-011
**Title:** BuildModifier.add_skill() to new group

**Category:** Positive

**Description:** Проверка метода add_skill() для новой группы скиллов

**Preconditions:**
- Группа с указанным label не существует

**Test Steps:**
1. Вызвать `modifier.add_skill(gem, "Movement")`
2. Проверить создание новой группы

**Expected Result:**
- Новая группа создана
- Группа имеет enabled=True
- Gem добавлен в группу

---

## Test Case: TC-BUILD-MODIFIER-012
**Title:** BuildModifier.add_skill() with GrantedAbility

**Category:** Positive

**Description:** Проверка метода add_skill() с GrantedAbility

**Preconditions:**
- Валидный GrantedAbility объект создан

**Test Steps:**
1. Создать GrantedAbility
2. Вызвать `modifier.add_skill(ability, "Auras")`
3. Проверить результат

**Expected Result:**
- Ability добавлен в группу
- Группа найдена или создана

---

## Test Case: TC-BUILD-MODIFIER-013
**Title:** BuildModifier.equip_item() creates new item set and initializes _pending_item_sets

**Category:** Positive

**Description:** Проверка метода equip_item() при создании нового item set и инициализации _pending_item_sets (покрывает строку 149)

**Preconditions:**
- _pending_item_sets не существует
- item_set_index указывает на несуществующий набор

**Test Steps:**
1. Убедиться, что _pending_item_sets отсутствует
2. Вызвать `modifier.equip_item(item, ItemSlot.RING1, item_set_index=1)`
3. Проверить инициализацию _pending_item_sets

**Expected Result:**
- _pending_item_sets инициализирован
- _pending_item_sets является словарем
- item_set_index присутствует в _pending_item_sets

---

## Test Case: TC-BUILD-MODIFIER-014
**Title:** BuildModifier.equip_item() modifies existing set and initializes _pending_item_sets

**Category:** Positive

**Description:** Проверка метода equip_item() при модификации существующего item set и инициализации _pending_item_sets (покрывает строку 198)

**Preconditions:**
- Item set существует
- _pending_item_sets не инициализирован

**Test Steps:**
1. Убедиться, что _pending_item_sets отсутствует
2. Вызвать `modifier.equip_item(item, ItemSlot.HELMET, item_set_index=0)`
3. Проверить инициализацию _pending_item_sets

**Expected Result:**
- _pending_item_sets инициализирован
- Существующий item set модифицирован

---

## Test Case: TC-BUILD-MODIFIER-015
**Title:** BuildModifier.add_skill() initializes _pending_skill_groups

**Category:** Positive

**Description:** Проверка метода add_skill() при инициализации _pending_skill_groups (покрывает строку 236)

**Preconditions:**
- _pending_skill_groups не инициализирован
- Группа скиллов не существует

**Test Steps:**
1. Убедиться, что _pending_skill_groups отсутствует
2. Вызвать `modifier.add_skill(gem, "NewGroup")`
3. Проверить инициализацию _pending_skill_groups

**Expected Result:**
- _pending_skill_groups инициализирован
- Новая группа создана

---

## Test Case: TC-BUILD-MODIFIER-016
**Title:** BuildModifier.remove_skill() with existing skill

**Category:** Positive

**Description:** Проверка метода remove_skill() для существующего скилла

**Preconditions:**
- Скилл добавлен в группу

**Test Steps:**
1. Добавить скилл в группу
2. Вызвать `modifier.remove_skill(gem, "Main")`
3. Проверить удаление

**Expected Result:**
- Скилл удален из группы
- simple_build._is_mutable is True

---

## Test Case: TC-BUILD-MODIFIER-017
**Title:** BuildModifier.unequip_item() with equipped item

**Category:** Positive

**Description:** Проверка метода unequip_item() для экипированного предмета

**Preconditions:**
- Предмет экипирован

**Test Steps:**
1. Экипировать предмет
2. Вызвать `modifier.unequip_item(ItemSlot.HELMET)`
3. Проверить результат

**Expected Result:**
- Предмет удален из слота
- simple_build._is_mutable is True

---

## Test Case: TC-BUILD-MODIFIER-018
**Title:** BuildModifier.set_level() with valid level

**Category:** Positive

**Description:** Проверка метода set_level() с валидным уровнем

**Preconditions:**
- BuildModifier инициализирован

**Test Steps:**
1. Вызвать `modifier.set_level(90)`
2. Проверить изменение уровня

**Expected Result:**
- Уровень билда изменен на 90
- simple_build._is_mutable is True

---

## Test Case: TC-BUILD-MODIFIER-019
**Title:** BuildModifier.set_level() with invalid level

**Category:** Negative

**Description:** Проверка метода set_level() с невалидным уровнем

**Preconditions:**
- BuildModifier инициализирован

**Test Steps:**
1. Вызвать `modifier.set_level(0)` или `modifier.set_level(101)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Level must be between 1 and 100"

---

## Test Case: TC-BUILD-MODIFIER-020
**Title:** BuildModifier.set_bandit() with valid choice

**Category:** Positive

**Description:** Проверка метода set_bandit() с валидным выбором

**Preconditions:**
- BuildModifier инициализирован

**Test Steps:**
1. Вызвать `modifier.set_bandit("Alira")`
2. Проверить изменение bandit

**Expected Result:**
- bandit изменен на "Alira"
- simple_build._is_mutable is True
