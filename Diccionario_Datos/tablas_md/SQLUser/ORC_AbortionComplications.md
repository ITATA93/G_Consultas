# SQLUser.ORC_AbortionComplications

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ABOCOM_RowId | bigint | PK |  | NO | - |
| ABOCOM_AbortionEdit | varchar |  |  | SI | Abortion Edit  |
| ABOCOM_Code | varchar |  |  | NO | Code |
| ABOCOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ABOCOM_CreatedDate | date |  |  | SI | Created Date |
| ABOCOM_CreatedTime | time |  |  | SI | Created Time |
| ABOCOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ABOCOM_DateFrom | date |  |  | SI | Date From |
| ABOCOM_DateTo | date |  |  | SI | Date To |
| ABOCOM_Desc | varchar |  |  | NO | Description |
| ABOCOM_Owner | varchar |  |  | SI | Owner |
| ABOCOM_PregnancyDeliveryEdit | varchar |  |  | SI | Pregnancy Delivery Edit  |
| ABOCOM_UpdatedDate | date |  |  | SI | Updated Date |
| ABOCOM_UpdatedTime | time |  |  | SI | Updated Time |
| ABOCOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ50DR | - |  |  | SI | Child Reference: Special Test 4 ( + or - ) |
| Q49Q1 | - |  |  | SI | Impingement |
| Q49Q2 | - |  |  | SI | Left |
| Q49Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*