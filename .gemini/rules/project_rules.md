---
description: Project Rules for TrakCare/ALMA Data Mapping and Query System
---

# Project Rules: TrakCare/ALMA Data Mapping

## 🔒 Security Policy (CRITICAL)

**All database operations must adhere to STRICT READ-ONLY protocols.**

1.  **NO WRITES**: `UPDATE`, `DELETE`, `INSERT`, `TRUNCATE`, and `DROP` commands are **ABSOLUTELY FORBIDDEN**.
2.  **MANDATORY LIMITS**: Every `SELECT` statement **MUST** include `TOP {N}` (e.g., `TOP 100`).
    *   Default Limit: 100
    *   Hard Maximum: 1000
3.  **TIMEOUT**: Queries must not exceed 30 seconds execution time.
4.  **LARGE TABLES**: `WHERE` clauses are **MANDATORY** when querying core tables (e.g., `PA_Adm`, `OE_Order`) to prevent scan overflows.

## 🏗️ Project Structure & Conventions

### Database Context
*   **Platform**: InterSystems IRIS
*   **Namespace**: `LIVE-CLOV`
*   **Schema**: `SQLUser` (Default)

### Naming Standards
*   **Foreign Keys**: Suffix `_DR` (e.g., `PAADM_PAPMI_DR`)
*   **Primary Keys**: Suffix `_RowId`
*   **Parent Refs**: Suffix `_ParRef`

### Table Prefixes
*   `PA_`: Patient Administration (Admisión, Pacientes)
*   `MR_`: Medical Records (Registro Clínico)
*   `OE_`: Order Entry (Órdenes)
*   `CT_`: Code Tables (Configuración)
*   `ARC_`: Accounts Receivable (Facturación)

## 🤖 Agent Roles & Responsibilities

When acting as an agent, adopt the persona relevant to the current subtask:

*   **Mapper**: Analyze schema, explain relations. (See: `skill_mapeo_trakcare`)
*   **Query Builder**: Write safe, efficient SQL. (See: `skill_constructor_consultas`)
*   **Clinical Analyst**: Translate medical needs to technical specs. (See: `skill_analisis_clinico`)

## 🛠️ Workflows

1.  **Always Check Dictionary First**: Before guessing a table name, use `skill_diccionario_buscar`.
2.  **Verify Safety**: Before presenting ANY SQL to the user, validate it against the Security Policy.
3.  **Document**: Add headers to SQL files explaining purpose, author, and limitations.
