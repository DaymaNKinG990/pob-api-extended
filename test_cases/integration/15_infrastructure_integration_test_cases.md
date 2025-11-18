# Infrastructure Integration Test Cases

## Module: tests/integrations/test_infrastructure_integration.py

### Overview
Интеграционные тест-кейсы для проверки взаимодействия инфраструктурных компонентов (HTTPClient, Cache, BuildFactory).

---

## Test Case: TC-INT-INFRA-001
**Title:** Factory with custom HTTP client

**Category:** Positive

**Integration:** BuildFactory ↔ HTTPClient

**Description:** Проверка работы BuildFactory с кастомным HTTP client

**Preconditions:**
- Нет

**Test Steps:**
1. Создать кастомный HTTPClient (mock)
2. Создать BuildFactory с кастомным HTTP client
3. Использовать factory для загрузки build

**Expected Result:**
- factory использует кастомный HTTP client
- build загружен успешно

---

## Test Case: TC-INT-INFRA-002
**Title:** Factory from URL uses HTTP client

**Category:** Positive

**Integration:** BuildFactory ↔ HTTPClient

**Description:** Проверка, что BuildFactory.from_url() использует HTTP client

**Preconditions:**
- Нет

**Test Steps:**
1. Создать mock HTTPClient
2. Создать BuildFactory с mock HTTP client
3. Загрузить build через factory.from_url()
4. Проверить, что HTTP client вызван

**Expected Result:**
- HTTP client вызван
- build загружен успешно

---

## Test Case: TC-INT-INFRA-003
**Title:** Factory async with custom HTTP client

**Category:** Positive

**Integration:** BuildFactory ↔ AsyncHTTPClient

**Description:** Проверка работы BuildFactory с кастомным async HTTP client

**Preconditions:**
- Нет

**Test Steps:**
1. Создать кастомный AsyncHTTPClient (mock)
2. Создать BuildFactory с кастомным async HTTP client
3. Использовать factory для асинхронной загрузки build

**Expected Result:**
- factory использует кастомный async HTTP client
- build загружен успешно

---

## Test Case: TC-INT-INFRA-004
**Title:** Cache with factory

**Category:** Positive

**Integration:** Cache ↔ BuildFactory

**Description:** Проверка работы Cache с BuildFactory

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Cache
2. Создать BuildFactory с cache
3. Загрузить build через factory
4. Проверить, что данные кешируются

**Expected Result:**
- Данные кешируются
- Повторная загрузка использует cache

---

## Test Case: TC-INT-INFRA-005
**Title:** Cache stores and retrieves data

**Category:** Positive

**Integration:** Cache

**Description:** Проверка хранения и получения данных из Cache

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Cache
2. Сохранить данные через cache.set()
3. Получить данные через cache.get()
4. Проверить соответствие

**Expected Result:**
- Данные сохранены
- Данные получены корректно

---

## Test Case: TC-INT-INFRA-006
**Title:** Cache integration with API parsing

**Category:** Positive

**Integration:** Cache ↔ PathOfBuildingAPI ↔ BuildFactory

**Description:** Проверка интеграции Cache с парсингом API

**Preconditions:**
- Есть sample_xml fixture

**Test Steps:**
1. Создать Cache
2. Создать BuildFactory с cache
3. Парсить XML через factory
4. Проверить, что результаты кешируются

**Expected Result:**
- Результаты кешируются
- Повторный парсинг использует cache

---

## Test Case: TC-INT-INFRA-007
**Title:** HTTP client with caching strategy

**Category:** Positive

**Integration:** HTTPClient ↔ Cache

**Description:** Проверка работы HTTP client с caching strategy

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Cache
2. Создать HTTPClient с cache
3. Выполнить HTTP запрос
4. Проверить, что ответ кешируется

**Expected Result:**
- Ответ кешируется
- Повторный запрос использует cache

---

## Test Case: TC-INT-INFRA-008
**Title:** Factory HTTP cache integration

**Category:** Positive

**Integration:** BuildFactory ↔ HTTPClient ↔ Cache

**Description:** Проверка интеграции BuildFactory с HTTP client и cache

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Cache
2. Создать HTTPClient с cache
3. Создать BuildFactory с HTTP client
4. Загрузить build через factory.from_url()
5. Проверить кеширование

**Expected Result:**
- build загружен
- Данные кешируются

---

## Test Case: TC-INT-INFRA-009
**Title:** Factory handles HTTP errors

**Category:** Negative

**Integration:** BuildFactory ↔ HTTPClient

**Description:** Проверка обработки HTTP ошибок в BuildFactory

**Preconditions:**
- Нет

**Test Steps:**
1. Создать mock HTTPClient, который выбрасывает ошибку
2. Создать BuildFactory с mock HTTP client
3. Попытаться загрузить build через factory.from_url()
4. Проверить обработку ошибки

**Expected Result:**
- Ошибка обработана корректно
- Выбрасывается соответствующее исключение

---

## Test Case: TC-INT-INFRA-010
**Title:** Cache handles eviction

**Category:** Positive

**Integration:** Cache

**Description:** Проверка обработки eviction в Cache

**Preconditions:**
- Нет

**Test Steps:**
1. Создать Cache с ограниченным размером
2. Добавить данные до превышения лимита
3. Проверить, что старые данные удаляются (eviction)

**Expected Result:**
- Eviction работает корректно
- Cache не превышает лимит

---
