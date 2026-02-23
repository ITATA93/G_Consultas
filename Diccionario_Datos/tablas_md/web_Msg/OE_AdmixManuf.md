# web_Msg.OE_AdmixManuf

**Schema:** web_Msg
**Columnas:** 37
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| MANUF_AdditionalCost | double |  |  | SI | Additional Cost |
| MANUF_Batch | varchar |  |  | SI | Batch |
| MANUF_Childsub | double |  |  | SI | Childsub |
| MANUF_CompletedDate | date |  |  | SI | UpdateDate |
| MANUF_CompletedTime | time |  |  | SI | UpdateTime |
| MANUF_CompletedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| MANUF_ExpiryDate | date |  |  | SI | ExpiryDate |
| MANUF_ExpiryTime | time |  |  | SI | ExpiryTime |
| MANUF_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| MANUF_ManufacturedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| MANUF_NurseManufacturedSolventVolumeBeforeMixing | double |  |  | SI | Nurse Manufactured Solvent Volume Before Mixing |
| MANUF_NurseManufacturedVolume | double |  |  | SI | Nurse Manufactured Volume |
| MANUF_OEOrdExec_DR | varchar |  | FK | SI | Des Ref OEOrdExec |
| MANUF_OrderDate | date |  |  | SI | OrderDate |
| MANUF_ParRef | bigint |  |  | SI | OE_OrdAdmix Parent Reference
Required by User.OEA... |
| MANUF_PartialStatus | varchar |  |  | SI | PartialStatus |
| MANUF_Quantity | double |  |  | SI | Quantity |
| MANUF_ReasManufAbort_DR | bigint |  | FK | SI | Des Ref ReasonManufactureAbort |
| MANUF_ReassignedFrom_DR | varchar |  | FK | SI | Reassigned From |
| MANUF_RecomDilOverReas_DR | bigint |  | FK | SI | des Ref OECRecommendedDilOverReason |
| MANUF_RowId | varchar |  |  | SI | - |
| MANUF_StartedDate | date |  |  | SI | StartedDate |
| MANUF_StartedTime | time |  |  | SI | UpdateTime |
| MANUF_StartedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| MANUF_ToBeReassigned | varchar |  |  | SI | To Be Reassigned |
| MANUF_TransactionNo | varchar |  |  | SI | MANUFTransactionNo |
| MANUF_UpdateDate | date |  |  | SI | UpdateDate |
| MANUF_UpdateHospital_DR | bigint |  | FK | SI | des Ref CTHospital |
| MANUF_UpdateTime | time |  |  | SI | UpdateTime |
| MANUF_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| MANUF_UserDefinedExpiry | varchar |  |  | SI | User Defined Expiry |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*