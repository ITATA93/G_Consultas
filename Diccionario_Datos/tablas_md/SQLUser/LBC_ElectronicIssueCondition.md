# SQLUser.LBC_ElectronicIssueCondition

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCEIC_RowID | bigint | PK |  | NO | - |
| LBCEIC_Active | varchar |  |  | SI | Active
Will be overwritten by LBCEICAlwaysActive |
| LBCEIC_AlwaysActive | bit |  |  | SI | Always Active
Cannot be set via the UI |
| LBCEIC_Caption | varchar |  |  | SI | Caption |
| LBCEIC_Code | varchar |  |  | NO | Code |
| LBCEIC_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCEIC_CreatedDate | date |  |  | SI | Created Date |
| LBCEIC_CreatedTime | time |  |  | SI | Created Time |
| LBCEIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCEIC_Desc | varchar |  |  | NO | Description |
| LBCEIC_Duration | integer |  |  | SI | Duration
In days |
| LBCEIC_DurationEnabled | bit |  |  | SI | Duration Enabled
Cannot be set via the UI |
| LBCEIC_IsCondition | bit |  |  | SI | Is a condition to be considered in the EI calculat... |
| LBCEIC_Sequence | numeric |  |  | SI | Display sequence |
| LBCEIC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCEIC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCEIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q09Q1 | - |  |  | SI | Name |
| Q09Q2 | - |  |  | SI | Relationship |
| Q09Q3 | - |  |  | SI | Address |
| Q09Q4 | - |  |  | SI | Phone |
| Q09Q5 | - |  |  | SI | Permission to take patient on ward leave |
| Q09Q6 | - |  |  | SI | Permission to take patient within hospital campus |
| Q09Q7 | - |  |  | SI | Requires supervised visit |
| Q09Q8 | - |  |  | SI | Dummy1 |
| Q09Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*