# TradeAPI ↔ PathOfBuildingAPI Integration Test Cases

## Module: tests/integrations/test_trade_api_integration.py

### Overview
Интеграционные тест-кейсы для проверки взаимодействия между TradeAPI и PathOfBuildingAPI.

### None-Handling Policy
TradeAPI follows a strict None-handling policy:

- **Parameter-level None values** (`items=None`, `filters=None`, `query=None`): These are considered invalid and will raise `TypeError` with a clear error message. This ensures type safety and prevents runtime errors.

- **Filter value-level None values** (`TradeFilter.value=None`, `TradeFilter.min_value=None`, `TradeFilter.max_value=None`): These are treated as "ignore this filter" and are gracefully skipped during filtering. This allows optional filter conditions.

**Examples:**
- `TradeAPI.filter_items(items=None, filters=[...])` → Raises `TypeError: items parameter cannot be None`
- `TradeAPI.filter_items(items=[...], filters=None)` → Raises `TypeError: filters parameter cannot be None`
- `TradeAPI.filter_items(items=[...], filters=[TradeFilter(FilterType.RARITY, value=None)])` → Filter is ignored, all items returned

---

## Test Case: TC-INT-TRADE-API-001
**Title:** Filter build items by rarity

**Category:** Positive

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items build по редкости

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с rarity
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- isinstance(filtered_items, list)
- len(filtered_items) >= 1 (или конкретное ожидаемое количество, например >= 2)
- Все items имеют указанную rarity: assert all(item.rarity.lower() == "rare" for item in filtered_items)
- Пример: первый item имеет rarity == "Rare" (или указанное значение)
- Если исходный build содержит items с разной rarity, то len(filtered_items) < len(original_items)

---

## Test Case: TC-INT-TRADE-API-002
**Title:** Filter build items by base type

**Category:** Positive

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items build по base type

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с base_type
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- isinstance(filtered_items, list)
- len(filtered_items) >= 1 (или конкретное ожидаемое количество)
- Все items содержат указанный base_type в base: assert all("Leather Belt" in item.base for item in filtered_items) (пример с "Leather Belt")
- Пример: первый item имеет base, содержащий указанный base_type (например, "Leather Belt" in filtered_items[0].base)
- Если исходный build содержит items с разными base_type, то len(filtered_items) < len(original_items)

---

## Test Case: TC-INT-TRADE-API-003
**Title:** Filter build items by item level

**Category:** Positive

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items build по item level

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с item_level_min
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- isinstance(filtered_items, list)
- len(filtered_items) >= 1 (или конкретное ожидаемое количество)
- Все items имеют item_level >= item_level_min: assert all(item.item_level >= 80 for item in filtered_items) (пример с min=80)
- Если указан item_level_max, то все items имеют item_level <= item_level_max: assert all(item.item_level <= 84 for item in filtered_items) (пример с max=84)
- Пример: первый item имеет item_level в диапазоне [item_level_min, item_level_max] или >= item_level_min
- Если исходный build содержит items с разными item_level, то len(filtered_items) < len(original_items)

---

## Test Case: TC-INT-TRADE-API-004
**Title:** Search build items with query

**Category:** Positive

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка поиска items build по query

**Preconditions:**
- Есть build fixture с items
- Build содержит items с различными name, base_type, rarity

**Test Steps:**
1. Получить items из build
2. Создать TradeQuery с search query (например, base_type="sword" или filters с rarity="unique")
3. Искать items через TradeAPI.search_items()
4. Получить список всех item.uid из исходных items для проверки исключений

**Expected Result:**
- results is not None
- isinstance(results, list)
- Если results не пустой, то для каждого result в results:
  - result.item is not None
  - Если query.base_type указан, то query.base_type.lower() содержится в result.item.base.lower()
  - Если query.filters содержит FilterType.RARITY, то result.item.rarity.lower() == filter.value.lower()
  - Если query.filters содержит FilterType.BASE_TYPE, то filter.value.lower() содержится в result.item.base.lower()
  - Если query.filters содержит FilterType.ITEM_LEVEL с min_value, то result.item.item_level >= filter.min_value
  - Если query.filters содержит FilterType.ITEM_LEVEL с max_value, то result.item.item_level <= filter.max_value
  - Если query.filters содержит FilterType.QUALITY с min_value, то result.item.quality is not None и result.item.quality >= filter.min_value
  - Если query.filters содержит FilterType.QUALITY с max_value, то result.item.quality is not None и result.item.quality <= filter.max_value
  - Если query.filters содержит FilterType.SOCKETS с min_value, то result.item.sockets is not None и sum(len(group) for group in result.item.sockets) >= filter.min_value
- Проверить, что items, которые должны быть исключены запросом, отсутствуют в results:
  - Создать список excluded_item_uids из исходных items, которые не соответствуют критериям поиска
  - Для каждого result в results: result.item.uid не должен быть в excluded_item_uids
- Если query содержит несколько фильтров, все фильтры должны применяться одновременно (AND логика)
- len(results) >= 0 (может быть пустым, если нет совпадений)
- Все элементы являются TradeResult: assert all(isinstance(r, TradeResult) for r in results)
- Каждый TradeResult содержит item: assert all(hasattr(r, 'item') and r.item is not None for r in results)
- Каждый TradeResult имеет match_score в диапазоне [0.0, 100.0]: assert all(0.0 <= r.match_score <= 100.0 for r in results)
- Результаты отсортированы по match_score по убыванию: assert results == sorted(results, key=lambda x: x.match_score, reverse=True)
- Если есть результаты, то первый результат имеет наивысший match_score: assert len(results) == 0 or all(results[0].match_score >= r.match_score for r in results[1:])
- Пример: если results не пуст, то results[0].item.base содержит search query или соответствует критериям поиска

---

## Test Case: TC-INT-TRADE-API-005
**Title:** Filter build items by quality

**Category:** Positive

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items build по quality

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с quality_min
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- isinstance(filtered_items, list)
- len(filtered_items) >= 1 (или конкретное ожидаемое количество)
- Все items имеют quality не None и quality >= quality_min: assert all(item.quality is not None and item.quality >= 20 for item in filtered_items) (пример с min=20)
- Если указан quality_max, то все items имеют quality <= quality_max: assert all(item.quality <= 30 for item in filtered_items) (пример с max=30)
- Пример: первый item имеет quality в диапазоне [quality_min, quality_max] или >= quality_min
- Если исходный build содержит items с разными quality, то len(filtered_items) < len(original_items)

---

## Test Case: TC-INT-TRADE-API-006
**Title:** Filter build items by sockets

**Category:** Positive

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items build по sockets

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с sockets_min
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- isinstance(filtered_items, list)
- len(filtered_items) >= 1 (или конкретное ожидаемое количество)
- Все items имеют sockets не None: assert all(item.sockets is not None for item in filtered_items)
- Все items имеют общее количество sockets >= sockets_min: assert all(sum(len(group) for group in item.sockets) >= 4 for item in filtered_items) (пример с min=4)
- Пример: первый item имеет sockets с общим количеством >= sockets_min (например, sum(len(group) for group in filtered_items[0].sockets) >= 4)
- Если исходный build содержит items с разным количеством sockets, то len(filtered_items) < len(original_items)

---

## Test Case: TC-INT-TRADE-API-007
**Title:** Search build items with price range

**Category:** Positive

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка поиска items build с price range

**Preconditions:**
- Есть build fixture с items
- Build содержит items с различными ценами (или можно использовать TradeAPI.estimate_item_price() для получения цен)

**Test Steps:**
1. Получить items из build
2. Для каждого item получить/оценить цену через TradeAPI.estimate_item_price(item) или использовать предустановленные цены
3. Создать TradeQuery с price_range (например, min_price=5.0, max_price=50.0)
4. Искать items через TradeAPI.search_items()
5. Для каждого result в results установить result.price и result.currency на основе оцененной цены (или использовать предустановленные цены)
6. Применить фильтрацию по price_range: отфильтровать results, оставив только те, где result.price находится в диапазоне [min_price, max_price] (сохранить в filtered_results)
7. Получить список всех item.uid из исходных items для проверки исключений

**Expected Result:**
- results is not None
- isinstance(results, list)
- len(results) >= 0 (может быть пустым, если нет совпадений)
- Все элементы являются TradeResult: assert all(isinstance(r, TradeResult) for r in results)
- Если results не пустой, то для каждого result в results:
  - result.item is not None: assert all(hasattr(r, 'item') and r.item is not None for r in results)
  - result.price is not None: assert all(hasattr(r, 'price') and r.price is not None for r in results)
  - Если query.price_range.min_price указан (например, 5.0), то result.price >= query.price_range.min_price: assert all(r.price >= 5.0 for r in results) (пример с min=5.0)
  - Если query.price_range.max_price указан и не равен float("inf") (например, 50.0), то result.price <= query.price_range.max_price: assert all(r.price <= 50.0 for r in results) (пример с max=50.0)
  - result.currency == query.price_range.currency (если price_range указан): assert all(r.currency == "chaos" for r in results) (пример с currency="chaos")
- Пример: если price_range = PriceRange(min_price=10.0, max_price=50.0), то все r.price в [10.0, 50.0]
- После фильтрации по price_range, если filtered_results не пустой, то для каждого result в filtered_results:
  - result.price >= query.price_range.min_price (если min_price указан): assert all(r.price >= query.price_range.min_price for r in filtered_results)
  - result.price <= query.price_range.max_price (если max_price указан и не равен float("inf")): assert all(r.price <= query.price_range.max_price for r in filtered_results)
  - result.currency == query.price_range.currency (если price_range указан): assert all(r.currency == query.price_range.currency for r in filtered_results)
- Проверить, что items, которые должны быть исключены price_range, отсутствуют в filtered_results:
  - Создать список excluded_item_uids из исходных items, у которых оцененная цена < min_price или оцененная цена > max_price
  - Для каждого result в filtered_results: result.item.uid не должен быть в excluded_item_uids: assert all(r.item.uid not in excluded_item_uids for r in filtered_results)
- Если price_range комбинируется с другими фильтрами (base_type, filters), все критерии должны применяться одновременно: результаты соответствуют и фильтрам, и price_range
- Результаты отсортированы по match_score по убыванию: assert results == sorted(results, key=lambda x: x.match_score, reverse=True)

---

## Test Case: TC-INT-TRADE-API-008
**Title:** TradeAPI with modified build items

**Category:** Positive

**Integration:** TradeAPI ↔ BuildModifier ↔ PathOfBuildingAPI

**Description:** Проверка работы TradeAPI с модифицированными build items

**Preconditions:**
- Есть build fixture

**Test Steps:**
1. Модифицировать build (добавить/изменить items)
2. Получить items из модифицированного build
3. Использовать TradeAPI для фильтрации/поиска

**Expected Result:**
- TradeAPI.filter_items() или TradeAPI.search_items() успешно выполняется с модифицированными items
- Результаты не None: filtered_items is not None или results is not None
- isinstance(filtered_items, list) или isinstance(results, list)
- len(filtered_items) >= 0 или len(results) >= 0
- Если применены фильтры, то все items в filtered_items соответствуют критериям фильтрации
## Test Case: TC-INT-TRADE-API-009
**Title:** Filter items with invalid non-numeric item_level parameter

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки невалидного нечислового параметра item_level в фильтре

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.ITEM_LEVEL и min_value="invalid_string"
3. Попытаться фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- Возникает TypeError или ValidationError
- Или возвращается пустой список items
- Ошибка содержит информацию о невалидном типе параметра

---

## Test Case: TC-INT-TRADE-API-010
**Title:** Filter items with invalid rarity string value

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки невалидной строки rarity в фильтре

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.RARITY и value="INVALID_RARITY"
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- filtered_items является пустым списком (нет совпадений)
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-011
**Title:** Edge: filter handles negative min_value boundary — all items with item_level >= -10 pass and no exceptions are raised

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки граничного случая с отрицательным значением min_value в фильтре item_level. Все items должны проходить фильтр, так как item_level всегда >= -10, и не должно возникать исключений

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.ITEM_LEVEL и min_value=-10
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- Все items имеют item_level >= -10 (все items проходят фильтр, так как отрицательное значение min_value является граничным случаем)
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-012
**Title:** Filter empty build items list

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации пустого списка items

**Preconditions:**
- Есть build fixture без items или пустой список items

**Test Steps:**
1. Получить пустой список items из build
2. Создать TradeFilter с любыми параметрами
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- filtered_items является пустым списком
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-013
**Title:** Filter items with filters that return zero results

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items с фильтрами, которые не находят совпадений

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с параметрами, которые не соответствуют ни одному item (например, item_level_min=999)
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- filtered_items является пустым списком
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-014
**Title:** Filter items with missing base_type field

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки items с отсутствующим полем base_type

**Preconditions:**
- Есть build fixture с items, где некоторые items имеют base=None или пустую строку

**Test Steps:**
1. Получить items из build (включая items с base=None)
2. Создать TradeFilter с FilterType.BASE_TYPE и value="SomeBase"
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- Items с base=None или пустой строкой исключаются из результатов
- Не возникает AttributeError или TypeError
- Обработка выполняется gracefully

---

## Test Case: TC-INT-TRADE-API-015
**Title:** Filter items with missing sockets field

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки items с отсутствующим полем sockets

**Preconditions:**
- Есть build fixture с items, где некоторые items имеют sockets=None

**Test Steps:**
1. Получить items из build (включая items с sockets=None)
2. Создать TradeFilter с FilterType.SOCKETS и min_value=4
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- Items с sockets=None исключаются из результатов
- Не возникает AttributeError или TypeError
- Обработка выполняется gracefully

---

## Test Case: TC-INT-TRADE-API-016
**Title:** Filter items with missing quality field

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки items с отсутствующим полем quality

**Preconditions:**
- Есть build fixture с items, где некоторые items имеют quality=None

**Test Steps:**
1. Получить items из build (включая items с quality=None)
2. Создать TradeFilter с FilterType.QUALITY и min_value=10
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- Items с quality=None исключаются из результатов
- Не возникает AttributeError или TypeError
- Обработка выполняется gracefully

---

## Test Case: TC-INT-TRADE-API-017
**Title:** Filter items with boundary item_level values (minimum)

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items с граничным минимальным значением item_level

**Preconditions:**
- Есть build fixture с items различного item_level

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.ITEM_LEVEL и min_value=1
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- Все items имеют item_level >= 1
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-018
**Title:** Filter items with boundary item_level values (maximum)

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items с граничным максимальным значением item_level

**Preconditions:**
- Есть build fixture с items различного item_level

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.ITEM_LEVEL и max_value=100
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- Все items имеют item_level <= 100
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-019
**Title:** Filter items with quality at boundary value 0

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items с граничным значением quality=0

**Preconditions:**
- Есть build fixture с items, включая items с quality=0

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.QUALITY и min_value=0
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- Все items имеют quality >= 0 (включая quality=0)
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-020
**Title:** Filter items with quality at boundary value 100

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items с граничным значением quality=100

**Preconditions:**
- Есть build fixture с items, включая items с quality=100

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.QUALITY и max_value=100
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- Все items имеют quality <= 100 (включая quality=100)
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-021
**Title:** Search items with very large build containing many items

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка производительности поиска items в очень большом build с множеством items

**Preconditions:**
- Есть build fixture с большим количеством items (1000+ items)

**Test Steps:**
1. Получить items из большого build
2. Создать TradeQuery с несколькими фильтрами
3. Выполнить поиск items через TradeAPI.search_items()
4. Измерить время выполнения

**Expected Result:**
- results is not None
- isinstance(results, list)
- Поиск завершается в разумное время (< 5 секунд для 1000 items)
- Не возникает ошибок памяти или таймаутов

---

## Test Case: TC-INT-TRADE-API-022
**Title:** Filter items with very large response payload

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки очень большого ответа при фильтрации items

**Preconditions:**
- Есть build fixture с очень большим количеством items (5000+ items)

**Test Steps:**
1. Получить items из очень большого build
2. Создать TradeFilter с широкими критериями (например, item_level_min=1)
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- isinstance(filtered_items, list)
- Фильтрация завершается успешно
- Не возникает ошибок памяти или производительности

---

## API Contract: Filter Items Behavior

**Contract Definition:**
- `filter_items(filters=None)` - передача `None` для всего параметра `filters` является ошибкой и должна вызывать `TypeError`
- `TradeFilter` объекты с `value=None` или `value=""` - валидные фильтры, которые игнорируются (no-op) и пропускают все предметы без изменений
- Различие: `filters=None` означает отсутствие параметра списка фильтров (ошибка), а `TradeFilter(value=None)` означает валидный фильтр с пустым значением (игнорируется)

---

## Test Case: TC-INT-TRADE-API-023
**Title:** Filter items with None/null filter values

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки валидных TradeFilter объектов с None/null значениями. Согласно API контракту, отдельные TradeFilter с value=None должны игнорироваться (no-op) и возвращать все предметы без изменений.

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать валидный TradeFilter с FilterType.RARITY и value=None
3. Фильтровать items через TradeAPI.filter_items(items=items, filters=[TradeFilter(...)])

**Expected Result:**
- Не возникает исключений (TypeError не ожидается, так как filters - валидный список)
- filtered_items is not None
- filtered_items содержит все исходные items без изменений (фильтр с value=None игнорируется как no-op)
- len(filtered_items) == len(items)

---

## Test Case: TC-INT-TRADE-API-024
**Title:** Filter items with empty string filter values

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки валидных TradeFilter объектов с пустыми строками. Согласно API контракту, отдельные TradeFilter с value="" должны игнорироваться (no-op) и возвращать все предметы без изменений.

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать валидный TradeFilter с FilterType.BASE_TYPE и value=""
3. Фильтровать items через TradeAPI.filter_items(items=items, filters=[TradeFilter(...)])

**Expected Result:**
- Не возникает исключений (TypeError не ожидается, так как filters - валидный список)
- filtered_items is not None
- filtered_items содержит все исходные items без изменений (фильтр с value="" игнорируется как no-op)
- len(filtered_items) == len(items)

---

## Test Case: TC-INT-TRADE-API-025
**Title:** Search items with invalid TradeQuery parameters

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки невалидных параметров TradeQuery согласно политике None-handling

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeQuery с filters=None (явно установленным) или невалидными данными
3. Попытаться выполнить поиск через TradeAPI.search_items()

**Expected Result:**
- Если filters=None в TradeQuery, то при вызове search_items возникает TypeError
- Ошибка содержит сообщение: "filters parameter cannot be None. Expected list[TradeFilter]."
- Для других невалидных параметров может возникать TypeError или ValidationError в зависимости от типа ошибки

---

## Test Case: TC-INT-TRADE-API-026
**Title:** Filter items with reversed min/max range values

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки фильтров с обращенными min/max значениями (min > max)

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.ITEM_LEVEL, min_value=100, max_value=1
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- filtered_items является пустым списком (нет items в невалидном диапазоне)
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-027
**Title:** Search items with empty filters list

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка поиска items с пустым списком фильтров

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeQuery с filters=[]
3. Выполнить поиск через TradeAPI.search_items()

**Expected Result:**
- results is not None
- isinstance(results, list)
- results содержит все items из исходного списка
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-028
**Title:** Filter items with multiple conflicting filters

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items с множественными конфликтующими фильтрами

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать несколько TradeFilter с конфликтующими критериями (например, rarity="UNIQUE" и rarity="RARE")
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- filtered_items является пустым списком (нет items, удовлетворяющих всем фильтрам)
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-029
**Title:** Filter items with invalid FilterType enum value

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки невалидного значения FilterType

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Попытаться создать TradeFilter с несуществующим FilterType (например, через прямое присваивание)
3. Попытаться фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- Возникает ValueError или AttributeError при создании фильтра
- Или фильтр игнорируется при фильтрации
- Ошибка содержит информацию о невалидном FilterType

---

## Test Case: TC-INT-TRADE-API-030
**Title:** Search items with None items list

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки None вместо списка items согласно политике None-handling

**Preconditions:**
- Нет требований к build fixture

**Test Steps:**
1. Создать TradeQuery с валидными параметрами
2. Попытаться выполнить поиск через TradeAPI.search_items(items=None, query=query)

**Expected Result:**
- Возникает TypeError
- Ошибка содержит точное сообщение: "items parameter cannot be None. Expected list[Item]."
- isinstance(error, TypeError) == True

---

## Test Case: TC-INT-TRADE-API-031
**Title:** Filter items with None filters list

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки None вместо списка фильтров согласно политике None-handling

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Попытаться фильтровать items через TradeAPI.filter_items(items=items, filters=None)

**Expected Result:**
- Возникает TypeError
- Ошибка содержит точное сообщение: "filters parameter cannot be None. Expected list[TradeFilter]."
- isinstance(error, TypeError) == True

---

## Test Case: TC-INT-TRADE-API-032
**Title:** Search items with invalid price range (negative prices)

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки отрицательных значений в price range

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeQuery с PriceRange(min_price=-10, max_price=-5)
3. Выполнить поиск через TradeAPI.search_items()

**Expected Result:**
- results is not None
- isinstance(results, list)
- Отрицательные цены обрабатываются gracefully (игнорируются или возвращают пустой список)
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-033
**Title:** Filter items with very large numeric filter values

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки очень больших числовых значений в фильтрах

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.ITEM_LEVEL и min_value=999999
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- filtered_items является пустым списком (нет items с таким высоким item_level)
- Не возникает OverflowError или других исключений

---

## Test Case: TC-INT-TRADE-API-034
**Title:** Search items with special characters in base_type

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки специальных символов в base_type

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeQuery с base_type="Item@#$%^&*()"
3. Выполнить поиск через TradeAPI.search_items()

**Expected Result:**
- results is not None
- isinstance(results, list)
- Специальные символы обрабатываются gracefully
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-035
**Title:** Filter items with unicode characters in filter values

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки unicode символов в значениях фильтров

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeFilter с FilterType.BASE_TYPE и value="アイテム"
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- isinstance(filtered_items, list)
- Unicode символы обрабатываются корректно
- Не возникает UnicodeEncodeError или других исключений

---

## Test Case: TC-INT-TRADE-API-036
**Title:** Search items with extremely long query string

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки очень длинной строки запроса

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeQuery с base_type="A" * 10000
3. Выполнить поиск через TradeAPI.search_items()

**Expected Result:**
- results is not None
- isinstance(results, list)
- Очень длинная строка обрабатывается без ошибок
- Не возникает MemoryError или других исключений

---

## Test Case: TC-INT-TRADE-API-037
**Title:** Filter items with all filter types simultaneously

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка фильтрации items со всеми типами фильтров одновременно

**Preconditions:**
- Есть build fixture с items, имеющими различные свойства

**Test Steps:**
1. Получить items из build
2. Создать список TradeFilter со всеми доступными FilterType
3. Фильтровать items через TradeAPI.filter_items()

**Expected Result:**
- filtered_items is not None
- isinstance(filtered_items, list)
- Все фильтры применяются корректно
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-038
**Title:** Search items with invalid league name

**Category:** Negative

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка обработки невалидного имени лиги в TradeQuery

**Preconditions:**
- Есть build fixture с items

**Test Steps:**
1. Получить items из build
2. Создать TradeQuery с league=""
3. Выполнить поиск через TradeAPI.search_items()

**Expected Result:**
- results is not None
- isinstance(results, list)
- Пустое имя лиги обрабатывается gracefully
- Не возникает исключений

---

## Test Case: TC-INT-TRADE-API-039
**Title:** Generate trade URL with invalid query parameters

**Category:** Negative

**Integration:** TradeAPI

**Description:** Проверка генерации trade URL с невалидными параметрами запроса

**Preconditions:**
- Нет требований к build fixture

**Test Steps:**
1. Создать TradeQuery с невалидными параметрами (например, league=None)
2. Попытаться сгенерировать URL через TradeAPI.generate_trade_url()

**Expected Result:**
- Возникает TypeError или ValidationError
- Или URL генерируется с дефолтными значениями
- Ошибка содержит информацию о невалидных параметрах

---

## Test Case: TC-INT-TRADE-API-040
**Title:** Estimate price for item with all None optional fields

**Category:** Edge

**Integration:** TradeAPI ↔ PathOfBuildingAPI

**Description:** Проверка оценки цены для item со всеми опциональными полями равными None

**Preconditions:**
- Есть build fixture с item, где quality=None, sockets=None, shaper=None, elder=None

**Test Steps:**
1. Получить item из build с минимальными полями
2. Вызвать TradeAPI.estimate_item_price(item)

**Expected Result:**
- Возвращается PriceRange объект
- min_price и max_price имеют валидные значения
- Не возникает AttributeError или TypeError

---
