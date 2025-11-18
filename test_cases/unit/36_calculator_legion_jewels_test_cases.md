# Calculator Legion Jewels Unit Test Cases

## Module: pobapi.calculator.legion_jewels

### Overview
Юнит-тест-кейсы для модуля calculator.legion_jewels, который отвечает за обработку Legion (Timeless) Jewels.

---

## Test Case: TC-CALC-LEGION-001
**Title:** LegionJewelType constants

**Category:** Positive

**Description:** Проверка констант LegionJewelType

**Preconditions:**
- Нет

**Test Steps:**
1. Проверить значения констант LegionJewelType
2. Проверить результаты

**Expected Result:**
- LegionJewelType.GLORIOUS_VANITY == 1
- LegionJewelType.LETHAL_PRIDE == 2
- LegionJewelType.BRUTAL_RESTRAINT == 3
- LegionJewelType.MILITANT_FAITH == 4
- LegionJewelType.ELEGANT_HUBRIS == 5

---

## Test Case: TC-CALC-LEGION-002
**Title:** LegionJewelData.__init__() basic initialization

**Category:** Positive

**Description:** Проверка базовой инициализации LegionJewelData

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `LegionJewelData(jewel_type=1, seed=12345)`
2. Проверить значения атрибутов

**Expected Result:**
- data.jewel_type == 1
- data.seed == 12345
- data.node_id is None
- data.modified_nodes == {}

---

## Test Case: TC-CALC-LEGION-003
**Title:** LegionJewelData.__init__() with node_id

**Category:** Positive

**Description:** Проверка инициализации LegionJewelData с node_id

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `LegionJewelData(jewel_type=1, seed=12345, node_id=39085)`
2. Проверить значения атрибутов

**Expected Result:**
- data.node_id == 39085
- node_id установлен корректно

---

## Test Case: TC-CALC-LEGION-004
**Title:** LegionJewelData.__init__() with modified_nodes

**Category:** Positive

**Description:** Проверка инициализации LegionJewelData с modified_nodes

**Preconditions:**
- Нет

**Test Steps:**
1. Создать modified_nodes dict
2. Вызвать LegionJewelData с modified_nodes
3. Проверить результат

**Expected Result:**
- data.modified_nodes == modified
- modified_nodes установлены корректно

---

## Test Case: TC-CALC-LEGION-005
**Title:** LegionJewelData.__post_init__() default modified_nodes

**Category:** Positive

**Description:** Проверка __post_init__ для установки дефолтных modified_nodes

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать LegionJewelData с modified_nodes=None
2. Проверить результат

**Expected Result:**
- data.modified_nodes == {}
- Дефолтное значение установлено

---

## Test Case: TC-CALC-LEGION-006
**Title:** LegionJewelHelper.__init__() no directory

**Category:** Positive

**Description:** Проверка инициализации LegionJewelHelper без директории

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `LegionJewelHelper()`
2. Проверить значения атрибутов

**Expected Result:**
- helper.data_directory is None
- helper._lut_cache == {}

---

## Test Case: TC-CALC-LEGION-007
**Title:** LegionJewelHelper.__init__() with directory

**Category:** Positive

**Description:** Проверка инициализации LegionJewelHelper с директорией

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `LegionJewelHelper(data_directory="/test/path")`
2. Проверить значения атрибутов

**Expected Result:**
- helper.data_directory == "/test/path"
- helper._lut_cache == {}

---

## Test Case: TC-CALC-LEGION-008
**Title:** LegionJewelHelper._find_jewel_file() no directory

**Category:** Edge Case

**Description:** Проверка метода _find_jewel_file() без установленной директории

**Preconditions:**
- Нет

**Test Steps:**
1. Создать LegionJewelHelper без директории
2. Вызвать `_find_jewel_file("GloriousVanity")`
3. Проверить результат

**Expected Result:**
- result is None
- Отсутствие директории обработано корректно

---

## Test Case: TC-CALC-LEGION-009
**Title:** LegionJewelHelper._find_jewel_file() file not found

**Category:** Negative

**Description:** Проверка метода _find_jewel_file() для несуществующего файла

**Preconditions:**
- Временная директория создана

**Test Steps:**
1. Создать LegionJewelHelper с временной директорией
2. Вызвать _find_jewel_file() для несуществующего файла
3. Проверить результат

**Expected Result:**
- result is None
- Несуществующий файл обработан корректно

---

## Test Case: TC-CALC-LEGION-010
**Title:** LegionJewelHelper._find_jewel_file() .bin file

**Category:** Positive

**Description:** Проверка метода _find_jewel_file() для поиска .bin файла

**Preconditions:**
- .bin файл создан в TimelessJewelData директории

**Test Steps:**
1. Создать .bin файл в TimelessJewelData
2. Вызвать _find_jewel_file()
3. Проверить результат

**Expected Result:**
- result is not None
- result.endswith("GloriousVanity.bin")
- .bin файл найден

---

## Test Case: TC-CALC-LEGION-011
**Title:** LegionJewelHelper._find_jewel_file() .zip file

**Category:** Positive

**Description:** Проверка метода _find_jewel_file() для поиска .zip файла

**Preconditions:**
- .zip файл создан в TimelessJewelData директории

**Test Steps:**
1. Создать .zip файл в TimelessJewelData
2. Вызвать _find_jewel_file()
3. Проверить результат

**Expected Result:**
- result is not None
- result.endswith("GloriousVanity.zip")
- .zip файл найден

---

## Test Case: TC-CALC-LEGION-012
**Title:** LegionJewelHelper.load_timeless_jewel() invalid type

**Category:** Negative

**Description:** Проверка метода load_timeless_jewel() для невалидного типа

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать load_timeless_jewel() с невалидным типом (например, 99 или 0)
2. Проверить возвращаемое значение

**Expected Result:**
- Метод возвращает False
- Исключение не выбрасывается
- Никакие другие значения не возвращаются (не None, не True)

---

## Test Case: TC-CALC-LEGION-013
**Title:** LegionJewelHelper.load_timeless_jewel() Glorious Vanity no node

**Category:** Positive

**Description:** Проверка метода load_timeless_jewel() для Glorious Vanity без node_id

**Preconditions:**
- Валидный файл данных для "Glorious Vanity" должен существовать в директории данных, либо тестовый харнес должен инициализировать LegionJewelHelper с валидной директорией данных, содержащей файл `GloriousVanity.bin` или `GloriousVanity.zip` в поддиректории `TimelessJewelData`
- Альтернативно: доступен mock/test fixture с данными Glorious Vanity (например, `glorious_vanity_fixture` или временная директория с созданным файлом `TimelessJewelData/GloriousVanity.bin`)
- Ожидаемый путь к файлу: `{data_directory}/TimelessJewelData/GloriousVanity.bin` или `{data_directory}/TimelessJewelData/GloriousVanity.zip`
- LegionJewelHelper должен быть инициализирован перед вызовом load_timeless_jewel() (либо с указанием data_directory, либо без него для проверки поведения при отсутствии директории)

**Test Steps:**
1. Вызвать load_timeless_jewel() для Glorious Vanity без node_id
2. Проверить результат

**Expected Result:**
- Результат корректен
- Обработка без node_id работает

---

## Test Case: TC-CALC-LEGION-014
**Title:** LegionJewelHelper.load_timeless_jewel() already loaded

**Category:** Positive

**Description:** Проверка метода load_timeless_jewel() для уже загруженного джема

**Preconditions:**
- Джем уже загружен в кэш

**Test Steps:**
1. Загрузить джем в кэш
2. Вызвать load_timeless_jewel() снова
3. Проверить результат

**Expected Result:**
- Кэш использован
- Результат корректен

---

## Test Case: TC-CALC-LEGION-015
**Title:** LegionJewelHelper.load_timeless_jewel() file not found

**Category:** Negative

**Description:** Проверка метода load_timeless_jewel() для несуществующего файла

**Preconditions:**
- Файл не существует

**Test Steps:**
1. Вызвать load_timeless_jewel() для несуществующего файла
2. Проверить обработку ошибки

**Expected Result:**
- Метод возвращает `False` (не выбрасывает исключение)
- Никакие исключения (включая FileNotFoundError, OSError) не просачиваются наружу
- Все ошибки обрабатываются внутри метода и преобразуются в возврат `False`

---

## Test Case: TC-CALC-LEGION-016
**Title:** LegionJewelHelper.load_timeless_jewel() success

**Category:** Positive

**Description:** Проверка метода load_timeless_jewel() для успешной загрузки

**Preconditions:**
- Валидный файл существует

**Test Steps:**
1. Создать валидный файл джема
2. Вызвать load_timeless_jewel()
3. Проверить результат

**Expected Result:**
- Джем загружен успешно
- Кэш обновлен
- Результат корректен

---

## Test Case: TC-CALC-LEGION-017
**Title:** LegionJewelHelper.read_lut() not loaded

**Category:** Edge Case

**Description:** Проверка метода read_lut() для незагруженного джема

**Preconditions:**
- Джем не загружен

**Test Steps:**
1. Вызвать read_lut() для незагруженного джема
2. Проверить результат

**Expected Result:**
- Ошибка обработана корректно
- Выбрасывается исключение или возвращается None

---

## Test Case: TC-CALC-LEGION-018
**Title:** LegionJewelHelper.read_lut() loaded but no data

**Category:** Edge Case

**Description:** Проверка метода read_lut() для загруженного джема без данных

**Preconditions:**
- Джем загружен, но данных нет

**Test Steps:**
1. Загрузить джем без данных
2. Вызвать read_lut()
3. Проверить результат

**Expected Result:**
Returns None if no LUT data is available; no exception is raised and the method completes gracefully

---

## Test Case: TC-CALC-LEGION-019
**Title:** LegionJewelHelper.get_node_modifications() with modified_nodes

**Category:** Positive

**Description:** Проверка метода get_node_modifications() с modified_nodes

**Preconditions:**
- LegionJewelData с modified_nodes

**Test Steps:**
1. Создать LegionJewelData с modified_nodes
2. Вызвать get_node_modifications()
3. Проверить результат

**Expected Result:**
- Модификации узлов возвращены
- Результат корректен
