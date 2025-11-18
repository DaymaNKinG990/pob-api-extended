# Validator ↔ Parser Integration Test Cases

## Module: tests/integrations/test_integration.py::TestValidatorParserIntegration

### Overview
Integration test cases for verifying the interaction between validators (InputValidator, XMLValidator) and parsers (BuildInfoParser).

---

## Test Case: TC-INT-VALIDATOR-PARSER-001
**Title:** Validate then parse valid XML

**Category:** Positive

**Integration:** InputValidator ↔ XMLValidator ↔ BuildInfoParser

**Description:** Verify the complete flow: XML bytes validation → XML structure validation → build info parsing

**Preconditions:**
- Valid XML is available (sample_xml fixture)

**Test Steps:**
1. Encode sample_xml to bytes
2. Validate XML bytes through InputValidator.validate_xml_bytes()
3. Parse XML to root element through fromstring()
4. Validate XML structure through XMLValidator.validate_build_structure()
5. Parse build info through BuildInfoParser.parse()

**Expected Result:**
- Validation passes successfully
- Parsing passes successfully
- build_info["class_name"] == "Scion"

---

## Test Case: TC-INT-VALIDATOR-PARSER-002
**Title:** Invalid XML fails validation

**Category:** Negative

**Integration:** InputValidator

**Description:** Verify handling of invalid XML (empty bytes)

**Preconditions:**
- None

**Test Steps:**
1. Attempt to validate empty bytes through InputValidator.validate_xml_bytes(b"")

**Expected Result:**
- ValidationError is raised

---

## Test Case: TC-INT-VALIDATOR-PARSER-003
**Title:** Incomplete XML fails structure validation

**Category:** Negative

**Integration:** XMLValidator ↔ BuildInfoParser

**Description:** Verify handling of incomplete XML (missing required elements)

**Preconditions:**
- None

**Test Steps:**
1. Create incomplete XML (only Build element, without required elements)
2. Parse XML to root element
3. Attempt to validate structure through XMLValidator.validate_build_structure()

**Expected Result:**
- ValidationError is raised with a message containing "Required element"

---
