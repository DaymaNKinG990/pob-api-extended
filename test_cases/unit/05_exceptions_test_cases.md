# Exceptions Unit Test Cases

## Module: pobapi.exceptions

### Overview
Юнит-тест-кейсы для модуля exceptions. Тесты проверяют классы исключений: наследование, возможность выброса и сохранение сообщений.

---

## Test Case: TC-EXCEPTIONS-001
**Title:** Verify PobAPIError inheritance from Exception

**Category:** Positive

**Description:** Проверка наследования класса PobAPIError от Exception

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `issubclass(PobAPIError, Exception)`
2. Проверить результат

**Expected Result:**
- Функция возвращает True
- PobAPIError является подклассом Exception

---

## Test Case: TC-EXCEPTIONS-002
**Title:** Verify InvalidImportCodeError inheritance from PobAPIError

**Category:** Positive

**Description:** Проверка наследования класса InvalidImportCodeError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `issubclass(InvalidImportCodeError, PobAPIError)`
2. Проверить результат

**Expected Result:**
- Функция возвращает True
- InvalidImportCodeError является подклассом PobAPIError

---

## Test Case: TC-EXCEPTIONS-003
**Title:** Verify InvalidURLError inheritance from PobAPIError

**Category:** Positive

**Description:** Проверка наследования класса InvalidURLError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `issubclass(InvalidURLError, PobAPIError)`
2. Проверить результат

**Expected Result:**
- Функция возвращает True
- InvalidURLError является подклассом PobAPIError

---

## Test Case: TC-EXCEPTIONS-004
**Title:** Verify NetworkError inheritance from PobAPIError

**Category:** Positive

**Description:** Проверка наследования класса NetworkError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `issubclass(NetworkError, PobAPIError)`
2. Проверить результат

**Expected Result:**
- Функция возвращает True
- NetworkError является подклассом PobAPIError

---

## Test Case: TC-EXCEPTIONS-005
**Title:** Verify ParsingError inheritance from PobAPIError

**Category:** Positive

**Description:** Проверка наследования класса ParsingError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `issubclass(ParsingError, PobAPIError)`
2. Проверить результат

**Expected Result:**
- Функция возвращает True
- ParsingError является подклассом PobAPIError

---

## Test Case: TC-EXCEPTIONS-006
**Title:** Verify ValidationError inheritance from PobAPIError

**Category:** Positive

**Description:** Проверка наследования класса ValidationError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `issubclass(ValidationError, PobAPIError)`
2. Проверить результат

**Expected Result:**
- Функция возвращает True
- ValidationError является подклассом PobAPIError

---

## Test Case: TC-EXCEPTIONS-007
**Title:** Raise PobAPIError with message

**Category:** Positive

**Description:** Проверка возможности выброса исключения PobAPIError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise PobAPIError("Test error")`
2. Перехватить исключение
3. Проверить тип исключения

**Expected Result:**
- Исключение успешно выброшено
- Тип исключения - PobAPIError

---

## Test Case: TC-EXCEPTIONS-008
**Title:** Raise InvalidImportCodeError with message

**Category:** Positive

**Description:** Проверка возможности выброса исключения InvalidImportCodeError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise InvalidImportCodeError("Invalid import code")`
2. Перехватить исключение
3. Проверить тип исключения

**Expected Result:**
- Исключение успешно выброшено
- Тип исключения - InvalidImportCodeError

---

## Test Case: TC-EXCEPTIONS-009
**Title:** Raise InvalidURLError with message

**Category:** Positive

**Description:** Проверка возможности выброса исключения InvalidURLError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise InvalidURLError("Invalid URL")`
2. Перехватить исключение
3. Проверить тип исключения

**Expected Result:**
- Исключение успешно выброшено
- Тип исключения - InvalidURLError

---

## Test Case: TC-EXCEPTIONS-010
**Title:** Raise NetworkError with message

**Category:** Positive

**Description:** Проверка возможности выброса исключения NetworkError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise NetworkError("Network error")`
2. Перехватить исключение
3. Проверить тип исключения

**Expected Result:**
- Исключение успешно выброшено
- Тип исключения - NetworkError

---

## Test Case: TC-EXCEPTIONS-011
**Title:** Raise ParsingError with message

**Category:** Positive

**Description:** Проверка возможности выброса исключения ParsingError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise ParsingError("Parsing error")`
2. Перехватить исключение
3. Проверить тип исключения

**Expected Result:**
- Исключение успешно выброшено
- Тип исключения - ParsingError

---

## Test Case: TC-EXCEPTIONS-012
**Title:** Raise ValidationError with message

**Category:** Positive

**Description:** Проверка возможности выброса исключения ValidationError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise ValidationError("Validation error")`
2. Перехватить исключение
3. Проверить тип исключения

**Expected Result:**
- Исключение успешно выброшено
- Тип исключения - ValidationError

---

## Test Case: TC-EXCEPTIONS-013
**Title:** Preserve error message in PobAPIError

**Category:** Positive

**Description:** Проверка сохранения сообщения об ошибке в исключении PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise PobAPIError("Test error")`
2. Перехватить исключение
3. Проверить, что сообщение соответствует ожидаемому

**Expected Result:**
- Сообщение об ошибке сохранено
- str(exception) == "Test error" или exception.args[0] == "Test error"

---

## Test Case: TC-EXCEPTIONS-014
**Title:** Preserve error message in InvalidImportCodeError

**Category:** Positive

**Description:** Проверка сохранения сообщения об ошибке в исключении InvalidImportCodeError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise InvalidImportCodeError("Invalid import code")`
2. Перехватить исключение
3. Проверить, что сообщение соответствует ожидаемому

**Expected Result:**
- Сообщение об ошибке сохранено
- Сообщение соответствует переданному значению

---

## Test Case: TC-EXCEPTIONS-015
**Title:** Catch child exception as base PobAPIError

**Category:** Positive

**Description:** Проверка перехвата дочернего исключения через базовый класс PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise InvalidImportCodeError("Error")`
2. Перехватить исключение как PobAPIError
3. Проверить успешность перехвата

**Expected Result:**
- Исключение успешно перехвачено
- Можно обработать все дочерние исключения через базовый класс

---

## Test Case: TC-EXCEPTIONS-016
**Title:** Catch specific exception type

**Category:** Positive

**Description:** Проверка перехвата конкретного типа исключения

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise InvalidImportCodeError("Error")`
2. Перехватить исключение как InvalidImportCodeError
3. Проверить успешность перехвата

**Expected Result:**
- Исключение успешно перехвачено
- Тип исключения определен корректно

---

## Test Case: TC-EXCEPTIONS-017
**Title:** Exception with empty message

**Category:** Edge Case

**Description:** Проверка обработки исключения с пустым сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise PobAPIError("")`
2. Перехватить исключение
3. Проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Сообщение пустое, но доступно

---

## Test Case: TC-EXCEPTIONS-018
**Title:** Exception with special characters in message

**Category:** Edge Case

**Description:** Проверка обработки исключения со специальными символами в сообщении

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise PobAPIError("Test: error & message <with> symbols")`
2. Перехватить исключение
3. Проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Специальные символы сохранены корректно
