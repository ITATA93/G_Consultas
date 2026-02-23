# web_Msg.AR_BillingItem

**Schema:** web_Msg
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ARBI_BillItem_DR | bigint |  | FK | SI | Billing Item
Required by User.ARBillingItem. |
| ARBI_BillRule_DR | varchar |  | FK | SI | Billing Rule |
| ARBI_ConeRule_DR | varchar |  | FK | SI | Coning Rule |
| ARBI_DateOfService | date |  |  | SI | Date of Service |
| ARBI_Initiation_DR | bigint |  | FK | SI | Initiation Code |
| ARBI_LabEpisode_DR | bigint |  | FK | SI | LBEpisode Reference |
| ARBI_LocLabBilling_DR | varchar |  | FK | SI | Location Lab Billing |
| ARBI_MasterLabEpisode_DR | bigint |  | FK | SI | Master Lab Episode
The Patient details are based ... |
| ARBI_OrdItem_DR | varchar |  | FK | SI | OrderItem Reference |
| ARBI_PAAdm_DR | bigint |  | FK | SI | Admission
PAAdm (Admission Episode) |
| ARBI_PAPerson_DR | bigint |  | FK | SI | Patient
PAPerson (Patient) (User.PAPerson)  |
| ARBI_PaymentAgreement_DR | bigint |  | FK | SI | Payment Agreement |
| ARBI_Price | double |  |  | SI | Price |
| ARBI_RowID | varchar |  |  | SI | - |
| ARBI_ScheduleTariffBillingItem_DR | varchar |  | FK | SI | Schedule Tarif Billing Item |
| ARBI_ScheduleTariff_DR | varchar |  | FK | SI | Billing Schedule Tariff |
| ARBI_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container |
| ARBI_Status | varchar |  |  | SI | Billing Item Status |
| ARBI_TestSet_DR | bigint |  | FK | SI | Test Set |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*