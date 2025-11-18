# Config Unit Test Cases

## Module: pobapi.config

### Overview
Юнит-тест-кейсы для модуля config, который содержит dataclass `Config` для конфигурации билда.

---

## Test Case: TC-CONFIG-001
**Title:** Config.__init__() with defaults

**Category:** Positive

**Description:** Проверка инициализации Config с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `Config()`
2. Проверить дефолтные значения

**Expected Result:**
- Дефолтные значения установлены корректно
- Объект создан успешно

---

## Test Case: TC-CONFIG-002
**Title:** Config.__init__() with all parameters

**Category:** Positive

**Description:** Проверка инициализации Config со всеми параметрами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config со всеми параметрами
2. Проверить значения

**Expected Result:**
- Все поля установлены
- Значения соответствуют переданным параметрам

---

## Test Case: TC-CONFIG-003
**Title:** Config resistance_penalty values

**Category:** Positive

**Description:** Проверка значений resistance_penalty

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с resistance_penalty=0
2. Создать Config с resistance_penalty=-30
3. Создать Config с resistance_penalty=-60
4. Проверить значения

**Expected Result:**
- Все валидные значения установлены корректно
- Результат корректен

---

## Test Case: TC-CONFIG-004
**Title:** Config enemy_level range

**Category:** Positive

**Description:** Проверка диапазона enemy_level (1-100)

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с enemy_level=1
2. Создать Config с enemy_level=100
3. Создать Config с enemy_level=50
4. Проверить значения

**Expected Result:**
- Все значения в диапазоне установлены корректно
- Результат корректен

---

## Test Case: TC-CONFIG-003-INVALID
**Title:** Config resistance_penalty invalid values validation

**Category:** Negative

**Description:** Проверка валидации невалидных значений resistance_penalty. Должна быть реализована валидация, которая отклоняет значения вне допустимого диапазона [0, -30, -60].

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Config с resistance_penalty=10
2. Попытаться создать Config с resistance_penalty=-100
3. Проверить, что оба вызова вызывают исключение

**Expected Result:**
- При создании Config с resistance_penalty=10 должно быть выброшено ValidationError (или ValueError, если дизайн выберет это) с сообщением, указывающим, что значение должно быть одним из [0, -30, -60]
- При создании Config с resistance_penalty=-100 должно быть выброшено ValidationError (или ValueError, если дизайн выберет это) с сообщением, указывающим, что значение должно быть одним из [0, -30, -60]
- Конструкция Config не должна завершаться успешно для невалидных значений
- Исключение должно содержать информативное сообщение об ошибке с указанием допустимых значений

---

## Test Case: TC-CONFIG-004-INVALID
**Title:** Config enemy_level invalid values validation

**Category:** Negative

**Description:** Проверка валидации невалидных значений enemy_level. Должна быть реализована валидация, которая отклоняет значения вне допустимого диапазона [1, 100].

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать Config с enemy_level=0
2. Попытаться создать Config с enemy_level=101
3. Попытаться создать Config с enemy_level=-1
4. Проверить, что все три вызова вызывают исключение

**Expected Result:**
- При создании Config с enemy_level=0 должно быть выброшено ValidationError (или ValueError, если дизайн выберет это) с сообщением, указывающим, что значение должно быть >= 1 и <= 100
- При создании Config с enemy_level=101 должно быть выброшено ValidationError (или ValueError, если дизайн выберет это) с сообщением, указывающим, что значение должно быть >= 1 и <= 100
- При создании Config с enemy_level=-1 должно быть выброшено ValidationError (или ValueError, если дизайн выберет это) с сообщением, указывающим, что значение должно быть >= 1 и <= 100
- Конструкция Config не должна завершаться успешно для невалидных значений
- Исключение должно содержать информативное сообщение об ошибке с указанием допустимого диапазона [1, 100]

---

## Test Case: TC-CONFIG-005
**Title:** Config boolean flags

**Category:** Positive

**Description:** Проверка всех boolean флагов конфигурации

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с различными boolean флагами
2. Проверить значения

**Expected Result:**
- Все флаги установлены корректно
- Дефолтные значения False
- Результат корректен

---

## Test Case: TC-CONFIG-006
**Title:** Config condition flags

**Category:** Positive

**Description:** Проверка флагов условий (is_stationary, is_moving, и т.д.)

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с condition флагами
2. Проверить значения

**Expected Result:**
- is_stationary, is_moving установлены
- is_on_full_life, is_on_low_life установлены
- is_on_full_energy_shield установлен
- Результат корректен

---

## Test Case: TC-CONFIG-007
**Title:** Config charge settings

**Category:** Positive

**Description:** Проверка настроек зарядов

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с настройками зарядов
2. Проверить значения

**Expected Result:**
- use_power_charges, max_power_charges установлены
- use_frenzy_charges, max_frenzy_charges установлены
- use_endurance_charges, max_endurance_charges установлены
- Результат корректен

---

## Test Case: TC-CONFIG-008
**Title:** Config buff flags

**Category:** Positive

**Description:** Проверка флагов баффов (onslaught, fortify, и т.д.)

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с buff флагами
2. Проверить значения

**Expected Result:**
- onslaught, fortify, tailwind установлены
- adrenaline, phasing установлены
- Результат корректен

---

## Test Case: TC-CONFIG-009
**Title:** Config curse levels

**Category:** Positive

**Description:** Проверка уровней проклятий

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с уровнями проклятий
2. Проверить значения

**Expected Result:**
- Все curse_* поля установлены
- Результат корректен

---

## Test Case: TC-CONFIG-010
**Title:** Config enemy settings

**Category:** Positive

**Description:** Проверка настроек врага

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с enemy настройками
2. Проверить значения

**Expected Result:**
- enemy_physical_reduction установлен
- enemy_hexproof, enemy_resistances установлены
- Результат корректен

---

## Test Case: TC-CONFIG-011
**Title:** Config map mods

**Category:** Positive

**Description:** Проверка модов карты

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Config с map mods
2. Проверить значения

**Expected Result:**
- less_recovery, no_regen установлены
- minus_max_resists, less_aoe установлены
- Результат корректен

---

## Test Case: TC-CONFIG-012
**Title:** Config dataclass behavior

**Category:** Positive

**Description:** Проверка поведения dataclass

**Preconditions:**
- Нет

**Test Steps:**
1. Создать два Config объекта с одинаковыми значениями
2. Создать Config объект с разными значениями
3. Проверить сравнение

**Expected Result:**
- Объекты с одинаковыми значениями равны
- Объекты с разными значениями не равны
- Dataclass поведение работает корректно
