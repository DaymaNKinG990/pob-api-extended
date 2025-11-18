# HTTP Client Unit Test Cases

## Module: pobapi.util (HTTP Client implementation)

### Overview
Юнит-тест-кейсы для модуля HTTP Client, который реализует HTTPClient protocol через requests.

---

## Test Case: TC-HTTP-CLIENT-001
**Title:** _get_default_http_client() returns client

**Category:** Positive

**Description:** Проверка функции _get_default_http_client() для получения HTTP клиента

**Preconditions:**
- Кэш HTTP клиента очищен

**Test Steps:**
1. Вызвать `_get_default_http_client()`
2. Проверить результат

**Expected Result:**
- client is not None
- hasattr(client, "get")

---

## Test Case: TC-HTTP-CLIENT-002
**Title:** HTTPClient.get() successful request

**Category:** Positive

**Description:** Проверка метода get() для успешного HTTP запроса

**Preconditions:**
- requests.get замокан
- Mock response создан

**Test Steps:**
1. Замокать requests.get с успешным ответом
2. Получить HTTP клиент
3. Вызвать client.get("https://example.com", timeout=5.0)
4. Проверить результат

**Expected Result:**
- result == "test content"
- requests.get вызван с правильными параметрами

---

## Test Case: TC-HTTP-CLIENT-003
**Title:** HTTPClient.get() timeout error

**Category:** Negative

**Description:** Проверка метода get() для обработки timeout ошибки

**Preconditions:**
- requests.get замокан для выброса Timeout

**Test Steps:**
1. Замокать requests.get для выброса requests.Timeout
2. Получить HTTP клиент
3. Вызвать client.get()
4. Перехватить исключение

**Expected Result:**
- Выбрасывается NetworkError
- Сообщение содержит "Connection timed out"

---

## Test Case: TC-HTTP-CLIENT-004
**Title:** HTTPClient.get() connection error

**Category:** Negative

**Description:** Проверка метода get() для обработки connection error

**Preconditions:**
- requests.get замокан для выброса ConnectionError

**Test Steps:**
1. Замокать requests.get для выброса requests.ConnectionError
2. Получить HTTP клиент
3. Вызвать client.get()
4. Перехватить исключение

**Expected Result:**
- Выбрасывается NetworkError
- Сообщение содержит "Network connection failed"

---

## Test Case: TC-HTTP-CLIENT-005
**Title:** HTTPClient.get() HTTP error response

**Category:** Negative

**Description:** Проверка метода get() для обработки HTTP error response

**Preconditions:**
- requests.get замокан для выброса HTTPError

**Test Steps:**
1. Замокать requests.get для выброса requests.HTTPError
2. Получить HTTP клиент
3. Вызвать client.get()
4. Перехватить исключение

**Expected Result:**
- Выбрасывается NetworkError
- Сообщение содержит "HTTP error"

---

## Test Case: TC-HTTP-CLIENT-006
**Title:** HTTPClient.get() too many redirects

**Category:** Negative

**Description:** Проверка метода get() для обработки too many redirects

**Preconditions:**
- requests.get замокан для выброса TooManyRedirects

**Test Steps:**
1. Замокать requests.get для выброса requests.TooManyRedirects
2. Получить HTTP клиент
3. Вызвать client.get()
4. Перехватить исключение

**Expected Result:**
- Выбрасывается NetworkError
- Сообщение содержит "Too many redirects"

---

## Test Case: TC-HTTP-CLIENT-007
**Title:** HTTPClient.get() general request exception

**Category:** Negative

**Description:** Проверка метода get() для обработки общего request exception

**Preconditions:**
- requests.get замокан для выброса RequestException

**Test Steps:**
1. Замокать requests.get для выброса requests.RequestException
2. Получить HTTP клиент
3. Вызвать client.get()
4. Перехватить исключение

**Expected Result:**
- Выбрасывается NetworkError
- Сообщение содержит "Request failed"

---

## Test Case: TC-HTTP-CLIENT-008
**Title:** _fetch_xml_from_url() with custom HTTP client

**Category:** Positive

**Description:** Проверка функции _fetch_xml_from_url() с кастомным HTTP клиентом

**Preconditions:**
- Mock HTTP client создан
- _fetch_xml_from_import_code замокан

**Test Steps:**
1. Создать mock_client
2. Замокать _fetch_xml_from_import_code
3. Вызвать _fetch_xml_from_url() с custom client
4. Проверить результат

**Expected Result:**
- Возвращаются валидные XML байты
- mock_client.get вызван
- _get_default_http_client не вызван

---

## Test Case: TC-HTTP-CLIENT-009
**Title:** _fetch_xml_from_url() with invalid URL

**Category:** Negative

**Description:** Проверка функции _fetch_xml_from_url() с невалидным URL

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `_fetch_xml_from_url("https://example.com/test")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidURLError
- Невалидный URL обработан корректно
