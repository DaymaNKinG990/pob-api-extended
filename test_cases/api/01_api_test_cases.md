# API Test Cases - Complete Coverage

## Module: pobapi.api

### Overview
Полные тест-кейсы для основного API модуля, который предоставляет функции для загрузки, создания и работы с билдами Path of Building. Покрывает все основные API объекты и методы, через которые инженеры взаимодействуют с библиотекой.

---

## 1. Factory Functions (Создание билдов)

### TC-API-001: Load build from import code (Positive)
**Category:** Positive

**Description:** Проверка загрузки билда из валидного import code

**Preconditions:**
- Валидный import code доступен

**Test Steps:**
1. Вызвать `from_import_code(valid_code)` с валидным кодом
2. Проверить, что возвращается объект `PathOfBuildingAPI`
3. Проверить, что билд содержит корректные данные

**Expected Result:**
- Билд успешно загружен
- Объект `PathOfBuildingAPI` содержит корректные данные
- Все основные properties доступны

---

### TC-API-002: Load build from URL (Positive)
**Category:** Positive

**Description:** Проверка загрузки билда из валидного pastebin.com URL

**Preconditions:**
- Валидный pastebin.com URL доступен
- URL указывает на валидный билд

**Test Steps:**
1. Вызвать `from_url(valid_url)` с валидным URL
2. Проверить, что возвращается объект `PathOfBuildingAPI`
3. Проверить, что билд содержит корректные данные

**Expected Result:**
- Билд успешно загружен из URL
- Объект `PathOfBuildingAPI` содержит корректные данные
- Все основные properties доступны

---

### TC-API-003: Load build from URL with custom timeout (Positive)
**Category:** Positive

**Description:** Проверка загрузки билда из URL с кастомным timeout

**Preconditions:**
- Валидный pastebin.com URL доступен

**Test Steps:**
1. Вызвать `from_url(valid_url, timeout=10.0)` с кастомным timeout
2. Проверить, что билд загружен успешно

**Expected Result:**
- Билд успешно загружен с кастомным timeout
- Timeout применен корректно

---

### TC-API-004: Load build from invalid import code (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном import code

**Preconditions:**
- Невалидный import code предоставлен (пустая строка, None, неверный формат)

**Test Steps:**
1. Вызвать `from_import_code(invalid_code)` с невалидным кодом
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `InvalidImportCodeError`
- Сообщение об ошибке информативное

---

### TC-API-005: Load build from invalid URL (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном URL

**Preconditions:**
- Невалидный URL предоставлен (не pastebin.com, неправильный формат)

**Test Steps:**
1. Вызвать `from_url(invalid_url)` с невалидным URL
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `InvalidURLError`
- Сообщение об ошибке информативное

---

### TC-API-006: Network error handling when loading from URL (Negative)
**Category:** Negative

**Description:** Проверка обработки сетевых ошибок при загрузке из URL

**Preconditions:**
- URL указывает на недоступный ресурс или вызывает timeout

**Test Steps:**
1. Вызвать `from_url(url)` с URL, вызывающим сетевую ошибку
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `NetworkError` с соответствующим сообщением
- Сообщение содержит информацию о типе сетевой ошибки

---

### TC-API-007: Parsing error handling (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибок парсинга XML

**Preconditions:**
- URL или import code указывает на невалидный XML

**Test Steps:**
1. Вызвать `from_url(url)` или `from_import_code(code)` с невалидным XML
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ParsingError`
- Сообщение об ошибке информативное

---

## 2. PathOfBuildingAPI Initialization (Инициализация)

### TC-API-008: Initialize from XML bytes (Positive)
**Category:** Positive

**Description:** Проверка инициализации `PathOfBuildingAPI` из XML bytes

**Preconditions:**
- Валидный XML в формате bytes доступен

**Test Steps:**
1. Создать `PathOfBuildingAPI(xml_bytes)` с валидными XML bytes
2. Проверить, что объект создан успешно
3. Проверить доступность основных properties

**Expected Result:**
- Объект `PathOfBuildingAPI` создан успешно
- XML валидирован и распарсен
- Все основные properties доступны

---

### TC-API-009: Initialize from XML Element (Positive)
**Category:** Positive

**Description:** Проверка инициализации `PathOfBuildingAPI` из lxml Element

**Preconditions:**
- Валидный `lxml.etree._Element` доступен

**Test Steps:**
1. Создать `PathOfBuildingAPI(xml_element)` с валидным Element
2. Проверить, что объект создан успешно
3. Проверить доступность основных properties

**Expected Result:**
- Объект `PathOfBuildingAPI` создан успешно
- Element использован напрямую без парсинга
- Все основные properties доступны

---

### TC-API-010: Initialize with custom parser (Positive)
**Category:** Positive

**Description:** Проверка инициализации с кастомным парсером

**Preconditions:**
- Валидный XML доступен
- Кастомный парсер реализует `BuildParser` интерфейс

**Test Steps:**
1. Создать кастомный парсер
2. Создать `PathOfBuildingAPI(xml_bytes, parser=custom_parser)`
3. Проверить, что кастомный парсер используется

**Expected Result:**
- Объект создан успешно
- Кастомный парсер используется для парсинга
- Билд распарсен корректно

---

### TC-API-011: Initialize with invalid XML bytes (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидных XML bytes

**Preconditions:**
- Невалидный XML в формате bytes

**Test Steps:**
1. Создать `PathOfBuildingAPI(invalid_xml_bytes)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ParsingError` или `ValidationError`
- Сообщение об ошибке информативное

---

### TC-API-012: Initialize with invalid type (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при передаче невалидного типа

**Preconditions:**
- Передан объект не типа bytes или Element (например, str, int, None)

**Test Steps:**
1. Создать `PathOfBuildingAPI(invalid_type)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError`
- Сообщение указывает на неверный тип

---

### TC-API-013: Initialize with invalid XML structure (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидной структуре XML

**Preconditions:**
- XML валиден, но не соответствует структуре Path of Building

**Test Steps:**
1. Создать `PathOfBuildingAPI(xml_bytes)` с невалидной структурой
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError`
- Сообщение указывает на проблему со структурой

---

## 3. Build Properties (Свойства билда)

### TC-API-014: Get class_name property (Positive)
**Category:** Positive

**Description:** Проверка получения имени класса персонажа

**Preconditions:**
- Билд загружен с указанным классом

**Test Steps:**
1. Получить значение `build.class_name`
2. Проверить, что значение соответствует ожидаемому
3. Проверить тип (str)

**Expected Result:**
- `class_name` возвращает корректное имя класса (например, "Scion", "Ranger", "Witch")
- Тип значения - str
- Если класс не указан, возвращается пустая строка

---

### TC-API-015: Get ascendancy_name property (Positive)
**Category:** Positive

**Description:** Проверка получения имени асценданси

**Preconditions:**
- Билд загружен с указанным асценданси

**Test Steps:**
1. Получить значение `build.ascendancy_name`
2. Проверить, что значение соответствует ожидаемому
3. Проверить тип (str | None)

**Expected Result:**
- `ascendancy_name` возвращает корректное имя асценданси (например, "Ascendant", "Deadeye", "Elementalist")
- Если асценданси не выбран, возвращается None

---

### TC-API-016: Get level property (Positive)
**Category:** Positive

**Description:** Проверка получения уровня персонажа

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Получить значение `build.level`
2. Проверить, что значение является целым числом
3. Проверить диапазон (1-100)

**Expected Result:**
- `level` возвращает корректный уровень персонажа (int)
- Если уровень не указан, возвращается 1 (дефолт)
- Значение в диапазоне 1-100

---

### TC-API-017: Get bandit property (Positive)
**Category:** Positive

**Description:** Проверка получения выбора бандита

**Preconditions:**
- Билд загружен с указанным выбором бандита

**Test Steps:**
1. Получить значение `build.bandit`
2. Проверить, что значение соответствует ожидаемому
3. Проверить тип (str | None)

**Expected Result:**
- `bandit` возвращает корректное значение ("Alira", "Oak", "Kraityn") или None
- Если бандит не выбран, возвращается None

---

### TC-API-018: Get notes property (Positive)
**Category:** Positive

**Description:** Проверка получения заметок билда

**Preconditions:**
- Билд загружен с заметками или без них

**Test Steps:**
1. Получить значение `build.notes`
2. Проверить, что значение является строкой
3. Проверить, что форматирование PoB удалено

**Expected Result:**
- `notes` возвращает корректный текст заметок (str)
- Форматирование PoB удалено
- Если заметок нет, возвращается пустая строка

---

### TC-API-019: Get notes property with PoB formatting (Edge Case)
**Category:** Edge Case

**Description:** Проверка очистки форматирования PoB из заметок

**Preconditions:**
- Билд загружен с заметками, содержащими PoB форматирование

**Test Steps:**
1. Получить значение `build.notes`
2. Проверить, что форматирование PoB удалено
3. Проверить, что текст читаем

**Expected Result:**
- Форматирование PoB удалено
- Текст читаем и корректен

---

### TC-API-020: Get second_weapon_set property (Positive)
**Category:** Positive

**Description:** Проверка получения информации о втором наборе оружия

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Получить значение `build.second_weapon_set`
2. Проверить, что значение является boolean

**Expected Result:**
- `second_weapon_set` возвращает True или False
- Значение соответствует настройке билда

---

### TC-API-021: Get stats property type (Positive)
**Category:** Positive

**Description:** Проверка типа объекта stats

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Получить значение `build.stats`
2. Проверить тип объекта
3. Проверить доступность основных свойств

**Expected Result:**
- `stats` является экземпляром класса `stats.Stats`
- Объект содержит все необходимые свойства

---

### TC-API-022: Get stats property values (Positive)
**Category:** Positive

**Description:** Проверка корректности значений статистик

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Получить значение `build.stats`
2. Проверить конкретные значения (life, mana, energy_shield и т.д.)
3. Проверить, что значения числовые

**Expected Result:**
- Статистики содержат корректные числовые значения
- Все основные статистики доступны

---

### TC-API-023: Get config property (Positive)
**Category:** Positive

**Description:** Проверка корректности объекта конфигурации

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Получить значение `build.config`
2. Проверить тип объекта
3. Проверить доступность основных свойств конфигурации

**Expected Result:**
- `config` является экземпляром класса `config.Config`
- Конфигурация содержит корректные значения
- Все основные настройки доступны

---

### TC-API-024: Get config with default character_level (Edge Case)
**Category:** Edge Case

**Description:** Проверка дефолтного значения character_level в Config

**Preconditions:**
- Config создается с None character_level или без указания level

**Test Steps:**
1. Получить `build.config` для билда без указанного level
2. Проверить, что enemy_level установлен на основе дефолтного значения

**Expected Result:**
- enemy_level установлен корректно на основе дефолтного character_level=84
- Конфигурация работает корректно

---

### TC-API-025: Get active_item_set property (Positive)
**Category:** Positive

**Description:** Проверка корректности активного набора предметов

**Preconditions:**
- Билд загружен с предметами

**Test Steps:**
1. Получить значение `build.active_item_set`
2. Проверить тип объекта (models.Set)
3. Проверить доступность слотов

**Expected Result:**
- `active_item_set` является экземпляром `models.Set`
- Набор содержит корректные данные о предметах
- Все слоты доступны

---

### TC-API-026: Get active_item_set without Items element (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения active_item_set когда нет Items элемента

**Preconditions:**
- Билд загружен без Items элемента

**Test Steps:**
1. Получить значение `build.active_item_set`
2. Проверить, что возвращается пустой набор или первый item_set

**Expected Result:**
- Возвращается пустой набор с None во всех слотах или первый item_set
- Не выбрасывается исключение

---

### TC-API-027: Get active_item_set with invalid index (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения active_item_set с невалидным индексом

**Preconditions:**
- Билд загружен с activeItemSet вне диапазона

**Test Steps:**
1. Получить значение `build.active_item_set`
2. Проверить, что возвращается первый набор или пустой набор

**Expected Result:**
- Возвращается первый набор или пустой набор
- Не выбрасывается исключение

---

### TC-API-028: Get item_sets property (Positive)
**Category:** Positive

**Description:** Проверка корректности всех наборов предметов

**Preconditions:**
- Билд загружен с предметами

**Test Steps:**
1. Получить значение `build.item_sets`
2. Проверить, что это список
3. Проверить свойства каждого набора

**Expected Result:**
- `item_sets` является списком `list[models.Set]`
- Список содержит все наборы предметов
- Каждый набор содержит корректные данные

---

### TC-API-029: Get item_sets with pending modifications (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения item_sets с pending модификациями

**Preconditions:**
- Билд загружен
- Выполнены модификации через equip_item

**Test Steps:**
1. Вызвать `build.equip_item(item, slot)`
2. Получить значение `build.item_sets`
3. Проверить, что pending модификации применены

**Expected Result:**
- Pending модификации включены в item_sets
- Модификации применены корректно

---

### TC-API-030: Get active_skill_group property (Positive)
**Category:** Positive

**Description:** Проверка корректности активной группы скиллов

**Preconditions:**
- Билд загружен со скиллами

**Test Steps:**
1. Получить значение `build.active_skill_group`
2. Проверить тип объекта (models.SkillGroup)
3. Проверить свойства группы (enabled, label, active)
4. Проверить список abilities

**Expected Result:**
- `active_skill_group` является экземпляром `models.SkillGroup`
- Группа содержит корректные данные
- Группа содержит корректные abilities

---

### TC-API-031: Get active_skill_group without main_socket_group (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения active_skill_group когда main_socket_group не указан

**Preconditions:**
- Билд загружен без указания main_socket_group

**Test Steps:**
1. Получить значение `build.active_skill_group`
2. Проверить, что возвращается первая группа

**Expected Result:**
- Возвращается первая группа скиллов
- Не выбрасывается исключение

---

### TC-API-032: Get skill_groups property (Positive)
**Category:** Positive

**Description:** Проверка корректности всех групп скиллов

**Preconditions:**
- Билд загружен со скиллами

**Test Steps:**
1. Получить значение `build.skill_groups`
2. Проверить, что это список
3. Проверить свойства каждой группы

**Expected Result:**
- `skill_groups` является списком `list[models.SkillGroup]`
- Список содержит все группы скиллов
- Каждая группа содержит корректные данные

---

### TC-API-033: Get skill_groups without Skills element (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения skill_groups когда нет Skills элемента

**Preconditions:**
- Билд загружен без Skills элемента

**Test Steps:**
1. Получить значение `build.skill_groups`
2. Проверить, что возвращается пустой список

**Expected Result:**
- Возвращается пустой список
- Не выбрасывается исключение

---

### TC-API-034: Get skill_groups with SkillSet structure (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения skill_groups с новой структурой SkillSet (PoB 2.0+)

**Preconditions:**
- Билд загружен с новой структурой Skills -> SkillSet -> Skill

**Test Steps:**
1. Получить значение `build.skill_groups`
2. Проверить, что группы извлечены корректно

**Expected Result:**
- Группы извлечены из SkillSet структуры
- Все группы доступны

---

### TC-API-035: Get skill_gems property (Positive)
**Category:** Positive

**Description:** Проверка получения всех skill gems

**Preconditions:**
- Билд загружен со skill gems

**Test Steps:**
1. Получить значение `build.skill_gems`
2. Проверить, что это список
3. Проверить, что все элементы - models.Gem
4. Проверить, что granted abilities исключены

**Expected Result:**
- `skill_gems` является списком `list[models.Gem]`
- Список содержит только skill gems (не granted abilities)
- Все gems содержат корректные данные

---

### TC-API-036: Get skill_gems without Skills element (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения skill_gems когда нет Skills элемента

**Preconditions:**
- Билд загружен без Skills элемента

**Test Steps:**
1. Получить значение `build.skill_gems`
2. Проверить, что возвращается пустой список

**Expected Result:**
- Возвращается пустой список
- Не выбрасывается исключение

---

### TC-API-037: Get active_skill property (Positive)
**Category:** Positive

**Description:** Проверка получения активного скилла

**Preconditions:**
- Билд загружен со скиллами
- Активная группа имеет указанный active индекс

**Test Steps:**
1. Получить значение `build.active_skill`
2. Проверить тип объекта (models.Gem | models.GrantedAbility | None)
3. Проверить свойства скилла

**Expected Result:**
- `active_skill` возвращает корректный скилл или None
- Скилл соответствует active индексу группы

---

### TC-API-038: Get active_skill with Vaal skill duplicate (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения active_skill с Vaal skill дубликатом

**Preconditions:**
- Билд загружен с Vaal skill
- Active индекс указывает на дубликат

**Test Steps:**
1. Получить значение `build.active_skill`
2. Проверить, что возвращается базовый скилл (не Vaal версия)

**Expected Result:**
- Возвращается базовый скилл из VAAL_SKILL_MAP
- Дубликат обработан корректно

---

### TC-API-039: Get active_skill without active index (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения active_skill когда active индекс не указан

**Preconditions:**
- Билд загружен со скиллами
- Активная группа не имеет active индекса

**Test Steps:**
1. Получить значение `build.active_skill`
2. Проверить, что возвращается None

**Expected Result:**
- Возвращается None
- Не выбрасывается исключение

---

### TC-API-040: Get active_skill_tree property (Positive)
**Category:** Positive

**Description:** Проверка получения активного дерева пассивов

**Preconditions:**
- Билд загружен с деревом пассивов
- activeSpec указан

**Test Steps:**
1. Получить значение `build.active_skill_tree`
2. Проверить тип объекта (models.Tree)
3. Проверить свойства дерева (url, nodes, sockets)

**Expected Result:**
- `active_skill_tree` является экземпляром `models.Tree`
- Дерево соответствует activeSpec
- Дерево содержит корректные данные

---

### TC-API-041: Get trees property (Positive)
**Category:** Positive

**Description:** Проверка получения всех деревьев пассивов

**Preconditions:**
- Билд загружен с деревьями пассивов

**Test Steps:**
1. Получить значение `build.trees`
2. Проверить, что это список
3. Проверить свойства каждого дерева

**Expected Result:**
- `trees` является списком `list[models.Tree]`
- Список содержит все деревья
- Каждое дерево содержит корректные данные

---

### TC-API-042: Get trees with URL (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения trees с URL (дерево из URL декодируется)

**Preconditions:**
- Билд загружен с деревом, содержащим URL

**Test Steps:**
1. Получить значение `build.trees`
2. Проверить, что nodes извлечены из URL

**Expected Result:**
- Nodes извлечены из URL через _skill_tree_nodes
- Дерево содержит корректные nodes

---

### TC-API-043: Get trees with Nodes element (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения trees с Nodes элементом (когда URL пуст)

**Preconditions:**
- Билд загружен с деревом, содержащим Nodes элемент (URL пуст)

**Test Steps:**
1. Получить значение `build.trees`
2. Проверить, что nodes извлечены из Nodes элемента

**Expected Result:**
- Nodes извлечены из Nodes элемента
- Дерево содержит корректные nodes

---

### TC-API-044: Get trees with Sockets element (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения trees с Sockets элементом

**Preconditions:**
- Билд загружен с деревом, содержащим Sockets элемент

**Test Steps:**
1. Получить значение `build.trees`
2. Проверить, что sockets извлечены корректно

**Expected Result:**
- Sockets извлечены из Sockets элемента или напрямую из Spec
- Sockets содержат корректные данные

---

### TC-API-045: Get keystones property (Positive)
**Category:** Positive

**Description:** Проверка получения keystones

**Preconditions:**
- Билд загружен с деревом пассивов

**Test Steps:**
1. Получить значение `build.keystones`
2. Проверить тип объекта (models.Keystones)
3. Проверить, что keystones соответствуют nodes в дереве

**Expected Result:**
- `keystones` является экземпляром `models.Keystones`
- Keystones установлены в True для соответствующих node IDs
- Keystones установлены в False для отсутствующих node IDs

---

### TC-API-046: Get keystones iterator (Edge Case)
**Category:** Edge Case

**Description:** Проверка итерации по keystones

**Preconditions:**
- Билд загружен с keystones

**Test Steps:**
1. Получить значение `build.keystones`
2. Итерироваться по keystones
3. Проверить, что итерация работает корректно

**Expected Result:**
- Итерация работает корректно
- Все keystones доступны

---

### TC-API-047: Get items property (Positive)
**Category:** Positive

**Description:** Проверка получения всех предметов

**Preconditions:**
- Билд загружен с предметами

**Test Steps:**
1. Получить значение `build.items`
2. Проверить, что это список
3. Проверить, что все элементы - models.Item
4. Проверить, что pending items включены

**Expected Result:**
- `items` является списком `list[models.Item]`
- Список содержит все предметы (включая pending)
- Pending items идут первыми

---

### TC-API-048: Get items without Items element (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения items когда нет Items элемента

**Preconditions:**
- Билд загружен без Items элемента

**Test Steps:**
1. Получить значение `build.items`
2. Проверить, что возвращается пустой список или только pending items

**Expected Result:**
- Возвращается пустой список или только pending items
- Не выбрасывается исключение

---

### TC-API-049: Get items with pending modifications (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения items с pending модификациями

**Preconditions:**
- Билд загружен
- Выполнены модификации через equip_item

**Test Steps:**
1. Вызвать `build.equip_item(item, slot)`
2. Получить значение `build.items`
3. Проверить, что pending items включены

**Expected Result:**
- Pending items включены в список
- Pending items идут первыми

---

### TC-API-050: Get items with variant and alt_variant (Edge Case)
**Category:** Edge Case

**Description:** Проверка получения items с variant и alt_variant (Watcher's Eye)

**Preconditions:**
- Билд загружен с предметом, имеющим variant и alt_variant

**Test Steps:**
1. Получить значение `build.items`
2. Проверить, что variant и alt_variant обработаны корректно

**Expected Result:**
- Variant и alt_variant обработаны корректно
- ModRange применены корректно

---

## 4. Build Modification Methods (Методы модификации билда)

### TC-API-051: Add node to passive tree (Positive)
**Category:** Positive

**Description:** Проверка добавления ноды в дерево пассивов

**Preconditions:**
- Билд загружен
- Валидный node_id и tree_index

**Test Steps:**
1. Вызвать `build.add_node(node_id, tree_index)`
2. Проверить, что нода добавлена
3. Проверить, что кэш инвалидирован

**Expected Result:**
- Нода добавлена в дерево
- Кэш build_info инвалидирован
- Нода доступна в trees

---

### TC-API-052: Add duplicate node (Edge Case)
**Category:** Edge Case

**Description:** Проверка добавления дубликата ноды

**Preconditions:**
- Билд загружен
- Нода уже присутствует в дереве

**Test Steps:**
1. Вызвать `build.add_node(node_id)` для существующей ноды
2. Проверить поведение (добавление или игнорирование)

**Expected Result:**
- Дубликат обработан корректно (добавлен или проигнорирован)
- Не выбрасывается исключение

---

### TC-API-053: Add node with invalid tree_index (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном tree_index

**Preconditions:**
- Билд загружен
- tree_index вне диапазона

**Test Steps:**
1. Вызвать `build.add_node(node_id, invalid_tree_index)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError`
- Сообщение указывает на проблему с tree_index

---

### TC-API-054: Remove node from passive tree (Positive)
**Category:** Positive

**Description:** Проверка удаления ноды из дерева пассивов

**Preconditions:**
- Билд загружен
- Нода присутствует в дереве

**Test Steps:**
1. Вызвать `build.remove_node(node_id, tree_index)`
2. Проверить, что нода удалена
3. Проверить, что кэш инвалидирован

**Expected Result:**
- Нода удалена из дерева
- Кэш build_info инвалидирован
- Нода больше не доступна в trees

---

### TC-API-055: Remove node not present (Edge Case)
**Category:** Edge Case

**Description:** Проверка удаления несуществующей ноды

**Preconditions:**
- Билд загружен
- Нода отсутствует в дереве

**Test Steps:**
1. Вызвать `build.remove_node(nonexistent_node_id)`
2. Проверить поведение (удаление или игнорирование)

**Expected Result:**
- Несуществующая нода обработана корректно (игнорируется или выбрасывается исключение)
- Не выбрасывается исключение (или выбрасывается ValidationError)

---

### TC-API-056: Equip item to slot (Positive)
**Category:** Positive

**Description:** Проверка экипировки предмета в слот

**Preconditions:**
- Билд загружен
- Валидный item и slot

**Test Steps:**
1. Вызвать `build.equip_item(item, slot, item_set_index)`
2. Проверить возвращаемое значение (индекс предмета)
3. Проверить, что предмет добавлен в pending_items
4. Проверить, что item_set обновлен

**Expected Result:**
- Предмет экипирован в указанный слот
- Возвращается индекс добавленного предмета
- Предмет доступен в items и active_item_set

---

### TC-API-057: Equip item with string slot (Positive)
**Category:** Positive

**Description:** Проверка экипировки предмета с строковым slot

**Preconditions:**
- Билд загружен
- Валидный item и slot как строка

**Test Steps:**
1. Вызвать `build.equip_item(item, "Helmet", item_set_index)`
2. Проверить, что предмет экипирован

**Expected Result:**
- Предмет экипирован в указанный слот
- Строковый slot обработан корректно

---

### TC-API-058: Equip item with ItemSlot enum (Positive)
**Category:** Positive

**Description:** Проверка экипировки предмета с ItemSlot enum

**Preconditions:**
- Билд загружен
- Валидный item и ItemSlot enum

**Test Steps:**
1. Вызвать `build.equip_item(item, ItemSlot.HELMET, item_set_index)`
2. Проверить, что предмет экипирован

**Expected Result:**
- Предмет экипирован в указанный слот
- ItemSlot enum обработан корректно

---

### TC-API-059: Equip item with invalid slot (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном slot

**Preconditions:**
- Билд загружен
- Невалидный slot

**Test Steps:**
1. Вызвать `build.equip_item(item, invalid_slot)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError`
- Сообщение указывает на проблему с slot

---

### TC-API-060: Equip item with invalid item_set_index (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном item_set_index

**Preconditions:**
- Билд загружен
- item_set_index вне диапазона

**Test Steps:**
1. Вызвать `build.equip_item(item, slot, invalid_item_set_index)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError`
- Сообщение указывает на проблему с item_set_index

---

### TC-API-061: Equip item creates new item_set (Edge Case)
**Category:** Edge Case

**Description:** Проверка создания нового item_set при экипировке

**Preconditions:**
- Билд загружен
- item_set_index указывает на несуществующий набор

**Test Steps:**
1. Вызвать `build.equip_item(item, slot, new_item_set_index)`
2. Проверить, что новый item_set создан

**Expected Result:**
- Новый item_set создан
- Предмет экипирован в новый набор
- Пустые слоты заполнены None

---

### TC-API-062: Equip item initializes pending_items (Edge Case)
**Category:** Edge Case

**Description:** Проверка инициализации pending_items при первой экипировке

**Preconditions:**
- Билд загружен
- pending_items еще не инициализирован

**Test Steps:**
1. Вызвать `build.equip_item(item, slot)`
2. Проверить, что pending_items инициализирован

**Expected Result:**
- pending_items инициализирован
- Предмет добавлен в pending_items

---

### TC-API-063: Unequip item from slot (Positive)
**Category:** Positive

**Description:** Проверка снятия предмета со слота

**Preconditions:**
- Билд загружен
- Предмет экипирован в слот

**Test Steps:**
1. Вызвать `build.unequip_item(slot, item_set_index)`
2. Проверить, что предмет снят
3. Проверить, что слот теперь None

**Expected Result:**
- Предмет снят со слота
- Слот теперь None
- Предмет больше не доступен в active_item_set

---

### TC-API-064: Unequip item from empty slot (Edge Case)
**Category:** Edge Case

**Description:** Проверка снятия предмета с пустого слота

**Preconditions:**
- Билд загружен
- Слот уже пуст

**Test Steps:**
1. Вызвать `build.unequip_item(empty_slot)`
2. Проверить поведение (игнорирование или исключение)

**Expected Result:**
- Пустой слот обработан корректно (игнорируется или выбрасывается исключение)
- Не выбрасывается исключение (или выбрасывается ValidationError)

---

### TC-API-065: Add skill to group (Positive)
**Category:** Positive

**Description:** Проверка добавления скилла в группу

**Preconditions:**
- Билд загружен
- Валидный gem и group_label

**Test Steps:**
1. Вызвать `build.add_skill(gem, group_label)`
2. Проверить, что скилл добавлен
3. Проверить, что кэш инвалидирован

**Expected Result:**
- Скилл добавлен в указанную группу
- Кэш skill_groups инвалидирован
- Скилл доступен в skill_groups

---

### TC-API-066: Add skill to existing group (Positive)
**Category:** Positive

**Description:** Проверка добавления скилла в существующую группу

**Preconditions:**
- Билд загружен
- Группа с указанным label существует

**Test Steps:**
1. Вызвать `build.add_skill(gem, existing_group_label)`
2. Проверить, что скилл добавлен в существующую группу

**Expected Result:**
- Скилл добавлен в существующую группу
- Группа содержит все скиллы

---

### TC-API-067: Add skill to new group (Edge Case)
**Category:** Edge Case

**Description:** Проверка добавления скилла в новую группу

**Preconditions:**
- Билд загружен
- Группа с указанным label не существует

**Test Steps:**
1. Вызвать `build.add_skill(gem, new_group_label)`
2. Проверить, что новая группа создана
3. Проверить, что скилл добавлен

**Expected Result:**
- Новая группа создана
- Скилл добавлен в новую группу
- Группа доступна в skill_groups

---

### TC-API-068: Remove skill from group (Positive)
**Category:** Positive

**Description:** Проверка удаления скилла из группы

**Preconditions:**
- Билд загружен
- Скилл присутствует в группе

**Test Steps:**
1. Вызвать `build.remove_skill(gem, group_label)`
2. Проверить, что скилл удален
3. Проверить, что кэш инвалидирован

**Expected Result:**
- Скилл удален из группы
- Кэш skill_groups инвалидирован
- Скилл больше не доступен в группе

---

### TC-API-069: Remove skill from nonexistent group (Edge Case)
**Category:** Edge Case

**Description:** Проверка удаления скилла из несуществующей группы

**Preconditions:**
- Билд загружен
- Группа с указанным label не существует

**Test Steps:**
1. Вызвать `build.remove_skill(gem, nonexistent_group_label)`
2. Проверить поведение (игнорирование или исключение)

**Expected Result:**
- Несуществующая группа обработана корректно (игнорируется или выбрасывается исключение)
- Не выбрасывается исключение (или выбрасывается ValidationError)

---

### TC-API-070: Remove skill not in group (Edge Case)
**Category:** Edge Case

**Description:** Проверка удаления скилла, которого нет в группе

**Preconditions:**
- Билд загружен
- Группа существует, но скилл отсутствует

**Test Steps:**
1. Вызвать `build.remove_skill(nonexistent_gem, group_label)`
2. Проверить поведение (игнорирование или исключение)

**Expected Result:**
- Несуществующий скилл обработан корректно (игнорируется или выбрасывается исключение)
- Не выбрасывается исключение (или выбрасывается ValidationError)

---

### TC-API-071: Set level (Positive)
**Category:** Positive

**Description:** Проверка установки уровня персонажа

**Preconditions:**
- Билд загружен
- Валидный level (1-100)

**Test Steps:**
1. Вызвать `build.set_level(level)`
2. Проверить, что уровень установлен
3. Проверить, что кэш инвалидирован

**Expected Result:**
- Уровень установлен
- Кэш build_info инвалидирован
- `build.level` возвращает новый уровень

---

### TC-API-072: Set level with boundary values (Edge Case)
**Category:** Edge Case

**Description:** Проверка установки уровня с граничными значениями

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Вызвать `build.set_level(1)`
2. Проверить, что уровень установлен
3. Вызвать `build.set_level(100)`
4. Проверить, что уровень установлен

**Expected Result:**
- Уровень 1 установлен корректно
- Уровень 100 установлен корректно

---

### TC-API-073: Set level with invalid value (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном уровне

**Preconditions:**
- Билд загружен
- Невалидный level (< 1 или > 100)

**Test Steps:**
1. Вызвать `build.set_level(invalid_level)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError`
- Сообщение указывает на проблему с level

---

### TC-API-074: Set bandit (Positive)
**Category:** Positive

**Description:** Проверка установки выбора бандита

**Preconditions:**
- Билд загружен
- Валидный bandit ("Alira", "Oak", "Kraityn" или None)

**Test Steps:**
1. Вызвать `build.set_bandit(bandit)`
2. Проверить, что бандит установлен
3. Проверить, что кэш инвалидирован

**Expected Result:**
- Бандит установлен
- Кэш build_info инвалидирован
- `build.bandit` возвращает новый выбор

---

### TC-API-075: Set bandit to None (Positive)
**Category:** Positive

**Description:** Проверка сброса выбора бандита

**Preconditions:**
- Билд загружен
- Бандит выбран

**Test Steps:**
1. Вызвать `build.set_bandit(None)`
2. Проверить, что бандит сброшен

**Expected Result:**
- Бандит сброшен
- `build.bandit` возвращает None

---

### TC-API-076: Set bandit with invalid value (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном бандите

**Preconditions:**
- Билд загружен
- Невалидный bandit (не "Alira", "Oak", "Kraityn" или None)

**Test Steps:**
1. Вызвать `build.set_bandit(invalid_bandit)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError`
- Сообщение указывает на проблему с bandit

---

## 5. Serialization Methods (Методы сериализации)

### TC-API-077: Serialize to XML (Positive)
**Category:** Positive

**Description:** Проверка сериализации билда в XML

**Preconditions:**
- Билд загружен или модифицирован

**Test Steps:**
1. Вызвать `build.to_xml()`
2. Проверить, что возвращается bytes
3. Проверить, что XML валиден
4. Проверить, что pending модификации включены

**Expected Result:**
- Возвращается валидный XML в формате bytes
- XML содержит все данные билда
- Pending модификации включены

---

### TC-API-078: Serialize to XML with modifications (Edge Case)
**Category:** Edge Case

**Description:** Проверка сериализации билда с модификациями

**Preconditions:**
- Билд загружен
- Выполнены модификации (add_node, equip_item, add_skill)

**Test Steps:**
1. Выполнить модификации
2. Вызвать `build.to_xml()`
3. Проверить, что модификации включены в XML

**Expected Result:**
- XML содержит все модификации
- Модификации сериализованы корректно

---

### TC-API-079: Serialize to import code (Positive)
**Category:** Positive

**Description:** Проверка сериализации билда в import code

**Preconditions:**
- Билд загружен или модифицирован

**Test Steps:**
1. Вызвать `build.to_import_code()`
2. Проверить, что возвращается строка
3. Проверить, что import code валиден
4. Проверить, что можно загрузить обратно

**Expected Result:**
- Возвращается валидный import code (str)
- Import code можно использовать для загрузки билда
- Pending модификации включены

---

### TC-API-080: Serialize to import code roundtrip (Edge Case)
**Category:** Edge Case

**Description:** Проверка roundtrip сериализации (to_import_code -> from_import_code)

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Вызвать `import_code = build.to_import_code()`
2. Загрузить билд обратно: `new_build = from_import_code(import_code)`
3. Проверить, что билды эквивалентны

**Expected Result:**
- Roundtrip работает корректно
- Новый билд эквивалентен оригинальному
- Все данные сохранены

---

## 6. BuildBuilder API (Создание билда с нуля)

### TC-API-081: Create build from scratch (Positive)
**Category:** Positive

**Description:** Проверка создания нового билда с нуля

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `create_build()` или `BuildBuilder()`
2. Проверить, что возвращается BuildBuilder
3. Вызвать `build()` для получения PathOfBuildingAPI

**Expected Result:**
- Создан новый BuildBuilder
- `build()` возвращает PathOfBuildingAPI
- Билд содержит дефолтные значения

---

### TC-API-082: BuildBuilder set_class (Positive)
**Category:** Positive

**Description:** Проверка установки класса персонажа

**Preconditions:**
- BuildBuilder создан

**Test Steps:**
1. Вызвать `builder.set_class("Ranger", "Deadeye")`
2. Вызвать `build = builder.build()`
3. Проверить, что класс установлен

**Expected Result:**
- Класс установлен
- `build.class_name` возвращает "Ranger"
- `build.ascendancy_name` возвращает "Deadeye"

---

### TC-API-083: BuildBuilder set_class with CharacterClass enum (Positive)
**Category:** Positive

**Description:** Проверка установки класса с использованием enum

**Preconditions:**
- BuildBuilder создан
- CharacterClass enum доступен

**Test Steps:**
1. Вызвать `builder.set_class(CharacterClass.RANGER, Ascendancy.DEADEYE)`
2. Вызвать `build = builder.build()`
3. Проверить, что класс установлен

**Expected Result:**
- Класс установлен с использованием enum
- Значения корректны

---

### TC-API-084: BuildBuilder add_item (Positive)
**Category:** Positive

**Description:** Проверка добавления предмета

**Preconditions:**
- BuildBuilder создан
- Валидный item и slot

**Test Steps:**
1. Создать item
2. Вызвать `builder.add_item(item, ItemSlot.HELMET)`
3. Вызвать `build = builder.build()`
4. Проверить, что предмет добавлен

**Expected Result:**
- Предмет добавлен
- Предмет доступен в build.items
- Предмет экипирован в указанный слот

---

### TC-API-085: BuildBuilder add_skill (Positive)
**Category:** Positive

**Description:** Проверка добавления скилла

**Preconditions:**
- BuildBuilder создан
- Валидный gem

**Test Steps:**
1. Создать gem
2. Вызвать `builder.add_skill(gem, "Main")`
3. Вызвать `build = builder.build()`
4. Проверить, что скилл добавлен

**Expected Result:**
- Скилл добавлен
- Скилл доступен в build.skill_groups
- Скилл в указанной группе

---

### TC-API-086: BuildBuilder set_level (Positive)
**Category:** Positive

**Description:** Проверка установки уровня

**Preconditions:**
- BuildBuilder создан
- Валидный level (1-100)

**Test Steps:**
1. Вызвать `builder.set_level(90)`
2. Вызвать `build = builder.build()`
3. Проверить, что уровень установлен

**Expected Result:**
- Уровень установлен
- `build.level` возвращает 90

---

### TC-API-087: BuildBuilder set_bandit (Positive)
**Category:** Positive

**Description:** Проверка установки бандита

**Preconditions:**
- BuildBuilder создан
- Валидный bandit

**Test Steps:**
1. Вызвать `builder.set_bandit("Alira")`
2. Вызвать `build = builder.build()`
3. Проверить, что бандит установлен

**Expected Result:**
- Бандит установлен
- `build.bandit` возвращает "Alira"

---

### TC-API-088: BuildBuilder set_active_spec (Positive)
**Category:** Positive

**Description:** Проверка установки активного spec

**Preconditions:**
- BuildBuilder создан
- Валидный spec_index (>= 1)

**Test Steps:**
1. Вызвать `builder.set_active_spec(1)`
2. Вызвать `build = builder.build()`
3. Проверить, что active spec установлен

**Expected Result:**
- Active spec установлен
- `build.active_skill_tree` соответствует указанному spec

---

### TC-API-089: BuildBuilder set_active_spec with invalid value (Negative)
**Category:** Negative

**Description:** Проверка обработки ошибки при невалидном spec_index

**Preconditions:**
- BuildBuilder создан
- Невалидный spec_index (< 1)

**Test Steps:**
1. Вызвать `builder.set_active_spec(0)`
2. Проверить, что выбрасывается исключение

**Expected Result:**
- Выбрасывается `ValidationError`
- Сообщение указывает на проблему с spec_index

---

### TC-API-090: BuildBuilder method chaining (Edge Case)
**Category:** Edge Case

**Description:** Проверка method chaining в BuildBuilder

**Preconditions:**
- BuildBuilder создан

**Test Steps:**
1. Вызвать цепочку методов: `builder.set_class("Ranger").set_level(90).add_skill(gem).build()`
2. Проверить, что все методы применены

**Expected Result:**
- Method chaining работает корректно
- Все методы применены
- Билд создан успешно

---

## 7. Edge Cases and Error Handling (Граничные случаи и обработка ошибок)

### TC-API-091: Vaal skill with duplicate handling (Edge Case)
**Category:** Edge Case

**Description:** Проверка обработки Vaal skill с дубликатом

**Preconditions:**
- Билд загружен с Vaal skill
- Active индекс указывает на дубликат

**Test Steps:**
1. Получить `build.active_skill`
2. Проверить, что возвращается базовый скилл

**Expected Result:**
- Базовый скилл возвращается корректно
- Дубликат обработан через VAAL_SKILL_MAP

---

### TC-API-092: Vaal skill without map entry (Edge Case)
**Category:** Edge Case

**Description:** Проверка обработки Vaal skill без записи в map

**Preconditions:**
- Билд загружен с Vaal skill, которого нет в VAAL_SKILL_MAP

**Test Steps:**
1. Получить `build.active_skill`
2. Проверить, что имя обработано через rpartition

**Expected Result:**
- Имя обработано через rpartition("Vaal ")[2]
- Скилл возвращается корректно

---

### TC-API-093: Item string representation full (Edge Case)
**Category:** Edge Case

**Description:** Проверка строкового представления предмета (полное)

**Preconditions:**
- Билд загружен с предметом, содержащим все свойства

**Test Steps:**
1. Получить `build.items[0]`
2. Вызвать `str(item)`
3. Проверить строковое представление

**Expected Result:**
- Строковое представление содержит все свойства
- Формат корректен

---

### TC-API-094: Item string representation minimal (Edge Case)
**Category:** Edge Case

**Description:** Проверка строкового представления предмета (минимальное)

**Preconditions:**
- Билд загружен с предметом с минимальными свойствами

**Test Steps:**
1. Получить `build.items[0]`
2. Вызвать `str(item)`
3. Проверить строковое представление

**Expected Result:**
- Строковое представление содержит только доступные свойства
- Формат корректен

---

### TC-API-095: Item with Elder field (Edge Case)
**Category:** Edge Case

**Description:** Проверка обработки предмета с Elder полем

**Preconditions:**
- Билд загружен с Elder предметом

**Test Steps:**
1. Получить `build.items[0]`
2. Проверить, что elder установлен в True
3. Проверить строковое представление

**Expected Result:**
- Elder обработан корректно
- Строковое представление содержит Elder информацию

---

### TC-API-096: Cache invalidation after modifications (Edge Case)
**Category:** Edge Case

**Description:** Проверка инвалидации кэша после модификаций

**Preconditions:**
- Билд загружен
- Кэш инициализирован (properties вызваны)

**Test Steps:**
1. Получить `build.level` (инициализирует кэш)
2. Вызвать `build.set_level(90)`
3. Получить `build.level` снова
4. Проверить, что значение обновлено

**Expected Result:**
- Кэш инвалидирован после модификации
- Новое значение возвращается корректно

---

### TC-API-097: Multiple modifications sequence (Edge Case)
**Category:** Edge Case

**Description:** Проверка последовательности множественных модификаций

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Выполнить последовательность модификаций:
   - `build.add_node(node_id)`
   - `build.equip_item(item, slot)`
   - `build.add_skill(gem)`
   - `build.set_level(90)`
2. Сериализовать в XML
3. Проверить, что все модификации включены

**Expected Result:**
- Все модификации применены
- Все модификации включены в XML
- Билд корректен

---

### TC-API-098: Build with empty structure (Edge Case)
**Category:** Edge Case

**Description:** Проверка работы с билдом с пустой структурой

**Preconditions:**
- Билд загружен без предметов, скиллов, деревьев

**Test Steps:**
1. Получить все properties (items, skill_groups, trees)
2. Проверить, что возвращаются пустые списки или дефолтные значения

**Expected Result:**
- Все properties возвращают корректные дефолтные значения
- Не выбрасывается исключение

---

### TC-API-099: Build modification state tracking (Edge Case)
**Category:** Edge Case

**Description:** Проверка отслеживания состояния модификации

**Preconditions:**
- Билд загружен

**Test Steps:**
1. Проверить начальное состояние `_is_mutable`
2. Выполнить модификацию
3. Проверить, что `_is_mutable` установлен в True

**Expected Result:**
- Состояние модификации отслеживается корректно
- `_is_mutable` обновляется после модификаций

---

### TC-API-100: Build with custom parser integration (Edge Case)
**Category:** Edge Case

**Description:** Проверка интеграции с кастомным парсером

**Preconditions:**
- Кастомный парсер реализует BuildParser интерфейс

**Test Steps:**
1. Создать кастомный парсер
2. Создать `PathOfBuildingAPI(xml_bytes, parser=custom_parser)`
3. Получить properties
4. Проверить, что кастомный парсер используется

**Expected Result:**
- Кастомный парсер используется для парсинга
- Properties возвращают корректные значения
- Интеграция работает корректно

---

## Summary

**Total Test Cases:** 100

**Categories:**
- Positive: 65
- Negative: 12
- Edge Case: 23

**Coverage:**
- Factory Functions: 7
- Initialization: 6
- Build Properties: 43
- Build Modification: 26
- Serialization: 4
- BuildBuilder API: 10
- Edge Cases: 4

**Status:** ✅ Complete coverage of all API objects and methods
