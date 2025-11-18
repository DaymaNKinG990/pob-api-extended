# Async Util Unit Test Cases

## Module: pobapi.async_util

### Overview
Юнит-тест-кейсы для модуля async_util, который содержит асинхронные версии утилитарных функций.

---

## Test Case: TC-ASYNC-UTIL-001
**Title:** _fetch_xml_from_url_async() with valid URL

**Category:** Positive

**Description:** Проверка асинхронной функции _fetch_xml_from_url_async() с валидным URL

**Preconditions:**
- MockAsyncHTTPClient создан
- Валидный import code в response

**Test Steps:**
1. Создать MockAsyncHTTPClient с валидным import code
2. Вызвать await _fetch_xml_from_url_async()
3. Проверить результат

**Expected Result:**
- Функция успешно выполняется
- Возвращаются валидные XML байты

---

## Test Case: TC-ASYNC-UTIL-002
**Title:** _fetch_xml_from_url_async() with invalid URL

**Category:** Negative

**Description:** Проверка асинхронной функции _fetch_xml_from_url_async() с невалидным URL

**Preconditions:**
- MockAsyncHTTPClient создан

**Test Steps:**
1. Создать MockAsyncHTTPClient
2. Вызвать await _fetch_xml_from_url_async("https://example.com/test", client)
3. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidURLError
- Невалидный URL обработан корректно

---

## Test Case: TC-ASYNC-UTIL-003
**Title:** _fetch_xml_from_url_async() without HTTP client

**Category:** Negative

**Description:** Проверка асинхронной функции _fetch_xml_from_url_async() без HTTP клиента

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать await _fetch_xml_from_url_async("https://pastebin.com/test", None)
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValueError
- Сообщение содержит "Async HTTP client is required"

---

## Test Case: TC-ASYNC-UTIL-004
**Title:** _fetch_xml_from_url_async() with network error

**Category:** Negative

**Description:** Проверка асинхронной функции _fetch_xml_from_url_async() при сетевой ошибке

**Preconditions:**
- MockAsyncHTTPClient настроен для выброса исключения

**Test Steps:**
1. Создать MockAsyncHTTPClient с should_raise=Exception("Network error")
2. Вызвать await _fetch_xml_from_url_async()
3. Перехватить исключение

**Expected Result:**
- Выбрасывается NetworkError
- Сообщение содержит "Async request failed"

---

## Test Case: TC-ASYNC-UTIL-005
**Title:** _fetch_xml_from_import_code_async() with empty string

**Category:** Negative

**Description:** Проверка асинхронной функции _fetch_xml_from_import_code_async() с пустой строкой

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать await _fetch_xml_from_import_code_async("")
2. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidImportCodeError

---

## Test Case: TC-ASYNC-UTIL-006
**Title:** _fetch_xml_from_import_code_async() with None value

**Category:** Negative

**Description:** Проверка асинхронной функции _fetch_xml_from_import_code_async() с None значением

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать await _fetch_xml_from_import_code_async(None)
2. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidImportCodeError

---

## Test Case: TC-ASYNC-UTIL-007
**Title:** _fetch_xml_from_import_code_async() with invalid base64

**Category:** Negative

**Description:** Проверка асинхронной функции _fetch_xml_from_import_code_async() с невалидным base64

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать await _fetch_xml_from_import_code_async("invalid_base64!!!")
2. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidImportCodeError
- Сообщение содержит "Failed to decode"

---

## Test Case: TC-ASYNC-UTIL-008
**Title:** _fetch_xml_from_import_code_async() with invalid zlib

**Category:** Negative

**Description:** Проверка асинхронной функции _fetch_xml_from_import_code_async() с невалидным zlib

**Preconditions:**
- Валидный base64, но невалидный zlib

**Test Steps:**
1. Создать валидный base64 из невалидных zlib данных
2. Вызвать await _fetch_xml_from_import_code_async(invalid_zlib)
3. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidImportCodeError
- Сообщение содержит "Failed to decompress"
