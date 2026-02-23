# SQLUser.PAC_ReferralPathSuggestion

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFSUG_RowId | bigint | PK |  | NO | - |
| Q40Q1 | - |  |  | SI | Food given |
| Q40Q2 | - |  |  | SI | Reaction |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFSUG_Code | varchar |  |  | NO | Code |
| REFSUG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFSUG_CreatedDate | date |  |  | SI | Created Date |
| REFSUG_CreatedTime | time |  |  | SI | Created Time |
| REFSUG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFSUG_DateFrom | date |  |  | SI | Date From |
| REFSUG_DateTo | date |  |  | SI | Date To |
| REFSUG_Desc | varchar |  |  | NO | Description |
| REFSUG_FirstAccess | varchar |  |  | SI | First Access |
| REFSUG_Owner | varchar |  |  | SI | Owner |
| REFSUG_Subregion_DR | bigint |  | FK | SI | Subregion  |
| REFSUG_UpdatedDate | date |  |  | SI | Updated Date |
| REFSUG_UpdatedTime | time |  |  | SI | Updated Time |
| REFSUG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*