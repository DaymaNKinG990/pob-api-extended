# API Test Cases

## Описание

Эта папка содержит структурированные тест-кейсы для API тестов проекта pob-api-extended. Тест-кейсы описаны в формате Markdown и организованы по модулям.

**Важно:** API тесты (`test_api.py`, `test_api_edge_cases.py`, `test_api_modification.py`) находятся здесь, а не в `test_cases/unit/`, так как они тестируют API-интерфейс, а не отдельные unit-компоненты.

## Структура файлов

- `01_api_test_cases.md` - Тест-кейсы для основного API модуля (pobapi.api) ✅
- `02_builders_test_cases.md` - Тест-кейсы для модуля builders (pobapi.builders) ✅
- `03_parsers_test_cases.md` - Тест-кейсы для модуля parsers (pobapi.parsers) ✅
- `04_validators_test_cases.md` - Тест-кейсы для модуля validators (pobapi.validators) ✅
- `05_exceptions_test_cases.md` - Тест-кейсы для модуля exceptions (pobapi.exceptions) ✅
- `06_types_test_cases.md` - Тест-кейсы для модуля types (pobapi.types) ✅
- `07_util_test_cases.md` - Тест-кейсы для модуля util (pobapi.util) ✅

## Формат тест-кейса

Каждый тест-кейс содержит следующую информацию:

- **Test Case ID**: Уникальный идентификатор (например, TC-API-001)
- **Title**: Название тест-кейса
- **Category**: Категория теста (Positive, Negative, Edge Case)
- **Description**: Описание того, что тестируется
- **Preconditions**: Предусловия для выполнения теста
- **Test Steps**: Пошаговые действия для выполнения теста
- **Expected Result**: Ожидаемый результат выполнения теста

## Категории тестов

- **Positive**: Тесты, проверяющие нормальное (успешное) поведение
- **Negative**: Тесты, проверяющие обработку ошибок и невалидных данных
- **Edge Case**: Тесты, проверяющие граничные случаи и особые условия

## Использование

Эти тест-кейсы можно использовать для:

1. **Документирования** существующих тестов
2. **Планирования** новых тестов
3. **Проверки покрытия** тестами
4. **Ручного тестирования** функциональности
5. **Автоматизации** тестирования (как спецификация)

## Статус покрытия

Текущие тест-кейсы основаны на анализе существующих API тестов в `tests/unit/`.

### Покрытые модули:
- ✅ API (`test_api.py`, `test_api_edge_cases.py`, `test_api_modification.py`) - тест-кейсы в `01_api_test_cases.md`
- ✅ Builders (pobapi.builders) - тест-кейсы в `02_builders_test_cases.md`
- ✅ Parsers (pobapi.parsers) - тест-кейсы в `03_parsers_test_cases.md`
- ✅ Validators (pobapi.validators) - тест-кейсы в `04_validators_test_cases.md`
- ✅ Exceptions (pobapi.exceptions) - тест-кейсы в `05_exceptions_test_cases.md`
- ✅ Types (pobapi.types) - тест-кейсы в `06_types_test_cases.md`
- ✅ Util (pobapi.util) - тест-кейсы в `07_util_test_cases.md`

**Примечание:** Дополнительные unit-тесты для других модулей (Build Modifier, Factory, Cache и т.д.) находятся в `test_cases/unit/`.

## Добавление новых тест-кейсов

При добавлении новых тест-кейсов:

1. Определите, к какому модулю относится тест-кейс
2. Откройте соответствующий файл или создайте новый
3. Используйте единый формат описания
4. Присвойте уникальный ID (продолжайте нумерацию)
5. Укажите категорию теста

## Связь с кодом

Тест-кейсы соответствуют тестам в `tests/unit/`:
- `01_api_test_cases.md` ↔ `test_api.py`, `test_api_edge_cases.py`, `test_api_modification.py`
- `02_builders_test_cases.md` ↔ `test_builders.py`
- `03_parsers_test_cases.md` ↔ тесты парсеров в `tests/unit/`
- `04_validators_test_cases.md` ↔ тесты валидаторов в `tests/unit/`
- `05_exceptions_test_cases.md` ↔ тесты исключений в `tests/unit/`
- `06_types_test_cases.md` ↔ тесты типов в `tests/unit/`
- `07_util_test_cases.md` ↔ тесты утилит в `tests/unit/`

**Дополнительные тесты:**
- Дополнительные unit-тесты (Build Modifier, Factory, Cache, Calculator и т.д.) находятся в `test_cases/unit/`
- Integration тесты должны быть в `test_cases/integration/` (если есть)

## Обновление

Тест-кейсы должны обновляться при:
- Добавлении новых тестов
- Изменении существующих тестов
- Изменении функциональности модулей
- Обнаружении новых граничных случаев
