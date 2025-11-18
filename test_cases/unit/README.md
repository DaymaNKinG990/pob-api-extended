# Unit Test Cases

## Описание

Эта папка содержит структурированные тест-кейсы для всех юнит-тестов проекта pob-api-extended. Тест-кейсы описаны в формате Markdown и организованы по модулям.

**Важно:** Юнит-тесты проверяют отдельные функции, методы и классы в изоляции, а не интеграционное поведение через API.

## Структура файлов

- `01_builders_test_cases.md` - Тест-кейсы для модуля builders (методы классов StatsBuilder, ConfigBuilder, ItemSetBuilder)
- `02_util_functions_test_cases.md` - Тест-кейсы для утилитарных функций модуля util (_get_stat, _item_text, _get_pos, edge cases, exception handling)
- `03_validators_test_cases.md` - Тест-кейсы для модуля validators (статические методы InputValidator, XMLValidator)
- `04_parsers_test_cases.md` - Тест-кейсы для модуля parsers (статические методы классов парсеров)
- `05_exceptions_test_cases.md` - Тест-кейсы для модуля exceptions (классы исключений, наследование, выброс)
- `06_types_test_cases.md` - Тест-кейсы для модуля types (enum классы, методы PassiveNodeID)
- `07_build_modifier_test_cases.md` - Тест-кейсы для модуля build_modifier (BuildModifier класс, модификация билдов)
- `08_factory_test_cases.md` - Тест-кейсы для модуля factory (BuildFactory класс, создание билдов)
- `09_cache_test_cases.md` - Тест-кейсы для модуля cache (Cache класс, декоратор @cached)
- `10_build_builder_test_cases.md` - Тест-кейсы для модуля build_builder (BuildBuilder класс, построение билдов)
- `11_serializers_test_cases.md` - Тест-кейсы для модуля serializers (BuildXMLSerializer, ImportCodeGenerator)
- `12_model_validators_test_cases.md` - Тест-кейсы для модуля model_validators (ModelValidator, функции валидации)
- `13_init_test_cases.md` - Тест-кейсы для модуля __init__ (импорт модулей, обработка опциональных зависимостей)
- `14_calculator_engine_test_cases.md` - Тест-кейсы для модуля calculator.engine (CalculationEngine)
- `15_calculator_modifiers_test_cases.md` - Тест-кейсы для модуля calculator.modifiers (ModifierSystem)
- `16_calculator_skill_modifier_parser_test_cases.md` - Тест-кейсы для модуля calculator.skill_modifier_parser (SkillModifierParser)
- `17_interfaces_test_cases.md` - Тест-кейсы для модуля interfaces (Protocol классы, абстрактные классы)
- `18_http_client_test_cases.md` - Тест-кейсы для модуля HTTP Client (RequestsHTTPClient реализация)
- `19_async_util_test_cases.md` - Тест-кейсы для модуля async_util (асинхронные функции)
- `20_crafting_test_cases.md` - Тест-кейсы для модуля crafting (ItemCraftingAPI, модификаторы)
- `21_trade_test_cases.md` - Тест-кейсы для модуля trade (TradeAPI, фильтры, запросы)
- `22_calculator_damage_test_cases.md` - Тест-кейсы для модуля calculator.damage (DamageCalculator, DamageBreakdown)
- `23_calculator_defense_test_cases.md` - Тест-кейсы для модуля calculator.defense (DefenseCalculator, DefenseStats)
- `24_calculator_resource_test_cases.md` - Тест-кейсы для модуля calculator.resource (ResourceCalculator)
- `25_calculator_skill_stats_test_cases.md` - Тест-кейсы для модуля calculator.skill_stats (SkillStatsCalculator)
- `26_calculator_item_modifier_parser_test_cases.md` - Тест-кейсы для модуля calculator.item_modifier_parser (ItemModifierParser)
- `27_calculator_passive_tree_parser_test_cases.md` - Тест-кейсы для модуля calculator.passive_tree_parser (PassiveTreeParser)
- `28_calculator_game_data_test_cases.md` - Тест-кейсы для модуля calculator.game_data (GameDataLoader, PassiveNode, SkillGem, UniqueItem)
- `29_calculator_penetration_test_cases.md` - Тест-кейсы для модуля calculator.penetration (PenetrationCalculator)
- `30_calculator_conditional_test_cases.md` - Тест-кейсы для модуля calculator.conditional (ConditionEvaluator)
- `31_calculator_config_parser_test_cases.md` - Тест-кейсы для модуля calculator.config_modifier_parser (ConfigModifierParser)
- `32_calculator_unique_item_parser_test_cases.md` - Тест-кейсы для модуля calculator.unique_item_parser (UniqueItemParser)
- `33_calculator_jewel_parser_test_cases.md` - Тест-кейсы для модуля calculator.jewel_parser (JewelParser)
- `34_calculator_party_test_cases.md` - Тест-кейсы для модуля calculator.party (PartyCalculator, PartyMember)
- `35_calculator_minion_test_cases.md` - Тест-кейсы для модуля calculator.minion (MinionCalculator, MinionStats)
- `36_calculator_legion_jewels_test_cases.md` - Тест-кейсы для модуля calculator.legion_jewels (LegionJewelHelper, LegionJewelData, LegionJewelType)
- `37_calculator_mirage_test_cases.md` - Тест-кейсы для модуля calculator.mirage (MirageCalculator, MirageStats)
- `38_calculator_pantheon_test_cases.md` - Тест-кейсы для модуля calculator.pantheon (PantheonTools, PantheonGod, PantheonSoul)
- `39_coverage_gaps_test_cases.md` - Тест-кейсы для модуля test_coverage_gaps (покрытие оставшихся строк в api.py и parsers.py)
- `40_decorators_test_cases.md` - Тест-кейсы для модуля decorators (memoized_property, listify)
- `41_stats_test_cases.md` - Тест-кейсы для модуля stats (Stats dataclass)
- `42_models_test_cases.md` - Тест-кейсы для модуля models (Gem, SkillGroup, Tree, Item, Set, Keystones)
- `43_config_test_cases.md` - Тест-кейсы для модуля config (Config dataclass)
- `44_constants_test_cases.md` - Тест-кейсы для модуля constants (KEYSTONE_IDS, MONSTER_DAMAGE_TABLE, и др.)
- `45_unique_items_extended_test_cases.md` - Тест-кейсы для модуля calculator.unique_items_extended (EXTENDED_UNIQUE_EFFECTS)

## Формат тест-кейса

Каждый тест-кейс содержит следующую информацию:

- **Test Case ID**: Уникальный идентификатор (например, TC-BUILDERS-001)
- **Title**: Название тест-кейса
- **Category**: Категория теста (Positive, Negative, Edge Case)
- **Description**: Описание того, что тестируется
- **Preconditions**: Предусловия для выполнения теста
- **Test Steps**: Пошаговые действия для выполнения теста
- **Expected Result**: Ожидаемый результат выполнения теста

## Категории тестов

- **Positive**: Тесты, проверяющие нормальное (успешное) поведение функции/метода
- **Negative**: Тесты, проверяющие обработку ошибок и невалидных данных
- **Edge Case**: Тесты, проверяющие граничные случаи и особые условия

## Особенности юнит-тестирования

Юнит-тесты в этом проекте проверяют:

1. **Отдельные методы классов** (например, `StatsBuilder.build()`, `ConfigBuilder.build()`)
2. **Утилитарные функции** (например, `_get_stat()`, `_item_text()`)
3. **Статические методы валидации** (например, `InputValidator.validate_url()`)
4. **Методы парсеров** (например, `BuildInfoParser.parse()`, `SkillsParser.parse_skill_groups()`)
5. **Параметризованные тесты** с различными входными данными
6. **Граничные случаи** (пустые данные, отсутствующие элементы, None значения)
7. **Обработку ошибок** на уровне функций/методов

## Использование

Эти тест-кейсы можно использовать для:

1. **Документирования** существующих юнит-тестов
2. **Планирования** новых юнит-тестов
3. **Проверки покрытия** тестами отдельных функций и методов
4. **Понимания** того, какие аспекты функций должны быть протестированы
5. **Автоматизации** тестирования (как спецификация)

## Статус покрытия

Текущие тест-кейсы основаны на анализе существующих юнит-тестов в `tests/unit/`.

### Покрытые модули:
- ✅ Builders (15 тест-кейсов)
- ✅ Util Functions (25 тест-кейсов)
- ✅ Validators (18 тест-кейсов)
- ✅ Parsers (18 тест-кейсов)
- ✅ Exceptions (18 тест-кейсов)
- ✅ Types (22 тест-кейса)
- ✅ Build Modifier (20 тест-кейсов)
- ✅ Factory (15 тест-кейсов)
- ✅ Cache (18 тест-кейсов)
- ✅ Build Builder (23 тест-кейса)
- ✅ Serializers (17 тест-кейсов)
- ✅ Model Validators (31 тест-кейс)
- ✅ Init Module (10 тест-кейсов)
- ✅ Calculator Engine (18 тест-кейсов)
- ✅ Calculator Modifiers (18 тест-кейсов)
- ✅ Calculator Skill Modifier Parser (15 тест-кейсов)
- ✅ Interfaces (11 тест-кейсов)
- ✅ HTTP Client (9 тест-кейсов)
- ✅ Async Util (8 тест-кейсов)
- ✅ Crafting (26 тест-кейсов)
- ✅ Trade (28 тест-кейсов)
- ✅ Calculator Damage (19 тест-кейсов)
- ✅ Calculator Defense (20 тест-кейсов)
- ✅ Calculator Resource (18 тест-кейсов)
- ✅ Calculator Skill Stats (18 тест-кейсов)
- ✅ Calculator Item Modifier Parser (25 тест-кейсов)
- ✅ Calculator Passive Tree Parser (20 тест-кейсов)
- ✅ Calculator Game Data (28 тест-кейсов)
- ✅ Calculator Penetration (13 тест-кейсов)
- ✅ Calculator Conditional (18 тест-кейсов)
- ✅ Calculator Config Parser (19 тест-кейсов)
- ✅ Calculator Unique Item Parser (10 тест-кейсов)
- ✅ Calculator Jewel Parser (20 тест-кейсов)
- ✅ Calculator Party (19 тест-кейсов)
- ✅ Calculator Minion (19 тест-кейсов)
- ✅ Calculator Legion Jewels (19 тест-кейсов)
- ✅ Calculator Mirage (19 тест-кейсов)
- ✅ Calculator Pantheon (15 тест-кейсов)
- ✅ Coverage Gaps (7 тест-кейсов)
- ✅ Decorators (10 тест-кейсов)
- ✅ Stats (15 тест-кейсов)
- ✅ Models (20 тест-кейсов)
- ✅ Config (12 тест-кейсов)
- ✅ Constants (12 тест-кейсов)
- ✅ Unique Items Extended (10 тест-кейсов)

### Модули, требующие дополнения:
- ⏳ Оставшиеся 5 unit-тестов (нужно уточнить, какие именно)
- ✅ API тесты находятся в `test_cases/api/` и исключены из подсчета unit-тестов
- ✅ Все модули из `pobapi/` покрыты тест-кейсами (см. CODE_COVERAGE_ANALYSIS.md)

## Связь с кодом

Тест-кейсы соответствуют тестам в `tests/unit/`:
- `01_builders_test_cases.md` ↔ `test_builders.py`
- `02_util_functions_test_cases.md` ↔ `test_util.py`, `test_util_edge_cases.py`, `test_util_exception_handling.py`
- `03_validators_test_cases.md` ↔ `test_validators.py`
- `04_parsers_test_cases.md` ↔ `test_parsers.py`
- `05_exceptions_test_cases.md` ↔ `test_exceptions.py`
- `06_types_test_cases.md` ↔ `test_types.py`
- `07_build_modifier_test_cases.md` ↔ `test_build_modifier.py`
- `08_factory_test_cases.md` ↔ `test_factory.py`
- `09_cache_test_cases.md` ↔ `test_cache.py`
- `10_build_builder_test_cases.md` ↔ `test_build_builder.py`
- `11_serializers_test_cases.md` ↔ `test_serializers.py`
- `12_model_validators_test_cases.md` ↔ `test_model_validators.py`
- `13_init_test_cases.md` ↔ `test_init.py`
- `14_calculator_engine_test_cases.md` ↔ `test_calculator_engine.py`
- `15_calculator_modifiers_test_cases.md` ↔ `test_calculator_modifiers.py`
- `16_calculator_skill_modifier_parser_test_cases.md` ↔ `test_calculator_skill_modifier_parser.py`
- `17_interfaces_test_cases.md` ↔ `test_interfaces.py`
- `18_http_client_test_cases.md` ↔ `test_http_client.py`
- `19_async_util_test_cases.md` ↔ `test_async_util.py`
- `20_crafting_test_cases.md` ↔ `test_crafting.py`
- `21_trade_test_cases.md` ↔ `test_trade.py`
- `22_calculator_damage_test_cases.md` ↔ `test_calculator_damage.py`
- `23_calculator_defense_test_cases.md` ↔ `test_calculator_defense.py`
- `24_calculator_resource_test_cases.md` ↔ `test_calculator_resource.py`
- `25_calculator_skill_stats_test_cases.md` ↔ `test_calculator_skill_stats.py`
- `26_calculator_item_modifier_parser_test_cases.md` ↔ `test_calculator_item_modifier_parser.py`
- `27_calculator_passive_tree_parser_test_cases.md` ↔ `test_calculator_passive_tree_parser.py`
- `28_calculator_game_data_test_cases.md` ↔ `test_calculator_game_data.py`
- `29_calculator_penetration_test_cases.md` ↔ `test_calculator_penetration.py`
- `30_calculator_conditional_test_cases.md` ↔ `test_calculator_conditional.py`
- `31_calculator_config_parser_test_cases.md` ↔ `test_calculator_config_parser.py`
- `32_calculator_unique_item_parser_test_cases.md` ↔ `test_calculator_unique_item_parser.py`
- `33_calculator_jewel_parser_test_cases.md` ↔ `test_calculator_jewel_parser.py`
- `34_calculator_party_test_cases.md` ↔ `test_calculator_party.py`
- `35_calculator_minion_test_cases.md` ↔ `test_calculator_minion.py`
- `36_calculator_legion_jewels_test_cases.md` ↔ `test_calculator_legion_jewels.py`
- `37_calculator_mirage_test_cases.md` ↔ `test_calculator_mirage.py`
- `38_calculator_pantheon_test_cases.md` ↔ `test_calculator_pantheon.py`
- `39_coverage_gaps_test_cases.md` ↔ `test_coverage_gaps.py`
- `40_decorators_test_cases.md` ↔ `pobapi/decorators.py` (прямое покрытие кода)
- `41_stats_test_cases.md` ↔ `pobapi/stats.py` (прямое покрытие кода)
- `42_models_test_cases.md` ↔ `pobapi/models.py` (прямое покрытие кода)
- `43_config_test_cases.md` ↔ `pobapi/config.py` (прямое покрытие кода)
- `44_constants_test_cases.md` ↔ `pobapi/constants.py` (прямое покрытие кода)
- `45_unique_items_extended_test_cases.md` ↔ `pobapi/calculator/unique_items_extended.py` (прямое покрытие кода)

## Валидация тестов

См. отчеты о соответствии юнит-тестов тест-кейсам:

1. **[TEST_VALIDATION_REPORT.md](./TEST_VALIDATION_REPORT.md)** - Основной отчет о валидации
2. **[DETAILED_VALIDATION_REPORT.md](./DETAILED_VALIDATION_REPORT.md)** - Детальный анализ модулей
3. **[VALIDATION_SUMMARY.md](./VALIDATION_SUMMARY.md)** - Итоговая сводка

Отчеты проверяют:
- ✅ **Корректность** - правильно ли тесты проверяют функциональность
- ✅ **Атомарность** - проверяет ли тест одну вещь
- ✅ **Параметризация** - используется ли где нужно
- ✅ **Моки** - используются ли где нужно
- ✅ **Соответствие логике** - соответствует ли тест логике проверки в тест-кейсах

**Итоговая оценка:** Отлично (9.5/10)

**Покрытие тест-кейсов:** ~95% (для реализованных методов - 100%)

---

## Добавление новых тест-кейсов

При добавлении новых тест-кейсов:

1. Определите, к какому модулю относится тест-кейс
2. Определите, какую функцию/метод он тестирует
3. Откройте соответствующий файл или создайте новый
4. Используйте единый формат описания
5. Присвойте уникальный ID (продолжайте нумерацию)
6. Укажите категорию теста
7. Фокусируйтесь на тестировании отдельной функции/метода в изоляции

## Обновление

Тест-кейсы должны обновляться при:
- Добавлении новых юнит-тестов
- Изменении существующих юнит-тестов
- Изменении функциональности модулей
- Обнаружении новых граничных случаев
