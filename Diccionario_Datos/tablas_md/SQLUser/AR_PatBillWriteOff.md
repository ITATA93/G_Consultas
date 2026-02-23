# SQLUser.AR_PatBillWriteOff

**Schema:** SQLUser
**Columnas:** 35
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WO_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| Q04Q1 | - |  |  | SI | Farmaco |
| Q04Q2 | - |  |  | SI | Vía Administración (Oral, IM, EV, Otra No Especifi... |
| Q04Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WO_AccountingPeriod_DR | bigint |  | FK | SI | Des Ref AccountingPeriod |
| WO_Active | varchar |  |  | SI | Active |
| WO_Amount | double |  |  | SI | Amount |
| WO_AuxInsType | varchar |  |  | SI | AuxInsType |
| WO_ChequeNumber | varchar |  |  | SI | Cheque Number |
| WO_Childsub | double |  |  | NO | Childsub |
| WO_Comments | varchar |  |  | SI | Comments |
| WO_Date | date |  |  | SI | Date |
| WO_DeActivateAccountingPeriod_DR | bigint |  | FK | SI | Des Ref De-Activate AccountingPeriod |
| WO_DeActivateDate | date |  |  | SI | De-Activate Date |
| WO_DeActivateGLBatch_DR | bigint |  | FK | SI | Des Ref De-Activate GL Batch |
| WO_DeActivateGLPostFlag | varchar |  |  | SI | De-Activate GL Post Flag |
| WO_DeActivateHospital_DR | bigint |  | FK | SI | Des Ref De-Activate Hospital |
| WO_DeActivateTime | time |  |  | SI | De-Activate Time |
| WO_DeActivateUser_DR | bigint |  | FK | SI | Des Ref De-Activate User |
| WO_GLBatch_DR | bigint |  | FK | SI | Des Ref GLBatch |
| WO_GLPostFlag | varchar |  |  | SI | GLPostFlag |
| WO_InactiveAccountingPeriod_DR | bigint |  | FK | SI | Des Ref Inactive AccountingPeriod |
| WO_InactiveGLBatch_DR | bigint |  | FK | SI | Des Ref Inactive GL Batch |
| WO_InactiveGLPostFlag | varchar |  |  | SI | Inactive GL Post Flag |
| WO_ReasonWO_DR | bigint |  | FK | SI | Des Ref Reason |
| WO_RowId | varchar |  |  | NO | - |
| WO_ServTaxAmount | double |  |  | SI | Service Tax Amount |
| WO_ServTax_DR | bigint |  | FK | SI | Des Ref ServTax |
| WO_Time | time |  |  | SI | Time |
| WO_TransferPatBill | varchar |  |  | SI | Transfer to Pat Bill |
| WO_UpdateDate | date |  |  | SI | Update Date |
| WO_UpdateTime | time |  |  | SI | Update Time |
| WO_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| WO_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*