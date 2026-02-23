# questionnaire.QTCANGREP

> Angiogram Report

**Schema:** questionnaire
**Columnas:** 160
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Angiogram Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Weight (kgs) |
| Q01ObsDR | varchar |  | FK | SI | Weight (kgs) DR |
| Q02 | varchar |  |  | SI | Height (cm) |
| Q02ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q03 | varchar |  |  | SI | Risk Factors |
| Q04 | varchar |  |  | SI | Clinical Details |
| Q05 | varchar |  |  | SI | Current Medication |
| Q06 | varchar |  |  | SI | Consultant |
| Q07 | date |  |  | SI | Date of Investigation |
| Q08 | varchar |  |  | SI | 1st Operator |
| Q09 | varchar |  |  | SI | 2nd Operator |
| Q10 | varchar |  |  | SI | Procedure |
| Q11 | varchar |  |  | SI | Radiographers |
| Q12 | varchar |  |  | SI | Catheterisation |
| Q13 | varchar |  |  | SI | Site |
| Q14 | varchar |  |  | SI | Phasic |
| Q15 | varchar |  |  | SI | Mean |
| Q16 | numeric |  |  | SI | Left Ventricle |
| Q17 | varchar |  |  | SI | Catheters used |
| Q18 | varchar |  |  | SI | Oxygen Saturation |
| Q19 | varchar |  |  | SI | Mid RA |
| Q20 | varchar |  |  | SI | Low RA |
| Q21 | varchar |  |  | SI | IVC |
| Q22 | varchar |  |  | SI | IRV Outflow |
| Q23 | varchar |  |  | SI | RVTV |
| Q24 | varchar |  |  | SI | RPA |
| Q25 | varchar |  |  | SI | LPA |
| Q26 | varchar |  |  | SI | Mixed |
| Q27 | varchar |  |  | SI | LV |
| Q28 | varchar |  |  | SI | AO |
| Q29 | varchar |  |  | SI | LA |
| Q30 | varchar |  |  | SI | PV |
| Q31 | varchar |  |  | SI | Medication used or prescribed during procedure |
| Q32 | varchar |  |  | SI | Arterial Access 1 |
| Q33 | varchar |  |  | SI | Arterial Access 2 |
| Q34 | varchar |  |  | SI | Arterial Access 3 |
| Q35 | varchar |  |  | SI | Venous Access 1 |
| Q36 | varchar |  |  | SI | Venous Access 2 |
| Q37 | varchar |  |  | SI | Venous Access 3 |
| Q38 | varchar |  |  | SI | Access Problems |
| Q39 | varchar |  |  | SI | Contrast Medium |
| Q40 | numeric |  |  | SI | Contrast Medium (ml) |
| Q41 | numeric |  |  | SI | Procedure Time (min) |
| Q42 | numeric |  |  | SI | Screening Time |
| Q43 | bigint |  |  | SI | Angiographic Findings |
| Q43TxtOnly | bigint |  |  | SI | Angiographic Findings Plain Text Only |
| Q44 | varchar |  |  | SI | Further Management and advice to GP |
| Q45 | varchar |  |  | SI | Reported by  |
| Q46 | numeric |  |  | SI | Left Ventricle |
| Q47 | numeric |  |  | SI | Left Ventricle M |
| Q48 | numeric |  |  | SI | End Diastolic (mmHg) |
| Q49 | numeric |  |  | SI | End Diastolic (mmHg) M |
| Q50 | numeric |  |  | SI | Aorta |
| Q51 | numeric |  |  | SI | Pulmonary Artery |
| Q52 | numeric |  |  | SI | Pulmonary Artery M |
| Q53 | numeric |  |  | SI | Right ventricle |
| Q54 | numeric |  |  | SI | Right ventricle M |
| Q55 | numeric |  |  | SI | Right Atrium |
| Q56 | numeric |  |  | SI | Right Atrium M |
| Q57 | numeric |  |  | SI | PA Wedge |
| Q58 | numeric |  |  | SI | PA Wedge M |
| Q59 | numeric |  |  | SI | Left Atrium |
| Q60 | numeric |  |  | SI | Left Atrium M |
| Q61 | numeric |  |  | SI | CO 1 |
| Q62 | numeric |  |  | SI | CO 2 |
| Q63 | numeric |  |  | SI | Heart Rate |
| Q64 | numeric |  |  | SI | AV Gradient |
| Q65 | numeric |  |  | SI | MV Gradient |
| Q66 | varchar |  |  | SI | Notes |
| Q67 | date |  |  | SI | Report Date |
| Q68 | varchar |  |  | SI | Other Procedure |
| Q69 | varchar |  |  | SI | Prox RCA |
| Q69ObsDR | varchar |  | FK | SI | Prox RCA DR |
| Q70 | varchar |  |  | SI | Segment |
| Q71 | varchar |  |  | SI | Stenosis |
| Q72 | varchar |  |  | SI | Lesion Type |
| Q73 | varchar |  |  | SI | TIMI Flow |
| Q74 | varchar |  |  | SI | Mid RCA |
| Q74ObsDR | varchar |  | FK | SI | Mid RCA DR |
| Q75 | varchar |  |  | SI | RPL1 (small) |
| Q75ObsDR | varchar |  | FK | SI | RPL1 (small) DR |
| Q76 | varchar |  |  | SI | RPL2 (small) |
| Q76ObsDR | varchar |  | FK | SI | RPL2 (small) DR |
| Q77 | varchar |  |  | SI | Mid LAD |
| Q77ObsDR | varchar |  | FK | SI | Mid LAD DR |
| Q78 | varchar |  |  | SI | Dist LAD |
| Q78ObsDR | varchar |  | FK | SI | Dist LAD DR |
| Q79 | varchar |  |  | SI | Left Main |
| Q79ObsDR | varchar |  | FK | SI | Left Main DR |
| Q80 | varchar |  |  | SI | Left Circumflex |
| Q80ObsDR | varchar |  | FK | SI | Left Circumflex DR |
| Q81 | varchar |  |  | SI | Coronary Anatomy |
| Q82 | varchar |  |  | SI | Dominance |
| Q83 | varchar |  |  | SI | Lesion Prox |
| Q84 | varchar |  |  | SI | Lesion Mid RCA |
| Q85 | varchar |  |  | SI | Lesion RPL1 |
| Q86 | varchar |  |  | SI | Lesion RPL2 |
| Q87 | varchar |  |  | SI | Lesion Mid LAD |
| Q88 | varchar |  |  | SI | Lesion Dist LAD |
| Q89 | varchar |  |  | SI | Lesion Left Main |
| Q90 | varchar |  |  | SI | Lesion left Cir |
| Q91 | varchar |  |  | SI | TIMI Prox RCA |
| Q91ObsDR | varchar |  | FK | SI | TIMI Prox RCA DR |
| Q92 | varchar |  |  | SI | TIMI Mid RCA |
| Q92ObsDR | varchar |  | FK | SI | TIMI Mid RCA DR |
| Q93 | varchar |  |  | SI | TIMI RPL1 |
| Q93ObsDR | varchar |  | FK | SI | TIMI RPL1 DR |
| Q94 | varchar |  |  | SI | TIMI RPL2 |
| Q94ObsDR | varchar |  | FK | SI | TIMI RPL2 DR |
| Q95 | varchar |  |  | SI | TIMI Mid LAD |
| Q95ObsDR | varchar |  | FK | SI | TIMI Mid LAD DR |
| Q96 | varchar |  |  | SI | TIMI Dist LAD |
| Q96ObsDR | varchar |  | FK | SI | TIMI Dist LAD DR |
| Q97 | varchar |  |  | SI | TIMI Left Main |
| Q97ObsDR | varchar |  | FK | SI | TIMI Left Main DR |
| Q98 | varchar |  |  | SI | TIMI Left Main |
| Q98ObsDR | varchar |  | FK | SI | TIMI Left Main DR |
| Q99 | varchar |  |  | SI | TIMI Circum |
| Q99ObsDR | varchar |  | FK | SI | TIMI Circum DR |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*