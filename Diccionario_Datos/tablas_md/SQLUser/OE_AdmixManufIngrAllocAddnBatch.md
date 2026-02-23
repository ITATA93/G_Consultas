# SQLUser.OE_AdmixManufIngrAllocAddnBatch

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AMIAAB_ParRef | varchar | PK |  | NO | OE_OrdAdmixAllocation Parent Reference |
| AMIAAB_Childsub | double |  |  | NO | Childsub |
| AMIAAB_ExtStkBatchID | varchar |  |  | SI | External Stock BatchID |
| AMIAAB_ExtStkDetails | varchar |  |  | SI | External Stock Details |
| AMIAAB_INCIRN_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| AMIAAB_INCLB_DR | varchar |  | FK | SI | Des Ref INCItmLcBt |
| AMIAAB_Quantity | double |  |  | SI | Quantity |
| AMIAAB_RowId | varchar |  |  | NO | - |
| CQ03 | - |  |  | SI | (null) |
| CQ04 | - |  |  | SI | (null) |
| CQ47 | - |  |  | SI | (null) |
| CQ49 | - |  |  | SI | (null) |
| CQ52 | - |  |  | SI | (null) |
| CQ53 | - |  |  | SI | (null) |
| CQ54 | - |  |  | SI | (null) |
| ChildQ05DR | - |  |  | SI | Child Reference: Evaluation |
| Q01 | - |  |  | SI | Wound Assessment |
| Q02 | - |  |  | SI | Location on body map |
| Q03 | - |  |  | SI | Wound site |
| Q04 | - |  |  | SI | Type of wound |
| Q155 | - |  |  | SI | Evaluation |
| Q156 | - |  |  | SI | Treatment |
| Q157 | - |  |  | SI | Pain Assessment |
| Q17 | - |  |  | SI | Expected date to heal |
| Q18 | - |  |  | SI | Achieved healing date |
| Q20 | - |  |  | SI | Established aetiology within 14 days |
| Q21 | - |  |  | SI | Established aetiology within 14 days date achieved |
| Q22 | - |  |  | SI | Established aetiology within 14 days review date |
| Q23 | - |  |  | SI | Control underlying factors within 14 days |
| Q24 | - |  |  | SI | Control underlying factors within 14 days date ach... |
| Q25 | - |  |  | SI | Control underlying factors within 14 days review d... |
| Q26 | - |  |  | SI | Control pain within 7 days |
| Q27 | - |  |  | SI | Control pain within 7 days date achieved |
| Q28 | - |  |  | SI | Control pain within 7 days review date |
| Q29 | - |  |  | SI | Absence of necrotic tissue within 14 days |
| Q30 | - |  |  | SI | Absence of necrotic tissue within 14 days date ach... |
| Q31 | - |  |  | SI | Absence of necrotic tissue within 14 days review d... |
| Q32 | - |  |  | SI | Absence of clinical infections within 14 days |
| Q33 | - |  |  | SI | Absence of clinical infections within 14 date achi... |
| Q34 | - |  |  | SI | Absence of clinical infections within 14 review da... |
| Q35 | - |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q36 | - |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q37 | - |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q38 | - |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q39 | - |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q40 | - |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q41 | - |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q42 | - |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q43 | - |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q44 | - |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q45 | - |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q46 | - |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q47 | - |  |  | SI | Care plan |
| Q48 | - |  |  | SI | Wound image |
| Q48TxtOnly | - |  |  | SI | Wound image Plain Text Only |
| Q49 | - |  |  | SI | Acquired location |
| Q50 | - |  |  | SI | Comments |
| Q51 | - |  |  | SI | Site Detail |
| Q52 | - |  |  | SI | Laterality |
| Q53 | - |  |  | SI | Orientation |
| Q54 | - |  |  | SI | Type of wound |
| Q55 | - |  |  | SI | Please specify |
| Q56 | - |  |  | SI | Stage of pressure injury |
| Q57 | - |  |  | SI | Packing in situ? |
| Q58 | - |  |  | SI | Number of packs in situ |
| Q59 | - |  |  | SI | Details of packing |
| Q60 | - |  |  | SI | Location on body map (Front / Side) |
| Q61 | - |  |  | SI | Location on body map (Feet) |
| Q64 | - |  |  | SI | Swab taken? |
| Q65 | - |  |  | SI | Date |
| Q66 | - |  |  | SI | Time |
| Q67 | - |  |  | SI | Include patient in hospital - acquired injuries pr... |
| Q68 | - |  |  | SI | Female body map |
| Q69 | - |  |  | SI | Wound site |
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