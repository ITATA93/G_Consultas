# SQLUser.CT_LocLinkWard

**Schema:** SQLUser
**Columnas:** 170
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WARD_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| Q01 | - |  |  | SI | Weight (kgs) |
| Q01ObsDR | - |  |  | SI | Weight (kgs) DR |
| Q02 | - |  |  | SI | Height (cm) |
| Q02ObsDR | - |  |  | SI | Height (cm) DR |
| Q03 | - |  |  | SI | Risk Factors |
| Q04 | - |  |  | SI | Clinical Details |
| Q05 | - |  |  | SI | Current Medication |
| Q06 | - |  |  | SI | Consultant |
| Q07 | - |  |  | SI | Date of Investigation |
| Q08 | - |  |  | SI | 1st Operator |
| Q09 | - |  |  | SI | 2nd Operator |
| Q10 | - |  |  | SI | Procedure |
| Q11 | - |  |  | SI | Radiographers |
| Q12 | - |  |  | SI | Catheterisation |
| Q13 | - |  |  | SI | Site |
| Q14 | - |  |  | SI | Phasic |
| Q15 | - |  |  | SI | Mean |
| Q16 | - |  |  | SI | Left Ventricle |
| Q17 | - |  |  | SI | Catheters used |
| Q18 | - |  |  | SI | Oxygen Saturation |
| Q19 | - |  |  | SI | Mid RA |
| Q20 | - |  |  | SI | Low RA |
| Q21 | - |  |  | SI | IVC |
| Q22 | - |  |  | SI | IRV Outflow |
| Q23 | - |  |  | SI | RVTV |
| Q24 | - |  |  | SI | RPA |
| Q25 | - |  |  | SI | LPA |
| Q26 | - |  |  | SI | Mixed |
| Q27 | - |  |  | SI | LV |
| Q28 | - |  |  | SI | AO |
| Q29 | - |  |  | SI | LA |
| Q30 | - |  |  | SI | PV |
| Q31 | - |  |  | SI | Medication used or prescribed during procedure |
| Q32 | - |  |  | SI | Arterial Access 1 |
| Q33 | - |  |  | SI | Arterial Access 2 |
| Q34 | - |  |  | SI | Arterial Access 3 |
| Q35 | - |  |  | SI | Venous Access 1 |
| Q36 | - |  |  | SI | Venous Access 2 |
| Q37 | - |  |  | SI | Venous Access 3 |
| Q38 | - |  |  | SI | Access Problems |
| Q39 | - |  |  | SI | Contrast Medium |
| Q40 | - |  |  | SI | Contrast Medium (ml) |
| Q41 | - |  |  | SI | Procedure Time (min) |
| Q42 | - |  |  | SI | Screening Time |
| Q43 | - |  |  | SI | Angiographic Findings |
| Q43TxtOnly | - |  |  | SI | Angiographic Findings Plain Text Only |
| Q44 | - |  |  | SI | Further Management and advice to GP |
| Q45 | - |  |  | SI | Reported by |
| Q46 | - |  |  | SI | Left Ventricle |
| Q47 | - |  |  | SI | Left Ventricle M |
| Q48 | - |  |  | SI | End Diastolic (mmHg) |
| Q49 | - |  |  | SI | End Diastolic (mmHg) M |
| Q50 | - |  |  | SI | Aorta |
| Q51 | - |  |  | SI | Pulmonary Artery |
| Q52 | - |  |  | SI | Pulmonary Artery M |
| Q53 | - |  |  | SI | Right ventricle |
| Q54 | - |  |  | SI | Right ventricle M |
| Q55 | - |  |  | SI | Right Atrium |
| Q56 | - |  |  | SI | Right Atrium M |
| Q57 | - |  |  | SI | PA Wedge |
| Q58 | - |  |  | SI | PA Wedge M |
| Q59 | - |  |  | SI | Left Atrium |
| Q60 | - |  |  | SI | Left Atrium M |
| Q61 | - |  |  | SI | CO 1 |
| Q62 | - |  |  | SI | CO 2 |
| Q63 | - |  |  | SI | Heart Rate |
| Q64 | - |  |  | SI | AV Gradient |
| Q65 | - |  |  | SI | MV Gradient |
| Q66 | - |  |  | SI | Notes |
| Q67 | - |  |  | SI | Report Date |
| Q68 | - |  |  | SI | Other Procedure |
| Q69 | - |  |  | SI | Prox RCA |
| Q69ObsDR | - |  |  | SI | Prox RCA DR |
| Q70 | - |  |  | SI | Segment |
| Q71 | - |  |  | SI | Stenosis |
| Q72 | - |  |  | SI | Lesion Type |
| Q73 | - |  |  | SI | TIMI Flow |
| Q74 | - |  |  | SI | Mid RCA |
| Q74ObsDR | - |  |  | SI | Mid RCA DR |
| Q75 | - |  |  | SI | RPL1 (small) |
| Q75ObsDR | - |  |  | SI | RPL1 (small) DR |
| Q76 | - |  |  | SI | RPL2 (small) |
| Q76ObsDR | - |  |  | SI | RPL2 (small) DR |
| Q77 | - |  |  | SI | Mid LAD |
| Q77ObsDR | - |  |  | SI | Mid LAD DR |
| Q78 | - |  |  | SI | Dist LAD |
| Q78ObsDR | - |  |  | SI | Dist LAD DR |
| Q79 | - |  |  | SI | Left Main |
| Q79ObsDR | - |  |  | SI | Left Main DR |
| Q80 | - |  |  | SI | Left Circumflex |
| Q80ObsDR | - |  |  | SI | Left Circumflex DR |
| Q81 | - |  |  | SI | Coronary Anatomy |
| Q82 | - |  |  | SI | Dominance |
| Q83 | - |  |  | SI | Lesion Prox |
| Q84 | - |  |  | SI | Lesion Mid RCA |
| Q85 | - |  |  | SI | Lesion RPL1 |
| Q86 | - |  |  | SI | Lesion RPL2 |
| Q87 | - |  |  | SI | Lesion Mid LAD |
| Q88 | - |  |  | SI | Lesion Dist LAD |
| Q89 | - |  |  | SI | Lesion Left Main |
| Q90 | - |  |  | SI | Lesion left Cir |
| Q91 | - |  |  | SI | TIMI Prox RCA |
| Q91ObsDR | - |  |  | SI | TIMI Prox RCA DR |
| Q92 | - |  |  | SI | TIMI Mid RCA |
| Q92ObsDR | - |  |  | SI | TIMI Mid RCA DR |
| Q93 | - |  |  | SI | TIMI RPL1 |
| Q93ObsDR | - |  |  | SI | TIMI RPL1 DR |
| Q94 | - |  |  | SI | TIMI RPL2 |
| Q94ObsDR | - |  |  | SI | TIMI RPL2 DR |
| Q95 | - |  |  | SI | TIMI Mid LAD |
| Q95ObsDR | - |  |  | SI | TIMI Mid LAD DR |
| Q96 | - |  |  | SI | TIMI Dist LAD |
| Q96ObsDR | - |  |  | SI | TIMI Dist LAD DR |
| Q97 | - |  |  | SI | TIMI Left Main |
| Q97ObsDR | - |  |  | SI | TIMI Left Main DR |
| Q98 | - |  |  | SI | TIMI Left Main |
| Q98ObsDR | - |  |  | SI | TIMI Left Main DR |
| Q99 | - |  |  | SI | TIMI Circum |
| Q99ObsDR | - |  |  | SI | TIMI Circum DR |
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
| WARD_Childsub | double |  |  | NO | Childsub |
| WARD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WARD_CreatedDate | date |  |  | SI | Created Date |
| WARD_CreatedTime | time |  |  | SI | Created Time |
| WARD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WARD_RowId | varchar |  |  | NO | - |
| WARD_UpdatedDate | date |  |  | SI | Updated Date |
| WARD_UpdatedTime | time |  |  | SI | Updated Time |
| WARD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| WARD_Ward_DR | bigint |  | FK | SI | Des Ref PACWard |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*