# SQLUser.PAC_QuestionAnswer

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QANS_RowId | bigint | PK |  | NO | - |
| QANS_Code | varchar |  |  | NO | Code |
| QANS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QANS_CreatedDate | date |  |  | SI | Created Date |
| QANS_CreatedTime | time |  |  | SI | Created Time |
| QANS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QANS_DateFrom | date |  |  | SI | Date From |
| QANS_DateTo | date |  |  | SI | Date To |
| QANS_Desc | varchar |  |  | NO | Description |
| QANS_Owner | varchar |  |  | SI | Owner |
| QANS_UpdatedDate | date |  |  | SI | Updated Date |
| QANS_UpdatedTime | time |  |  | SI | Updated Time |
| QANS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*