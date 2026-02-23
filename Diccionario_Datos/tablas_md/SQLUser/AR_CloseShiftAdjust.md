# SQLUser.AR_CloseShiftAdjust

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADJ_ParRef | bigint | PK |  | NO | AR_CloseShift Parent Reference |
| ADJ_Amount | double |  |  | SI | Amount |
| ADJ_Childsub | double |  |  | NO | Childsub |
| ADJ_Comments | varchar |  |  | SI | Comments |
| ADJ_Date | date |  |  | SI | Date |
| ADJ_Reason_DR | bigint |  | FK | SI | Des Ref Reason |
| ADJ_RowId | varchar |  |  | NO | - |
| ADJ_Time | time |  |  | SI | Time |
| ADJ_ToFromCashierUser_DR | bigint |  | FK | SI | To/From Cashier - Des Ref SSUser |
| ADJ_ToFromShift_DR | bigint |  | FK | SI | To/From Shift - Des Ref ARCloseShift |
| ADJ_UpdateDate | date |  |  | SI | UpdateDate |
| ADJ_UpdateTime | time |  |  | SI | UpdateTime |
| ADJ_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q37Q1 | - |  |  | SI | Nombre y apellidos |
| Q37Q2 | - |  |  | SI | Edad |
| Q37Q3 | - |  |  | SI | Relación de parentesco |
| Q37Q4 | - |  |  | SI | Tipo |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*