# Util Test Cases

## Module: pobapi.util

### Overview
Тест-кейсы для модуля util, который содержит утилитарные функции для работы с данными.

---

## Test Case: TC-UTIL-001
**Title:** Fetch XML from valid pastebin.com URL

**Category:** Positive

**Description:** Проверка получения XML из валидного pastebin.com URL

**Preconditions:**
- Валидный pastebin.com URL доступен
- URL содержит валидный XML контент

**Test Steps:**
1. Вызвать `_fetch_xml_from_url("https://pastebin.com/valid_id")`
2. Проверить возвращаемый XML

**Expected Result:**
- XML успешно получен
- Возвращаемые данные являются валидным XML

---

## Test Case: TC-UTIL-002
**Title:** Fetch XML from invalid URL domain

**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном домене URL

**Preconditions:**
- URL с невалидным доменом предоставлен

**Test Steps:**
1. Вызвать `_fetch_xml_from_url("https://example.com/test")`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `InvalidURLError`

---

## Test Case: TC-UTIL-003
**Title:** Handle network timeout error

**Category:** Negative

**Description:** Проверка обработки ошибки таймаута сети

**Preconditions:**
- URL вызывает таймаут сети

**Test Steps:**
1. Замокировать `requests.get` для выброса `Timeout`
2. Вызвать `_fetch_xml_from_url("https://pastebin.com/test")`
3. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `NetworkError` с сообщением "Connection timed out"

---

## Test Case: TC-UTIL-004
**Title:** Handle network connection error

**Category:** Negative

**Description:** Проверка обработки ошибки соединения сети

**Preconditions:**
- URL вызывает ошибку соединения

**Test Steps:**
1. Замокировать `requests.get` для выброса `ConnectionError`
2. Вызвать `_fetch_xml_from_url("https://pastebin.com/test")`
3. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `NetworkError` с сообщением "Network connection failed"

---

## Test Case: TC-UTIL-005
**Title:** Handle too many redirects error

**Category:** Negative

**Description:** Проверка обработки ошибки слишком большого количества редиректов

**Preconditions:**
- URL вызывает ошибку редиректов

**Test Steps:**
1. Замокировать `requests.get` для выброса `TooManyRedirects`
2. Вызвать `_fetch_xml_from_url("https://pastebin.com/test")`
3. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `NetworkError` с сообщением "Too many redirects"

---

## Test Case: TC-UTIL-006
**Title:** Handle generic request exception

**Category:** Negative

**Description:** Проверка обработки общей ошибки запроса

**Preconditions:**
- URL вызывает общую ошибку запроса

**Test Steps:**
1. Замокировать `requests.get` для выброса `RequestException`
2. Вызвать `_fetch_xml_from_url("https://pastebin.com/test")`
3. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `NetworkError` с сообщением "Request failed"

---

## Test Case: TC-UTIL-007
**Title:** Handle HTTP error (404, 500, etc.)

**Category:** Negative

**Description:** Проверка обработки HTTP ошибок

**Preconditions:**
- URL возвращает HTTP ошибку

**Test Steps:**
1. Замокировать `requests.get` для выброса `HTTPError` с кодом 404
2. Вызвать `_fetch_xml_from_url("https://pastebin.com/test")`
3. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `NetworkError` с сообщением "HTTP error"

---

## Test Case: TC-UTIL-008
**Title:** Fetch XML from valid import code

**Category:** Positive

**Description:** Проверка получения XML из валидного import code

**Preconditions:**
- Валидный import code предоставлен

**Test Steps:**
1. Вызвать `_fetch_xml_from_import_code(valid_code)`
2. Проверить возвращаемый XML

**Expected Result:**
- XML успешно получен и декодирован
- Возвращаемые данные являются валидным XML

---

## Test Case: TC-UTIL-009
**Title:** Fetch XML from empty import code

**Category:** Negative

**Description:** Проверка обработки пустого import code

**Preconditions:**
- Пустой import code предоставлен

**Test Steps:**
1. Вызвать `_fetch_xml_from_import_code("")`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `InvalidImportCodeError` с сообщением "Failed to decode"

---

## Test Case: TC-UTIL-010
**Title:** Fetch XML from None import code

**Category:** Negative

**Description:** Проверка обработки None import code

**Preconditions:**
- None предоставлен как import code

**Test Steps:**
1. Вызвать `_fetch_xml_from_import_code(None)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `InvalidImportCodeError`

---

## Test Case: TC-UTIL-011
**Title:** Fetch XML from invalid base64 import code

**Category:** Negative

**Description:** Проверка обработки невалидного base64 в import code

**Preconditions:**
- Import code содержит невалидный base64

**Test Steps:**
1. Вызвать `_fetch_xml_from_import_code("invalid_base64!!!")`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `InvalidImportCodeError` с сообщением "Failed to decode"

---

## Test Case: TC-UTIL-012
**Title:** Fetch XML from invalid zlib import code

**Category:** Negative

**Description:** Проверка обработки невалидного zlib в import code

**Preconditions:**
- Import code содержит валидный base64, но невалидный zlib

**Test Steps:**
1. Создать валидный base64 из не сжатых данных
2. Вызвать `_fetch_xml_from_import_code(invalid_zlib_code)`
3. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `InvalidImportCodeError` с сообщением "Failed to decompress"

---

## Test Case: TC-UTIL-013
**Title:** Get stat from text list with matching prefix

**Category:** Positive

**Description:** Проверка получения статистики из списка текста с совпадающим префиксом

**Preconditions:**
- Список текста содержит строку с нужным префиксом

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique", "Quality: 20"], "Rarity: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Возвращается "Unique"

---

## Test Case: TC-UTIL-014
**Title:** Get stat from text list with different prefix

**Category:** Positive

**Description:** Проверка получения статистики с другим префиксом

**Preconditions:**
- Список текста содержит строку с другим префиксом

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique", "Quality: 20"], "Quality: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Возвращается "20"

---

## Test Case: TC-UTIL-015
**Title:** Get stat for exact match (boolean)

**Category:** Positive

**Description:** Проверка получения статистики для точного совпадения (boolean)

**Preconditions:**
- Список текста содержит точное совпадение

**Test Steps:**
1. Вызвать `_get_stat(["Shaper Item", "Elder Item"], "Shaper Item")`
2. Проверить возвращаемое значение

**Expected Result:**
- Возвращается True

---

## Test Case: TC-UTIL-016
**Title:** Get stat when stat not found

**Category:** Edge Case

**Description:** Проверка получения статистики, когда она не найдена

**Preconditions:**
- Список текста не содержит нужную статистику

**Test Steps:**
1. Вызвать `_get_stat(["Rarity: Unique"], "Quality: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Возвращается пустая строка ""

---

## Test Case: TC-UTIL-017
**Title:** Get stat from empty text list

**Category:** Edge Case

**Description:** Проверка получения статистики из пустого списка

**Preconditions:**
- Список текста пуст

**Test Steps:**
1. Вызвать `_get_stat([], "Rarity: ")`
2. Проверить возвращаемое значение

**Expected Result:**
- Возвращается пустая строка ""

---

## Test Case: TC-UTIL-018
**Title:** Extract item text after Implicits marker

**Category:** Positive

**Description:** Проверка извлечения текста предмета после маркера Implicits

**Preconditions:**
- Список текста содержит маркер "Implicits: N"

**Test Steps:**
1. Вызвать `_item_text(["Rarity: Unique", "Test Item", "Implicits: 2", "+10 to maximum Life", "+20 to maximum Mana"])`
2. Проверить возвращаемые элементы

**Expected Result:**
- Возвращаются элементы после маркера Implicits
- Элементы "+10 to maximum Life" и "+20 to maximum Mana" присутствуют
- Элемент "Rarity: Unique" отсутствует

---

## Test Case: TC-UTIL-019
**Title:** Extract item text without Implicits marker

**Category:** Edge Case

**Description:** Проверка извлечения текста предмета без маркера Implicits

**Preconditions:**
- Список текста не содержит маркер Implicits

**Test Steps:**
1. Вызвать `_item_text(["Rarity: Unique", "Test Item"])`
2. Преобразовать результат в список
3. Проверить, что список пуст

**Expected Result:**
- Возвращается пустой список

---

## Test Case: TC-UTIL-020
**Title:** Extract item text with Implicits: 1 but no items

**Category:** Edge Case

**Description:** Проверка извлечения текста предмета с Implicits: 1, но без элементов

**Preconditions:**
- Список текста содержит "Implicits: 1", но нет элементов после него

**Test Steps:**
1. Вызвать `_item_text(["Rarity: Unique", "Test Item", "Implicits: 1"])`
2. Проверить возвращаемые элементы

**Expected Result:**
- Возвращается пустой список

---

## Test Case: TC-UTIL-021
**Title:** HTTP client caching

**Category:** Positive

**Description:** Проверка кэширования HTTP клиента

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `_get_default_http_client()` первый раз и сохранить результат в `client1`
2. Вызвать `_get_default_http_client()` второй раз и сохранить результат в `client2`
3. Проверить, что `id(client1) == id(client2)` (один и тот же экземпляр объекта)

**Expected Result:**
- `client1` и `client2` являются одним и тем же объектом (идентичны по `id()`)
- HTTP клиент кэшируется и переиспользуется между вызовами

---

## Test Case: TC-UTIL-022
**Title:** Clear HTTP client cache

**Category:** Positive

**Description:** Проверка очистки кэша HTTP клиента и создания нового экземпляра

**Preconditions:**
- HTTP клиент был создан и закэширован через вызов `_get_default_http_client()` или `_fetch_xml_from_url()`
- Глобальный кэш модуля `pobapi.util._default_http_client` содержит экземпляр клиента

**Test Steps:**
1. Получить текущий HTTP клиент через `_get_default_http_client()` и сохранить ссылку на объект (oldClient)
2. Убедиться, что `oldClient is not None`
3. Очистить кэш HTTP клиента: установить `pobapi.util._default_http_client = None`
4. (Опционально) Установить spy/mock на конструктор `RequestsHTTPClient` для отслеживания создания нового экземпляра
5. Вызвать `_get_default_http_client()` снова (или `_fetch_xml_from_url()` с замоканным requests.get)
6. Получить новый клиент (newClient) и проверить, что `newClient is not oldClient` (разные объекты)
7. (Если используется spy) Проверить, что конструктор `RequestsHTTPClient` был вызван после очистки кэша

**Expected Result:**
- `oldClient is not None` - старый клиент существует
- После очистки кэша `pobapi.util._default_http_client is None`
- `newClient is not None` - новый клиент создан
- `newClient is not oldClient` - новый клиент является другим объектом (не тот же экземпляр)
- (Если используется spy) Конструктор `RequestsHTTPClient` был вызван после очистки кэша
- Новый клиент функционален и может выполнять HTTP запросы
