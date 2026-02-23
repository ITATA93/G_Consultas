# SQLUser.PAC_PrevSpecialTreatment

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PST_RowId | bigint | PK |  | NO | - |
| ChildQ18DR | - |  |  | SI | Child Reference: Cannulation |
| PST_Code | varchar |  |  | NO | Code |
| PST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PST_CreatedDate | date |  |  | SI | Created Date |
| PST_CreatedTime | time |  |  | SI | Created Time |
| PST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PST_DateFrom | date |  |  | SI | Date From |
| PST_DateTo | date |  |  | SI | Date To |
| PST_Desc | varchar |  |  | NO | Description |
| PST_Owner | varchar |  |  | SI | Owner |
| PST_UpdatedDate | date |  |  | SI | Updated Date |
| PST_UpdatedTime | time |  |  | SI | Updated Time |
| PST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q11Q1 | - |  |  | SI | Wound   site 	 |
| Q11Q2 | - |  |  | SI | Body Site	 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*