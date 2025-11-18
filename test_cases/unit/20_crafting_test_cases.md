# Crafting Unit Test Cases

## Module: pobapi.crafting

### Overview
Юнит-тест-кейсы для модуля crafting, который содержит классы для крафта предметов.

---

## Test Case: TC-CRAFTING-001
**Title:** ItemModifier.__init__() with defaults

**Category:** Positive

**Description:** Проверка инициализации ItemModifier с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ItemModifier с минимальными параметрами
2. Проверить значения атрибутов

**Expected Result:**
- mod.name == "of Life"
- mod.stat == "Life"
- mod.min_value == 10.0
- mod.max_value == 20.0
- mod.tags == []

---

## Test Case: TC-CRAFTING-002
**Title:** ItemModifier.__init__() with tags

**Category:** Positive

**Description:** Проверка инициализации ItemModifier с тегами

**Preconditions:**
- Нет

**Test Steps:**
1. Создать ItemModifier с tags=["armour", "belt"]
2. Проверить значение tags

**Expected Result:**
- mod.tags == ["armour", "belt"]

---

## Test Case: TC-CRAFTING-003
**Title:** CraftingModifier.to_modifier() conversion

**Category:** Positive

**Description:** Проверка метода to_modifier() для преобразования CraftingModifier в Modifier

**Preconditions:**
- ItemModifier и CraftingModifier созданы

**Test Steps:**
1. Создать ItemModifier
2. Создать CraftingModifier с roll_value
3. Вызвать crafting_mod.to_modifier(source="test")
4. Проверить результат

**Expected Result:**
- modifier.stat == "Life"
- modifier.value == roll_value
- modifier.mod_type == ModifierType.FLAT
- modifier.source == "test"

---

## Test Case: TC-CRAFTING-004
**Title:** CraftingResult.__init__() with defaults

**Category:** Positive

**Description:** Проверка инициализации CraftingResult с дефолтными значениями

**Preconditions:**
- Нет

**Test Steps:**
1. Создать CraftingResult(success=True)
2. Проверить значения атрибутов

**Expected Result:**
- result.success is True
- result.item_text == ""
- result.modifiers == []
- result.prefix_count == 0
- result.suffix_count == 0
- result.error == ""

---

## Test Case: TC-CRAFTING-005
**Title:** CraftingResult.__init__() with values

**Category:** Positive

**Description:** Проверка инициализации CraftingResult со значениями

**Preconditions:**
- Модификаторы созданы

**Test Steps:**
1. Создать список модификаторов
2. Создать CraftingResult со всеми параметрами
3. Проверить значения

**Expected Result:**
- Все значения установлены корректно
- result.modifiers содержит переданные модификаторы

---

## Test Case: TC-CRAFTING-006
**Title:** ItemCraftingAPI.get_modifiers_by_type() prefix

**Category:** Positive

**Description:** Проверка метода get_modifiers_by_type() для получения префиксов

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_modifiers_by_type("prefix")`
2. Проверить результат

**Expected Result:**
- Результат является непустым списком (len(result) > 0)
- Каждый элемент в результате является экземпляром ItemModifier
- Для каждого модификатора mod в результате:
  - `mod.is_prefix is True` (все модификаторы являются префиксами)
  - `mod.is_suffix is False` (ни один не является суффиксом)
  - `mod.name` является непустой строкой
  - `mod.stat` является непустой строкой
  - `mod.mod_type` является экземпляром ModifierType
  - `mod.tier` является экземпляром ModifierTier
  - `mod.min_value` является числом типа float и >= 0
  - `mod.max_value` является числом типа float и >= mod.min_value
  - `mod.item_level_required` является целым числом >= 1
  - `mod.tags` является списком (может быть пустым)
- Все модификаторы имеют item_level_required <= 100 (дефолтный item_level)
- В результате присутствуют модификаторы для различных статов (например, "Life", "Mana", "EnergyShield", "PhysicalDamage")
- Критерии приемки: все элементы соответствуют типу prefix, нет элементов с is_suffix=True, структура данных корректна

---

## Test Case: TC-CRAFTING-007
**Title:** ItemCraftingAPI.get_modifiers_by_type() suffix

**Category:** Positive

**Description:** Проверка метода get_modifiers_by_type() для получения суффиксов

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_modifiers_by_type("suffix")`
2. Проверить результат

**Expected Result:**
- Результат является непустым списком (len(result) > 0)
- Каждый элемент в результате является экземпляром ItemModifier
- Для каждого модификатора mod в результате:
  - `mod.is_suffix is True` (все модификаторы являются суффиксами)
  - `mod.is_prefix is False` (ни один не является префиксом)
  - `mod.name` является непустой строкой
  - `mod.stat` является непустой строкой
  - `mod.mod_type` является экземпляром ModifierType
  - `mod.tier` является экземпляром ModifierTier
  - `mod.min_value` является числом типа float и >= 0
  - `mod.max_value` является числом типа float и >= mod.min_value
  - `mod.item_level_required` является целым числом >= 1
  - `mod.tags` является списком (может быть пустым)
- Все модификаторы имеют item_level_required <= 100 (дефолтный item_level)
- В результате присутствуют модификаторы для различных статов (например, "FireResistance", "ColdResistance", "LightningResistance", "CritChance")
- Критерии приемки: все элементы соответствуют типу suffix, нет элементов с is_prefix=True, структура данных корректна

---

## Test Case: TC-CRAFTING-008
**Title:** ItemCraftingAPI.get_modifiers_by_type() invalid type

**Category:** Negative

**Description:** Проверка метода get_modifiers_by_type() с невалидным типом

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_modifiers_by_type("invalid")`
2. Использовать `pytest.raises(ValueError)` для перехвата исключения
3. Проверить, что исключение имеет тип ValueError

**Expected Result:**
- Выбрасывается ValueError

---

## Test Case: TC-CRAFTING-009
**Title:** ItemCraftingAPI.get_modifiers_by_type() with item level

**Category:** Positive

**Description:** Проверка метода get_modifiers_by_type() с учетом item level

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_modifiers_by_type("prefix", item_level=80)`
2. Проверить результат

**Expected Result:**
- Возвращаются только модификаторы, доступные для указанного item level

---

## Test Case: TC-CRAFTING-010
**Title:** ItemCraftingAPI.get_modifiers_by_type() with tags

**Category:** Positive

**Description:** Проверка метода get_modifiers_by_type() с фильтрацией по тегам

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_modifiers_by_type("prefix", tags=["armour"])`
2. Проверить результат

**Expected Result:**
- Возвращаются только модификаторы с указанными тегами

---

## Test Case: TC-CRAFTING-011
**Title:** ItemCraftingAPI.get_modifiers_by_stat() with stat name

**Category:** Positive

**Description:** Проверка метода get_modifiers_by_stat() для получения модификаторов по стату

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_modifiers_by_stat("Life")`
2. Проверить результат

**Expected Result:**
- Результат является непустым списком (len(result) > 0)
- Каждый элемент в результате является экземпляром ItemModifier
- Для каждого модификатора mod в результате:
  - `mod.stat == "Life"` (все модификаторы относятся к стату "Life")
  - `mod.name` является непустой строкой
  - `mod.mod_type` является экземпляром ModifierType
  - `mod.tier` является экземпляром ModifierTier
  - `mod.min_value` является числом типа float и >= 0
  - `mod.max_value` является числом типа float и >= mod.min_value
  - `mod.item_level_required` является целым числом >= 1
  - `mod.tags` является списком (может быть пустым)
  - `mod.is_prefix` или `mod.is_suffix` равно True (модификатор должен быть либо префиксом, либо суффиксом)
- Все модификаторы имеют item_level_required <= 100 (дефолтный item_level)
- В результате присутствуют модификаторы с разными tier (например, T1, T2)
- В результате присутствуют модификаторы с is_prefix=True (префиксы для Life)
- Критерии приемки: все элементы имеют stat="Life", нет элементов с другими статами, структура данных корректна, присутствуют как префиксы, так и возможно суффиксы для Life

---

## Test Case: TC-CRAFTING-012
**Title:** ItemCraftingAPI.get_modifiers_by_stat() with tags

**Category:** Positive

**Description:** Проверка метода get_modifiers_by_stat() с фильтрацией по тегам

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_modifiers_by_stat("Life", tags=["belt"])`
2. Проверить результат

**Expected Result:**
- Возвращаются модификаторы с указанными тегами

---

## Test Case: TC-CRAFTING-013
**Title:** ItemCraftingAPI.get_available_prefixes()

**Category:** Positive

**Description:** Проверка метода get_available_prefixes() для получения доступных префиксов

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_available_prefixes()`
2. Проверить результат

**Expected Result:**
- Результат является непустым списком (len(result) > 0)
- Каждый элемент в результате является экземпляром ItemModifier
- Для каждого модификатора mod в результате:
  - `mod.is_prefix is True` (все модификаторы являются префиксами)
  - `mod.is_suffix is False` (ни один не является суффиксом)
  - `mod.name` является непустой строкой
  - `mod.stat` является непустой строкой
  - `mod.mod_type` является экземпляром ModifierType
  - `mod.tier` является экземпляром ModifierTier
  - `mod.min_value` является числом типа float и >= 0
  - `mod.max_value` является числом типа float и >= mod.min_value
  - `mod.item_level_required` является целым числом >= 1
  - `mod.tags` является списком (может быть пустым)
- Все модификаторы имеют item_level_required <= 100 (дефолтный item_level)
- В результате присутствуют модификаторы для различных статов (например, "Life", "Mana", "EnergyShield", "PhysicalDamage", "FireDamage", "AttackSpeed")
- В результате присутствуют модификаторы с разными tier (например, T1, T2)
- Результат идентичен вызову `get_modifiers_by_type("prefix")` (метод является оберткой)
- Критерии приемки: все элементы соответствуют типу prefix, нет элементов с is_suffix=True, структура данных корректна, результат эквивалентен get_modifiers_by_type("prefix")

---

## Test Case: TC-CRAFTING-014
**Title:** ItemCraftingAPI.get_available_suffixes()

**Category:** Positive

**Description:** Проверка метода get_available_suffixes() для получения доступных суффиксов

**Preconditions:**
- ItemCraftingAPI инициализирован

**Test Steps:**
1. Вызвать `api.get_available_suffixes()`
2. Проверить результат

**Expected Result:**
- Результат является непустым списком (len(result) > 0)
- Каждый элемент в результате является экземпляром ItemModifier
- Для каждого модификатора mod в результате:
  - `mod.is_suffix is True` (все модификаторы являются суффиксами)
  - `mod.is_prefix is False` (ни один не является префиксом)
  - `mod.name` является непустой строкой
  - `mod.stat` является непустой строкой
  - `mod.mod_type` является экземпляром ModifierType
  - `mod.tier` является экземпляром ModifierTier
  - `mod.min_value` является числом типа float и >= 0
  - `mod.max_value` является числом типа float и >= mod.min_value
  - `mod.item_level_required` является целым числом >= 1
  - `mod.tags` является списком (может быть пустым)
- Все модификаторы имеют item_level_required <= 100 (дефолтный item_level)
- В результате присутствуют модификаторы для различных статов (например, "FireResistance", "ColdResistance", "LightningResistance", "CritChance", "CritMultiplier", "MovementSpeed", "Strength", "Dexterity", "Intelligence")
- В результате присутствуют модификаторы с разными tier (например, T1)
- Результат идентичен вызову `get_modifiers_by_type("suffix")` (метод является оберткой)
- Критерии приемки: все элементы соответствуют типу suffix, нет элементов с is_prefix=True, структура данных корректна, результат эквивалентен get_modifiers_by_type("suffix")

---

## Test Case: TC-CRAFTING-015
**Title:** ItemCraftingAPI.craft_item() success

**Category:** Positive

**Description:** Проверка метода craft_item() для успешного крафта

**Preconditions:**
- Валидный базовый предмет создан
- Достаточно модификаторов доступно

**Test Steps:**
1. Создать базовый предмет: "Iron Sword", item level 10
2. Создать список модификаторов:
   - Prefixes: ["+5 Damage prefix A", "+2 Attack Speed prefix B"] (2 префикса)
   - Suffixes: ["+10 Life suffix C", "+5 Mana suffix D"] (2 суффикса)
   - Максимальные лимиты: max_prefixes=3, max_suffixes=3
3. Вызвать `api.craft_item(base_item, modifiers)`
4. Проверить результат

**Expected Result:**
- result.success is True
- result.modifiers содержит примененные модификаторы (2 префикса и 2 суффикса)
- result.prefix_count == 2 (в пределах лимита max_prefixes=3)
- result.suffix_count == 2 (в пределах лимита max_suffixes=3)
- result.item_text сгенерирован и содержит все примененные модификаторы
- Все модификаторы имеют item_level_required <= 10 (уровень базового предмета)

---

## Test Case: TC-CRAFTING-016
**Title:** ItemCraftingAPI.craft_item() too many prefixes

**Category:** Negative

**Description:** Проверка метода craft_item() при слишком большом количестве префиксов

**Preconditions:**
- Базовый предмет создан
- Слишком много префиксов в модификаторах

**Test Steps:**
1. Создать базовый предмет: "Iron Sword", item level 10
2. Создать список модификаторов с 3 префиксами:
   - Prefixes: ["+5 Damage prefix A", "+2 Attack Speed prefix B", "+8 Life prefix C"] (3 префикса)
   - Максимальный лимит: max_prefixes=2 (разрешено только 2 префикса)
3. Вызвать `api.craft_item(base_item, modifiers)`
4. Проверить результат

**Expected Result:**
- result.success is False или выбрасывается исключение
- Ошибка указывает на слишком много префиксов
- Сообщение об ошибке содержит информацию о превышении лимита: "Too many prefixes: 3 provided, maximum allowed is 2"
- result.error содержит описание проблемы с префиксами

---

## Test Case: TC-CRAFTING-017
**Title:** ItemCraftingAPI.craft_item() too many suffixes

**Category:** Negative

**Description:** Проверка метода craft_item() при слишком большом количестве суффиксов

**Preconditions:**
- Базовый предмет создан
- Слишком много суффиксов в модификаторах

**Test Steps:**
1. Создать базовый предмет: "Iron Sword", item level 10
2. Создать список модификаторов с 4 суффиксами:
   - Suffixes: ["+10 Life suffix A", "+5 Mana suffix B", "+8 Fire Resistance suffix C", "+6 Cold Resistance suffix D"] (4 суффикса)
   - Максимальный лимит: max_suffixes=3 (разрешено только 3 суффикса)
3. Вызвать `api.craft_item(base_item, modifiers)`
4. Проверить результат

**Expected Result:**
- result.success is False или выбрасывается исключение
- Ошибка указывает на слишком много суффиксов
- Сообщение об ошибке содержит информацию о превышении лимита: "Too many suffixes: 4 provided, maximum allowed is 3"
- result.error содержит описание проблемы с суффиксами

---

## Test Case: TC-CRAFTING-018
**Title:** ItemCraftingAPI.craft_item() insufficient item level

**Category:** Negative

**Description:** Проверка метода craft_item() при недостаточном item level

**Preconditions:**
- Базовый предмет с низким item level
- Модификаторы требуют более высокий level

**Test Steps:**
1. Создать базовый предмет: "Iron Sword", item level 1
2. Создать список модификаторов, требующих минимальный item level 5:
   - Модификатор A: item_level_required=5 (требует уровень 5)
   - Модификатор B: item_level_required=5 (требует уровень 5)
   - Базовый предмет имеет уровень 1, что ниже минимального требования (5)
3. Вызвать `api.craft_item(base_item, modifiers)`
4. Проверить результат

**Expected Result:**
- result.success is False или выбрасывается исключение
- Ошибка указывает на недостаточный item level
- Сообщение об ошибке содержит информацию о несоответствии уровня: "Item level 1 is too low for modifier requiring level 5" или "Insufficient item level: 1 < 5 (minimum required)"
- result.error содержит описание проблемы с item level

---

## Test Case: TC-CRAFTING-019
**Title:** ItemCraftingAPI.craft_item() with implicits

**Category:** Positive

**Description:** Проверка метода craft_item() с предметом, имеющим implicits

**Preconditions:**
- Базовый предмет с implicits создан

**Test Steps:**
1. Создать базовый предмет с implicits
2. Вызвать `api.craft_item()`
3. Проверить результат

**Expected Result:**
- result.success is True
- Implicits сохранены в item_text

---

## Test Case: TC-CRAFTING-020
**Title:** ItemCraftingAPI.generate_item_text() with modifier types

**Category:** Positive

**Description:** Проверка метода generate_item_text() с различными типами модификаторов

**Preconditions:**
- Модификаторы разных типов созданы

**Test Steps:**
1. Создать модификаторы разных типов (prefix и suffix)
2. Вызвать `api.generate_item_text(base_item_type, prefixes=prefixes, suffixes=suffixes)`
3. Проверить результат

**Expected Result:**

**Format Structure:**
The generated `item_text` must follow this exact structure and ordering:
1. **Item name** (first line): Base item type name
2. **Rarity** (second line): `"Rarity: RARE"`
3. **Implicit modifiers** (if any): One line per implicit modifier, appearing **BEFORE** all explicit modifiers
4. **Prefix modifiers** (if any): All prefix modifiers, one per line, appearing **AFTER** implicits
5. **Suffix modifiers** (if any): All suffix modifiers, one per line, appearing **AFTER** prefixes

**Canonical Ordering:**
- Implicits → Prefixes → Suffixes (implicits always come first, then prefixes, then suffixes)

**Formatting Rules:**
- Each entry must be on a separate line (newline `\n` delimiter)
- **Implicit modifiers**: Added as-is from the `implicit_mods` parameter (no formatting transformation applied). Each implicit string is appended directly, one per line, in the order provided.
- **Explicit modifiers (prefixes/suffixes)**: Formatted according to modifier type:
  - Flat modifiers: `+{value} to maximum {stat}` for Life/Mana/EnergyShield, or `+{value} to {stat}` for others
  - Percentage modifiers: `{value}% {type} {stat}` where type is one of: `increased`, `more`, `reduced`, `less`
- Values are displayed as integers (no decimal places)
- Prefixes must appear before suffixes in the output

**Implicit-Explicit Modifier Interaction:**
- Implicits and explicit modifiers are shown **separately** (not merged or deduplicated)
- If an implicit and explicit modifier affect the same stat, both appear as separate lines
- No deduplication or merging logic is applied between implicits and explicit modifiers
- Implicits maintain their original string format and are not transformed to match explicit modifier formatting

**Modifier Format Examples:**
- FLAT Life: `+50 to maximum Life`
- FLAT Physical Damage: `+10 to Physical Damage`
- INCREASED: `25% increased maximum Life`
- MORE: `15% more Fire Damage`
- REDUCED: `20% reduced Mana Cost`
- LESS: `10% less Damage`

**Concrete Example Output 1:**
```
Leather Belt
Rarity: RARE
+45 to maximum Life
+30 to maximum Mana
12% increased maximum Energy Shield
8% increased Fire Resistance
5% increased Cold Resistance
```

**Concrete Example Output 2:**
```
Steel Ring
Rarity: RARE
+25 to Physical Damage
15% increased Attack Speed
+50 to maximum Life
10% more Fire Damage
20% reduced Mana Cost
```

**Concrete Example Output 3 (with implicits + prefixes + suffixes):**
```
Leather Belt
Rarity: RARE
+20 to maximum Life
+15 to maximum Mana
+45 to maximum Life
12% increased maximum Energy Shield
8% increased Fire Resistance
5% increased Cold Resistance
```

**Example 3 Explanation:**
- Lines 1-2: Item name and rarity
- Lines 3-4: **Implicit modifiers** (appear first, as-is from `implicit_mods`)
- Lines 5-7: **Prefix modifiers** (formatted explicit modifiers)
- Lines 8-9: **Suffix modifiers** (formatted explicit modifiers)
- Note: Both implicit `+20 to maximum Life` (line 3) and explicit `+45 to maximum Life` (line 5) appear separately, demonstrating no deduplication

**Assertions:**
- `item_text` starts with base_item_type
- `item_text` contains `"Rarity: RARE"` on second line
- **Implicit modifiers** (if provided) appear immediately after "Rarity: RARE" and before all explicit modifiers
- **Implicit modifiers** are added as-is without formatting transformation
- All prefix modifiers appear in correct format after implicits and before suffixes
- All suffix modifiers appear in correct format after prefixes
- Each explicit modifier line matches expected format pattern for its type
- Values are displayed as integers
- Implicits and explicit modifiers are shown separately (no merging or deduplication)

---

## Test Case: TC-CRAFTING-021
**Title:** ItemCraftingAPI.generate_item_text() with implicits

**Category:** Positive

**Description:** Проверка метода generate_item_text() с implicits

**Preconditions:**
- Модификаторы и implicits созданы

**Test Steps:**
1. Создать модификаторы и implicits
2. Вызвать `api.generate_item_text(modifiers, implicits=implicits)`
3. Проверить результат

**Expected Result:**
- item_text содержит implicits
- Результат корректен

---

## Test Case: TC-CRAFTING-022
**Title:** ItemCraftingAPI.generate_item_text() empty

**Category:** Edge Case

**Description:** Проверка метода generate_item_text() с пустым списком модификаторов

**Preconditions:**
- Нет

**Test Steps:**
1. Вызвать `api.generate_item_text(base_item_type="Leather Belt", prefixes=[], suffixes=[], implicit_mods=[])`
2. Проверить результат

**Expected Result:**
- item_text равен точно: `"Leather Belt\nRarity: RARE"`
- Формат: первая строка - base_item_type, вторая строка - "Rarity: RARE", без дополнительных строк

---

## Test Case: TC-CRAFTING-023
**Title:** ItemCraftingAPI.calculate_modifier_value() perfect roll

**Category:** Positive

**Description:** Проверка метода calculate_modifier_value() для perfect roll

**Preconditions:**
- ItemModifier создан

**Test Steps:**
1. Создать ItemModifier с min_value и max_value
2. Вызвать `api.calculate_modifier_value(modifier, roll=1.0)`
3. Проверить результат

**Expected Result:**
- value == max_value (perfect roll)

---

## Test Case: TC-CRAFTING-024
**Title:** ItemCraftingAPI.calculate_modifier_value() minimum roll

**Category:** Positive

**Description:** Проверка метода calculate_modifier_value() для minimum roll

**Preconditions:**
- ItemModifier создан

**Test Steps:**
1. Создать ItemModifier с min_value и max_value
2. Вызвать `api.calculate_modifier_value(modifier, roll=0.0)`
3. Проверить результат

**Expected Result:**
- value == min_value (minimum roll)

---

## Test Case: TC-CRAFTING-025
**Title:** ItemCraftingAPI.calculate_modifier_value() mid roll

**Category:** Positive

**Description:** Проверка метода calculate_modifier_value() для mid roll

**Preconditions:**
- ItemModifier создан

**Test Steps:**
1. Создать ItemModifier с min_value и max_value
2. Вызвать `api.calculate_modifier_value(modifier, roll=0.5)`
3. Проверить результат

**Expected Result:**
- value = min_value + (max_value - min_value) * roll
- value находится между min_value и max_value
- Значение пропорционально roll
- Example: min_value=10, max_value=20, roll=0.5 → value=15

---

## Test Case: TC-CRAFTING-026
**Title:** ItemCraftingAPI.calculate_modifier_value() clamped

**Category:** Edge Case

**Description:** Проверка метода calculate_modifier_value() для clamped значений

**Preconditions:**
- ItemModifier создан

**Test Steps:**
1. Создать ItemModifier
2. Вызвать `api.calculate_modifier_value(modifier, roll=2.0)` (больше 1.0)
3. Проверить результат

**Expected Result:**
- value == max_value (clamped)
- Значение не превышает max_value
