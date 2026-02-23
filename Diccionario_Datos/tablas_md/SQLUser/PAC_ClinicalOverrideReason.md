# SQLUser.PAC_ClinicalOverrideReason

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COR_RowId | bigint | PK |  | NO | - |
| COR_Code | varchar |  |  | NO | Code |
| COR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COR_CreatedDate | date |  |  | SI | Created Date |
| COR_CreatedTime | time |  |  | SI | Created Time |
| COR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COR_DateFrom | date |  |  | SI | Date From |
| COR_DateTo | date |  |  | SI | Date To |
| COR_Desc | varchar |  |  | NO | Description |
| COR_Owner | varchar |  |  | SI | Owner |
| COR_UpdatedDate | date |  |  | SI | Updated Date |
| COR_UpdatedTime | time |  |  | SI | Updated Time |
| COR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ10DR | - |  |  | SI | Child Reference: Insulin sensitivity factor |
| Q09Q1 | - |  |  | SI | Time from |
| Q09Q2 | - |  |  | SI | Time to |
| Q09Q3 | - |  |  | SI | Insulin to carbohydrate ratio |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*