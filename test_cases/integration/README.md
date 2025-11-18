# Integration Test Cases

## Описание

Эта папка содержит структурированные тест-кейсы для всех интеграционных тестов проекта pob-api-extended. Тест-кейсы описаны в формате Markdown и организованы по интеграционным сценариям.

**Важно:** Интеграционные тесты проверяют взаимодействие между несколькими компонентами системы, а не отдельные функции в изоляции.

## Структура файлов

Тест-кейсы организованы по интеграционным сценариям:

- `01_validator_parser_integration_test_cases.md` - Интеграция валидаторов и парсеров
- `02_parser_builder_integration_test_cases.md` - Интеграция парсеров и билдеров
- `03_factory_integration_test_cases.md` - Интеграция фабрики с другими компонентами
- `04_api_calculation_engine_integration_test_cases.md` - Интеграция API и CalculationEngine
- `05_build_modifier_serializer_integration_test_cases.md` - Интеграция BuildModifier и сериализаторов
- `06_calculator_components_integration_test_cases.md` - Интеграция компонентов калькулятора
- `07_calculator_modifier_integration_test_cases.md` - Интеграция ModifierSystem и калькуляторов
- `08_parser_api_integration_test_cases.md` - Интеграция парсеров и API
- `09_parser_serializer_integration_test_cases.md` - Интеграция парсеров и сериализаторов
- `10_trade_api_integration_test_cases.md` - Интеграция TradeAPI и PathOfBuildingAPI
- `11_trees_parser_integration_test_cases.md` - Интеграция TreesParser с другими компонентами
- `12_crafting_api_integration_test_cases.md` - Интеграция CraftingAPI и PathOfBuildingAPI
- `13_infrastructure_integration_test_cases.md` - Интеграция инфраструктурных компонентов (HTTP, Cache)

## Формат тест-кейса

Каждый тест-кейс содержит следующую информацию:

- **Test Case ID**: Уникальный идентификатор (например, TC-INT-VALIDATOR-PARSER-001)
- **Title**: Название тест-кейса
- **Category**: Категория теста (Positive, Negative, Edge Case)
- **Integration**: Какие компоненты интегрируются (ComponentA ↔ ComponentB)
- **Description**: Описание того, что тестируется
- **Preconditions**: Предусловия для выполнения теста
- **Test Steps**: Пошаговые действия для выполнения теста
- **Expected Result**: Ожидаемый результат выполнения теста

## Категории тестов

- **Positive**: Тесты, проверяющие нормальное (успешное) взаимодействие компонентов
- **Negative**: Тесты, проверяющие обработку ошибок при взаимодействии компонентов
- **Edge Case**: Тесты, проверяющие граничные случаи взаимодействия

## Особенности интеграционного тестирования

Интеграционные тесты в этом проекте проверяют:

1. **Взаимодействие компонентов** (например, `PathOfBuildingAPI` ↔ `CalculationEngine`)
2. **Потоки данных** между компонентами (например, XML → Parser → Builder → API)
3. **Сериализация/десериализация** (например, Build → XML → Build)
4. **Обработку ошибок** на уровне интеграции
5. **Полные рабочие процессы** (end-to-end scenarios)
6. **Интеграцию с внешними системами** (HTTP, Cache)

## Использование

Эти тест-кейсы можно использовать для:

1. **Документирования** существующих интеграционных тестов
2. **Планирования** новых интеграционных тестов
3. **Проверки покрытия** интеграций между компонентами
4. **Понимания** того, какие интеграции должны быть протестированы
5. **Автоматизации** тестирования (как спецификация)

## Статус покрытия

Текущие тест-кейсы основаны на анализе существующих интеграционных тестов в `tests/integrations/`.

### Покрытые интеграции:

- ✅ Validator ↔ Parser
- ✅ Parser ↔ Builder
- ✅ Factory ↔ Parser/Builder
- ✅ API ↔ CalculationEngine
- ✅ BuildModifier ↔ Serializer
- ✅ Calculator Components
- ✅ ModifierSystem ↔ Calculators
- ✅ Parser ↔ API
- ✅ Parser ↔ Serializer
- ✅ TradeAPI ↔ PathOfBuildingAPI
- ✅ TreesParser ↔ Other Components
- ✅ CraftingAPI ↔ PathOfBuildingAPI
- ✅ Infrastructure (HTTP, Cache)

## Связь с кодом

Тест-кейсы соответствуют тестам в `tests/integrations/`:
- `01_validator_parser_integration_test_cases.md` ↔ `test_integration.py::TestValidatorParserIntegration`
- `02_parser_builder_integration_test_cases.md` ↔ `test_integration.py::TestParserBuilderIntegration`
- `03_factory_integration_test_cases.md` ↔ `test_integration.py::TestFactoryIntegration`
- `04_api_calculation_engine_integration_test_cases.md` ↔ `test_api_calculation_engine_integration.py`
- `05_build_modifier_serializer_integration_test_cases.md` ↔ `test_build_modifier_serializer_integration.py`
- `06_calculator_components_integration_test_cases.md` ↔ `test_calculator_components_integration.py`
- `07_calculator_modifier_integration_test_cases.md` ↔ `test_calculator_modifier_integration.py`
- `08_parser_api_integration_test_cases.md` ↔ `test_parser_api_integration.py`
- `09_parser_serializer_integration_test_cases.md` ↔ `test_parser_serializer_integration.py`
- `10_trade_api_integration_test_cases.md` ↔ `test_trade_api_integration.py`
- `11_trees_parser_integration_test_cases.md` ↔ `test_trees_parser_integration.py`
- `12_crafting_api_integration_test_cases.md` ↔ `test_crafting_api_integration.py`
- `13_infrastructure_integration_test_cases.md` ↔ `test_infrastructure_integration.py`
