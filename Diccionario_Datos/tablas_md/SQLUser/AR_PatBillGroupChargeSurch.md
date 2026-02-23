# SQLUser.AR_PatBillGroupChargeSurch

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUR_ParRef | varchar | PK |  | NO | AR_PatBillGroupCharges Parent Reference |
| Q12Q1 | - |  |  | SI | Tipo Dispositivo |
| Q12Q2 | - |  |  | SI | Sistema de Drenaje |
| Q12Q3 | - |  |  | SI | Actividad |
| Q12Q4 | - |  |  | SI | Estado |
| Q12Q5 | - |  |  | SI | Contenido Drenado |
| Q12Q6 | - |  |  | SI | N° Días de Dispositivo |
| Q12Q7 | - |  |  | SI | ¿Es necesario el DI? |
| Q12Q8 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SUR_Childsub | double |  |  | NO | Childsub |
| SUR_Desc | varchar |  |  | SI | Description |
| SUR_GovtShare | double |  |  | SI | Govt Share |
| SUR_HandicappedAssocShare | double |  |  | SI | Handicapped Assoc Share |
| SUR_InsCoShare | double |  |  | SI | Ins Co Share |
| SUR_NoDays | double |  |  | SI | No of Days |
| SUR_PatientShare | double |  |  | SI | Patient Share |
| SUR_QtyDay | double |  |  | SI | Qty/Day |
| SUR_RowId | varchar |  |  | NO | - |
| SUR_SurchDiscountType | double |  |  | SI | Surcharge Discount Type |
| SUR_Surcharge_DR | bigint |  | FK | SI | Des Ref to Surcharge Code |
| SUR_TotalAmt | double |  |  | SI | Total Amt |
| SUR_UnitPrice | double |  |  | SI | Unit Price |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*