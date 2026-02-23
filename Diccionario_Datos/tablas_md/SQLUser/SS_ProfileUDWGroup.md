# SQLUser.SS_ProfileUDWGroup

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| UDW_ParRef | bigint | PK |  | NO | Parent table |
| UDW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| UDW_QuestAdmRestrict | varchar |  |  | SI | Questionnaire Restricted to Episode |
| UDW_QuestApptOnly | varchar |  |  | SI | Questionnaire Applied to Appointment Only |
| UDW_QuestReadOnly | varchar |  |  | SI | Questionnaire Read Only |
| UDW_RowID | varchar |  |  | NO | - |
| UDW_UDWAdminAccess | varchar |  |  | SI | Has Access to Edit a Questionnaire Code Table (SSU... |
| UDW_UDWGroup_DR | bigint |  | FK | SI | UDW Group |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*