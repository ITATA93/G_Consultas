# SQLUser.SS_UserCashier

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CASS_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| CASS_BankRefNumber | varchar |  |  | SI | Bank Reference Number |
| CASS_BatchRefNumber | varchar |  |  | SI | Batch Reference Number |
| CASS_Cashier_DR | bigint |  | FK | SI | Des Ref SSUser |
| CASS_Childsub | double |  |  | NO | Childsub |
| CASS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CASS_CreatedDate | date |  |  | SI | Created Date |
| CASS_CreatedTime | time |  |  | SI | Created Time |
| CASS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CASS_DateFrom | date |  |  | SI | Date From |
| CASS_DateTo | date |  |  | SI | Date To |
| CASS_RowId | varchar |  |  | NO | - |
| CASS_UpdatedDate | date |  |  | SI | Updated Date |
| CASS_UpdatedTime | time |  |  | SI | Updated Time |
| CASS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*