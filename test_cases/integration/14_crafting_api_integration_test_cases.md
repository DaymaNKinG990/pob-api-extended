# CraftingAPI ↔ PathOfBuildingAPI Integration Test Cases

## Module: tests/integrations/test_crafting_api_integration.py

### Overview
Integration test cases for checking interaction between ItemCraftingAPI and PathOfBuildingAPI.

---

## Test Case: TC-INT-CRAFTING-API-001
**Title:** Craft item and add to build

**Category:** Positive

**Integration:** ItemCraftingAPI ↔ PathOfBuildingAPI

**Description:** Check item creation through CraftingAPI and adding to build

**Preconditions:**
- Build fixture exists
- Modifiers available in database

**Test Steps:**
1. Get available modifiers through ItemCraftingAPI.get_modifiers_by_type()
2. Create CraftingModifier for prefix and suffix
3. Create item through ItemCraftingAPI.craft_item()
4. Create Item from crafted item_text
5. Add item to build

**Expected Result:**
- result.success is True
- result.item_text != ""
- Item added to build

---

## Test Case: TC-INT-CRAFTING-API-002
**Title:** Craft item with modifiers from build stats

**Category:** Positive

**Integration:** ItemCraftingAPI ↔ PathOfBuildingAPI ↔ CalculationEngine

**Description:** Check item creation with modifiers based on build stats

**Preconditions:**
- Build fixture exists
- Modifiers available in database

**Test Steps:**
1. Calculate build stats through CalculationEngine
2. Select modifiers based on stats
3. Create item through ItemCraftingAPI.craft_item()
4. Add item to build

**Expected Result:**
- result.success is True
- Item created with correct modifiers

---

## Test Case: TC-INT-CRAFTING-API-003
**Title:** Craft item and serialize build

**Category:** Positive

**Integration:** ItemCraftingAPI ↔ PathOfBuildingAPI ↔ BuildXMLSerializer

**Description:** Check item creation and build serialization

**Preconditions:**
- Build fixture exists
- Modifiers available in database

**Test Steps:**
1. Create item through ItemCraftingAPI.craft_item()
2. Add item to build
3. Serialize build to XML
4. Verify that crafted item is in XML

**Expected Result:**
- xml is not None
- Crafted item is present in XML

---

## Test Case: TC-INT-CRAFTING-API-004
**Title:** Craft multiple items for build

**Category:** Positive

**Integration:** ItemCraftingAPI ↔ PathOfBuildingAPI

**Description:** Check creation of multiple items for build

**Preconditions:**
- Build fixture exists
- Modifiers available in database

**Test Steps:**
1. Create multiple items through ItemCraftingAPI.craft_item()
2. Add all items to build
3. Verify that all items are added

**Expected Result:**
- All items created successfully
- All items added to build

---

## Test Case: TC-INT-CRAFTING-API-005
**Title:** Craft item with build config requirements

**Category:** Positive

**Integration:** ItemCraftingAPI ↔ PathOfBuildingAPI

**Description:** Check item creation considering build config requirements

**Preconditions:**
- Build fixture with config exists
- Modifiers available in database

**Test Steps:**
1. Get config from build
2. Select modifiers considering config (enemy_level, etc.)
3. Create item through ItemCraftingAPI.craft_item()
4. Add item to build

**Expected Result:**
- result.success is True
- Item created considering config

---

## Test Case: TC-INT-CRAFTING-API-006
**Title:** Craft item and calculate stats

**Category:** Positive

**Integration:** ItemCraftingAPI ↔ PathOfBuildingAPI ↔ CalculationEngine

**Description:** Check item creation and stats recalculation

**Preconditions:**
- Build fixture exists
- Modifiers available in database

**Test Steps:**
1. Get initial stats through CalculationEngine
2. Create item through ItemCraftingAPI.craft_item()
3. Add item to build
4. Recalculate stats
5. Verify changes

**Expected Result:**
- Stats recalculated
- Stats changed after adding item

---
