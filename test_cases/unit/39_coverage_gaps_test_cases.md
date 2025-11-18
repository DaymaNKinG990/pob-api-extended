# Coverage Gaps Unit Test Cases

## Module: tests/unit/test_coverage_gaps.py

### Overview
Unit test cases for the test_coverage_gaps module, which covers remaining uncovered lines in api.py and parsers.py.

---

## Test Case: TC-COVERAGE-GAPS-001
**Title:** TestSkillsElementMissing.test_skill_groups_empty_skills_element() empty Skills element

**Category:** Edge Case

**Description:** Test skill_groups when Skills element is empty (covers api.py line 130)

**Preconditions:**
- None

**Test Steps:**
1. Create XML with empty Skills element
   ```xml
   <Skills/>
   ```
2. Create PathOfBuildingAPI from XML
3. Call build.skill_groups
4. Verify result

**Expected Result:**
- build.skill_groups == [] (empty list)
- type(build.skill_groups) == list
- len(build.skill_groups) == 0
- None check in api.py line 191 (skills_element is None) is covered: when Skills element is missing or empty, method returns empty list without exceptions

---

## Test Case: TC-COVERAGE-GAPS-002
**Title:** TestSkillsElementMissing.test_skill_gems_empty_skills_element() empty Skills element

**Category:** Edge Case

**Description:** Test skill_gems when Skills element is empty (covers api.py line 200)

**Preconditions:**
- None

**Test Steps:**
1. Create XML with empty Skills element
   ```xml
   <Skills/>
   ```
2. Create PathOfBuildingAPI from XML
3. Call build.skill_gems
4. Verify result

**Expected Result:**
- build.skill_gems == [] (empty list)
- type(build.skill_gems) == list
- len(build.skill_gems) == 0
- None check in api.py line 274 (skills_element is None) is covered: when Skills element is missing or empty, method returns empty list without exceptions

---

## Test Case: TC-COVERAGE-GAPS-003
**Title:** TestSkillsElementMissing.test_skill_groups_with_skillset() with SkillSet

**Category:** Positive

**Description:** Test skill_groups when Skills element contains SkillSet (covers api.py line 130)

**Preconditions:**
- None

**Test Steps:**
1. Create XML with Skills element containing SkillSet
   ```xml
   <Skills>
       <SkillSet>
           <Skill enabled="true" label="Test Group" mainActiveSkill="1">
               <Gem gemId="1" nameSpec="Arc" enabled="true"
                    level="20" quality="0" skillId="Arc"/>
           </Skill>
       </SkillSet>
   </Skills>
   ```
2. Create PathOfBuildingAPI from XML
3. Call build.skill_groups
4. Verify result

**Expected Result:**
- type(build.skill_groups) == list
- len(build.skill_groups) == N (where N is the number of Skill elements in SkillSet)
- Each element in build.skill_groups is an instance of models.SkillGroup
- For each SkillGroup: group.enabled has type bool, group.label has type str (can be None), group.active has type int | None, group.abilities has type list
- SkillSet structure (Skills -> SkillSet -> Skill) is processed correctly: all Skill elements from SkillSet are converted to SkillGroup objects

---

## Test Case: TC-COVERAGE-GAPS-004
**Title:** TestSkillsElementMissing.test_skill_gems_with_skillset() with SkillSet

**Category:** Positive

**Description:** Test skill_gems when Skills element contains SkillSet (covers api.py line 200)

**Preconditions:**
- None

**Test Steps:**
1. Create XML with Skills element containing SkillSet
   ```xml
   <Skills>
       <SkillSet>
           <Skill enabled="true" label="Test Group" mainActiveSkill="1">
               <Gem gemId="1" nameSpec="Arc" enabled="true"
                    level="20" quality="0" skillId="Arc"/>
               <Gem gemId="2" nameSpec="Fireball" enabled="true"
                    level="20" quality="0" skillId="Fireball" support="true"/>
           </Skill>
       </SkillSet>
   </Skills>
   ```
2. Create PathOfBuildingAPI from XML
3. Call build.skill_gems
4. Verify result

**Expected Result:**
- type(build.skill_gems) == list
- len(build.skill_gems) == N (where N is the number of Gem elements in Skill elements without source attribute)
- Each element in build.skill_gems is an instance of models.Gem
- For each Gem: gem.name has type str, gem.enabled has type bool, gem.level has type int, gem.quality has type int | None, gem.support has type bool
- Gems from Skill elements with source attribute are not included in result
- SkillSet structure is processed correctly: all Gem elements from SkillSet are extracted and filtered by source

---

## Test Case: TC-COVERAGE-GAPS-005
**Title:** TestParserSkillsetStructure.test_parser_skillset_structure() SkillsParser structure

**Category:** Positive

**Description:** Test SkillsParser structure for SkillSet (covers parsers.py)

**Preconditions:**
- None

**Test Steps:**
1. Create XML with SkillSet structure
   ```xml
   <Skills>
       <SkillSet>
           <Skill enabled="true" label="Test Group" mainActiveSkill="1">
               <Gem gemId="1" nameSpec="Arc" enabled="true"
                    level="20" quality="0" skillId="Arc"/>
           </Skill>
       </SkillSet>
   </Skills>
   ```
2. Use SkillsParser for parsing
3. Verify result structure

**Expected Result:**
- SkillsParser.parse_skill_groups(xml_root) returns list[dict]
- len(result) == N (where N is the number of Skill elements in SkillSet)
- Each element in result is a dict with keys: "enabled" (bool), "label" (str | None), "main_active_skill" (int | None), "source" (str | None), "abilities" (list)
- result[0]["enabled"] == True (if enabled="true" in XML)
- result[0]["label"] == "Test Group" (corresponds to label attribute in XML)
- result[0]["main_active_skill"] == 1 (if mainActiveSkill="1" in XML, otherwise None)
- result[0]["abilities"] is a list of XML elements (ability elements)
- Lines parsers.py 58-76 are covered (SkillSet structure processing)

---

## Test Case: TC-COVERAGE-GAPS-006
**Title:** TestTreesParserSockets.test_trees_parser_with_sockets_element() TreesParser with sockets

**Category:** Positive

**Description:** Test TreesParser with sockets element (covers parsers.py)

**Preconditions:**
- None

**Test Steps:**
1. Create XML with sockets element in Tree
   ```xml
   <Tree activeSpec="1">
       <Spec>
           <URL>https://www.pathofexile.com/passive-skill-tree/AAAABgAAAAAA</URL>
           <Sockets>
               <Socket nodeId="123" itemId="1"/>
               <Socket nodeId="456" itemId="2"/>
           </Sockets>
       </Spec>
   </Tree>
   ```
2. Use TreesParser for parsing
3. Verify result

**Expected Result:**
- TreesParser.parse_trees(xml_root) returns list[dict]
- len(result) == 1 (one Spec element)
- result[0] is a dict with keys: "url" (str), "nodes" (list[int]), "sockets" (dict[int, int])
- result[0]["sockets"] == {123: 1, 456: 2} (dictionary with nodeId: itemId pairs from Socket elements)
- type(result[0]["sockets"]) == dict
- Sockets element (Spec -> Sockets -> Socket) is processed correctly: all Socket elements are extracted and converted to dictionary
- Lines parsers.py 235-242 are covered (Sockets wrapper element processing)

---

## Test Case: TC-COVERAGE-GAPS-007
**Title:** TestTreesParserSockets.test_api_trees_with_sockets_element() API trees with sockets

**Category:** Positive

**Description:** Test API trees with sockets element (covers api.py)

**Preconditions:**
- None

**Test Steps:**
1. Create XML with sockets element in Tree
   ```xml
   <Tree activeSpec="1">
       <Spec>
           <URL>https://www.pathofexile.com/passive-skill-tree/AAAABgAAAAAA</URL>
           <Sockets>
               <Socket nodeId="123" itemId="1"/>
               <Socket nodeId="456" itemId="2"/>
           </Sockets>
       </Spec>
   </Tree>
   ```
2. Create PathOfBuildingAPI from XML
3. Verify sockets element processing

**Expected Result:**
- type(build.trees) == list
- len(build.trees) == 1 (one Spec element)
- Each element in build.trees is an instance of models.Tree
- build.trees[0].sockets == {123: 1, 456: 2} (dictionary with nodeId: itemId pairs)
- type(build.trees[0].sockets) == dict
- build.trees[0].url has type str
- build.trees[0].nodes has type list[int]
- Sockets element is processed correctly through TreesParser: all Socket elements are extracted and converted to sockets dictionary in Tree object
