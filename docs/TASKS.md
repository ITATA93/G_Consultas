# Tasks -- AG_Consultas

> Cross-project task delegation board.
> Managed by `AG_Plantilla/scripts/cross_task.py`.
>
> **Agents**: Check this file on session start for pending incoming tasks.


## Local Tasks

(none)

## Incoming (tasks requested to this project)

### TASK-2026-0002: Classify and archive unused Claude skills
- **From**: AG_Plantilla
- **Priority**: P2-Medium
- **Status**: DONE
- **Created**: 2026-02-18
- **Completed**: 2026-02-18
- **Description**: Classified all 11 Claude skills — ALL are domain-specific (diccionario-*) and RELEVANT. No archival needed. 4 Gemini skills also all RELEVANT. Documented in DEVLOG.


## Outgoing (tasks delegated to other projects)

(none)

## Completed

### [P2] EVALUATE AGENTS AND SKILLS ✅
- Status: **DONE** (2026-02-18)
- Source: AG_Plantilla (ecosystem consolidation 2026-02-18)
- Evaluator: Antigravity (Gemini)

#### Manifest Agents (7/7 relevant)
| Agent | Verdict | Notes |
|-------|---------|-------|
| `code-analyst` | ✅ Keep | Analyzing SQL scripts, ETL pipelines, Python utilities |
| `doc-writer` | ✅ Keep | Maintaining docs/, diccionario MD files, README |
| `code-reviewer` | ✅ Keep | Reviewing SQL queries for safety, Python code quality |
| `test-writer` | ✅ Keep | Testing ETL scripts, db_config.py |
| `db-analyst` | ✅ **Core** | SQL queries, schema analysis, IRIS/SIDRA — primary agent for this project |
| `deployer` | ✅ Keep | Lower direct use but valid for ETL scheduling/automation |
| `researcher` | ✅ Keep | TrakCare/IRIS documentation, clinical coding standards |

#### Claude Skills (11 found — corrected from "0")
- 11 diccionario-* skills in `.claude/skills/` (stats, sync, buscar, export, etc.)
- All project-specific and actively relevant — **no archival needed**

#### Gemini Skills (4 found — corrected from "0")
- `skill_analisis_clinico.md`, `skill_constructor_consultas.md`, `skill_diccionario_buscar.md`, `skill_mapeo_trakcare.md`
- All project-specific and actively relevant — **no archival needed**

#### Claude Agents (3 specialized — beyond manifest)
- `analisis_clinico.agent`, `constructor_consultas.agent`, `mapeo_trakcare.agent`
- All domain-specific to AG_Consultas — **keep**

#### Workflows (2/2 valid)
- `deep-research-update.md` — ✅ Relevant for TrakCare/IRIS knowledge updates
- `turbo-ops.md` — ✅ Universal safe operations, applicable

#### Summary
All assets confirmed relevant. No archival needed. Original task description incorrectly reported 0 skills; actual count is 11 Claude + 4 Gemini.
