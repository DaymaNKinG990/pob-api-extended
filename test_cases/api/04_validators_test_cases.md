# Validators Test Cases

## Module: pobapi.validators

### Overview
Тест-кейсы для модуля validators, который отвечает за валидацию входных данных.

---

## Test Case: TC-VALIDATORS-001
**Title:** Validate valid pastebin.com URL

**Category:** Positive

**Description:** Проверка валидации валидного URL pastebin.com

**Preconditions:**
- Валидный pastebin.com URL предоставлен

**Test Steps:**
1. Вызвать `InputValidator.validate_url(url)` с валидным URL
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-VALIDATORS-002
**Title:** Validate URL with non-string type

**Category:** Negative

**Description:** Проверка валидации URL с неверным типом данных

**Preconditions:**
- URL предоставлен как не-строка (например, число)

**Test Steps:**
1. Вызвать `InputValidator.validate_url(123)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "URL must be a string"

---

## Test Case: TC-VALIDATORS-003
**Title:** Validate empty URL

**Category:** Negative

**Description:** Проверка валидации пустого URL

**Preconditions:**
- Пустая строка предоставлена как URL

**Test Steps:**
1. Вызвать `InputValidator.validate_url("")`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "URL cannot be empty"

---

## Test Case: TC-VALIDATORS-004
**Title:** Validate URL from non-pastebin domain

**Category:** Negative

**Description:** Проверка валидации URL с другого домена

**Preconditions:**
- URL предоставлен с домена, отличного от pastebin.com

**Test Steps:**
1. Вызвать `InputValidator.validate_url("https://example.com/test")`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "must be a pastebin.com link"

---

## Test Case: TC-VALIDATORS-005
**Title:** Validate valid import code

**Category:** Positive

**Description:** Проверка валидации валидного import code

**Preconditions:**
- Валидный import code предоставлен

**Test Steps:**
1. Вызвать `InputValidator.validate_import_code(code)` с валидным кодом
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-VALIDATORS-006
**Title:** Validate import code with non-string type

**Category:** Negative

**Description:** Проверка валидации import code с неверным типом данных

**Preconditions:**
- Import code предоставлен как не-строка

**Test Steps:**
1. Вызвать `InputValidator.validate_import_code(123)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "Import code must be a string"

---

## Test Case: TC-VALIDATORS-007
**Title:** Validate empty import code

**Category:** Negative

**Description:** Проверка валидации пустого import code

**Preconditions:**
- Пустая строка предоставлена как import code

**Test Steps:**
1. Вызвать `InputValidator.validate_import_code("")`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "Import code cannot be empty"

---

## Test Case: TC-VALIDATORS-008
**Title:** Validate valid XML bytes

**Category:** Positive

**Description:** Проверка валидации валидных XML байтов

**Preconditions:**
- Валидные XML байты предоставлены

**Test Steps:**
1. Вызвать `InputValidator.validate_xml_bytes(xml_bytes)` с валидными байтами
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-VALIDATORS-009
**Title:** Validate XML bytes with non-bytes type

**Category:** Negative

**Description:** Проверка валидации XML байтов с неверным типом данных

**Preconditions:**
- XML предоставлен как не-байты (например, строка)

**Test Steps:**
1. Вызвать `InputValidator.validate_xml_bytes("not bytes")`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "XML must be bytes"

---

## Test Case: TC-VALIDATORS-010
**Title:** Validate empty XML bytes

**Category:** Negative

**Description:** Проверка валидации пустых XML байтов

**Preconditions:**
- Пустые байты предоставлены

**Test Steps:**
1. Вызвать `InputValidator.validate_xml_bytes(b"")`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "XML cannot be empty"

---

## Test Case: TC-VALIDATORS-011
**Title:** Validate valid XML structure

**Category:** Positive

**Description:** Проверка валидации валидной XML структуры

**Preconditions:**
- Валидный XML root предоставлен

**Test Steps:**
1. Вызвать `XMLValidator.validate_build_structure(xml_root)` с валидным root
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Валидация проходит успешно
- Исключение не выбрасывается

---

## Test Case: TC-VALIDATORS-012
**Title:** Validate XML structure with None root

**Category:** Negative

**Description:** Проверка валидации XML структуры с None root

**Preconditions:**
- None предоставлен как xml_root

**Test Steps:**
1. Вызвать `XMLValidator.validate_build_structure(None)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "XML root is None"

---

## Test Case: TC-VALIDATORS-013
**Title:** Validate XML structure with missing Build element

**Category:** Negative

**Description:** Проверка валидации XML структуры без Build элемента

**Preconditions:**
- XML root не содержит элемент Build

**Test Steps:**
1. Вызвать `XMLValidator.validate_build_structure(xml_root)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "Build element not found in XML structure"

---

## Test Case: TC-VALIDATORS-014
**Title:** Validate XML structure with invalid root name

**Category:** Negative

**Description:** Проверка валидации XML структуры с неверным именем корневого элемента

**Preconditions:**
- XML root имеет неверное имя корневого элемента

**Test Steps:**
1. Вызвать `XMLValidator.validate_build_structure(xml_root)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "Invalid XML root element name"

---

## Test Case: TC-VALIDATORS-015
**Title:** Validate multiple valid URLs

**Category:** Positive

**Description:** Проверка валидации нескольких валидных URL

**Preconditions:**
- Несколько валидных pastebin.com URL предоставлены

**Test Steps:**
1. Вызвать `InputValidator.validate_url(url)` для каждого URL
2. Проверить, что все валидации проходят успешно

**Expected Result:**
- Все валидации проходят успешно
- Исключения не выбрасываются

---

## Test Case: TC-VALIDATORS-016
**Title:** Validate import code with special characters

**Category:** Edge Case

**Description:** Проверка валидации import code со специальными символами. Import codes используют URL-safe base64 кодирование и должны содержать только допустимые символы: A-Z, a-z, 0-9, `-` (дефис), `_` (подчеркивание). Любые другие специальные символы (например, `+`, `/`, `@`, `#`, `$`, `%`, пробелы и т.д.) недопустимы.

**Preconditions:**
- Import code содержит недопустимые специальные символы (не из набора URL-safe base64)

**Test Data:**
- `"test+code"` (содержит `+`, недопустимый символ)
- `"test/code"` (содержит `/`, недопустимый символ)
- `"test@code"` (содержит `@`, недопустимый символ)
- `"test code"` (содержит пробел, недопустимый символ)

**Test Steps:**
1. Вызвать `InputValidator.validate_import_code(code)` с каждым тестовым кодом
2. Проверить результат валидации

**Expected Result:**
- Валидация проходит успешно (валидатор проверяет только тип и непустоту, не проверяет формат)
- Примечание: `InputValidator.validate_import_code()` не проверяет формат кода, только что это непустая строка. Фактическая проверка формата происходит при декодировании в `_fetch_xml_from_import_code()`, где недопустимые символы вызовут `InvalidImportCodeError` с сообщением "Failed to decode import code"

---

## Test Case: TC-VALIDATORS-017
**Title:** Validate XML bytes with invalid encoding

**Category:** Edge Case

**Description:** Проверка валидации XML байтов с неверной кодировкой

**Preconditions:**
- XML байты имеют неверную кодировку

**Test Steps:**
1. Вызвать `InputValidator.validate_xml_bytes(xml_bytes)` с байтами неверной кодировки
2. Проверить обработку

**Expected Result:**
- Валидация проходит успешно (если байты валидны)
- Или выбрасывается соответствующее исключение

---

## Test Case: TC-VALIDATORS-018
**Title:** Validate XML structure with malformed XML

**Category:** Negative

**Description:** Проверка валидации XML структуры с некорректным XML

**Preconditions:**
- XML имеет некорректную структуру

**Test Steps:**
1. Вызвать `XMLValidator.validate_build_structure(xml_root)` с некорректным XML
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError` с сообщением "XML structure is malformed or missing required elements"
