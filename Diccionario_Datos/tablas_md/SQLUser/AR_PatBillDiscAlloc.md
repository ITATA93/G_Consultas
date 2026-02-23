# SQLUser.AR_PatBillDiscAlloc

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DSAL_ParRef | bigint | PK |  | NO | AR_PatientBill Parent Reference |
| ChildQ07DR | - |  |  | SI | Child Reference: Dispositivos Vías Aéreas |
| DSAL_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| DSAL_ARPatBillDisc_DR | varchar |  | FK | SI | Des Ref ARPatBillDisc |
| DSAL_Amt | double |  |  | SI | Discount Amount |
| DSAL_BillAmt | double |  |  | SI | Bill Amt |
| DSAL_BillGrp_DR | bigint |  | FK | SI | Des Ref BillGrp |
| DSAL_BillItem_DR | varchar |  | FK | SI | Des Ref BillItem |
| DSAL_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| DSAL_Childsub | double |  |  | NO | Childsub |
| DSAL_Group | varchar |  |  | SI | Group |
| DSAL_Perc | double |  |  | SI | Discount Percentage |
| DSAL_RowId | varchar |  |  | NO | - |
| DSAL_ServiceTaxAmount | double |  |  | SI | Service Tax Amount |
| DSAL_ServiceTaxRate | double |  |  | SI | Service Tax Rate |
| Q06Q1 | - |  |  | SI | Tipo de Dispositivos |
| Q06Q2 | - |  |  | SI | Actividad |
| Q06Q3 | - |  |  | SI | Tamaño |
| Q06Q4 | - |  |  | SI | Ubicación |
| Q06Q5 | - |  |  | SI | N° Días Dispositivo Vías Urinaria |
| Q06Q6 | - |  |  | SI | ¿Es necesario el DI? |
| Q06Q7 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*