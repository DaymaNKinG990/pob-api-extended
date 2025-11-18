# Calculator Mirage Unit Test Cases

## Module: pobapi.calculator.mirage

### Overview
Юнит-тест-кейсы для модуля calculator.mirage, который отвечает за расчет миражей (Mirage Archer, Saviour и т.д.).

---

## Test Case: TC-CALC-MIRAGE-001
**Title:** MirageStats.__init__() basic initialization

**Category:** Positive

**Description:** Проверка базовой инициализации MirageStats

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `MirageStats(name="Test Mirage")`
2. Проверить значения атрибутов

**Expected Result:**
- stats.name == "Test Mirage"
- stats.count == 1
- stats.damage_multiplier == 1.0
- stats.speed_multiplier == 1.0
- stats.dps == 0.0
- stats.breakdown is None

---

## Test Case: TC-CALC-MIRAGE-002
**Title:** MirageStats.__init__() with all values

**Category:** Positive

**Description:** Проверка инициализации MirageStats со всеми значениями

**Preconditions:**
- DamageBreakdown создан

**Test Steps:**
1. Создать DamageBreakdown
2. Вызвать MirageStats со всеми параметрами
3. Проверить значения

**Expected Result:**
- Все значения установлены корректно
- stats.count == 3
- stats.damage_multiplier == 0.8
- stats.breakdown == breakdown

---

## Test Case: TC-CALC-MIRAGE-003
**Title:** MirageCalculator.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации MirageCalculator

**Preconditions:**
- Mock ModifierSystem и DamageCalculator созданы

**Test Steps:**
1. Создать MirageCalculator с mock объектами
2. Проверить инициализацию

**Expected Result:**
- calc.modifiers == mock_modifiers
- calc.damage_calc == mock_damage_calc

---

## Test Case: TC-CALC-MIRAGE-004
**Title:** MirageCalculator.calculate_mirage_archer() not triggered

**Category:** Positive

**Description:** Проверка метода calculate_mirage_archer() когда не триггерен

**Preconditions:**
- Контекст с triggeredByMirageArcher=False

**Test Steps:**
1. Создать контекст с triggeredByMirageArcher=False
2. Вызвать `calculate_mirage_archer("Arc", context)`
3. Проверить результат

**Expected Result:**
- result is None
- Не триггерен обработан корректно

---

## Test Case: TC-CALC-MIRAGE-005
**Title:** MirageCalculator.calculate_mirage_archer() triggered

**Category:** Positive

**Description:** Проверка метода calculate_mirage_archer() когда триггерен

**Preconditions:**
- Контекст с triggeredByMirageArcher=True
- Mock модификаторы настроены

**Test Steps:**
1. Создать контекст с triggeredByMirageArcher=True
2. Настроить mock модификаторы и damage calculator
3. Вызвать calculate_mirage_archer()
4. Проверить результат

**Expected Result:**
- result is not None
- result.name содержит "Mirage Archers"
- result.count == 1
- damage_multiplier и speed_multiplier рассчитаны
- breakdown присутствует

---

## Test Case: TC-CALC-MIRAGE-006
**Title:** MirageCalculator.calculate_saviour() wrong skill

**Category:** Positive

**Description:** Проверка метода calculate_saviour() для неправильного скилла

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать calculate_saviour() для неправильного скилла
2. Проверить результат

**Expected Result:**
- result is None
- Неправильный скилл обработан корректно

---

## Test Case: TC-CALC-MIRAGE-007
**Title:** MirageCalculator.calculate_saviour() correct skill

**Category:** Positive

**Description:** Проверка метода calculate_saviour() для правильного скилла

**Preconditions:**
- Контекст с правильным скиллом
- Mock модификаторы настроены

**Test Steps:**
1. Создать контекст с правильным скиллом
2. Настроить mock модификаторы
3. Вызвать calculate_saviour()
4. Проверить результат

**Expected Result:**
- result is not None
- Результат корректен

---

## Test Case: TC-CALC-MIRAGE-008
**Title:** MirageCalculator.calculate_saviour() dual wield same

**Category:** Positive

**Description:** Проверка метода calculate_saviour() для dual wield с одинаковыми скиллами

**Preconditions:**
- Контекст с dual wield

**Test Steps:**
1. Создать контекст с dual wield
2. Вызвать calculate_saviour()
3. Проверить результат

**Expected Result:**
- Результат корректен
- Dual wield обработан

---

## Test Case: TC-CALC-MIRAGE-009
**Title:** MirageCalculator.calculate_tawhoas_chosen() wrong skill

**Category:** Positive

**Description:** Проверка метода calculate_tawhoas_chosen() для неправильного скилла

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать calculate_tawhoas_chosen() для неправильного скилла
2. Проверить результат

**Expected Result:**
- result is None
- Неправильный скилл обработан корректно

---

## Test Case: TC-CALC-MIRAGE-010
**Title:** MirageCalculator.calculate_tawhoas_chosen() correct skill

**Category:** Positive

**Description:** Проверка метода calculate_tawhoas_chosen() для правильного скилла

**Preconditions:**
- Контекст с правильным скиллом
- Mock модификаторы настроены

**Test Steps:**
1. Создать контекст с правильным скиллом
2. Настроить mock модификаторы
3. Вызвать calculate_tawhoas_chosen()
4. Проверить результат

**Expected Result:**
- result is not None
- Результат корректен

---

## Test Case: TC-CALC-MIRAGE-011
**Title:** MirageCalculator.calculate_sacred_wisps() not triggered

**Category:** Positive

**Description:** Проверка метода calculate_sacred_wisps() когда не триггерен

**Preconditions:**
- Контекст с triggeredBySacredWisps=False

**Test Steps:**
1. Создать контекст с triggeredBySacredWisps=False
2. Вызвать calculate_sacred_wisps()
3. Проверить результат

**Expected Result:**
- result is None
- Не триггерен обработан корректно

---

## Test Case: TC-CALC-MIRAGE-012
**Title:** MirageCalculator.calculate_sacred_wisps() triggered

**Category:** Positive

**Description:** Проверка метода calculate_sacred_wisps() когда триггерен

**Preconditions:**
- Контекст с triggeredBySacredWisps=True
- Mock модификаторы настроены

**Test Steps:**
1. Создать контекст с triggeredBySacredWisps=True
2. Настроить mock модификаторы
3. Вызвать calculate_sacred_wisps()
4. Проверить результат

**Expected Result:**
- result is not None
- Результат корректен

---

## Test Case: TC-CALC-MIRAGE-013
**Title:** MirageCalculator.calculate_generals_cry() not triggered

**Category:** Positive

**Description:** Проверка метода calculate_generals_cry() когда не триггерен

**Preconditions:**
- Контекст с triggeredByGeneralsCry=False

**Test Steps:**
1. Создать контекст с triggeredByGeneralsCry=False
2. Вызвать calculate_generals_cry()
3. Проверить результат

**Expected Result:**
- result is None
- Не триггерен обработан корректно

---

## Test Case: TC-CALC-MIRAGE-014
**Title:** MirageCalculator.calculate_generals_cry() triggered

**Category:** Positive

**Description:** Проверка метода calculate_generals_cry() когда триггерен

**Preconditions:**
- Контекст с triggeredByGeneralsCry=True
- Mock модификаторы настроены

**Test Steps:**
1. Создать контекст с triggeredByGeneralsCry=True
2. Настроить mock модификаторы
3. Вызвать calculate_generals_cry()
4. Проверить результат

**Expected Result:**
- result is not None
- Результат корректен

---

## Test Case: TC-CALC-MIRAGE-015
**Title:** MirageCalculator.calculate_all_mirages() none

**Category:** Edge Case

**Description:** Проверка метода calculate_all_mirages() когда нет миражей

**Preconditions:**
- Контекст без триггеров миражей

**Test Steps:**
1. Создать контекст без триггеров
2. Вызвать calculate_all_mirages()
3. Проверить результат

**Expected Result:**
- result == []
- Отсутствие миражей обработано корректно

---

## Test Case: TC-CALC-MIRAGE-016
**Title:** MirageCalculator.calculate_all_mirages() some mirages

**Category:** Positive

**Description:** Проверка метода calculate_all_mirages() с некоторыми миражями

**Preconditions:**
- Контекст с некоторыми триггерами

**Test Steps:**
1. Создать контекст с некоторыми триггерами
2. Вызвать calculate_all_mirages()
3. Проверить результат

**Expected Result:**
- len(result) > 0
- Результат корректен

---

## Test Case: TC-CALC-MIRAGE-017
**Title:** MirageCalculator.calculate_all_mirages() multiple mirages

**Category:** Positive

**Description:** Проверка метода calculate_all_mirages() с несколькими миражями

**Preconditions:**
- Контекст с несколькими триггерами

**Test Steps:**
1. Создать контекст с несколькими триггерами
2. Вызвать calculate_all_mirages()
3. Проверить результат

**Expected Result:**
- len(result) > 1
- Все миражи рассчитаны
- Результат корректен

---

## Test Case: TC-CALC-MIRAGE-018
**Title:** MirageCalculator.calculate_mirage_archer() None context

**Category:** Edge Case

**Description:** Проверка метода calculate_mirage_archer() с None контекстом. Calculator should validate context at entry and normalize None to empty dict, then return None because triggeredByMirageArcher defaults to False.

**Preconditions:**
- MirageCalculator initialized with mock ModifierSystem and DamageCalculator
- Mock modifiers configured to return default values

**Test Steps:**
1. Configure mock modifiers to return default values for Mirage Archer stats
2. Configure mock damage calculator to return valid DPS and breakdown
3. Call `calculate_mirage_archer("Arc", None)` with None context
4. Assert that result is None (because triggeredByMirageArcher is False by default in empty context)

**Expected Result:**
- Calculator normalizes None context to empty dict {} at method entry (guard-clause behavior)
- Method does not raise any exception
- result is None (assert result is None)
- None context is handled gracefully without errors

---

## Test Case: TC-CALC-MIRAGE-019
**Title:** MirageCalculator.calculate_saviour() None context

**Category:** Edge Case

**Description:** Проверка метода calculate_saviour() с None контекстом. Calculator should validate context at entry and normalize None to empty dict, then return MirageStats because skill_name matches "Reflection".

**Preconditions:**
- MirageCalculator initialized with mock ModifierSystem and DamageCalculator
- Mock modifiers configured to return default values

**Test Steps:**
1. Configure mock modifiers to return default values for Saviour stats
2. Configure mock damage calculator to return valid DPS and breakdown
3. Call `calculate_saviour("Reflection", None)` with None context and valid skill name
4. Assert that result is not None (assert result is not None)
5. Assert that result is instance of MirageStats with correct attributes

**Expected Result:**
- Calculator normalizes None context to empty dict {} at method entry (guard-clause behavior)
- Method does not raise any exception
- result is not None (assert result is not None)
- result is instance of MirageStats
- result.name contains "Mirage Warriors"
- result.count, result.damage_multiplier, result.dps are set correctly
- None context is handled gracefully without errors
