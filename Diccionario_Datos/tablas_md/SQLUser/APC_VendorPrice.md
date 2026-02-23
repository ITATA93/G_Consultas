# SQLUser.APC_VendorPrice

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Pagar (AP)**. Gestión de proveedores y compras.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APCVP_ParRef | bigint | PK |  | NO | APC_Vendor Parent Reference |
| APCVP_Childsub | double |  |  | NO | Childsub |
| APCVP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APCVP_CreatedDate | date |  |  | SI | Created Date |
| APCVP_CreatedTime | time |  |  | SI | Created Time |
| APCVP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APCVP_DateFrom | date |  |  | NO | Date From |
| APCVP_DateTo | date |  |  | SI | Date To |
| APCVP_MinPOValue | double |  |  | NO | Vendor Minimum Purchase Order Price Value |
| APCVP_RowId | varchar |  |  | NO | - |
| APCVP_UpdatedDate | date |  |  | SI | Updated Date |
| APCVP_UpdatedTime | time |  |  | SI | Updated Time |
| APCVP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q54Q1 | - |  |  | SI | Tipo Examen |
| Q54Q2 | - |  |  | SI | Fecha |
| Q54Q3 | - |  |  | SI | Resultado |
| Q54Q4 | - |  |  | SI | Laboratorio |
| Q54Q5 | - |  |  | SI | Región |
| Q54Q6 | - |  |  | SI | País |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*