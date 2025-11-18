# Cache Unit Test Cases

## Module: pobapi.cache

### Overview
Юнит-тест-кейсы для модуля cache, который предоставляет функциональность кэширования.

---

## Test Case: TC-CACHE-001
**Title:** Cache.set() and Cache.get() basic operations

**Category:** Positive

**Description:** Проверка базовых операций set() и get()

**Preconditions:**
- Cache объект создан

**Test Steps:**
1. Вызвать `cache.set("key1", "value1")`
2. Вызвать `cache.get("key1")`
3. Проверить возвращаемое значение

**Expected Result:**
- cache.get("key1") == "value1"
- Значение успешно сохранено и получено

---

## Test Case: TC-CACHE-002
**Title:** Cache.get() with non-existent key

**Category:** Edge Case

**Description:** Проверка метода get() для несуществующего ключа

**Preconditions:**
- Cache объект создан
- Ключ не был установлен

**Test Steps:**
1. Вызвать `cache.get("nonexistent")`
2. Проверить возвращаемое значение

**Expected Result:**
- cache.get("nonexistent") is None

---

## Test Case: TC-CACHE-003
**Title:** Cache expiry with default TTL

**Category:** Positive

**Description:** Проверка истечения срока действия кэша с дефолтным TTL

**Preconditions:**
- Cache создан с default_ttl=1
- Используется freezegun для мокирования времени

**Test Steps:**
1. Зафиксировать время с помощью `freezegun.freeze_time()` на фиксированной дате (например, "2024-01-01 00:00:00")
2. Вызвать `cache.set("key1", "value1")`
3. Проверить, что значение доступно: cache.get("key1") == "value1"
4. Переместить замороженное время вперед на 1.1 секунды (используя `freeze_time(... + timedelta(seconds=1.1))` или `tick()`)
5. Проверить значение снова
6. Восстановить реальное время (выход из контекстного менеджера)

**Expected Result:**
- Сразу после установки: cache.get("key1") == "value1"
- После истечения TTL: cache.get("key1") is None

---

## Test Case: TC-CACHE-004
**Title:** Cache.set() with custom TTL

**Category:** Positive

**Description:** Проверка метода set() с кастомным TTL

**Preconditions:**
- Cache создан с default_ttl=10
- Используется freezegun для мокирования времени

**Test Steps:**
1. Зафиксировать время с помощью `freezegun.freeze_time()` на фиксированной дате (например, "2024-01-01 00:00:00")
2. Вызвать `cache.set("key1", "value1", ttl=1)`
3. Проверить значение: cache.get("key1") == "value1"
4. Переместить замороженное время вперед на 1.1 секунды (используя `freeze_time(... + timedelta(seconds=1.1))` или `tick()`)
5. Проверить значение снова
6. Восстановить реальное время (выход из контекстного менеджера)

**Expected Result:**
- Сразу после установки: cache.get("key1") == "value1"
- После истечения кастомного TTL: cache.get("key1") is None

---

## Test Case: TC-CACHE-005
**Title:** Cache.clear() removes all entries

**Category:** Positive

**Description:** Проверка метода clear() для удаления всех записей

**Preconditions:**
- Cache содержит несколько записей

**Test Steps:**
1. Установить несколько значений
2. Вызвать `cache.clear()`
3. Проверить, что все значения удалены

**Expected Result:**
- cache.get("key1") is None
- Все записи удалены

---

## Test Case: TC-CACHE-006
**Title:** Cache.delete() removes specific key

**Category:** Positive

**Description:** Проверка метода delete() для удаления конкретного ключа

**Preconditions:**
- Cache содержит несколько записей

**Test Steps:**
1. Установить "key1" и "key2"
2. Вызвать `cache.delete("key1")`
3. Проверить значения

**Expected Result:**
- cache.get("key1") is None
- cache.get("key2") == "value2"

---

## Test Case: TC-CACHE-007
**Title:** Cache.size() returns correct count

**Category:** Positive

**Description:** Проверка метода size() для получения количества записей

**Preconditions:**
- Cache объект создан

**Test Steps:**
1. Проверить размер пустого кэша
2. Добавить записи
3. Проверить размер после добавления

**Expected Result:**
- cache.size() == 0 для пустого кэша
- cache.size() == 2 после добавления двух записей

---

## Test Case: TC-CACHE-008
**Title:** Cache.stats() returns statistics

**Category:** Positive

**Description:** Проверка метода stats() для получения статистики

**Preconditions:**
- Cache создан с параметрами default_ttl=3600, max_size=1000

**Test Steps:**
1. Вызвать `cache.stats()`
2. Проверить значения статистики

**Expected Result:**
- stats["size"] == 0
- stats["max_size"] == 1000
- stats["default_ttl"] == 3600

---

## Test Case: TC-CACHE-009
**Title:** Cache evicts oldest entry when full

**Category:** Positive

**Description:** Проверка удаления самой старой записи при переполнении кэша

**Preconditions:**
- Cache создан с max_size=2

**Test Steps:**
1. Установить "key1"
2. Подождать 0.1 секунды
3. Установить "key2"
4. Установить "key3"
5. Проверить содержимое кэша

**Expected Result:**
- cache.get("key1") is None (удалена как самая старая)
- cache.get("key2") == "value2"
- cache.get("key3") == "value3"

---

## Test Case: TC-CACHE-010
**Title:** Cache does not evict when updating existing key

**Category:** Positive

**Description:** Проверка, что обновление существующего ключа не вызывает удаление

**Preconditions:**
- Cache создан с max_size=2
- Кэш заполнен

**Test Steps:**
1. Установить "key1" и "key2"
2. Обновить "key1" новым значением
3. Проверить содержимое кэша

**Expected Result:**
- cache.get("key1") == "value1_updated"
- cache.get("key2") == "value2"
- Оба ключа присутствуют

---

## Test Case: TC-CACHE-011
**Title:** Cache eviction when inserting into full cache

**Category:** Edge Case

**Description:** Проверка автоматического удаления старых записей при заполнении кэша через публичный API

**Preconditions:**
- Cache создан с max_size=1

**Test Steps:**
1. Установить "key1" со значением "value1"
2. Проверить размер кэша
3. Установить "key2" со значением "value2" (новый ключ, кэш заполнен)
4. Проверить содержимое кэша и размер

**Expected Result:**
- После шага 1: cache.size() == 1, cache.get("key1") == "value1"
- После шага 3: cache.size() == 1 (не превышает max_size)
- cache.get("key1") is None (удалена как самая старая)
- cache.get("key2") == "value2" (новая запись присутствует)
- Исключение не выбрасывается

---

## Test Case: TC-CACHE-012
**Title:** @cached decorator caches function results

**Category:** Positive

**Description:** Проверка декоратора @cached для кэширования результатов функции

**Preconditions:**
- Cache создан
- Функция декорирована @cached

**Test Steps:**
1. Вызвать декорированную функцию первый раз
2. Вызвать функцию второй раз с теми же аргументами
3. Проверить количество вызовов

**Expected Result:**
- Функция вызвана только один раз
- Второй вызов использует кэш
- Результаты одинаковые

---

## Test Case: TC-CACHE-013
**Title:** @cached decorator with cache expiry

**Category:** Positive

**Description:** Проверка декоратора @cached с истечением срока действия кэша

**Preconditions:**
- Cache создан с default_ttl=1
- Функция декорирована @cached(ttl=1)
- Используется freezegun для мокирования времени

**Test Steps:**
1. Зафиксировать время с помощью `freezegun.freeze_time()` на фиксированной дате (например, "2024-01-01 00:00:00")
2. Вызвать функцию первый раз
3. Переместить замороженное время вперед на 1.1 секунды (используя `freeze_time(... + timedelta(seconds=1.1))` или `tick()`)
4. Вызвать функцию снова
5. Проверить количество вызовов
6. Восстановить реальное время (выход из контекстного менеджера)

**Expected Result:**
- Функция вызвана дважды
- После истечения TTL кэш не используется

---

## Test Case: TC-CACHE-014
**Title:** @cached decorator with different arguments

**Category:** Positive

**Description:** Проверка декоратора @cached с разными аргументами

**Preconditions:**
- Функция декорирована @cached

**Test Steps:**
1. Вызвать функцию с аргументом 5
2. Вызвать функцию с аргументом 10
3. Проверить количество вызовов

**Expected Result:**
- Функция вызвана дважды
- Разные аргументы создают разные записи кэша

---

## Test Case: TC-CACHE-015
**Title:** get_cache() returns default cache instance

**Category:** Positive

**Description:** Проверка функции get_cache() для получения дефолтного экземпляра кэша

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `cache = get_cache()`
2. Проверить тип объекта

**Expected Result:**
- cache является экземпляром Cache
- Возвращается дефолтный кэш

---

## Test Case: TC-CACHE-016
**Title:** clear_cache() clears default cache

**Category:** Positive

**Description:** Проверка функции clear_cache() для очистки дефолтного кэша

**Preconditions:**
- Дефолтный кэш содержит записи

**Test Steps:**
1. Получить дефолтный кэш
2. Установить значение
3. Вызвать `clear_cache()`
4. Проверить значение

**Expected Result:**
- cache.get("key1") is None
- Кэш очищен

---

## Test Case: TC-CACHE-017
**Title:** Cache with zero TTL

**Category:** Edge Case

**Description:** Проверка кэша с TTL=0. TTL=0 означает немедленное истечение срока действия, значение должно быть недоступно сразу после установки.

**Preconditions:**
- Cache создан с default_ttl=0

**Test Steps:**
1. Вызвать `cache.set("key1", "value1", ttl=0)`
2. Немедленно вызвать `cache.get("key1")`
3. Проверить возвращаемое значение

**Expected Result:**
- cache.get("key1") is None (значение истекло немедленно из-за TTL=0)
- TTL=0 обрабатывается как немедленное истечение срока действия

---

## Test Case: TC-CACHE-018
**Title:** Cache with very large TTL

**Category:** Edge Case

**Description:** Проверка кэша с очень большим TTL

**Preconditions:**
- Cache создан с default_ttl=999999

**Test Steps:**
1. Установить значение
2. Проверить, что значение доступно

**Expected Result:**
- Значение доступно
- Большой TTL обрабатывается корректно
