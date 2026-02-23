# SQLUser.AR_BatchComm

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BCMT_ParRef | bigint | PK |  | NO | AR_Batch Parent Reference |
| BCMT_ARPBL_DR | bigint |  | FK | SI | Des Ref ARPBL - Not Used |
| BCMT_BatchStatus | varchar |  |  | SI | Batch Status At the time comment was entered. |
| BCMT_Childsub | double |  |  | NO | Childsub |
| BCMT_Comments | varchar |  |  | SI | Comments |
| BCMT_Date | date |  |  | SI | Date |
| BCMT_FutureDate | date |  |  | SI | Future Date |
| BCMT_LastUpdateDate | date |  |  | SI | LastUpateDate |
| BCMT_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| BCMT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| BCMT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| BCMT_OnHold | varchar |  |  | SI | OnHold |
| BCMT_RowId | varchar |  |  | NO | - |
| BCMT_ShortDesc | varchar |  |  | SI | Short Description |
| BCMT_Time | time |  |  | SI | Time |
| BCMT_User_DR | bigint |  | FK | SI | Des Ref User |
| Q25Q1 | - |  |  | SI | Nombre |
| Q25Q2 | - |  |  | SI | Edad (Aprox.) |
| Q25Q3 | - |  |  | SI | Domicilio |
| Q25Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*