# Interfaces Unit Test Cases

## Module: pobapi.interfaces

### Overview
Юнит-тест-кейсы для модуля interfaces, который содержит Protocol классы и абстрактные классы.

---

## Test Case: TC-INTERFACES-001
**Title:** HTTPClient protocol implementation check

**Category:** Positive

**Description:** Проверка реализации HTTPClient protocol

**Preconditions:**
- Mock объект создан с методом get

**Test Steps:**
1. Создать mock объект с методом get
2. Проверить isinstance(mock_client, HTTPClient)
3. Вызвать метод get

**Expected Result:**
- isinstance(mock_client, HTTPClient) == True
- mock_client.get() возвращает ожидаемое значение

---

## Test Case: TC-INTERFACES-002
**Title:** HTTPClient protocol method call

**Category:** Positive

**Description:** Проверка вызова метода HTTPClient protocol (покрывает строку 27)

**Preconditions:**
- MockHTTPClient класс реализует protocol

**Test Steps:**
1. Создать MockHTTPClient
2. Вызвать client.get("http://example.com", timeout=5.0)
3. Проверить результат и isinstance

**Expected Result:**
- Метод возвращает корректное значение
- isinstance(client, HTTPClient) == True

---

## Test Case: TC-INTERFACES-003
**Title:** HTTPClient protocol used in util

**Category:** Positive

**Description:** Проверка использования HTTPClient protocol в util (покрывает строку 27)

**Preconditions:**
- Mock HTTP client создан с spec=HTTPClient

**Test Steps:**
1. Создать mock_client с spec=HTTPClient
2. Вызвать mock_client.get()
3. Проверить результат

**Expected Result:**
- Protocol используется корректно
- Метод возвращает ожидаемое значение

---

## Test Case: TC-INTERFACES-004
**Title:** AsyncHTTPClient protocol implementation check

**Category:** Positive

**Description:** Проверка реализации AsyncHTTPClient protocol

**Preconditions:**
- Async mock функция создана

**Test Steps:**
1. Создать async mock функцию get
2. Присвоить mock_client.get = mock_get
3. Проверить isinstance(mock_client, AsyncHTTPClient)

**Expected Result:**
- isinstance(mock_client, AsyncHTTPClient) == True

---

## Test Case: TC-INTERFACES-005
**Title:** AsyncHTTPClient protocol method call

**Category:** Positive

**Description:** Проверка вызова метода AsyncHTTPClient protocol (покрывает строку 42)

**Preconditions:**
- MockAsyncHTTPClient класс реализует protocol

**Test Steps:**
1. Создать MockAsyncHTTPClient
2. Вызвать await client.get("http://example.com", timeout=5.0)
3. Проверить результат и isinstance

**Expected Result:**
- Метод возвращает корректное значение
- isinstance(client, AsyncHTTPClient) == True

---

## Test Case: TC-INTERFACES-006
**Title:** XMLParser abstract class implementation

**Category:** Positive

**Description:** Проверка реализации XMLParser абстрактного класса

**Preconditions:**
- ConcreteParser класс наследуется от XMLParser

**Test Steps:**
1. Создать ConcreteParser класс с методом parse
2. Создать экземпляр parser
3. Вызвать parser.parse(b"<root></root>")
4. Проверить результат

**Expected Result:**
- Парсер успешно создан
- parse() возвращает ожидаемый результат

---

## Test Case: TC-INTERFACES-007
**Title:** XMLParser abstract class raises error

**Category:** Negative

**Description:** Проверка, что XMLParser выбрасывает ошибку при попытке создания без реализации

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать XMLParser() напрямую
2. Перехватить исключение

**Expected Result:**
- Выбрасывается TypeError
- Абстрактный класс нельзя инстанцировать

---

## Test Case: TC-INTERFACES-008
**Title:** BuildParser abstract class implementation

**Category:** Positive

**Description:** Проверка реализации BuildParser абстрактного класса

**Preconditions:**
- ConcreteParser класс наследуется от BuildParser

**Test Steps:**
1. Создать ConcreteParser с методами parse_build_info, parse_skills, parse_items, parse_trees
2. Создать экземпляр parser
3. Вызвать все методы
4. Проверить результаты

**Expected Result:**
- Парсер успешно создан
- Все методы возвращают ожидаемые результаты

---

## Test Case: TC-INTERFACES-009
**Title:** BuildParser abstract class raises error

**Category:** Negative

**Description:** Проверка, что BuildParser выбрасывает ошибку при попытке создания без реализации

**Preconditions:**
- Нет

**Test Steps:**
1. Попытаться создать BuildParser() напрямую
2. Перехватить исключение

**Expected Result:**
- Выбрасывается TypeError
- Абстрактный класс нельзя инстанцировать

---

## Test Case: TC-INTERFACES-010
**Title:** BuildData protocol with mock implementation

**Category:** Positive

**Description:** Проверка BuildData protocol с mock реализацией (покрывает строки 110, 115, 120, 125, 130, 135, 140, 145)

**Preconditions:**
- Mock объект создан со всеми требуемыми свойствами

**Test Steps:**
1. Создать mock_build со всеми свойствами
2. Проверить isinstance(mock_build, BuildData)
3. Проверить доступность всех свойств

**Expected Result:**
- isinstance(mock_build, BuildData) == True
- Все свойства доступны и имеют ожидаемые значения

---

## Test Case: TC-INTERFACES-011
**Title:** BuildData protocol with real PathOfBuildingAPI object

**Category:** Positive

**Description:** Проверка BuildData protocol с реальным PathOfBuildingAPI объектом (покрывает Protocol property access)

**Preconditions:**
- Валидный билд создан через builder

**Test Steps:**
1. Создать билд через create_build()
2. Настроить билд (класс, уровень, дерево, скиллы)
3. Вызвать builder.build()
4. Проверить доступность всех свойств

**Expected Result:**
- Все свойства доступны через hasattr
- Доступ к свойствам покрывает Protocol property definitions
