# SQLUser.PAC_CordInsertion

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLCINSRT_RowId | bigint | PK |  | NO | - |
| PLCINSRT_Active | varchar |  |  | SI | Active |
| PLCINSRT_Code | varchar |  |  | NO | Code |
| PLCINSRT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLCINSRT_CreatedDate | date |  |  | SI | Created Date |
| PLCINSRT_CreatedTime | time |  |  | SI | Created Time |
| PLCINSRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLCINSRT_DateFrom | date |  |  | SI | Date From |
| PLCINSRT_DateTo | date |  |  | SI | Date To |
| PLCINSRT_Desc | varchar |  |  | NO | Description |
| PLCINSRT_NationalCode | varchar |  |  | SI | National code |
| PLCINSRT_Owner | varchar |  |  | SI | Owner |
| PLCINSRT_UpdatedDate | date |  |  | SI | Updated Date |
| PLCINSRT_UpdatedTime | time |  |  | SI | Updated Time |
| PLCINSRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q21AQ1 | - |  |  | SI | Clomid no of cycles |
| Q21AQ2 | - |  |  | SI | HMG no of cycles |
| Q21AQ3 | - |  |  | SI | Clomid ovulation |
| Q21AQ4 | - |  |  | SI | Clomid pregnancy |
| Q21AQ5 | - |  |  | SI | HMG ovulation |
| Q21AQ6 | - |  |  | SI | Gonadotrophin pregnancy |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*