# SQLUser.SS_GroupUDWGroup

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESRR_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| RESRR_Childsub | double |  |  | NO | Childsub |
| RESRR_QuestAdmRestrict | varchar |  |  | SI | QuestAdmRestrict |
| RESRR_QuestReadOnly | varchar |  |  | SI | QuestReadOnly |
| RESRR_RowId | varchar |  |  | NO | - |
| RESRR_UDWAdminAccess | varchar |  |  | SI | Has Access to Edit a Questionnaire Code Table (SSU... |
| RESRR_UDWGroup_DR | bigint |  | FK | SI | Des Ref UDW Group |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*