# Validators Unit Test Cases

## Module: pobapi.validators

### Overview
Юнит-тест-кейсы для модуля validators. Тесты проверяют статические методы классов валидации с различными входными данными.

---

## Test Case: TC-VALIDATORS-001
**Title:** InputValidator.validate_url() with valid pastebin.com URL

**Category:** Positive

**Description:** Проверка статического метода validate_url() с валидным pastebin.com URL

**Preconditions:**
- Валидный pastebin.com URL предоставлен

**Test Steps:**
1. Вызвать `InputValidator.validate_url("https://pastebin.com/abc123")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Метод выполняется без исключений
- Валидация проходит успешно

---

## Test Case: TC-VALIDATORS-002
**Title:** InputValidator.validate_url() with non-string type

**Category:** Negative

**Description:** Проверка статического метода validate_url() с неверным типом данных

**Preconditions:**
- URL предоставлен как не-строка (например, число)

**Test Steps:**
1. Вызвать `InputValidator.validate_url(123)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "URL must be a string"

---

## Test Case: TC-VALIDATORS-003
**Title:** InputValidator.validate_url() with empty string

**Category:** Negative

**Description:** Проверка статического метода validate_url() с пустой строкой

**Preconditions:**
- Пустая строка предоставлена как URL

**Test Steps:**
1. Вызвать `InputValidator.validate_url("")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "URL cannot be empty"

---

## Test Case: TC-VALIDATORS-004
**Title:** InputValidator.validate_url() with non-pastebin domain

**Category:** Negative

**Description:** Проверка статического метода validate_url() с URL другого домена

**Preconditions:**
- URL предоставлен с домена, отличного от pastebin.com

**Test Steps:**
1. Вызвать `InputValidator.validate_url("https://example.com/test")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "must be a pastebin.com link"

---

## Test Case: TC-VALIDATORS-005
**Title:** InputValidator.validate_import_code() with valid code

**Category:** Positive

**Description:** Проверка статического метода validate_import_code() с валидным кодом

**Preconditions:**
- Валидный import code предоставлен

**Test Steps:**
1. Вызвать `InputValidator.validate_import_code("eNqVkM1qwzAQhF8lz7kHXwIhB5NCaQq9+BAw1lq7YFm7WpNC3r1rJ...")`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Метод выполняется без исключений
- Валидация проходит успешно

---

## Test Case: TC-VALIDATORS-006
**Title:** InputValidator.validate_import_code() with non-string type

**Category:** Negative

**Description:** Проверка статического метода validate_import_code() с неверным типом данных

**Preconditions:**
- Import code предоставлен как не-строка

**Test Steps:**
1. Вызвать `InputValidator.validate_import_code(123)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Import code must be a string"

---

## Test Case: TC-VALIDATORS-007
**Title:** InputValidator.validate_import_code() with empty string

**Category:** Negative

**Description:** Проверка статического метода validate_import_code() с пустой строкой

**Preconditions:**
- Пустая строка предоставлена как import code

**Test Steps:**
1. Вызвать `InputValidator.validate_import_code("")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Import code cannot be empty"

---

## Test Case: TC-VALIDATORS-008
**Title:** InputValidator.validate_xml_bytes() with valid XML bytes

**Category:** Positive

**Description:** Проверка статического метода validate_xml_bytes() с валидными XML байтами

**Preconditions:**
- Валидные XML байты предоставлены

**Test Steps:**
1. Вызвать `InputValidator.validate_xml_bytes(b'<?xml version="1.0"?><root><Build/></root>')`
2. Проверить, что исключение не выбрасывается

**Expected Result:**
- Метод выполняется без исключений
- Валидация проходит успешно

---

## Test Case: TC-VALIDATORS-009
**Title:** InputValidator.validate_xml_bytes() with non-bytes type

**Category:** Negative

**Description:** Проверка статического метода validate_xml_bytes() с неверным типом данных

**Preconditions:**
- XML предоставлен как не-байты (например, строка)

**Test Steps:**
1. Вызвать `InputValidator.validate_xml_bytes("not bytes")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "XML must be bytes"

---

## Test Case: TC-VALIDATORS-010
**Title:** InputValidator.validate_xml_bytes() with empty bytes

**Category:** Negative

**Description:** Проверка статического метода validate_xml_bytes() с пустыми байтами

**Preconditions:**
- Пустые байты предоставлены

**Test Steps:**
1. Вызвать `InputValidator.validate_xml_bytes(b"")`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "XML cannot be empty"

---

## Test Case: TC-VALIDATORS-011
**Title:** XMLValidator.validate_build_structure() with valid XML

**Category:** Positive

**Description:** Проверка статического метода validate_build_structure() с валидной XML структурой

**Preconditions:**
- Валидный XML root предоставлен со всеми необходимыми элементами

**Test Steps:**
1. Создать валидный XML root
2. Вызвать `XMLValidator.validate_build_structure(xml_root)`
3. Проверить, что исключение не выбрасывается

**Expected Result:**
- Метод выполняется без исключений
- Валидация проходит успешно

---

## Test Case: TC-VALIDATORS-012
**Title:** XMLValidator.validate_build_structure() with None root

**Category:** Negative

**Description:** Проверка статического метода validate_build_structure() с None в качестве root

**Preconditions:**
- None предоставлен как xml_root

**Test Steps:**
1. Вызвать `XMLValidator.validate_build_structure(None)`
2. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "XML root is None"

---

## Test Case: TC-VALIDATORS-013
**Title:** XMLValidator.validate_build_structure() with missing Build element

**Category:** Negative

**Description:** Проверка статического метода validate_build_structure() при отсутствии элемента Build

**Preconditions:**
- XML root не содержит элемент Build

**Test Steps:**
1. Создать XML root без Build элемента
2. Вызвать `XMLValidator.validate_build_structure(xml_root)`
3. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Required element 'Build' not found"

---

## Test Case: TC-VALIDATORS-014
**Title:** XMLValidator.validate_build_structure() with missing Skills element

**Category:** Negative

**Description:** Проверка статического метода validate_build_structure() при отсутствии элемента Skills

**Preconditions:**
- XML root не содержит элемент Skills

**Test Steps:**
1. Создать XML root без Skills элемента
2. Вызвать `XMLValidator.validate_build_structure(xml_root)`
3. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Required element 'Skills' not found"

---

## Test Case: TC-VALIDATORS-015
**Title:** XMLValidator.validate_build_structure() with missing Items element

**Category:** Negative

**Description:** Проверка статического метода validate_build_structure() при отсутствии элемента Items

**Preconditions:**
- XML root не содержит элемент Items

**Test Steps:**
1. Создать XML root без Items элемента
2. Вызвать `XMLValidator.validate_build_structure(xml_root)`
3. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Required element 'Items' not found"

---

## Test Case: TC-VALIDATORS-016
**Title:** XMLValidator.validate_build_structure() with missing Tree element

**Category:** Negative

**Description:** Проверка статического метода validate_build_structure() при отсутствии элемента Tree

**Preconditions:**
- XML root не содержит элемент Tree

**Test Steps:**
1. Создать XML root без Tree элемента
2. Вызвать `XMLValidator.validate_build_structure(xml_root)`
3. Перехватить исключение

**Expected Result:**
- Выбрасывается ValidationError
- Сообщение содержит "Required element 'Tree' not found"

---

## Test Case: TC-VALIDATORS-017
**Title:** InputValidator.validate_url() with multiple valid URLs (parametrized)

**Category:** Positive

**Description:** Проверка статического метода validate_url() с несколькими валидными URL (параметризованный тест)

**Preconditions:**
- Несколько валидных pastebin.com URL предоставлены

**Test Steps:**
1. Вызвать `InputValidator.validate_url(url)` для каждого URL
2. Проверить, что все валидации проходят успешно

**Expected Result:**
- Все валидации проходят без исключений
- Метод работает корректно для всех валидных URL

---

## Test Case: TC-VALIDATORS-018
**Title:** InputValidator.validate_import_code() with multiple valid codes (parametrized)

**Category:** Positive

**Description:** Проверка статического метода validate_import_code() с несколькими валидными кодами (параметризованный тест)

**Preconditions:**
- Несколько валидных import code предоставлены

**Test Steps:**
1. Вызвать `InputValidator.validate_import_code(code)` для каждого кода
2. Проверить, что все валидации проходят успешно

**Expected Result:**
- Все валидации проходят без исключений
- Метод работает корректно для всех валидных кодов
