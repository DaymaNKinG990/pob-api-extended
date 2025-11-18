# Factory Unit Test Cases

## Module: pobapi.factory

### Overview
Юнит-тест-кейсы для модуля factory, который отвечает за создание билдов из различных источников.

---

## Test Case: TC-FACTORY-001
**Title:** BuildFactory.__init__() with defaults

**Category:** Positive

**Description:** Проверка инициализации BuildFactory с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `BuildFactory()`
2. Проверить значения _parser и _http_client

**Expected Result:**
- factory._parser является экземпляром DefaultBuildParser
- factory._http_client is None

---

## Test Case: TC-FACTORY-002
**Title:** BuildFactory.__init__() with custom parser

**Category:** Positive

**Description:** Проверка инициализации BuildFactory с кастомным парсером

**Preconditions:**
- MockBuildParser создан

**Test Steps:**
1. Создать MockBuildParser
2. Вызвать `BuildFactory(parser=parser)`
3. Проверить, что используется кастомный парсер

**Expected Result:**
- factory._parser == parser
- Кастомный парсер установлен

---

## Test Case: TC-FACTORY-003
**Title:** BuildFactory.__init__() with custom HTTP client

**Category:** Positive

**Description:** Проверка инициализации BuildFactory с кастомным HTTP клиентом

**Preconditions:**
- MockHTTPClient создан

**Test Steps:**
1. Создать MockHTTPClient
2. Вызвать `BuildFactory(http_client=http_client)`
3. Проверить, что используется кастомный клиент

**Expected Result:**
- factory._http_client == http_client
- Кастомный клиент установлен

---

## Test Case: TC-FACTORY-004
**Title:** BuildFactory.from_import_code() with invalid code

**Category:** Negative

**Description:** Проверка метода from_import_code() с невалидным кодом

**Preconditions:**
- BuildFactory инициализирован

**Test Steps:**
1. Вызвать `factory.from_import_code("invalid_code")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidImportCodeError

---

## Test Case: TC-FACTORY-004a
**Title:** BuildFactory.from_import_code() with valid code

**Category:** Positive

**Description:** Проверка метода from_import_code() с валидным кодом и создание Build объекта

**Preconditions:**
- BuildFactory инициализирован
- Валидный import code создан (base64 encoded zlib compressed XML с известным class_name)

**Test Steps:**
1. Создать валидный import code из XML с class_name="Witch"
2. Создать BuildFactory экземпляр: `factory = BuildFactory()`
3. Вызвать `xml_bytes = factory.from_import_code(valid_code)`
4. Вызвать `build = factory.from_xml_bytes(xml_bytes)`
5. Проверить созданный Build объект

**Expected Result:**
- XML bytes успешно получены из import code
- Build объект успешно создан
- build.class_name == "Witch" (соответствует данным из import code)

---

## Test Case: TC-FACTORY-005
**Title:** BuildFactory.from_xml_bytes() with valid XML

**Category:** Positive

**Description:** Проверка метода from_xml_bytes() с валидными XML байтами

**Preconditions:**
- Валидные XML байты предоставлены

**Test Steps:**
1. Создать валидные XML байты
2. Вызвать `factory.from_xml_bytes(xml_bytes)`
3. Проверить созданный билд

**Expected Result:**
- Билд успешно создан
- build.class_name соответствует XML данным

---

## Test Case: TC-FACTORY-006
**Title:** BuildFactory.from_xml_bytes() with invalid XML

**Category:** Negative

**Description:** Проверка метода from_xml_bytes() с невалидными XML байтами

**Preconditions:**
- Невалидные XML байты предоставлены

**Test Steps:**
1. Вызвать `factory.from_xml_bytes(b"invalid xml")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ParsingError
- Сообщение содержит "Failed to parse XML"

---

## Test Case: TC-FACTORY-007
**Title:** BuildFactory.from_xml_bytes() with custom parser

**Category:** Positive

**Description:** Проверка метода from_xml_bytes() с кастомным парсером

**Preconditions:**
- BuildFactory инициализирован с кастомным парсером
- Валидные XML байты предоставлены

**Test Steps:**
1. Создать BuildFactory с MockBuildParser
2. Вызвать `factory.from_xml_bytes(xml_bytes)`
3. Проверить использование кастомного парсера

**Expected Result:**
- Билд создан
- build._parser == custom_parser

---

## Test Case: TC-FACTORY-008
**Title:** BuildFactory.from_url() with mock HTTP client

**Category:** Positive

**Description:** Проверка метода from_url() с мок HTTP клиентом

**Preconditions:**
- BuildFactory инициализирован с MockHTTPClient
- MockHTTPClient возвращает валидный import code

**Test Steps:**
1. Создать BuildFactory с MockHTTPClient
2. Вызвать `factory.from_url("https://pastebin.com/test")`
3. Проверить возвращаемые XML байты

**Expected Result:**
- Возвращаются валидные XML байты
- XML содержит элемент Build

---

## Test Case: TC-FACTORY-009
**Title:** BuildFactory.from_url() with default HTTP client

**Category:** Positive

**Description:** Проверка метода from_url() с дефолтным HTTP клиентом

**Preconditions:**
- BuildFactory инициализирован без HTTP клиента
- requests.get замокан

**Test Steps:**
1. Замокать requests.get
2. Замокать _fetch_xml_from_import_code
3. Вызвать `factory.from_url("https://pastebin.com/test")`
4. Проверить использование дефолтного клиента

**Expected Result:**
- Используется дефолтный HTTP клиент
- Возвращаются валидные XML байты

---

## Test Case: TC-FACTORY-010
**Title:** BuildFactory.async_from_url() with async HTTP client

**Category:** Positive

**Description:** Проверка асинхронного метода async_from_url() с async HTTP клиентом

**Preconditions:**
- BuildFactory инициализирован с MockAsyncHTTPClient
- MockAsyncHTTPClient возвращает валидный import code

**Test Steps:**
1. Создать BuildFactory с MockAsyncHTTPClient
2. Вызвать `await factory.async_from_url("https://pastebin.com/test")`
3. Проверить созданный билд

**Expected Result:**
- Билд успешно создан
- build.class_name соответствует ожидаемому

---

## Test Case: TC-FACTORY-011
**Title:** BuildFactory.async_from_url() without async client

**Category:** Negative

**Description:** Проверка асинхронного метода async_from_url() без async HTTP клиента

**Preconditions:**
- BuildFactory инициализирован без async HTTP клиента

**Test Steps:**
1. Вызвать `await factory.async_from_url("https://pastebin.com/test")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValueError
- Сообщение содержит "Async HTTP client is required"

---

## Test Case: TC-FACTORY-012
**Title:** BuildFactory.async_from_import_code() with valid code

**Category:** Positive

**Description:** Проверка асинхронного метода async_from_import_code() с валидным кодом

**Preconditions:**
- Валидный import code предоставлен

**Test Steps:**
1. Создать валидный import code
2. Вызвать `await factory.async_from_import_code(import_code)`
3. Проверить созданный билд

**Expected Result:**
- Билд успешно создан
- build.class_name соответствует ожидаемому

---

## Test Case: TC-FACTORY-016
**Title:** BuildFactory.async_from_import_code() with invalid code

**Category:** Negative

**Description:** Проверка async_from_import_code() с невалидным кодом

**Preconditions:**
- BuildFactory инициализирован

**Test Steps:**
1. Вызвать `await factory.async_from_import_code("invalid_code")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается InvalidImportCodeError

---

## Test Case: TC-FACTORY-013
**Title:** BuildFactory.from_xml_bytes() with missing required elements

**Category:** Negative

**Description:** Проверка метода from_xml_bytes() с XML без обязательных элементов

**Preconditions:**
- XML байты не содержат обязательные элементы

**Test Steps:**
1. Создать XML без Build элемента
2. Вызвать `factory.from_xml_bytes(xml_bytes)`
3. Перехватить исключение

**Expected Result:**
- Выбрасывается ParsingError или ValidationError

---

## Test Case: TC-FACTORY-014
**Title:** BuildFactory.from_xml_bytes() with empty XML

**Category:** Negative

**Description:** Проверка метода from_xml_bytes() с пустым XML

**Preconditions:**
- Пустые XML байты предоставлены

**Test Steps:**
1. Вызвать `factory.from_xml_bytes(b"")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ParsingError или ValidationError

---

## Test Case: TC-FACTORY-015
**Title:** BuildFactory.from_url() with network error

**Category:** Negative

**Description:** Проверка метода from_url() при сетевой ошибке

**Preconditions:**
- HTTP клиент выбрасывает сетевую ошибку

**Test Steps:**
1. Настроить MockHTTPClient для выброса NetworkError
2. Вызвать `factory.from_url("https://pastebin.com/test")`
3. Перехватить исключение

**Expected Result:**
- Выбрасывается NetworkError
