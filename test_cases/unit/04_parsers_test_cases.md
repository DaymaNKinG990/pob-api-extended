# Parsers Unit Test Cases

## Module: pobapi.parsers

### Overview
Unit test cases for the parsers module. Tests validate static methods of parser classes against various XML structures.

---

## Test Case: TC-PARSERS-001
**Title:** BuildInfoParser.parse() with valid build info

**Category:** Positive

**Description:** Validation of static method BuildInfoParser.parse() with valid build information

**Preconditions:**
- XML root contains a valid Build element with all attributes

**Test Steps:**
1. Create XML root with a valid Build element
2. Call `BuildInfoParser.parse(xml_root)`
3. Verify all result fields

**Expected Result:**
- Method returns a dictionary
- result["class_name"] == "Scion"
- result["ascendancy_name"] == "Ascendant"
- result["level"] == "1"
- result["bandit"] == "Alira"
- result["main_socket_group"] == "1"

---

## Test Case: TC-PARSERS-002
**Title:** BuildInfoParser.parse() with missing Build element

**Category:** Negative

**Description:** Validation of static method BuildInfoParser.parse() when Build element is missing

**Preconditions:**
- XML root does not contain a Build element

**Test Steps:**
1. Create XML root without Build element
2. Call `BuildInfoParser.parse(xml_root)`
3. Catch the exception

**Expected Result:**
- ParsingError is raised
- Error message contains "Build element not found"

---

## Test Case: TC-PARSERS-003
**Title:** BuildInfoParser.parse() with optional fields missing

**Category:** Edge Case

**Description:** Validation of static method BuildInfoParser.parse() when optional fields are missing

**Preconditions:**
- XML root contains Build element with only required fields

**Test Steps:**
1. Create XML root with Build element without optional attributes
2. Call `BuildInfoParser.parse(xml_root)`
3. Verify optional fields

**Expected Result:**
- Method returns a dictionary
- Required fields are populated
- result["ascendancy_name"] is None
- result["bandit"] is None

---

## Test Case: TC-PARSERS-004
**Title:** SkillsParser.parse_skill_groups() with valid skill groups

**Category:** Positive

**Description:** Validation of static method SkillsParser.parse_skill_groups() with valid skill groups

**Preconditions:**
- XML root contains a valid Skills element with Skill elements

**Test Steps:**
1. Create XML root with valid skill groups
2. Call `SkillsParser.parse_skill_groups(xml_root)`
3. Verify result structure

**Expected Result:**
- Method returns a list
- len(result) == 1
- result[0]["enabled"] is True
- result[0]["label"] == "Test label"
- result[0]["main_active_skill"] == 1
- len(result[0]["abilities"]) == 1

---

## Test Case: TC-PARSERS-005
**Title:** SkillsParser.parse_skill_groups() with multiple skill groups

**Category:** Positive

**Description:** Validation of static method SkillsParser.parse_skill_groups() with multiple skill groups

**Preconditions:**
- XML root contains multiple Skill elements

**Test Steps:**
1. Create XML root with multiple Skill elements
2. Call `SkillsParser.parse_skill_groups(xml_root)`
3. Verify all groups

**Expected Result:**
- Method returns a list
- len(result) == 2
- result[0]["enabled"] is True
- result[1]["enabled"] is False
- result[1]["main_active_skill"] is None

---

## Test Case: TC-PARSERS-006
**Title:** SkillsParser.parse_skill_groups() with empty Skills element

**Category:** Edge Case

**Description:** Validation of static method SkillsParser.parse_skill_groups() when Skills element is missing

**Preconditions:**
- XML root does not contain a Skills element

**Test Steps:**
1. Create XML root without Skills element
2. Call `SkillsParser.parse_skill_groups(xml_root)`
3. Verify result

**Expected Result:**
- Method returns an empty list []
- len(result) == 0

---

## Test Case: TC-PARSERS-007
**Title:** SkillsParser.parse_skill_groups() with nil mainActiveSkill

**Category:** Edge Case

**Description:** Validation of static method SkillsParser.parse_skill_groups() with nil mainActiveSkill value

**Preconditions:**
- XML root contains Skill with mainActiveSkill="nil"

**Test Steps:**
1. Create XML root with Skill mainActiveSkill="nil"
2. Call `SkillsParser.parse_skill_groups(xml_root)`
3. Verify main_active_skill value

**Expected Result:**
- Method returns a list
- result[0]["main_active_skill"] is None

---

## Test Case: TC-PARSERS-008
**Title:** ItemsParser.parse_items() with valid items

**Category:** Positive

**Description:** Validation of static method ItemsParser.parse_items() with valid items

**Preconditions:**
- XML root contains a valid Items element with Item elements

**Test Steps:**
1. Create XML root with valid items
2. Call `ItemsParser.parse_items(xml_root)`
3. Verify result structure

**Expected Result:**
- Method returns a list
- len(result) == 1
- result[0]["rarity"] == "Unique"
- result[0]["name"] == "Inpulsa's Broken Heart"
- result[0]["base"] == "Sadist Garb"

---

## Test Case: TC-PARSERS-009
**Title:** ItemsParser.parse_items() with default rarity

**Category:** Edge Case

**Description:** Validation of static method ItemsParser.parse_items() with item without specified rarity

**Preconditions:**
- XML root contains Item without rarity attribute

**Test Steps:**
1. Create XML root with Item without rarity
2. Call `ItemsParser.parse_items(xml_root)`
3. Verify rarity value

**Expected Result:**
- Method returns a list
- result[0]["rarity"] == "Normal" (default value)

---

## Test Case: TC-PARSERS-010
**Title:** ItemsParser.parse_items() with empty Items element

**Category:** Edge Case

**Description:** Validation of static method ItemsParser.parse_items() when Items element is missing

**Preconditions:**
- XML root does not contain an Items element

**Test Steps:**
1. Create XML root without Items element
2. Call `ItemsParser.parse_items(xml_root)`
3. Verify result

**Expected Result:**
- Method returns an empty list []
- len(result) == 0

---

## Test Case: TC-PARSERS-011
**Title:** TreesParser.parse_trees() with valid trees

**Category:** Positive

**Description:** Validation of static method TreesParser.parse_trees() with valid trees

**Preconditions:**
- XML root contains a valid Trees element with Tree elements

**Test Steps:**
1. Create XML root with valid trees
2. Call `TreesParser.parse_trees(xml_root)`
3. Verify result structure

**Expected Result:**
- Method returns a list (array) of tree objects
- Each tree object contains the following fields:
  - `url` (string, required): URL of the passive skill tree (e.g., "https://pathofexile.com/passive-skill-tree/...")
  - `nodes` (array of integers, required): Array of passive tree node IDs, where each element is an integer (node ID)
  - `sockets` (object/dict, required): Dictionary where key is nodeId (integer), value is itemId (integer). Represents mapping of gem sockets to tree nodes

**Schema:**
```json
[
  {
    "url": "string",
    "nodes": [integer, integer, ...],
    "sockets": {
      "integer (nodeId)": "integer (itemId)"
    }
  }
]
```

**Example:**
```json
[
  {
    "url": "https://pathofexile.com/passive-skill-tree/AAAA",
    "nodes": [12345, 12346, 12347, 12348],
    "sockets": {
      "12345": 67890,
      "12346": 67891
    }
  },
  {
    "url": "https://pathofexile.com/passive-skill-tree/BBBB",
    "nodes": [23456, 23457],
    "sockets": {
      "23456": 78901
    }
  }
]
```

**Field Details:**
- `url`: string, required - Full URL of the passive skill tree from Path of Exile
- `nodes`: array of integers, required - List of node IDs that are selected in the tree. Each element is an integer (node ID)
- `sockets`: object (dict[int, int]), required - Dictionary of gem sockets, where key is node ID (integer), value is item ID (integer). Can be an empty object `{}` if there are no sockets

---

## Test Case: TC-PARSERS-012
**Title:** TreesParser.parse_trees() with empty Trees element

**Category:** Edge Case

**Description:** Validation of static method TreesParser.parse_trees() when Trees element is missing

**Preconditions:**
- XML root does not contain a Trees element

**Test Steps:**
1. Create XML root without Trees element
2. Call `TreesParser.parse_trees(xml_root)`
3. Verify result

**Expected Result:**
- Method returns an empty list []
- len(result) == 0

---

## Test Case: TC-PARSERS-013
**Title:** SkillsParser.parse_skill_groups() with multiple abilities

**Category:** Positive

**Description:** Validation of static method SkillsParser.parse_skill_groups() with skill group containing multiple abilities

**Preconditions:**
- XML root contains Skill with multiple Ability elements

**Test Steps:**
1. Create XML root with Skill containing multiple Ability elements
2. Call `SkillsParser.parse_skill_groups(xml_root)`
3. Verify abilities list

**Expected Result:**
- Method returns a list
- result[0]["abilities"] contains all abilities
- Each ability contains: name, enabled, level, gemId

---

## Test Case: TC-PARSERS-014
**Title:** ItemsParser.parse_items() with all item attributes

**Category:** Positive

**Description:** Validation of static method ItemsParser.parse_items() with item containing all attributes

**Preconditions:**
- XML root contains Item with all possible attributes

**Test Steps:**
1. Create XML root with Item with all attributes
2. Call `ItemsParser.parse_items(xml_root)`
3. Verify all item attributes

**Expected Result:**
- Method returns a list
- len(result) == 1
- parsed = result[0]

**Attribute Validations with Example Values and Assertions:**

1. **id (string)**: Unique identifier for the item
   - Example: `"abc123def456"`
   - Assertion: `assert isinstance(parsed.get("id"), str) and parsed.get("id") == "abc123def456"`

2. **name (string)**: Item display name
   - Example: `"Inpulsa's Broken Heart"`
   - Assertion: `assert parsed.get("name") == "Inpulsa's Broken Heart"`

3. **rarity (string)**: Item rarity tier
   - Example: `"Rare"`
   - Assertion: `assert parsed.get("rarity") == "Rare"`

4. **baseType (string)**: Base item type name
   - Example: `"Sadist Garb"`
   - Assertion: `assert parsed.get("baseType") == "Sadist Garb"`

5. **itemLevel (number)**: Item level
   - Example: `84`
   - Assertion: `assert isinstance(parsed.get("itemLevel"), int) and parsed.get("itemLevel") == 84`

6. **requiredLevel (number)**: Required character level to equip
   - Example: `68`
   - Assertion: `assert isinstance(parsed.get("requiredLevel"), int) and parsed.get("requiredLevel") == 68`

7. **quality (number)**: Item quality percentage (0-30)
   - Example: `20`
   - Assertion: `assert isinstance(parsed.get("quality"), int) and parsed.get("quality") == 20`

8. **sockets (structure)**: Socket configuration with count, color, and linking
   - Example: `[{"count": 4, "color": "R", "linked": True}, {"count": 2, "color": "B", "linked": False}]`
   - Assertion: `assert isinstance(parsed.get("sockets"), list) and len(parsed.get("sockets")) == 2 and len([s for s in parsed.get("sockets") if s.get("color") == "R"]) == 2`

9. **implicitMods (array of strings)**: Implicit modifiers
   - Example: `["+20 to maximum Life", "+10% to all Elemental Resistances"]`
   - Assertion: `assert isinstance(parsed.get("implicitMods"), list) and "+20 to maximum Life" in parsed.get("implicitMods")`

10. **explicitMods (array of strings)**: Explicit modifiers
    - Example: `["+50 to maximum Life", "+30% increased Elemental Damage"]`
    - Assertion: `assert isinstance(parsed.get("explicitMods"), list) and "+50 to maximum Life" in parsed.get("explicitMods")`

11. **enchantMods (array of strings)**: Enchantment modifiers
    - Example: `["Adds 20 to 30 Fire Damage to Attacks"]`
    - Assertion: `assert isinstance(parsed.get("enchantMods"), list) and len(parsed.get("enchantMods")) > 0`

12. **craftedMods (array of strings)**: Crafted modifiers
    - Example: `["+15% to Fire Resistance"]`
    - Assertion: `assert isinstance(parsed.get("craftedMods"), list) and "+15% to Fire Resistance" in parsed.get("craftedMods")`

13. **properties (map)**: Property name to value mapping
    - Example: `{"Armour": 500, "Energy Shield": 200, "Evasion Rating": 300}`
    - Assertion: `assert isinstance(parsed.get("properties"), dict) and parsed.get("properties").get("Armour") == 500`

14. **influences (array)**: Influence types on the item
    - Example: `["shaper", "elder"]`
    - Assertion: `assert isinstance(parsed.get("influences"), list) and "shaper" in parsed.get("influences") and "elder" in parsed.get("influences")`

15. **corrupted (boolean)**: Whether the item is corrupted
    - Example: `True`
    - Assertion: `assert isinstance(parsed.get("corrupted"), bool) and parsed.get("corrupted") is True`

16. **identified (boolean)**: Whether the item is identified
    - Example: `True`
    - Assertion: `assert isinstance(parsed.get("identified"), bool) and parsed.get("identified") is True`

17. **talismanTier (nullable number)**: Talisman tier if applicable
    - Example: `3` or `None`
    - Assertion: `assert parsed.get("talismanTier") is None or (isinstance(parsed.get("talismanTier"), int) and parsed.get("talismanTier") == 3)`

18. **socketedItems (array)**: Array of socketed item summaries
    - Example: `[{"name": "Support Gem", "level": 20}, {"name": "Skill Gem", "level": 21}]`
    - Assertion: `assert isinstance(parsed.get("socketedItems"), list) and len(parsed.get("socketedItems")) > 0`

19. **note/notes (string)**: Item note or notes
    - Example: `"~price 5 exalt"`
    - Assertion: `assert isinstance(parsed.get("note"), str) and "~price" in parsed.get("note")`

---

## Test Case: TC-PARSERS-015
**Title:** BuildInfoParser.parse() with special characters

**Category:** Edge Case

**Description:** Validation of static method BuildInfoParser.parse() with special characters in data

**Preconditions:**
- XML root contains special characters in attribute values

**Test Steps:**
1. Create XML root with special characters
2. Call `BuildInfoParser.parse(xml_root)`
3. Verify special character handling

**Expected Result:**
- Method returns a dictionary
- Special characters are correctly processed
- Values match expected results

---

## Test Case: TC-PARSERS-016
**Title:** SkillsParser.parse_skill_groups() with disabled abilities

**Category:** Edge Case

**Description:** Validation of static method SkillsParser.parse_skill_groups() with disabled abilities

**Preconditions:**
- XML root contains Ability with enabled="false"

**Test Steps:**
1. Create XML root with Ability enabled="false"
2. Call `SkillsParser.parse_skill_groups(xml_root)`
3. Verify enabled value for abilities

**Expected Result:**
- Method returns a list
- enabled is correctly set to False for disabled abilities

---

## Test Case: TC-PARSERS-017
**Title:** DefaultBuildParser.parse() with complete build

**Category:** Positive

**Description:** Validation of static method DefaultBuildParser.parse() with complete build

**Preconditions:**
- XML root contains complete build data

**Test Steps:**
1. Create XML root with complete build
2. Call `DefaultBuildParser.parse(xml_root)`
3. Verify all build components

**Expected Result:**
- Method returns a Build object with the following structure:

**Build Object Schema:**

```json
{
  "id": "string (optional)",
  "name": "string (optional)",
  "class": "string (required)",
  "level": "number (required)",
  "createdAt": "ISO string (optional)",
  "sources": {
    "buildInfo": "object (required)",
    "skills": "array (required)",
    "items": "array (required)",
    "trees": "array (required)"
  },
  "skills": [
    {
      "id": "string (required)",
      "name": "string (required)",
      "rank": "number (required)",
      "hotkey": "string (optional)"
    }
  ],
  "items": [
    {
      "slot": "string (required)",
      "id": "string (required)",
      "name": "string (required)",
      "quantity": "number (optional)"
    }
  ],
  "trees": [
    {
      "treeId": "string (required)",
      "nodes": [
        {
          "nodeId": "string (required)",
          "points": "number (required)"
        }
      ]
    }
  ]
}
```

**Field Requirements:**
- **Required fields:** `class`, `level`, `skills`, `items`
- **Optional fields:** `id`, `name`, `createdAt`, `quantity` (in items), `hotkey` (in skills)

**Parser Field Mapping:**
- **BuildInfoParser** → `class`, `level`, `createdAt` (if available), `id` (if available), `name` (if available)
- **SkillsParser** → `skills` array and skill-level info (id, name, rank, hotkey)
- **ItemsParser** → `items` array and slot assignments (slot, id, name, quantity)
- **TreesParser** → `trees` structure and node points (treeId, nodes with nodeId and points)

**Example Output:**

```json
{
  "id": "build_12345",
  "name": "My Lightning Build",
  "class": "Witch",
  "level": 85,
  "createdAt": "2024-01-15T10:30:00Z",
  "sources": {
    "buildInfo": {
      "class_name": "Witch",
      "ascendancy_name": "Elementalist",
      "level": "85",
      "bandit": "None"
    },
    "skills": [
      {
        "enabled": true,
        "label": "Main Skill",
        "abilities": []
      }
    ],
    "items": [
      {
        "name": "Lightning Coil",
        "base": "Full Wyrmscale",
        "rarity": "Unique"
      }
    ],
    "trees": [
      {
        "url": "https://www.pathofexile.com/passive-skill-tree/...",
        "nodes": [123, 456, 789],
        "sockets": {}
      }
    ]
  },
  "skills": [
    {
      "id": "skill_001",
      "name": "Arc",
      "rank": 1,
      "hotkey": "Q"
    }
  ],
  "items": [
    {
      "slot": "body_armour",
      "id": "item_001",
      "name": "Lightning Coil",
      "quantity": 1
    }
  ],
  "trees": [
    {
      "treeId": "tree_001",
      "nodes": [
        {
          "nodeId": "123",
          "points": 1
        },
        {
          "nodeId": "456",
          "points": 1
        }
      ]
    }
  ]
}
```

- All build components are correctly processed
- All required fields are present
- Optional fields may be missing or have null value

---

## Test Case: TC-PARSERS-018
**Title:** ItemsParser.parse_items() with malformed item text

**Category:** Negative

**Description:** Validation of static method ItemsParser.parse_items() with malformed item text. The parser MUST demonstrate deterministic behavior: raise ParsingError with a specific error message and not return partial results.

**Preconditions:**
- XML root contains Item with malformed text that cannot be correctly parsed

**Test Steps:**
1. Create XML root with Item with malformed text (e.g., "Item: Widget; Price: USD ten; Qty: two")
2. Call `ItemsParser.parse_items(xml_root)`
3. Catch the exception and verify its type and message

**Example Malformed Text:**
```
Item: Widget; Price: USD ten; Qty: two
```

**Expected Result:**
- Exception of type `ParsingError` is raised
- Exception message has format: `"Malformed item text: <reason>"`, where `<reason>` is the specific error cause (e.g., "invalid numeric value", "missing required field", "unexpected format")
- Partial result is NOT returned (all fields must be null/empty on error)
- Method does not return a dictionary with partially filled fields
