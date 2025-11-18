# Model Validators Unit Test Cases

## Module: pobapi.model_validators

### Overview
Юнит-тест-кейсы для модуля model_validators, который содержит валидаторы для моделей данных.

---

## Test Case: TC-MODEL-VALIDATORS-001
**Title:** ModelValidator.validate_type() with valid type

**Category:** Positive

**Description:** Проверка статического метода validate_type() с валидным типом

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_type("test", str, "name")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-002
**Title:** ModelValidator.validate_type() with invalid type

**Category:** Negative

**Description:** Проверка статического метода validate_type() с неверным типом

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_type(123, str, "name")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "must be of type"

---

## Test Case: TC-MODEL-VALIDATORS-003
**Title:** ModelValidator.validate_type() with None (allowed)

**Category:** Edge Case

**Description:** Проверка статического метода validate_type() с None (разрешено)

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_type(None, str, "name")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- None разрешен

---

## Test Case: TC-MODEL-VALIDATORS-004
**Title:** ModelValidator.validate_range() with value in range

**Category:** Positive

**Description:** Проверка статического метода validate_range() со значением в диапазоне

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_range(5, min_value=1, max_value=10, field_name="level")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-005
**Title:** ModelValidator.validate_range() with value below minimum

**Category:** Negative

**Description:** Проверка статического метода validate_range() со значением ниже минимума

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_range(0, min_value=1, max_value=10, field_name="level")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "must be >="

---

## Test Case: TC-MODEL-VALIDATORS-006
**Title:** ModelValidator.validate_range() with value above maximum

**Category:** Negative

**Description:** Проверка статического метода validate_range() со значением выше максимума

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_range(20, min_value=1, max_value=10, field_name="level")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "must be <="

---

## Test Case: TC-MODEL-VALIDATORS-007
**Title:** ModelValidator.validate_range() with None (allowed)

**Category:** Edge Case

**Description:** Проверка статического метода validate_range() с None (разрешено)

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_range(None, min_value=1, max_value=10, field_name="level")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- None разрешен

---

## Test Case: TC-MODEL-VALIDATORS-008
**Title:** ModelValidator.validate_range() with non-numeric value

**Category:** Negative

**Description:** Проверка статического метода validate_range() с нечисловым значением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_range("not a number", min_value=1, max_value=10, field_name="level")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "must be numeric"

---

## Test Case: TC-MODEL-VALIDATORS-009
**Title:** ModelValidator.validate_choice() with valid choice

**Category:** Positive

**Description:** Проверка статического метода validate_choice() с валидным выбором

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_choice("Normal", ["Normal", "Magic", "Rare"], "rarity")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-010
**Title:** ModelValidator.validate_choice() with invalid choice

**Category:** Negative

**Description:** Проверка статического метода validate_choice() с невалидным выбором

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_choice("Invalid", ["Normal", "Magic"], "rarity")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "must be one of"

---

## Test Case: TC-MODEL-VALIDATORS-011
**Title:** ModelValidator.validate_choice() with None (allowed)

**Category:** Edge Case

**Description:** Проверка статического метода validate_choice() с None (разрешено)

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_choice(None, ["Normal", "Magic"], "rarity")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- None разрешен

---

## Test Case: TC-MODEL-VALIDATORS-012
**Title:** ModelValidator.validate_not_empty() with valid value

**Category:** Positive

**Description:** Проверка статического метода validate_not_empty() с валидным значением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_not_empty("test", "name")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-013
**Title:** ModelValidator.validate_not_empty() with None

**Category:** Negative

**Description:** Проверка статического метода validate_not_empty() с None

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_not_empty(None, "name")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "cannot be None"

---

## Test Case: TC-MODEL-VALIDATORS-014
**Title:** ModelValidator.validate_not_empty() with empty string

**Category:** Negative

**Description:** Проверка статического метода validate_not_empty() с пустой строкой

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_not_empty("", "name")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "cannot be empty"

---

## Test Case: TC-MODEL-VALIDATORS-015
**Title:** ModelValidator.validate_not_empty() with empty list

**Category:** Negative

**Description:** Проверка статического метода validate_not_empty() с пустым списком

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_not_empty([], "items")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "cannot be empty"

---

## Test Case: TC-MODEL-VALIDATORS-016
**Title:** ModelValidator.validate_positive() with positive value

**Category:** Positive

**Description:** Проверка статического метода validate_positive() с положительным значением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_positive(1, "value")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-017
**Title:** ModelValidator.validate_positive() with zero

**Category:** Negative

**Description:** Проверка статического метода validate_positive() с нулем

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_positive(0, "value")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "must be positive"

---

## Test Case: TC-MODEL-VALIDATORS-018
**Title:** ModelValidator.validate_positive() with negative value

**Category:** Negative

**Description:** Проверка статического метода validate_positive() с отрицательным значением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_positive(-1, "value")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "must be positive"

---

## Test Case: TC-MODEL-VALIDATORS-019
**Title:** ModelValidator.validate_positive() with None (allowed)

**Category:** Edge Case

**Description:** Проверка статического метода validate_positive() с None (разрешено)

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `ModelValidator.validate_positive(None, "value")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- None разрешен

---

## Test Case: TC-MODEL-VALIDATORS-020
**Title:** validate_gem_level() with valid level

**Category:** Positive

**Description:** Проверка функции validate_gem_level() с валидным уровнем

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_gem_level(20, "level")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-021
**Title:** validate_gem_level() with level too low

**Category:** Negative

**Description:** Проверка функции validate_gem_level() с уровнем ниже допустимого

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_gem_level(0, "level")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError

---

## Test Case: TC-MODEL-VALIDATORS-022
**Title:** validate_gem_level() with level too high

**Category:** Negative

**Description:** Проверка функции validate_gem_level() с уровнем выше допустимого

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_gem_level(31, "level")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError

---

## Test Case: TC-MODEL-VALIDATORS-023
**Title:** validate_gem_quality() with valid quality

**Category:** Positive

**Description:** Проверка функции validate_gem_quality() с валидным качеством

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_gem_quality(20, "quality")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-024
**Title:** validate_gem_quality() with quality too low

**Category:** Negative

**Description:** Проверка функции validate_gem_quality() с качеством ниже допустимого

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_gem_quality(-1, "quality")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError

---

## Test Case: TC-MODEL-VALIDATORS-025
**Title:** validate_gem_quality() with quality too high

**Category:** Negative

**Description:** Проверка функции validate_gem_quality() с качеством выше допустимого

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_gem_quality(31, "quality")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError

---

## Test Case: TC-MODEL-VALIDATORS-026
**Title:** validate_character_level() with valid level

**Category:** Positive

**Description:** Проверка функции validate_character_level() с валидным уровнем

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_character_level(90, "level")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-027
**Title:** validate_character_level() with level out of range

**Category:** Negative

**Description:** Проверка функции validate_character_level() с уровнем вне диапазона

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_character_level(101, "level")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError

---

## Test Case: TC-MODEL-VALIDATORS-028
**Title:** validate_rarity() with valid rarity

**Category:** Positive

**Description:** Проверка функции validate_rarity() с валидной редкостью

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_rarity("Unique", "rarity")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-029
**Title:** validate_rarity() with invalid rarity

**Category:** Negative

**Description:** Проверка функции validate_rarity() с невалидной редкостью

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_rarity("Invalid", "rarity")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError

---

## Test Case: TC-MODEL-VALIDATORS-030
**Title:** validate_item_level_req() with valid level

**Category:** Positive

**Description:** Проверка функции validate_item_level_req() с валидным уровнем

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_item_level_req(68, "level_req")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-MODEL-VALIDATORS-031
**Title:** validate_resistance_penalty() with valid penalty

**Category:** Positive

**Description:** Проверка функции validate_resistance_penalty() с валидным штрафом

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `validate_resistance_penalty(-60, "penalty")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается
