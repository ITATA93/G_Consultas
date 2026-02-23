# SQLUser.PAC_CommunicationPrefs

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COMMPREFS_RowId | bigint | PK |  | NO | - |
| COMMPREFS_Code | varchar |  |  | NO | Code |
| COMMPREFS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COMMPREFS_CreatedDate | date |  |  | SI | Created Date |
| COMMPREFS_CreatedTime | time |  |  | SI | Created Time |
| COMMPREFS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COMMPREFS_DateFrom | date |  |  | SI | Date From |
| COMMPREFS_DateTo | date |  |  | SI | Date To |
| COMMPREFS_Desc | varchar |  |  | NO | Description |
| COMMPREFS_Owner | varchar |  |  | SI | Owner |
| COMMPREFS_UpdatedDate | date |  |  | SI | Updated Date |
| COMMPREFS_UpdatedTime | time |  |  | SI | Updated Time |
| COMMPREFS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q08Q1 | - |  |  | SI | Time from |
| Q08Q2 | - |  |  | SI | Time to |
| Q08Q3 | - |  |  | SI | Basal insulin infusion rate (units/hr) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*