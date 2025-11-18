# Exceptions Test Cases

## Module: pobapi.exceptions

### Overview
Тест-кейсы для модуля exceptions, который содержит все пользовательские исключения библиотеки.

---

## Test Case: TC-EXCEPTIONS-001
**Title:** Verify PobAPIError inheritance

**Category:** Positive

**Description:** Проверка наследования PobAPIError от Exception

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить, что `PobAPIError` является подклассом `Exception`
2. Использовать `issubclass(PobAPIError, Exception)`

**Expected Result:**
- `PobAPIError` наследуется от `Exception`
- Проверка возвращает True

---

## Test Case: TC-EXCEPTIONS-002
**Title:** Verify InvalidImportCodeError inheritance

**Category:** Positive

**Description:** Проверка наследования InvalidImportCodeError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить, что `InvalidImportCodeError` является подклассом `PobAPIError`
2. Использовать `issubclass(InvalidImportCodeError, PobAPIError)`

**Expected Result:**
- `InvalidImportCodeError` наследуется от `PobAPIError`
- Проверка возвращает True

---

## Test Case: TC-EXCEPTIONS-003
**Title:** Verify InvalidURLError inheritance

**Category:** Positive

**Description:** Проверка наследования InvalidURLError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить, что `InvalidURLError` является подклассом `PobAPIError`
2. Использовать `issubclass(InvalidURLError, PobAPIError)`

**Expected Result:**
- `InvalidURLError` наследуется от `PobAPIError`
- Проверка возвращает True

---

## Test Case: TC-EXCEPTIONS-004
**Title:** Verify NetworkError inheritance

**Category:** Positive

**Description:** Проверка наследования NetworkError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить, что `NetworkError` является подклассом `PobAPIError`
2. Использовать `issubclass(NetworkError, PobAPIError)`

**Expected Result:**
- `NetworkError` наследуется от `PobAPIError`
- Проверка возвращает True

---

## Test Case: TC-EXCEPTIONS-005
**Title:** Verify ParsingError inheritance

**Category:** Positive

**Description:** Проверка наследования ParsingError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить, что `ParsingError` является подклассом `PobAPIError`
2. Использовать `issubclass(ParsingError, PobAPIError)`

**Expected Result:**
- `ParsingError` наследуется от `PobAPIError`
- Проверка возвращает True

---

## Test Case: TC-EXCEPTIONS-006
**Title:** Verify ValidationError inheritance

**Category:** Positive

**Description:** Проверка наследования ValidationError от PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить, что `ValidationError` является подклассом `PobAPIError`
2. Использовать `issubclass(ValidationError, PobAPIError)`

**Expected Result:**
- `ValidationError` наследуется от `PobAPIError`
- Проверка возвращает True

---

## Test Case: TC-EXCEPTIONS-007
**Title:** Raise PobAPIError with message

**Category:** Positive

**Description:** Проверка возможности выброса PobAPIError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise PobAPIError("Test error")`
2. Перехватить исключение и проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Сообщение сохранено и доступно

---

## Test Case: TC-EXCEPTIONS-008
**Title:** Raise InvalidImportCodeError with message

**Category:** Positive

**Description:** Проверка возможности выброса InvalidImportCodeError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise InvalidImportCodeError("Invalid import code")`
2. Перехватить исключение и проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Сообщение сохранено и доступно

---

## Test Case: TC-EXCEPTIONS-009
**Title:** Raise InvalidURLError with message

**Category:** Positive

**Description:** Проверка возможности выброса InvalidURLError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise InvalidURLError("Invalid URL")`
2. Перехватить исключение и проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Сообщение сохранено и доступно

---

## Test Case: TC-EXCEPTIONS-010
**Title:** Raise NetworkError with message

**Category:** Positive

**Description:** Проверка возможности выброса NetworkError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise NetworkError("Network error")`
2. Перехватить исключение и проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Сообщение сохранено и доступно

---

## Test Case: TC-EXCEPTIONS-011
**Title:** Raise ParsingError with message

**Category:** Positive

**Description:** Проверка возможности выброса ParsingError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise ParsingError("Parsing error")`
2. Перехватить исключение и проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Сообщение сохранено и доступно

---

## Test Case: TC-EXCEPTIONS-012
**Title:** Raise ValidationError with message

**Category:** Positive

**Description:** Проверка возможности выброса ValidationError с сообщением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise ValidationError("Validation error")`
2. Перехватить исключение и проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Сообщение сохранено и доступно

---

## Test Case: TC-EXCEPTIONS-013
**Title:** Preserve error message in PobAPIError

**Category:** Positive

**Description:** Проверка сохранения сообщения об ошибке в PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise PobAPIError("Test error")`
2. Перехватить исключение и проверить, что сообщение соответствует ожидаемому

**Expected Result:**
- Сообщение об ошибке сохранено корректно
- Сообщение соответствует переданному значению

---

## Test Case: TC-EXCEPTIONS-014
**Title:** Preserve error message in InvalidImportCodeError

**Category:** Positive

**Description:** Проверка сохранения сообщения об ошибке в InvalidImportCodeError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `raise InvalidImportCodeError("Invalid import code")`
2. Перехватить исключение и проверить, что сообщение соответствует ожидаемому

**Expected Result:**
- Сообщение об ошибке сохранено корректно
- Сообщение соответствует переданному значению

---

## Test Case: TC-EXCEPTIONS-015
**Title:** Catch PobAPIError as base exception

**Category:** Positive

**Description:** Проверка перехвата всех дочерних исключений через PobAPIError

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать дочернее исключение (например, InvalidImportCodeError)
2. Перехватить его как PobAPIError

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
1. Вызвать InvalidImportCodeError
2. Перехватить его как InvalidImportCodeError

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
2. Перехватить исключение и проверить сообщение

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
2. Перехватить исключение и проверить сообщение

**Expected Result:**
- Исключение успешно выброшено
- Специальные символы сохранены корректно
