# Calculator Item Modifier Parser Unit Test Cases

## Module: pobapi.calculator.item_modifier_parser

### Overview
Unit test cases for the calculator.item_modifier_parser module, which is responsible for parsing item modifiers.

### Stat Name Normalization Rules
The parser normalizes stat names from item text to internal stat names using the following rules:
- Spaces are removed and words are capitalized (e.g., "Mana Cost" → "ManaCost", "Attack Speed" → "AttackSpeed")
- Common mappings are applied (e.g., "maximum Life" → "Life", "maximum Mana" → "Mana")
- Default normalization: lowercase input, then capitalize each word and join without spaces
- All stat assertions in expected results use normalized stat names

---

## Test Case: TC-CALC-ITEM-PARSER-001
**Title:** ItemModifierParser.parse_line() empty line

**Category:** Edge Case

**Description:** Test parse_line() method with an empty string

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("")`
2. Verify the result

**Expected Result:**
- `modifiers == []`
- Empty string is handled correctly

---

## Test Case: TC-CALC-ITEM-PARSER-002
**Title:** ItemModifierParser.parse_line() whitespace-only line

**Category:** Edge Case

**Description:** Test parse_line() method with a string containing only whitespace

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("   \n\t  ")`
2. Verify the result

**Expected Result:**
- `modifiers == []`
- Whitespace is handled correctly

---

## Test Case: TC-CALC-ITEM-PARSER-003
**Title:** ItemModifierParser.parse_line() basic flat pattern

**Category:** Positive

**Description:** Test parse_line() method for basic flat pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("+10 to Strength")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "Strength"`
- `modifiers[0].value == 10.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-004
**Title:** ItemModifierParser.parse_line() basic increased pattern

**Category:** Positive

**Description:** Test parse_line() method for basic increased pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("50% increased Damage")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "Damage"`
- `modifiers[0].value == 50.0`
- `modifiers[0].mod_type == ModifierType.INCREASED`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-005
**Title:** ItemModifierParser.parse_line() basic more pattern

**Category:** Positive

**Description:** Test parse_line() method for basic more pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("30% more Damage")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "Damage"`
- `modifiers[0].value == 30.0`
- `modifiers[0].mod_type == ModifierType.MORE`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-006
**Title:** ItemModifierParser.parse_line() basic reduced pattern

**Category:** Positive

**Description:** Test parse_line() method for basic reduced pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("20% reduced Mana Cost")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "ManaCost"` (normalized: "Mana Cost" → "ManaCost")
- `modifiers[0].value == -20.0`
- `modifiers[0].mod_type == ModifierType.REDUCED`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-007
**Title:** ItemModifierParser.parse_line() basic less pattern

**Category:** Positive

**Description:** Test parse_line() method for basic less pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("10% less Damage")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "Damage"`
- `modifiers[0].value == -10.0`
- `modifiers[0].mod_type == ModifierType.LESS`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-008
**Title:** ItemModifierParser.parse_line() with custom source

**Category:** Positive

**Description:** Test parse_line() method with custom source parameter

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("+10 to Strength", source="test_item")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "Strength"`
- `modifiers[0].value == 10.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].source == "test_item"`

---

## Test Case: TC-CALC-ITEM-PARSER-009
**Title:** ItemModifierParser.parse_line() conditional patterns

**Category:** Positive

**Description:** Test parse_line() method for conditional modifier patterns

**Preconditions:**
- None

**Test Steps:**
1. For each conditional pattern in the table below, call `ItemModifierParser.parse_line()` with the specified input string
2. Verify that the result matches the expected modifier structure

**Expected Result:**
All conditional patterns should be recognized and processed correctly. Each example should create a modifier with the correct structure.

### Conditional Pattern Test Cases:

| Condition Type | Input String | Expected Modifier |
|----------------|--------------|-------------------|
| **Recently Used Skill** | `"10% increased Damage if you've used a skill recently"` | `Modifier(stat="Damage", value=10.0, mod_type=ModifierType.INCREASED, conditions={"recently": "used_skill_recently"}, source="item")` |
| **On Kill** | `"15% increased Damage on kill"` | `Modifier(stat="Damage", value=15.0, mod_type=ModifierType.INCREASED, conditions={"on": "kill"}, source="item")` |
| **On Hit** | `"20% increased Damage on hit"` | `Modifier(stat="Damage", value=20.0, mod_type=ModifierType.INCREASED, conditions={"on": "hit"}, source="item")` |
| **On Crit** | `"25% increased Damage on crit"` | `Modifier(stat="Damage", value=25.0, mod_type=ModifierType.INCREASED, conditions={"on": "crit"}, source="item")` |
| **On Block** | `"30% increased Damage on block"` | `Modifier(stat="Damage", value=30.0, mod_type=ModifierType.INCREASED, conditions={"on": "block"}, source="item")` |
| **When Hit** | `"35% increased Damage when hit"` | `Modifier(stat="Damage", value=35.0, mod_type=ModifierType.INCREASED, conditions={"when": "hit"}, source="item")` |

---

## Test Case: TC-CALC-ITEM-PARSER-010
**Title:** ItemModifierParser.parse_line() adds damage pattern

**Category:** Positive

**Description:** Test parse_line() method for "Adds X to Y Z Damage" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("Adds 10 to 20 Fire Damage")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "AddedFireDamage"` (normalized: "Fire Damage" → "AddedFireDamage" with "Added" prefix)
- `modifiers[0].value == 15.0` (average of min: 10.0 and max: 20.0, calculated as (10.0 + 20.0) / 2.0)
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].source == "item"`
- `modifiers[0].conditions == {}` (empty conditions dict)

---

## Test Case: TC-CALC-ITEM-PARSER-011
**Title:** ItemModifierParser.parse_line() base damage pattern

**Category:** Positive

**Description:** Test parse_line() method for base damage pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("10 to 20 Physical Damage")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "BasePhysicalDamage"` (normalized: "Physical Damage" → "BasePhysicalDamage")
- `modifiers[0].mod_type == ModifierType.BASE`
- `modifiers[0].value == 15.0` (average of min: 10.0, max: 20.0)
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-012
**Title:** ItemModifierParser.parse_line() to maximum pattern

**Category:** Positive

**Description:** Test parse_line() method for "X to maximum Y" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("+20 to maximum Life")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "Life"` (normalized: "maximum Life" → "Life")
- `modifiers[0].value == 20.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-013
**Title:** ItemModifierParser.parse_line() conversion pattern

**Category:** Positive

**Description:** Test parse_line() method for damage conversion pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("50% of Physical Damage converted to Fire")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "PhysicalDamageToFireDamage"` (conversion stat format: "{from_stat}To{to_stat}")
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].value == 50.0` (conversion percentage)
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-014
**Title:** ItemModifierParser.parse_line() to all pattern

**Category:** Positive

**Description:** Test parse_line() method for "X to all Attributes" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("+5 to all Attributes")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 3` (one modifier for each attribute: Strength, Dexterity, Intelligence)
- `modifiers[0].stat == "Strength"` and `modifiers[0].value == 5.0`
- `modifiers[1].stat == "Dexterity"` and `modifiers[1].value == 5.0`
- `modifiers[2].stat == "Intelligence"` and `modifiers[2].value == 5.0`
- All modifiers have `mod_type == ModifierType.FLAT`
- All modifiers have `source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-015
**Title:** ItemModifierParser.parse_line() veiled pattern

**Category:** Positive

**Description:** Test parse_line() method for veiled modifiers

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("Veiled: +10 to Strength")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "Strength"`
- `modifiers[0].value == 10.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- Veiled modifier is recognized (may have special flag or metadata)
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-016
**Title:** ItemModifierParser.parse_line() corrupted pattern

**Category:** Positive

**Description:** Test parse_line() method for corrupted modifiers

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("Corrupted: 20% increased Damage")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "Damage"`
- `modifiers[0].value == 20.0`
- `modifiers[0].mod_type == ModifierType.INCREASED`
- Corrupted modifier is recognized (may have special flag or metadata)
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-017
**Title:** ItemModifierParser.parse_line() per pattern

**Category:** Positive

**Description:** Test parse_line() method for "X per Y" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("10% increased Damage per 5 Strength")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- `modifiers[0].stat == "DamagePerStrength"` (per pattern stat format: "{stat}Per{attribute}")
- `modifiers[0].mod_type == ModifierType.INCREASED`
- `modifiers[0].value == 2.0` (calculated as 10.0 / 5.0, representing % per unit of attribute)
- `modifiers[0].conditions == {"requires_attribute": "strength"}` (dependency stored in conditions)
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-018
**Title:** ItemModifierParser.parse_line() chance pattern

**Category:** Positive

**Description:** Test parse_line() method for "X% chance to Y" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("25% chance to Ignite")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- Chance pattern is recognized
- `modifiers[0].stat == "IgniteChance"` (normalized: "chance to Ignite" → "IgniteChance")
- `modifiers[0].value == 25.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-019
**Title:** ItemModifierParser.parse_line() socketed pattern

**Category:** Positive

**Description:** Test parse_line() method for "Socketed gems have X" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("Socketed gems have +1 to Level of all Gems")`
2. Verify the result

**Expected Result:**
- `len(modifiers) >= 1`
- Socketed pattern is recognized
- Modifier applies to socketed gems
- `modifiers[0].stat == "GemLevel"` or similar (normalized stat name)
- `modifiers[0].value == 1.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-020
**Title:** ItemModifierParser.parse_line() chance when pattern

**Category:** Positive

**Description:** Test parse_line() method for "X% chance to Y when Z" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("30% chance to Freeze when you Hit")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- Chance when pattern is recognized
- Condition is processed correctly
- `modifiers[0].stat == "FreezeChance"` (normalized)
- `modifiers[0].value == 30.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].conditions == {"when": "hit"}` or similar
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-021
**Title:** ItemModifierParser.parse_line() chance on pattern

**Category:** Positive

**Description:** Test parse_line() method for "X% chance to Y on Z" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("15% chance to Ignite on Kill")`
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- Chance on pattern is recognized
- Condition is processed correctly
- `modifiers[0].stat == "IgniteChance"` (normalized)
- `modifiers[0].value == 15.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].conditions == {"on": "kill"}` or similar
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-022
**Title:** ItemModifierParser.parse_line() unique item integration

**Category:** Positive

**Description:** Test parse_line() method with unique item modifier integration

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("+50 to maximum Life")` (example unique item modifier)
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- Modifier is recognized
- Integration works correctly
- `modifiers[0].stat == "Life"` (normalized: "maximum Life" → "Life")
- `modifiers[0].value == 50.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-023
**Title:** ItemModifierParser.parse_line() flat no plus pattern

**Category:** Positive

**Description:** Test parse_line() method for flat pattern without plus sign

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("10 to Strength")` (without "+")
2. Verify the result

**Expected Result:**
- `len(modifiers) == 1`
- Pattern is recognized even without "+" prefix
- `modifiers[0].stat == "Strength"`
- `modifiers[0].value == 10.0`
- `modifiers[0].mod_type == ModifierType.FLAT`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-024
**Title:** ItemModifierParser.parse_line() per stat pattern

**Category:** Positive

**Description:** Test parse_line() method for "X% increased Y per Z" pattern

**Preconditions:**
- None

**Test Steps:**
1. Call `ItemModifierParser.parse_line("2% increased Damage per 10 Strength")`
2. Verify the result

**Expected Result:**
- `len(modifiers) >= 1`
- Per stat pattern is recognized
- Modifier has dependency on Strength stat
- `modifiers[0].stat == "Damage"`
- `modifiers[0].value == 2.0` (per 10 Strength)
- `modifiers[0].mod_type == ModifierType.INCREASED`
- `modifiers[0].source == "item"`

---

## Test Case: TC-CALC-ITEM-PARSER-025
**Title:** ItemModifierParser.parse_line() complex conditional patterns

**Category:** Positive

**Description:** Test parse_line() method for complex conditional patterns with complete enumeration of all condition variants

**Preconditions:**
- None

**Test Steps:**
1. For each conditional pattern in the table below, call `ItemModifierParser.parse_line()` with the specified input string
2. Verify that the result matches the expected modifier structure

**Expected Result:**
All conditional patterns should be recognized and processed correctly. Each example should create a modifier with the correct structure.

### Parsing rules:

#### 1. Condition keyword mapping
Condition keywords in the input text are mapped to standardized condition keys:
- "Recently" → `"recently"`
- "On" → `"on"`
- "When" → `"when"`
- "If" → `"if"`

**Example:** `"if you've killed recently"` → condition key: `"recently"`

#### 2. Condition value normalization

**Phrase-to-token mapping:**

| Input Phrase | Normalized Token |
|--------------|------------------|
| "you've killed" | "killed" |
| "you have killed" | "killed" |
| "you kill" | "killed" |
| "you've blocked" | "blocked" |
| "you have blocked" | "blocked" |
| "you block" | "blocked" |
| "you've cast" | "cast" |
| "you have cast" | "cast" |
| "you cast" | "cast" |
| "taken damage" | "been_hit" |
| "you've taken damage" | "been_hit" |
| "you have taken damage" | "been_hit" |
| "you take damage" | "take_damage" |
| "you take" | "take_damage" |
| "been poisoned" | "poisoned" |
| "you've been poisoned" | "poisoned" |
| "you have been poisoned" | "poisoned" |
| "you are poisoned" | "poisoned" |
| "you're poisoned" | "poisoned" |
| "you've been stunned" | "stunned" |
| "you have been stunned" | "stunned" |
| "been stunned" | "stunned" |
| "you've been taunted" | "taunted" |
| "you have been taunted" | "taunted" |
| "been taunted" | "taunted" |
| "you've crit" | "crit" |
| "you have crit" | "crit" |
| "you crit" | "crit" |
| "you've hit" | "hit" |
| "you have hit" | "hit" |
| "you hit" | "hit" |
| "you've used a skill" | "used_skill" |
| "you have used a skill" | "used_skill" |
| "you use a skill" | "used_skill" |
| "used a skill" | "used_skill" |

**Normalization pipeline (pseudo-code):**

```
function normalize_condition_value(input: str) -> str:
    # Step 1: Convert to lowercase
    normalized = input.lower()

    # Step 2: Trim whitespace
    normalized = normalized.strip()

    # Step 3: Apply phrase-to-token mapping (check longest matches first)
    # Order matters: check multi-word phrases before single words
    for phrase, token in PHRASE_MAPPING.items():
        if normalized.contains(phrase):
            normalized = normalized.replace(phrase, token)
            break

    # Step 4: Replace remaining spaces with underscores
    normalized = normalized.replace(" ", "_")

    # Step 5: Handle "recently" suffix
    original_lower = input.lower()
    if "recently" in original_lower:
        if not normalized.endswith("_recently"):
            normalized = normalized + "_recently"

    return normalized
```

**Examples with "recently" suffix:**

| Input | Normalized Output |
|-------|-------------------|
| "you've killed recently" | "killed_recently" |
| "you've blocked recently" | "blocked_recently" |
| "you've cast recently" | "cast_recently" |
| "taken damage recently" | "been_hit_recently" |
| "you've taken damage recently" | "been_hit_recently" |
| "been poisoned recently" | "poisoned_recently" |
| "you've been stunned recently" | "stunned_recently" |
| "you've been taunted recently" | "taunted_recently" |
| "you've crit recently" | "crit_recently" |
| "you've used a skill recently" | "used_skill_recently" |

**Examples without "recently" suffix:**

| Input | Normalized Output |
|-------|-------------------|
| "you've killed" | "killed" |
| "you've blocked" | "blocked" |
| "taken damage" | "been_hit" |
| "you've been stunned" | "stunned" |
| "you've used a skill" | "used_skill" |

#### 3. Stat extraction and normalization
Stat names are extracted and normalized using the following rules:
- Strip prefixes like "chance to" or similar qualifiers
- For status effects (freeze/ignite/shock/poison/bleed): capitalize base stat word and append "Chance" (e.g., "freeze" → "FreezeChance")
- For damage/attack values: use direct mapping with proper capitalization (e.g., "damage" → "Damage", "attack speed" → "AttackSpeed")

**Example:** `"15% chance to ignite"` → normalized stat: `"IgniteChance"`

### Conditional Pattern Test Cases:

| Condition Type | Input String | Expected Modifier |
|----------------|--------------|-------------------|
| **Recently (if you've Z recently)** | `"10% chance to freeze if you've killed recently"` | `Modifier(stat="FreezeChance", value=10.0, mod_type=ModifierType.FLAT, conditions={"recently": "killed_recently"}, source="item")` |
| **Recently (if you Z recently)** | `"15% chance to ignite if you crit recently"` | `Modifier(stat="IgniteChance", value=15.0, mod_type=ModifierType.FLAT, conditions={"recently": "crit_recently"}, source="item")` |
| **Recently (used a skill)** | `"20% chance to shock if you've used a skill recently"` | `Modifier(stat="ShockChance", value=20.0, mod_type=ModifierType.FLAT, conditions={"recently": "used_skill_recently"}, source="item")` |
| **Recently (taken damage)** | `"25% chance to poison if you've taken damage recently"` | `Modifier(stat="PoisonChance", value=25.0, mod_type=ModifierType.FLAT, conditions={"recently": "been_hit_recently"}, source="item")` |
| **Recently (blocked)** | `"30% chance to bleed if you've blocked recently"` | `Modifier(stat="BleedChance", value=30.0, mod_type=ModifierType.FLAT, conditions={"recently": "blocked_recently"}, source="item")` |
| **On kill** | `"10% chance to freeze on kill"` | `Modifier(stat="FreezeChance", value=10.0, mod_type=ModifierType.FLAT, conditions={"on": "kill"}, source="item")` |
| **On hit** | `"15% chance to ignite on hit"` | `Modifier(stat="IgniteChance", value=15.0, mod_type=ModifierType.FLAT, conditions={"on": "hit"}, source="item")` |
| **On crit** | `"20% chance to shock on crit"` | `Modifier(stat="ShockChance", value=20.0, mod_type=ModifierType.FLAT, conditions={"on": "crit"}, source="item")` |
| **On block** | `"25% chance to poison on block"` | `Modifier(stat="PoisonChance", value=25.0, mod_type=ModifierType.FLAT, conditions={"on": "block"}, source="item")` |
| **When hit** | `"30% chance to bleed when hit"` | `Modifier(stat="BleedChance", value=30.0, mod_type=ModifierType.FLAT, conditions={"when": "hit"}, source="item")` |
| **When you kill** | `"10% chance to freeze when you kill"` | `Modifier(stat="FreezeChance", value=10.0, mod_type=ModifierType.FLAT, conditions={"when": "kill"}, source="item")` |
| **When you use a skill** | `"15% chance to ignite when you use a skill"` | `Modifier(stat="IgniteChance", value=15.0, mod_type=ModifierType.FLAT, conditions={"when": "use_skill"}, source="item")` |
| **When you take damage** | `"20% chance to shock when you take damage"` | `Modifier(stat="ShockChance", value=20.0, mod_type=ModifierType.FLAT, conditions={"when": "take_damage"}, source="item")` |
| **When you block** | `"25% chance to poison when you block"` | `Modifier(stat="PoisonChance", value=25.0, mod_type=ModifierType.FLAT, conditions={"when": "block"}, source="item")` |
| **When Z (generic)** | `"30% chance to freeze when you cast a spell"` | `Modifier(stat="FreezeChance", value=30.0, mod_type=ModifierType.FLAT, conditions={"when": "you cast a spell"}, source="item")` |
| **On Z (generic)** | `"10% chance to ignite on taking a critical strike"` | `Modifier(stat="IgniteChance", value=10.0, mod_type=ModifierType.FLAT, conditions={"on": "taking a critical strike"}, source="item")` |
| **If Z (generic)** | `"15% chance to shock if you have killed recently"` | `Modifier(stat="ShockChance", value=15.0, mod_type=ModifierType.FLAT, conditions={"if": "you have killed recently"}, source="item")` |

### Additional Conditional Patterns (for future implementation):

| Condition Type | Input String | Expected Modifier |
|----------------|--------------|-------------------|
| **Recently (flat modifier)** | `"+10 to Strength Recently"` | `Modifier(stat="Strength", value=10.0, mod_type=ModifierType.FLAT, conditions={"recently": True}, source="item")` |
| **On hit (increased modifier)** | `"20% increased Damage On hit"` | `Modifier(stat="Damage", value=20.0, mod_type=ModifierType.INCREASED, conditions={"on": "hit"}, source="item")` |
| **While chasing** | `"+5 to Accuracy While chasing"` | `Modifier(stat="Accuracy", value=5.0, mod_type=ModifierType.FLAT, conditions={"while": "chasing"}, source="item")` |
| **While disabled** | `"30% increased Damage While disabled"` | `Modifier(stat="Damage", value=30.0, mod_type=ModifierType.INCREASED, conditions={"while": "disabled"}, source="item")` |
| **During flask effect** | `"25% increased Damage during Flask Effect"` | `Modifier(stat="Damage", value=25.0, mod_type=ModifierType.INCREASED, conditions={"flask_effect": True}, source="item")` |
| **While charging** | `"+5 to Accuracy While charging"` | `Modifier(stat="Accuracy", value=5.0, mod_type=ModifierType.FLAT, conditions={"while": "charging"}, source="item")` |
| **On kill (flat modifier)** | `"+50 to Life On kill"` | `Modifier(stat="Life", value=50.0, mod_type=ModifierType.FLAT, conditions={"on": "kill"}, source="item")` |
| **When hit (increased modifier)** | `"15% increased Attack Speed when hit"` | `Modifier(stat="AttackSpeed", value=15.0, mod_type=ModifierType.INCREASED, conditions={"when": "hit"}, source="item")` |
| **On crit (more modifier)** | `"10% more Damage on crit"` | `Modifier(stat="Damage", value=10.0, mod_type=ModifierType.MORE, conditions={"on": "crit"}, source="item")` |
| **On block (reduced modifier)** | `"20% reduced Mana Cost on block"` | `Modifier(stat="ManaCost", value=-20.0, mod_type=ModifierType.REDUCED, conditions={"on": "block"}, source="item")` |

**Notes:**
- All modifiers must have `source="item"` (or the passed source parameter)
- Conditions must be correctly extracted and stored in the `conditions` field
- Values must be correctly parsed as float
- Modifier types must match the pattern (FLAT, INCREASED, MORE, REDUCED, LESS)
- Stats must be normalized according to parser rules (see Stat Name Normalization Rules section)
