# SQLUser.PAC_ContServiceProvided

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SERPROV_RowId | bigint | PK |  | NO | - |
| Q96Q1 | - |  |  | SI | Need Assessment	 |
| Q96Q2 | - |  |  | SI | Care |
| Q96Q3 | - |  |  | SI | Site Details	 |
| Q96Q4 | - |  |  | SI | Dressing Type / Appearance	 |
| Q96Q5 | - |  |  | SI | Peripheral IV Patency	 |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SERPROV_Code | varchar |  |  | NO | Code |
| SERPROV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SERPROV_CreatedDate | date |  |  | SI | Created Date |
| SERPROV_CreatedTime | time |  |  | SI | Created Time |
| SERPROV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SERPROV_DateFrom | date |  |  | SI | Date From |
| SERPROV_DateTo | date |  |  | SI | Date To |
| SERPROV_Desc | varchar |  |  | NO | Description |
| SERPROV_Owner | varchar |  |  | SI | Owner |
| SERPROV_UpdatedDate | date |  |  | SI | Updated Date |
| SERPROV_UpdatedTime | time |  |  | SI | Updated Time |
| SERPROV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*