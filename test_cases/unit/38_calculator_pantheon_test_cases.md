# Calculator Pantheon Unit Test Cases

## Module: pobapi.calculator.pantheon

### Overview
Юнит-тест-кейсы для модуля calculator.pantheon, который отвечает за обработку Pantheon бонусов.

---

## Test Case: TC-CALC-PANTHEON-001
**Title:** PantheonSoul.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации PantheonSoul

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `PantheonSoul(name="Test Soul", mods=["+10% to Fire Resistance"])`
2. Проверить значения атрибутов

**Expected Result:**
- soul.name == "Test Soul"
- soul.mods == ["+10% to Fire Resistance"]

---

## Test Case: TC-CALC-PANTHEON-002
**Title:** PantheonSoul.__init__() multiple mods

**Category:** Positive

**Description:** Проверка инициализации PantheonSoul с несколькими модификаторами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать список mods
2. Вызвать PantheonSoul с несколькими mods
3. Проверить результат

**Expected Result:**
- soul.mods == mods
- Все модификаторы установлены

---

## Test Case: TC-CALC-PANTHEON-003
**Title:** PantheonGod.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации PantheonGod

**Preconditions:**
- PantheonSoul создан

**Test Steps:**
1. Создать PantheonSoul
2. Вызвать `PantheonGod(name="The Brine King", souls=[soul])`
3. Проверить значения атрибутов

**Expected Result:**
- god.name == "The Brine King"
- len(god.souls) == 1
- god.souls[0] == soul

---

## Test Case: TC-CALC-PANTHEON-004
**Title:** PantheonGod.__init__() multiple souls

**Category:** Positive

**Description:** Проверка инициализации PantheonGod с несколькими souls

**Preconditions:**
- Несколько PantheonSoul созданы

**Test Steps:**
1. Создать несколько PantheonSoul
2. Вызвать PantheonGod с несколькими souls
3. Проверить результат

**Expected Result:**
- len(god.souls) == 2
- Все souls установлены

---

## Test Case: TC-CALC-PANTHEON-005
**Title:** PantheonTools.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации PantheonTools

**Preconditions:**
- Mock ModifierSystem создан

**Test Steps:**
1. Создать PantheonTools с mock_modifiers
2. Проверить инициализацию

**Expected Result:**
- tools.modifiers == mock_modifiers
- tools.parser is not None

---

## Test Case: TC-CALC-PANTHEON-006
**Title:** PantheonTools.apply_soul_mod() empty souls

**Category:** Edge Case

**Description:** Проверка метода apply_soul_mod() для бога без souls

**Preconditions:**
- PantheonGod с пустым списком souls

**Test Steps:**
1. Создать PantheonGod с souls=[]
2. Вызвать `tools.apply_soul_mod(god)`
3. Проверить результат

**Expected Result:**
- mock_modifiers.add_modifiers не вызван
- Пустой список обработан корректно

---

## Test Case: TC-CALC-PANTHEON-007
**Title:** PantheonTools.apply_soul_mod() no parsed mods

**Category:** Edge Case

**Description:** Проверка метода apply_soul_mod() когда parser возвращает пустой список

**Preconditions:**
- Parser замокан для возврата []

**Test Steps:**
1. Создать PantheonSoul с невалидными mods
2. Замокать parser для возврата []
3. Вызвать apply_soul_mod()
4. Проверить результат

**Expected Result:**
- mock_modifiers.add_modifiers не вызван
- Пустой список обработан корректно

---

## Test Case: TC-CALC-PANTHEON-008
**Title:** PantheonTools.apply_soul_mod() with parsed mods

**Category:** Positive

**Description:** Проверка метода apply_soul_mod() с распарсенными модификаторами

**Preconditions:**
- Parser замокан для возврата модификаторов

**Test Steps:**
1. Создать PantheonSoul с валидными mods
2. Замокать parser для возврата модификаторов
3. Вызвать apply_soul_mod()
4. Проверить результат

**Expected Result:**
- mock_modifiers.add_modifiers вызван
- Модификаторы добавлены с source prefix
- Результат корректен

---

## Test Case: TC-CALC-PANTHEON-009
**Title:** PantheonTools.apply_soul_mod() multiple souls

**Category:** Positive

**Description:** Проверка метода apply_soul_mod() с несколькими souls

**Preconditions:**
- PantheonGod с несколькими souls

**Test Steps:**
1. Создать PantheonGod с несколькими souls
2. Замокать parser для возврата модификаторов
3. Вызвать apply_soul_mod()
4. Проверить результат

**Expected Result:**
- Модификаторы от всех souls применены
- Результат корректен

---

## Test Case: TC-CALC-PANTHEON-010
**Title:** PantheonTools.apply_pantheon() None pantheon

**Category:** Edge Case

**Description:** Проверка метода apply_pantheon() с None pantheon

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `tools.apply_pantheon(None)`
2. Проверить результат

**Expected Result:**
- None обработан корректно
- mock_modifiers не вызван

---

## Test Case: TC-CALC-PANTHEON-011
**Title:** PantheonTools.apply_pantheon() major only

**Category:** Positive

**Description:** Проверка метода apply_pantheon() только с major soul

**Preconditions:**
- Pantheon с только major soul

**Test Steps:**
1. Создать Pantheon с только major soul
2. Вызвать apply_pantheon()
3. Проверить результат

**Expected Result:**
- Модификаторы от major soul применены
- Результат корректен

---

## Test Case: TC-CALC-PANTHEON-012
**Title:** PantheonTools.apply_pantheon() minor only

**Category:** Positive

**Description:** Проверка метода apply_pantheon() только с minor soul

**Preconditions:**
- Pantheon с только minor soul

**Test Steps:**
1. Создать Pantheon с только minor soul
2. Вызвать apply_pantheon()
3. Проверить результат

**Expected Result:**
- Модификаторы от minor soul применены
- Результат корректен

---

## Test Case: TC-CALC-PANTHEON-013
**Title:** PantheonTools.apply_pantheon() both souls

**Category:** Positive

**Description:** Проверка метода apply_pantheon() с обоими souls

**Preconditions:**
- Pantheon с major и minor souls

**Test Steps:**
1. Создать Pantheon с обоими souls
2. Вызвать apply_pantheon()
3. Проверить результат

**Expected Result:**
- Модификаторы от обоих souls применены
- Результат корректен

---

## Test Case: TC-CALC-PANTHEON-014
**Title:** PantheonTools.create_god() with souls

**Category:** Positive

**Description:** Проверка метода create_god() для создания бога с souls

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать create_god() с параметрами
2. Проверить результат

**Expected Result:**
- PantheonGod создан корректно
- Все souls установлены
- Результат корректен

---

## Test Case: TC-CALC-PANTHEON-015
**Title:** PantheonTools.create_god() empty souls

**Category:** Edge Case

**Description:** Проверка метода create_god() с пустым списком souls

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать create_god() с souls=[]
2. Проверить результат

**Expected Result:**
- PantheonGod создан с пустым списком souls
- Результат корректен
