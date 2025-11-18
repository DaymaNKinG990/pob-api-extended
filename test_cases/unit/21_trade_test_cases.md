# Trade Unit Test Cases

## Module: pobapi.trade

### Overview
Юнит-тест-кейсы для модуля trade, который содержит классы для работы с торговлей предметами.

---

## Test Case: TC-TRADE-001
**Title:** TradeFilter.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации TradeFilter

**Preconditions:**
- Нет

**Test Steps:**
1. Создать TradeFilter(filter_type=FilterType.RARITY, value="UNIQUE")
2. Проверить значения атрибутов

**Expected Result:**
- filter_obj.filter_type == FilterType.RARITY
- filter_obj.value == "UNIQUE"

---

## Test Case: TC-TRADE-002
**Title:** TradeQuery.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации TradeQuery

**Preconditions:**
- Нет

**Test Steps:**
1. Создать TradeQuery(league="Standard", base_type="Leather Belt")
2. Проверить значения атрибутов

**Expected Result:**
- query.league == "Standard"
- query.base_type == "Leather Belt"

---

## Test Case: TC-TRADE-003
**Title:** PriceRange.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации PriceRange

**Preconditions:**
- Нет

**Test Steps:**
1. Создать PriceRange(min_price=1.0, max_price=10.0, currency="chaos")
2. Проверить значения атрибутов

**Expected Result:**
- price_range.min_price == 1.0
- price_range.max_price == 10.0
- price_range.currency == "chaos"

---

## Test Case: TC-TRADE-004
**Title:** TradeResult.__init__() initialization

**Category:** Positive

**Description:** Проверка инициализации TradeResult

**Preconditions:**
- Валидный Item создан

**Test Steps:**
1. Создать валидный Item
2. Создать TradeResult(item=item, match_score=0.8)
3. Проверить значения атрибутов

**Expected Result:**
- result.item == item
- result.match_score == 0.8

---

## Test Case: TC-TRADE-005
**Title:** TradeAPI.filter_items() by rarity

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по редкости

**Preconditions:**
- Список предметов с разной редкостью создан

**Test Steps:**
1. Создать список предметов с разной редкостью
2. Создать фильтр TradeFilter(filter_type=FilterType.RARITY, value="Unique")
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются только предметы с редкостью "Unique"
- Количество отфильтрованных предметов корректно

---

## Test Case: TC-TRADE-006
**Title:** TradeAPI.filter_items() by base type

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по базовому типу

**Preconditions:**
- Список предметов с разными base types создан

**Test Steps:**
1. Создать список предметов с разными base types
2. Создать фильтр TradeFilter(filter_type=FilterType.BASE_TYPE, value="Leather Belt")
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются только предметы с указанным base type
- Все предметы содержат "Leather Belt" в base

---

## Test Case: TC-TRADE-007
**Title:** TradeAPI.filter_items() by item level

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по item level

**Preconditions:**
- Список предметов с разными item levels создан

**Test Steps:**
1. Создать список предметов с разными item levels
2. Создать фильтр TradeFilter(filter_type=FilterType.ITEM_LEVEL, min_value=80, max_value=90)
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются только предметы с item level в диапазоне 80-90
- Все предметы соответствуют диапазону

---

## Test Case: TC-TRADE-008
**Title:** TradeAPI.filter_items() by quality

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по качеству

**Preconditions:**
- Список предметов с разным качеством создан

**Test Steps:**
1. Создать список предметов с разным качеством
2. Создать фильтр TradeFilter(filter_type=FilterType.QUALITY, min_value=20)
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются только предметы с качеством >= 20
- Все предметы соответствуют фильтру

---

## Test Case: TC-TRADE-009
**Title:** TradeAPI.filter_items() with multiple filters

**Category:** Positive

**Description:** Проверка статического метода filter_items() с несколькими фильтрами

**Preconditions:**
- Список предметов создан
- Несколько фильтров созданы

**Test Steps:**
1. Создать список предметов
2. Создать несколько фильтров
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются предметы, соответствующие всем фильтрам
- Все фильтры применены корректно

---

## Test Case: TC-TRADE-010
**Title:** TradeAPI.filter_items() by boolean flags

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по булевым флагам

**Preconditions:**
- Список предметов с разными флагами создан

**Test Steps:**
1. Создать список предметов с разными флагами (shaper, elder и т.д.)
2. Создать фильтр для булевого флага
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются только предметы с указанным флагом
- Фильтрация корректна

---

## Test Case: TC-TRADE-011
**Title:** TradeAPI.filter_items() by sockets

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по количеству сокетов

**Preconditions:**
- Список предметов с разным количеством сокетов создан

**Test Steps:**
1. Создать список предметов с разным количеством сокетов
2. Создать фильтр TradeFilter(filter_type=FilterType.SOCKETS, min_value=6)
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются только предметы с >= 6 сокетами
- Фильтрация корректна

---

## Test Case: TC-TRADE-012
**Title:** TradeAPI.filter_items() by linked sockets

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по связанным сокетам

**Preconditions:**
- Список предметов с разным количеством связанных сокетов создан

**Test Steps:**
1. Создать список предметов с разным количеством связанных сокетов
2. Создать фильтр TradeFilter(filter_type=FilterType.LINKED_SOCKETS, min_value=5)
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются только предметы с >= 5 связанными сокетами
- Фильтрация корректна

---

## Test Case: TC-TRADE-013
**Title:** TradeAPI.filter_items() by modifier

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по модификатору

**Preconditions:**
- Список предметов с разными модификаторами создан

**Test Steps:**
1. Создать список предметов с разными модификаторами
2. Создать фильтр TradeFilter(filter_type=FilterType.MODIFIER, value="+50 to maximum Life")
3. Вызвать `TradeAPI.filter_items(items, filters)`
4. Проверить результат

**Expected Result:**
- Возвращаются только предметы с указанным модификатором
- Фильтрация корректна

---

## Test Case: TC-TRADE-014
**Title:** TradeAPI.filter_items() by stat value

**Category:** Positive

**Description:** Проверка статического метода filter_items() для фильтрации по значению стата

**Preconditions:**
- Список предметов создан
- Мок для парсинга модификаторов создан

**Test Steps:**
1. Создать список предметов
2. Замокать парсинг модификаторов
3. Создать фильтр для значения стата
4. Вызвать `TradeAPI.filter_items(items, filters)`
5. Проверить результат

**Expected Result:**
- Возвращаются только предметы с указанным значением стата
- Фильтрация корректна

---

## Test Case: TC-TRADE-015
**Title:** TradeAPI.search_items() basic search

**Category:** Positive

**Description:** Проверка статического метода search_items() для базового поиска

**Preconditions:**
- Список предметов создан
- TradeQuery создан

**Test Steps:**
1. Создать список предметов
2. Создать TradeQuery
3. Вызвать `TradeAPI.search_items(items, query)`
4. Проверить результат

**Expected Result:**
- Возвращаются предметы, соответствующие запросу
- Результат корректен

---

## Test Case: TC-TRADE-016
**Title:** TradeAPI.search_items() with match score

**Category:** Positive

**Description:** Проверка статического метода search_items() с match score

**Preconditions:**
- Список предметов создан
- TradeQuery создан

**Test Steps:**
1. Создать список предметов
2. Создать TradeQuery
3. Вызвать `TradeAPI.search_items(items, query, calculate_score=True)`
4. Проверить результат

**Expected Result:**
- Возвращаются TradeResult объекты с match_score
- Match score рассчитан корректно

---

## Test Case: TC-TRADE-017
**Title:** TradeAPI.generate_trade_url() basic URL

**Category:** Positive

**Description:** Проверка статического метода generate_trade_url() для генерации базового URL

**Preconditions:**
- TradeQuery создан

**Test Steps:**
1. Создать TradeQuery
2. Вызвать `TradeAPI.generate_trade_url(query)`
3. Проверить результат

**Expected Result:**
- Возвращается валидный URL
- URL содержит параметры запроса

---

## Test Case: TC-TRADE-018
**Title:** TradeAPI.generate_trade_url() with price range

**Category:** Positive

**Description:** Проверка статического метода generate_trade_url() с price range

**Preconditions:**
- TradeQuery и PriceRange созданы

**Test Steps:**
1. Создать TradeQuery и PriceRange
2. Вызвать `TradeAPI.generate_trade_url(query, price_range=price_range)`
3. Проверить результат

**Expected Result:**
- URL содержит параметры price range
- URL корректен

---

## Test Case: TC-TRADE-019
**Title:** TradeAPI.generate_trade_url() online only

**Category:** Positive

**Description:** Проверка статического метода generate_trade_url() с online only флагом

**Preconditions:**
- TradeQuery создан

**Test Steps:**
1. Создать TradeQuery
2. Вызвать `TradeAPI.generate_trade_url(query, online_only=True)`
3. Проверить результат

**Expected Result:**
- URL содержит параметр online only
- URL корректен

---

## Test Case: TC-TRADE-020
**Title:** TradeAPI.estimate_item_price() basic estimation

**Category:** Positive

**Description:** Проверка статического метода estimate_item_price() для базовой оценки цены

**Preconditions:**
- Валидный Item создан

**Test Steps:**
1. Создать валидный Item
2. Вызвать `TradeAPI.estimate_item_price(item)`
3. Проверить результат

**Expected Result:**
- Возвращается оценка цены
- Значение >= 0

---

## Test Case: TC-TRADE-021
**Title:** TradeAPI.estimate_item_price() by rarity

**Category:** Positive

**Description:** Проверка статического метода estimate_item_price() с учетом редкости

**Preconditions:**
- Предметы с разной редкостью созданы

**Test Steps:**
1. Создать предметы с разной редкостью
2. Вызвать `TradeAPI.estimate_item_price(item)` для каждого
3. Проверить результаты

**Expected Result:**
- Цены различаются в зависимости от редкости
- Unique предметы имеют более высокую цену

---

## Test Case: TC-TRADE-022
**Title:** TradeAPI.estimate_item_price() with quality

**Category:** Positive

**Description:** Проверка статического метода estimate_item_price() с учетом качества

**Preconditions:**
- Предметы с разным качеством созданы

**Test Steps:**
1. Создать предметы с разным качеством
2. Вызвать `TradeAPI.estimate_item_price(item)` для каждого
3. Проверить результаты

**Expected Result:**
- Цены различаются в зависимости от качества
- Более высокое качество увеличивает цену

---

## Test Case: TC-TRADE-023
**Title:** TradeAPI.estimate_item_price() with sockets

**Category:** Positive

**Description:** Проверка статического метода estimate_item_price() с учетом сокетов

**Preconditions:**
- Предметы с разным количеством сокетов созданы

**Test Steps:**
1. Создать предметы с разным количеством сокетов
2. Вызвать `TradeAPI.estimate_item_price(item)` для каждого
3. Проверить результаты

**Expected Result:**
- Цены различаются в зависимости от количества сокетов
- Больше сокетов увеличивает цену

---

## Test Case: TC-TRADE-024
**Title:** TradeAPI.estimate_item_price() with influence

**Category:** Positive

**Description:** Проверка статического метода estimate_item_price() с учетом влияния

**Preconditions:**
- Предметы с разным влиянием созданы

**Test Steps:**
1. Создать предметы с shaper/elder влиянием
2. Вызвать `TradeAPI.estimate_item_price(item)` для каждого
3. Проверить результаты

**Expected Result:**
- Предметы с влиянием имеют более высокую цену
- Цены корректны

---

## Test Case: TC-TRADE-025
**Title:** TradeAPI.compare_items() basic comparison

**Category:** Positive

**Description:** Проверка статического метода compare_items() для базового сравнения

**Preconditions:**
- Два валидных Item созданы

**Test Steps:**
1. Создать два Item
2. Вызвать `TradeAPI.compare_items(item1, item2)`
3. Проверить результат

**Expected Result:**
- Возвращается результат сравнения
- Результат корректен

---

## Test Case: TC-TRADE-026
**Title:** TradeAPI.compare_items() differences

**Category:** Positive

**Description:** Проверка статического метода compare_items() для выявления различий

**Preconditions:**
- Два Item с различиями созданы

**Test Steps:**
1. Создать два Item с различиями
2. Вызвать `TradeAPI.compare_items(item1, item2)`
3. Проверить различия

**Expected Result:**
- Различия выявлены корректно
- Результат содержит информацию о различиях

---

## Test Case: TC-TRADE-027
**Title:** TradeAPI.compare_items() sockets comparison

**Category:** Positive

**Description:** Проверка статического метода compare_items() для сравнения сокетов

**Preconditions:**
- Два Item с разными сокетами созданы

**Test Steps:**
1. Создать два Item с разными сокетами
2. Вызвать `TradeAPI.compare_items(item1, item2)`
3. Проверить сравнение сокетов

**Expected Result:**
- Различия в сокетах выявлены
- Результат корректен

---

## Test Case: TC-TRADE-028
**Title:** TradeAPI.calculate_match_score() base type no match

**Category:** Positive

**Description:** Проверка статического метода calculate_match_score() для base type без совпадения

**Preconditions:**
- Item и TradeQuery с разными base types созданы

**Test Steps:**
1. Создать Item с одним base type
2. Создать TradeQuery с другим base type
3. Вызвать `TradeAPI.calculate_match_score(item, query)`
4. Проверить результат

**Expected Result:**
- match_score низкий или 0
- Отсутствие совпадения учтено
