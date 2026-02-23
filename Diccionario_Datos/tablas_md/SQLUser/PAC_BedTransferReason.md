# SQLUser.PAC_BedTransferReason

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BTR_RowId | bigint | PK |  | NO | - |
| BTR_ClinicalReason | varchar |  |  | SI | Clinical Reason |
| BTR_Code | varchar |  |  | NO | Transfer Code |
| BTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BTR_CreatedDate | date |  |  | SI | Created Date |
| BTR_CreatedTime | time |  |  | SI | Created Time |
| BTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BTR_Desc | varchar |  |  | NO | Transfer Description |
| BTR_Owner | varchar |  |  | SI | Owner |
| BTR_RcFlag | varchar |  |  | SI | Archived Flag |
| BTR_TransferRemark | varchar |  |  | SI | Transfer Remark |
| BTR_UpdatedDate | date |  |  | SI | Updated Date |
| BTR_UpdatedTime | time |  |  | SI | Updated Time |
| BTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q27Q1 | - |  |  | SI | Date melioidosis titre completed |
| Q27Q2 | - |  |  | SI | Titre |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*