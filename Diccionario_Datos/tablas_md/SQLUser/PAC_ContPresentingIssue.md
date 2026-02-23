# SQLUser.PAC_ContPresentingIssue

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRESISS_RowId | bigint | PK |  | NO | - |
| ChildQ68DR | - |  |  | SI | Child Reference: Arterial Line Status	 |
| PRESISS_Code | varchar |  |  | NO | Code |
| PRESISS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRESISS_CreatedDate | date |  |  | SI | Created Date |
| PRESISS_CreatedTime | time |  |  | SI | Created Time |
| PRESISS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRESISS_DateFrom | date |  |  | SI | Date From |
| PRESISS_DateTo | date |  |  | SI | Date To |
| PRESISS_Desc | varchar |  |  | NO | Description |
| PRESISS_Owner | varchar |  |  | SI | Owner |
| PRESISS_UpdatedDate | date |  |  | SI | Updated Date |
| PRESISS_UpdatedTime | time |  |  | SI | Updated Time |
| PRESISS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q49Q1 | - |  |  | SI | Intervention |
| Q49Q2 | - |  |  | SI | Response	 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*