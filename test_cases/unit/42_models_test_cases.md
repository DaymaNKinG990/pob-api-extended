# Models Unit Test Cases

## Module: pobapi.models

### Overview
Юнит-тест-кейсы для модуля models, который содержит модели данных (Gem, GrantedAbility, SkillGroup, Tree, Item, Set, Keystones).

---

## Test Case: TC-MODELS-001
**Title:** Gem.__init__() with valid data

**Category:** Positive

**Description:** Проверка создания Gem с валидными данными

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Gem с name, enabled, level, quality, support
2. Проверить значения всех полей

**Expected Result:**
- Все поля установлены корректно
- Объект создан успешно

---

## Test Case: TC-MODELS-002
**Title:** Gem.__post_init__() validation - level range

**Category:** Negative

**Description:** Проверка валидации уровня гема в __post_init__

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Gem с level < 1
2. Попытаться создать Gem с level > 21
3. Проверить обработку ошибок

**Expected Result:**
- ValidationError при level < 1
- ValidationError при level > 21
- Ошибки обработаны корректно

---

## Test Case: TC-MODELS-003
**Title:** Gem.__post_init__() validation - quality range

**Category:** Negative

**Description:** Проверка валидации качества гема в __post_init__

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Gem с quality < 0
2. Попытаться создать Gem с quality > 23
3. Проверить обработку ошибок

**Expected Result:**
- ValidationError при quality < 0
- ValidationError при quality > 23
- Ошибки обработаны корректно

---

## Test Case: TC-MODELS-004
**Title:** Gem.__post_init__() validation - empty name

**Category:** Negative

**Description:** Проверка валидации пустого имени гема

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Gem с пустым name
2. Проверить обработку ошибки

**Expected Result:**
- ValidationError при пустом name
- Ошибка обработана корректно

---

## Test Case: TC-MODELS-005
**Title:** GrantedAbility.__init__() with defaults

**Category:** Positive

**Description:** Проверка создания GrantedAbility с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Создать GrantedAbility с минимальными параметрами
2. Проверить дефолтные значения

**Expected Result:**
- quality == None (дефолт)
- support == False (дефолт)
- Объект создан успешно

---

## Test Case: TC-MODELS-006
**Title:** SkillGroup.__init__() with abilities

**Category:** Positive

**Description:** Проверка создания SkillGroup с abilities

**Preconditions:**
- Gem или GrantedAbility объекты созданы

**Test Steps:**
1. Создать список Gem/GrantedAbility
2. Создать SkillGroup с abilities
3. Проверить значения

**Expected Result:**
- enabled, label, active установлены
- abilities содержит переданные объекты
- Результат корректен

---

## Test Case: TC-MODELS-007
**Title:** SkillGroup.__init__() with None active

**Category:** Positive

**Description:** Проверка создания SkillGroup с active=None

**Preconditions:**
- Нет

**Test Steps:**
1. Создать SkillGroup с active=None
2. Проверить значения

**Expected Result:**
- active is None
- Объект создан успешно

---

## Test Case: TC-MODELS-008
**Title:** Tree.__init__() with nodes and sockets

**Category:** Positive

**Description:** Проверка создания Tree с nodes и sockets

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Tree с url, nodes, sockets
2. Проверить значения

**Expected Result:**
- url установлен
- nodes содержит список ID
- sockets содержит словарь {node_id: item_id}
- Результат корректен

---

## Test Case: TC-MODELS-009
**Title:** Tree.__init__() with empty nodes and sockets

**Category:** Edge Case

**Description:** Проверка создания Tree с пустыми nodes и sockets

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Tree с пустым nodes=[]
2. Создать Tree с пустым sockets={}
3. Проверить значения

**Expected Result:**
- nodes == []
- sockets == {}
- Объект создан успешно

---

## Test Case: TC-MODELS-010
**Title:** Item.__init__() with valid data

**Category:** Positive

**Description:** Проверка создания Item с валидными данными

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Item со всеми параметрами
2. Проверить значения

**Expected Result:**
- Все поля установлены
- Объект создан успешно

---

## Test Case: TC-MODELS-011
**Title:** Item.__post_init__() validation - rarity

**Category:** Negative

**Description:** Проверка валидации rarity в __post_init__

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Item с невалидным rarity
2. Проверить обработку ошибки

**Expected Result:**
- ValidationError при невалидном rarity
- Ошибка обработана корректно

---

## Test Case: TC-MODELS-012
**Title:** Item.__post_init__() validation - empty name/base

**Category:** Negative

**Description:** Проверка валидации пустого name/base

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Item с пустым name
2. Попытаться создать Item с пустым base
3. Проверить обработку ошибок

**Expected Result:**
- ValidationError при пустом name
- ValidationError при пустом base
- Ошибки обработаны корректно

---

## Test Case: TC-MODELS-013
**Title:** Item.__post_init__() validation - level_req

**Category:** Negative

**Description:** Проверка валидации level_req в __post_init__

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Item с невалидным level_req
2. Проверить обработку ошибки

**Expected Result:**
- ValidationError при невалидном level_req
- Ошибка обработана корректно

---

## Test Case: TC-MODELS-014
**Title:** Item.__post_init__() validation - quality range

**Category:** Negative

**Description:** Проверка валидации quality в __post_init__

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Item с quality < 0
2. Попытаться создать Item с quality > 30
3. Проверить обработку ошибок

**Expected Result:**
- ValidationError при quality < 0
- ValidationError при quality > 30
- Ошибки обработаны корректно

---

## Test Case: TC-MODELS-015
**Title:** Item.__str__() representation

**Category:** Positive

**Description:** Проверка строкового представления Item

**Preconditions:**
- Item создан

**Test Steps:**
1. Создать Item с различными параметрами
2. Вызвать str(item)
3. Проверить результат

**Expected Result:**
- Строка содержит все важные поля
- Формат соответствует ожидаемому
- Результат корректен

---

## Test Case: TC-MODELS-016
**Title:** Set.__init__() with items

**Category:** Positive

**Description:** Проверка создания Set с items

**Preconditions:**
- Item объекты созданы

**Test Steps:**
1. Создать список Item
2. Создать Set с items
3. Проверить значения

**Expected Result:**
- items содержит переданные Item объекты
- Объект создан успешно

---

## Test Case: TC-MODELS-017
**Title:** Set.__init__() with empty items

**Category:** Edge Case

**Description:** Проверка создания Set с пустым items

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Set с items=[]
2. Проверить значения

**Expected Result:**
- items == []
- Объект создан успешно

---

## Test Case: TC-MODELS-018
**Title:** Keystones.__init__() with all keystones

**Category:** Positive

**Description:** Проверка создания Keystones со всеми кистоунами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Keystones со всеми параметрами
2. Проверить значения

**Expected Result:**
- Все поля установлены
- Объект создан успешно

---

## Test Case: TC-MODELS-019
**Title:** Keystones.__iter__() iteration

**Category:** Positive

**Description:** Проверка итерации по Keystones

**Preconditions:**
- Keystones создан с некоторыми активными кистоунами

**Test Steps:**
1. Создать Keystones с некоторыми True значениями
2. Итерироваться по объекту
3. Проверить результаты

**Expected Result:**
- Итерация возвращает только True кистоуны
- Порядок корректен
- Результат корректен

---

## Test Case: TC-MODELS-020
**Title:** Keystones.__iter__() empty iteration

**Category:** Edge Case

**Description:** Проверка итерации по Keystones без активных кистоунов

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Keystones со всеми False значениями
2. Итерироваться по объекту
3. Проверить результат

**Expected Result:**
- Итерация возвращает пустую последовательность
- Результат корректен
