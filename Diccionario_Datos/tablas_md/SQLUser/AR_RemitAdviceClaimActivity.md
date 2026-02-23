# SQLUser.AR_RemitAdviceClaimActivity

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACT_ParRef | varchar | PK |  | NO | AR_RemittanceAdvice Parent Reference |
| ACT_ActivityClaimStatus_DR | bigint |  | FK | SI | Des Ref to ARCActivityClaimStatus |
| ACT_ActivityCode | varchar |  |  | SI | Activity Code |
| ACT_ActivityID | varchar |  |  | SI | Activity ID |
| ACT_ActivityList | double |  |  | SI | Activity List |
| ACT_Childsub | double |  |  | NO | Childsub |
| ACT_Clinician_DR | varchar |  | FK | SI | Clinician, Des Ref CTCareProv |
| ACT_Date1 | date |  |  | SI | Date1 |
| ACT_Date2 | date |  |  | SI | Date2 |
| ACT_Date3 | date |  |  | SI | Date3 |
| ACT_Date4 | date |  |  | SI | Date4 |
| ACT_Date5 | date |  |  | SI | Date5 |
| ACT_DeniedAmount | double |  |  | SI | Denied Amount |
| ACT_GrossAmount | double |  |  | SI | Gross Amount |
| ACT_ItemMast_DR | varchar |  | FK | SI | Order Item, Des Ref ARCItmMast |
| ACT_NetAmount | double |  |  | SI | Net Amount |
| ACT_Number1 | double |  |  | SI | Number1 |
| ACT_Number2 | double |  |  | SI | Number2 |
| ACT_Number3 | double |  |  | SI | Number3 |
| ACT_Number4 | double |  |  | SI | Number4 |
| ACT_Number5 | double |  |  | SI | Number5 |
| ACT_OrdItem_DR | varchar |  | FK | SI | Des Ref to OEOrdItem |
| ACT_OrderingClinician_DR | varchar |  | FK | SI | Ordering Clinician, Des Ref CTCareProv |
| ACT_OriginalClaimAmount | double |  |  | SI | Original Claim Amount |
| ACT_OverrideItemMast_DR | varchar |  | FK | SI | Override Order Item, Des Ref ARCItmMast |
| ACT_PatBillGroupCharges_DR | varchar |  | FK | SI | Des Ref to ARPatBillGroupCharges |
| ACT_PatientAmount | double |  |  | SI | Patient Amount |
| ACT_PaymentAmount | double |  |  | SI | Payment Amount |
| ACT_PreviousPaymentAmount | double |  |  | SI | Previous Payment Amount |
| ACT_Quantity | double |  |  | SI | Quantity |
| ACT_ReasonActivityDenial_DR | bigint |  | FK | SI | Des Ref to ARCReasonForActivityDenial |
| ACT_RowId | varchar |  |  | NO | - |
| ACT_ServCat_DR | bigint |  | FK | SI | Activity Type, Des Ref ARCServCat |
| ACT_StartDate | date |  |  | SI | Start Date |
| ACT_StartTime | time |  |  | SI | Start Time |
| ACT_Text1 | varchar |  |  | SI | Text1 |
| ACT_Text2 | varchar |  |  | SI | Text2 |
| ACT_Text3 | varchar |  |  | SI | Text3 |
| ACT_Text4 | varchar |  |  | SI | Text4 |
| ACT_Text5 | varchar |  |  | SI | Text5 |
| ACT_VATAmount | double |  |  | SI | VAT Amount |
| ACT_VATPercentage | double |  |  | SI | VAT Percentage |
| ChildQ03DR | - |  |  | SI | Child Reference: Procedimientos |
| Q01 | - |  |  | SI | Fecha Atención |
| Q02 | - |  |  | SI | Hora Atención |
| Q05 | - |  |  | SI | Requiere Donante de Sangre |
| Q06 | - |  |  | SI | Prioridad |
| Q07 | - |  |  | SI | Convenio |
| Q08 | - |  |  | SI | Datos de Hospitalización |
| Q09 | - |  |  | SI | Tipo de Estadía |
| Q10 | - |  |  | SI | Centro |
| Q11 | - |  |  | SI | Fecha Estimada |
| Q12 | - |  |  | SI | Precauciones adicionales |
| Q13 | - |  |  | SI | Complejidad |
| Q14 | - |  |  | SI | UCI |
| Q15 | - |  |  | SI | Intermedio |
| Q16 | - |  |  | SI | Básica |
| Q17 | - |  |  | SI | Otros |
| Q18 | - |  |  | SI | Cirugía Robótica |
| Q19 | - |  |  | SI | Alergias |
| Q20 | - |  |  | SI | Proveedor |
| Q21 | - |  |  | SI | Implantes |
| Q22 | - |  |  | SI | Observaciones |
| Q23 | - |  |  | SI | Anestesia |
| Q24 | - |  |  | SI | Para el Paciente |
| Q25 | - |  |  | SI | Sobre Materiales Especiales - Rayos, etc. |
| Q26 | - |  |  | SI | Para Presupuestos |
| Q27 | - |  |  | SI | Profesional Clínico |
| Q28 | - |  |  | SI | Fecha Acordada |
| Q29 | - |  |  | SI | Fecha Desde |
| Q30 | - |  |  | SI | Fecha Hasta |
| Q31 | - |  |  | SI | Observacion General |
| Q32 | - |  |  | SI | Identificación del Paciente |
| Q33 | - |  |  | SI | Número |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*