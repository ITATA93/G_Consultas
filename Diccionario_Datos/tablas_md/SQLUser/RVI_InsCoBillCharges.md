# SQLUser.RVI_InsCoBillCharges

**Schema:** SQLUser
**Columnas:** 38
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | RVI_InsCompanyBill Parent Reference |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des REf to ARCIM |
| ITM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ITM_AnaestDuration | double |  |  | SI | Anaest Duration |
| ITM_BillSub_DR | varchar |  | FK | SI | Des Ref BillSubGr |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CutDays | double |  |  | SI | Cut Days |
| ITM_CutQty | double |  |  | SI | Cut Qty |
| ITM_DailyQty | double |  |  | SI | Daily Qty |
| ITM_Date | date |  |  | SI | Order Date |
| ITM_DayNight | varchar |  |  | SI | Day-Night |
| ITM_Doctor_DR | varchar |  | FK | SI | Des Ref Doctor |
| ITM_HandiShare | double |  |  | SI | Handicapped Association Share |
| ITM_InsAssocAnalisysCode | varchar |  |  | SI | Ins Assoc Analisys Code |
| ITM_InsCompanyShare | double |  |  | SI | Insurance Company Share |
| ITM_InsCoverStatus_DR | bigint |  | FK | SI | Insurance Cover Status |
| ITM_InsureStatus | varchar |  |  | SI | Insure Status |
| ITM_LineTotal | double |  |  | SI | Line Total |
| ITM_LocalGovtShare | double |  |  | SI | Local Govt Share |
| ITM_MaterialTotal | double |  |  | SI | Material Total |
| ITM_NFMIDepart_DR | varchar |  | FK | SI | Des Ref to NFMI Department |
| ITM_NoTimes | double |  |  | SI | No of Times |
| ITM_OccurrenceFlag | varchar |  |  | SI | Occurrence Flag |
| ITM_OintmentTreatDays | double |  |  | SI | Ointment Treat Days |
| ITM_OrdItem_DR | varchar |  | FK | SI | Des REf OrdItem |
| ITM_OrderTime | time |  |  | SI | Order Time |
| ITM_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ITM_PatInsFlag | varchar |  |  | SI | Patient Insurance Flag |
| ITM_PatientShare | double |  |  | SI | Patient Share |
| ITM_ReasonForChange_DR | bigint |  | FK | SI | Des Ref to RVCReasonForChange |
| ITM_ReasonForCut_DR | bigint |  | FK | SI | Des Ref ReasonForCut |
| ITM_ReclaimAmt | double |  |  | SI | Reclaim Amt |
| ITM_ReviewModified | varchar |  |  | SI | Review Modified |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_ServiceMaterial | varchar |  |  | SI | Service/Material |
| ITM_ServiceTotal | double |  |  | SI | Service Total |
| ITM_SpecialistSurcharge | double |  |  | SI | Specialist Surcharge |
| ITM_UnitPrice | double |  |  | SI | Unit Price |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*