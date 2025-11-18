# Calculator Skill Modifier Parser Unit Test Cases

## Module: pobapi.calculator.skill_modifier_parser

### Overview
Юнит-тест-кейсы для модуля SkillModifierParser, который парсит модификаторы из скиллов.

---

## Test Case: TC-CALC-SKILL-PARSER-001
**Title:** SkillModifierParser.parse_support_gem() with valid gem name

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() с валидным именем гема

**Preconditions:**
- Валидное имя support гема предоставлено

**Test Steps:**
1. Вызвать `SkillModifierParser.parse_support_gem("Increased Critical Damage Support", 20)`
2. Проверить возвращаемые модификаторы

**Expected Result:**
- Возвращается список модификаторов
- Модификаторы корректно распарсены

---

## Test Case: TC-CALC-SKILL-PARSER-002
**Title:** SkillModifierParser.parse_support_gem() with increased mod type

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() с increased типом модификатора

**Preconditions:**
- Support гем содержит increased модификаторы

**Test Steps:**
1. Вызвать `SkillModifierParser.parse_support_gem("Increased Critical Damage Support", 20)`
2. Проверить тип модификатора

**Expected Result:**
- Модификатор имеет mod_type == ModifierType.INCREASED
- Для crit статов используется INCREASED тип

---

## Test Case: TC-CALC-SKILL-PARSER-003
**Title:** SkillModifierParser.parse_support_gem() with reduced in stat name

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() с "reduced" в названии стата (покрывает строку 220)

**Preconditions:**
- Support гем содержит стат с "reduced" в названии

**Test Steps:**
1. Вызвать `SkillModifierParser.parse_support_gem()` с гемом, содержащим "reduced" в стате
2. Проверить парсинг

**Expected Result:**
- "reduced" в названии стата обработано корректно
- Модификатор распарсен правильно

---

## Test Case: TC-CALC-SKILL-PARSER-004
**Title:** SkillModifierParser.parse_support_gem() determines mod type from stat name

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() для определения типа модификатора из названия стата

**Preconditions:**
- Support гем содержит статы с increased/reduced в названии

**Test Steps:**
1. Вызвать `parse_support_gem()` с гемом, содержащим "increasedTestStat"
2. Вызвать `parse_support_gem()` с гемом, содержащим "reducedTestStat"
3. Проверить типы модификаторов

**Expected Result:**
- "increasedTestStat" → ModifierType.INCREASED
- "reducedTestStat" → ModifierType.REDUCED

---

## Test Case: TC-CALC-SKILL-PARSER-005
**Title:** SkillModifierParser.parse_support_gem() with gem level

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() с учетом уровня гема

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `parse_support_gem("Added Fire Damage Support", 1)` и проверить значение модификатора `moreFireDamage`
2. Вызвать `parse_support_gem("Added Fire Damage Support", 20)` и проверить значение модификатора `moreFireDamage`
3. Вызвать `parse_support_gem("Increased Critical Damage Support", 1)` и проверить значение модификатора `critMultiplier`
4. Вызвать `parse_support_gem("Increased Critical Damage Support", 20)` и проверить значение модификатора `critMultiplier`

**Expected Result:**
- Для "Added Fire Damage Support" level 1: `moreFireDamage = 39.0` (tolerance ±0.1)
- Для "Added Fire Damage Support" level 20: `moreFireDamage = 67.5` (tolerance ±0.1)
- Для "Increased Critical Damage Support" level 1: `critMultiplier = 30.0` (tolerance ±0.1)
- Для "Increased Critical Damage Support" level 20: `critMultiplier = 58.5` (tolerance ±0.1)
- Значения корректно масштабируются по формуле: `base_value + (gem_level - 1) * multiplier`

---

## Test Case: TC-CALC-SKILL-PARSER-006
**Title:** SkillModifierParser.parse_support_gem() with gem quality

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() с учетом качества гема

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `parse_support_gem("Added Fire Damage Support", 20, gem_quality=0)` и проверить значение модификатора `moreFireDamage`
2. Вызвать `parse_support_gem("Added Fire Damage Support", 20, gem_quality=20)` и проверить значение модификатора `moreFireDamage`
3. Вызвать `parse_support_gem("Increased Critical Damage Support", 20, gem_quality=0)` и проверить значение модификатора `critMultiplier`
4. Вызвать `parse_support_gem("Increased Critical Damage Support", 20, gem_quality=20)` и проверить значение модификатора `critMultiplier`

**Expected Result:**
- Для "Added Fire Damage Support" level 20 quality 0: `moreFireDamage = 67.5` (tolerance ±0.1)
- Для "Added Fire Damage Support" level 20 quality 20: `moreFireDamage = 67.5` (tolerance ±0.1) - качество пока не реализовано, значение должно оставаться базовым
- Для "Increased Critical Damage Support" level 20 quality 0: `critMultiplier = 58.5` (tolerance ±0.1)
- Для "Increased Critical Damage Support" level 20 quality 20: `critMultiplier = 58.5` (tolerance ±0.1) - качество пока не реализовано, значение должно оставаться базовым
- Метод не должен выбрасывать исключение при передаче качества гема

---

## Test Case: TC-CALC-SKILL-PARSER-007
**Title:** SkillModifierParser.parse_support_gem() with supported skill

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() с указанием поддерживаемого скилла. Тест проверяет фильтрацию, переименование и масштабирование модификаторов в зависимости от параметра supported_skill.

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `parse_support_gem()` без параметра supported_skill (None)
2. Вызвать `parse_support_gem()` с параметром supported_skill="Fireball"
3. Вызвать `parse_support_gem()` с параметром supported_skill="Fireball" для разных уровней гема (1, 10, 20)
4. Вызвать `parse_support_gem()` с параметром supported_skill=None для разных уровней гема (1, 10, 20)
5. Вызвать `parse_support_gem()` с неподдерживаемым скиллом (например, supported_skill="InvalidSkill")

**Expected Result:**

**1. Модификаторы, присутствующие только при указанном supported_skill:**
- Когда `supported_skill` указан, должны появляться модификаторы с префиксом "supported_" для следующих ключей:
  - `supported_moreFireDamage` (из "Added Fire Damage Support")
  - `supported_moreAreaOfEffect` (из "Increased Area of Effect Support")
  - `supported_moreElementalDamage` (из "Elemental Focus Support")
  - `supported_moreSpellDamage` (из "Controlled Destruction Support")
  - `supported_morePhysicalDamage` (из "Melee Physical Damage Support")
  - `supported_moreAttackSpeed` (из "Faster Attacks Support")
  - `supported_moreCastSpeed` (из "Faster Casting Support")
- Когда `supported_skill` равен None, эти модификаторы с префиксом "supported_" НЕ должны появляться
- Базовые модификаторы (без префикса "supported_") должны присутствовать в обоих случаях

**2. Правила переименования:**
- Модификаторы с ключами, содержащими "more", "less", "increased", "reduced", должны быть переименованы с префиксом "supported_" когда `supported_skill` указан
- Формула переименования: `supported_{original_stat_name}`
- Примеры:
  - `moreFireDamage` → `supported_moreFireDamage` (когда supported_skill указан)
  - `moreAreaOfEffect` → `supported_moreAreaOfEffect` (когда supported_skill указан)
  - `critChance` → `supported_critChance` (когда supported_skill указан)
- Флаговые модификаторы (boolean flags) НЕ переименовываются, но должны присутствовать только когда supported_skill указан:
  - `cannotIgnite`, `cannotFreeze`, `cannotShock` (из "Elemental Focus Support")

**3. Формула масштабирования по уровню гема:**
- Значения модификаторов масштабируются по формуле: `base_value + (gem_level - 1) * scaling_factor`
- Для "Added Fire Damage Support" (moreFireDamage):
  - Уровень 1: `39.0 + (1 - 1) * 1.5 = 39.0`
  - Уровень 10: `39.0 + (10 - 1) * 1.5 = 52.5`
  - Уровень 20: `39.0 + (20 - 1) * 1.5 = 67.5`
- Для "Increased Area of Effect Support" (moreAreaOfEffect):
  - Уровень 1: `49.0 + (1 - 1) * 1.5 = 49.0`
  - Уровень 10: `49.0 + (10 - 1) * 1.5 = 62.5`
  - Уровень 20: `49.0 + (20 - 1) * 1.5 = 77.5`
- Для "Increased Critical Strikes Support" (critChance):
  - Уровень 1: `100.0 + (1 - 1) * 5.0 = 100.0`
  - Уровень 10: `100.0 + (10 - 1) * 5.0 = 145.0`
  - Уровень 20: `100.0 + (20 - 1) * 5.0 = 195.0`
- Масштабирование применяется одинаково независимо от наличия `supported_skill`, но переименованные модификаторы должны иметь те же значения

**4. Граничные случаи:**
- Когда `supported_skill=None`: все модификаторы возвращаются без префикса "supported_", значения масштабируются по уровню гема
- Когда `supported_skill` указан (например, "Fireball"): модификаторы переименовываются с префиксом "supported_", значения масштабируются по уровню гема
- Когда `supported_skill` указан как неподдерживаемый скилл (например, "InvalidSkill"): поведение должно быть идентично случаю с валидным supported_skill (переименование применяется, фильтрация по типу скилла не выполняется в текущей реализации)
- Когда `supported_skill=""` (пустая строка): должно обрабатываться как None, модификаторы без префикса "supported_"

**5. Конкретные проверки для "Added Fire Damage Support" уровня 20:**
- Без supported_skill: должен присутствовать модификатор `moreFireDamage` со значением 67.5, тип ModifierType.MORE
- С supported_skill="Fireball": должен присутствовать модификатор `supported_moreFireDamage` со значением 67.5, тип ModifierType.MORE
- Оба случая должны также содержать модификатор `physicalToFire` со значением 50.0 (без переименования, так как это не модификатор типа more/less/increased/reduced)

---

## Test Case: TC-CALC-SKILL-PARSER-008
**Title:** SkillModifierParser.parse_support_gem() with unknown gem

**Category:** Edge Case

**Description:** Проверка статического метода parse_support_gem() с неизвестным гемом

**Preconditions:**
- Имя гема отсутствует в support_effects

**Test Steps:**
1. Вызвать `parse_support_gem("Unknown Gem", 20)`
2. Проверить результат

**Expected Result:**
- Возвращается пустой список модификаторов
- Исключение не выбрасывается

---

## Test Case: TC-CALC-SKILL-PARSER-009
**Title:** SkillModifierParser.parse_support_gem() with boolean effects

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() с булевыми эффектами

**Preconditions:**
- Support гем содержит булевые эффекты

**Test Steps:**
1. Вызвать `parse_support_gem()` с гемом, содержащим булевые эффекты
2. Проверить модификаторы

**Expected Result:**
- Булевые эффекты преобразованы в FLAG модификаторы
- Значения корректны (1.0 для True, 0.0 для False)

---

## Test Case: TC-CALC-SKILL-PARSER-010
**Title:** SkillModifierParser.parse_support_gem() with numeric effects

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() с числовыми эффектами

**Preconditions:**
- Support гем содержит числовые эффекты

**Test Steps:**
1. Вызвать `parse_support_gem()` с гемом, содержащим числовые эффекты
2. Проверить модификаторы

**Expected Result:**
- Числовые эффекты преобразованы в модификаторы
- Тип модификатора определен из названия стата

---

## Test Case: TC-CALC-SKILL-PARSER-011
**Title:** SkillModifierParser.parse_support_gem() handles reduced mod type correctly

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() для корректной обработки reduced типа модификатора

**Preconditions:**
- Support гем содержит reduced модификаторы

**Test Steps:**
1. Вызвать `parse_support_gem()` с гемом, содержащим reduced модификаторы
2. Проверить тип модификатора

**Expected Result:**
- Reduced модификаторы имеют ModifierType.REDUCED
- Парсинг корректен

---

## Test Case: TC-CALC-SKILL-PARSER-012
**Title:** SkillModifierParser.parse_support_gem() with zero level

**Category:** Edge Case

**Description:** Проверка статического метода parse_support_gem() с нулевым уровнем

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `parse_support_gem("Added Fire Damage Support", 0)` и проверить значение модификатора `moreFireDamage`
2. Вызвать `parse_support_gem("Increased Critical Damage Support", 0)` и проверить значение модификатора `critMultiplier`
3. Вызвать `parse_support_gem("Increased Area of Effect Support", 0)` и проверить значение модификатора `moreAreaOfEffect`

**Expected Result:**
- Для "Added Fire Damage Support" level 0: `moreFireDamage = 37.5` (tolerance ±0.1) - формула: 39.0 + (0-1)*1.5 = 37.5
- Для "Increased Critical Damage Support" level 0: `critMultiplier = 28.5` (tolerance ±0.1) - формула: 30.0 + (0-1)*1.5 = 28.5
- Для "Increased Area of Effect Support" level 0: `moreAreaOfEffect = 47.5` (tolerance ±0.1) - формула: 49.0 + (0-1)*1.5 = 47.5
- Метод не должен выбрасывать исключение при уровне 0
- Значения модификаторов рассчитываются корректно по формуле даже для нулевого уровня

---

## Test Case: TC-CALC-SKILL-PARSER-013
**Title:** SkillModifierParser.parse_support_gem() with maximum level

**Category:** Edge Case

**Description:** Проверка статического метода parse_support_gem() с максимальным уровнем

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `parse_support_gem("Added Fire Damage Support", 30)` и проверить значение модификатора `moreFireDamage`
2. Вызвать `parse_support_gem("Increased Critical Damage Support", 30)` и проверить значение модификатора `critMultiplier`
3. Вызвать `parse_support_gem("Spell Echo Support", 30)` и проверить значение модификатора `moreCastSpeed`

**Expected Result:**
- Для "Added Fire Damage Support" level 30: `moreFireDamage = 82.5` (tolerance ±0.1) - формула: 39.0 + (30-1)*1.5 = 82.5
- Для "Increased Critical Damage Support" level 30: `critMultiplier = 73.5` (tolerance ±0.1) - формула: 30.0 + (30-1)*1.5 = 73.5
- Для "Spell Echo Support" level 30: `moreCastSpeed = 128.0` (tolerance ±0.1) - формула: 70.0 + (30-1)*2.0 = 128.0
- Метод не должен выбрасывать исключение при уровне 30
- Значения модификаторов максимальны и корректно рассчитываются по формуле

---

## Test Case: TC-CALC-SKILL-PARSER-014
**Title:** SkillModifierParser.parse_support_gem() returns list of Modifier objects

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() для возврата списка объектов Modifier

**Preconditions:**
- Валидный support гем предоставлен

**Test Steps:**
1. Вызвать `parse_support_gem()`
2. Проверить тип возвращаемых объектов

**Expected Result:**
- Возвращается список
- Все элементы являются экземплярами Modifier
- Каждый модификатор имеет stat, value, mod_type, source

---

## Test Case: TC-CALC-SKILL-PARSER-015
**Title:** SkillModifierParser.parse_support_gem() source attribute format

**Category:** Positive

**Description:** Проверка статического метода parse_support_gem() для формата атрибута source

**Preconditions:**
- Валидный support гем предоставлен

**Test Steps:**
1. Вызвать `parse_support_gem("Test Gem", 20)`
2. Проверить формат source

**Expected Result:**
- source имеет формат "support:gem_name"
- Формат корректен
