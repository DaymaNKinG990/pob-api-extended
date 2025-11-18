# Error Handling Integration Test Cases

## Module: tests/integrations/test_integration.py::TestErrorHandlingIntegration

### Overview
Интеграционные тест-кейсы для проверки обработки ошибок на уровне интеграции между компонентами.

---

## Test Case: TC-INT-ERROR-001
**Title:** Validation error propagates

**Category:** Negative

**Integration:** InputValidator

**Description:** Проверка распространения ошибок валидации

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться валидировать пустые bytes через InputValidator.validate_xml_bytes(b"")

**Expected Result:**
- Выбрасывается ValidationError

---

## Test Case: TC-INT-ERROR-002
**Title:** Parsing error propagates

**Category:** Negative

**Integration:** BuildInfoParser

**Description:** Проверка распространения ошибок парсинга

**Preconditions:**
- Нет

**Test Steps:**
1. Создать XML с невалидной структурой (только Skills элемент без Build)
2. Парсить XML в root элемент
3. Попытаться парсить build info через BuildInfoParser.parse()

**Expected Result:**
- Выбрасывается ParsingError

---

## Test Case: TC-INT-ERROR-003
**Title:** Factory handles errors

**Category:** Negative

**Integration:** BuildFactory

**Description:** Проверка обработки ошибок фабрикой

**Preconditions:**
- Нет

**Test Steps:**
1. Создать BuildFactory
2. Попытаться создать build из невалидного XML через factory.from_xml_bytes(b"invalid xml")

**Expected Result:**
- Выбрасывается ParsingError

---
