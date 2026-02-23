# SQLUser.PAC_DocumentType

**Schema:** SQLUser
**Columnas:** 172
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOCTYPE_RowId | bigint | PK |  | NO | - |
| DOCTYPE_Code | varchar |  |  | NO | Code |
| DOCTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOCTYPE_CreatedDate | date |  |  | SI | Created Date |
| DOCTYPE_CreatedTime | time |  |  | SI | Created Time |
| DOCTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOCTYPE_DateFrom | date |  |  | SI | DateFrom |
| DOCTYPE_DateTo | date |  |  | SI | DateTo |
| DOCTYPE_Default | varchar |  |  | SI | Default |
| DOCTYPE_Desc | varchar |  |  | NO | Description |
| DOCTYPE_IsReferral | varchar |  |  | SI | Code |
| DOCTYPE_Owner | varchar |  |  | SI | Owner |
| DOCTYPE_ScanAdmDocSubType_DR | bigint |  | FK | SI | Des Ref ScanAdmDocSubType |
| DOCTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| DOCTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| DOCTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of call |
| Q02 | - |  |  | SI | Time of call |
| Q03 | - |  |  | SI | Interpreter |
| Q04 | - |  |  | SI | Access to transport |
| Q05 | - |  |  | SI | Support person present |
| Q06 | - |  |  | SI | Presentation |
| Q07 | - |  |  | SI | EDD |
| Q08 | - |  |  | SI | Gravida |
| Q09 | - |  |  | SI | Para |
| Q10 | - |  |  | SI | GBS status |
| Q100 | - |  |  | SI | Postnatal age |
| Q101 | - |  |  | SI | Postnatal age (days) |
| Q102 | - |  |  | SI | Complications with birth |
| Q103 | - |  |  | SI | Baby's date of birth |
| Q106 | - |  |  | SI | Complications with birth |
| Q107 | - |  |  | SI | Assessment notes |
| Q108 | - |  |  | SI | Patient advised to present |
| Q109 | - |  |  | SI | Management plan and notes |
| Q11 | - |  |  | SI | Multiple pregnancy |
| Q110 | - |  |  | SI | Date |
| Q111 | - |  |  | SI | Time |
| Q112 | - |  |  | SI | Postnatal Only |
| Q113 | - |  |  | SI | Access to transport |
| Q114 | - |  |  | SI | Date / Time membranes ruptured |
| Q115 | - |  |  | SI | Time membranes ruptured |
| Q116 | - |  |  | SI | Patient required to present for assessment |
| Q12 | - |  |  | SI | Previous C/S |
| Q13 | - |  |  | SI | Bleeding |
| Q14 | - |  |  | SI | Estimated amount |
| Q15 | - |  |  | SI | (If there is any bleeding, advise the woman to com... |
| Q16 | - |  |  | SI | Show |
| Q17 | - |  |  | SI | (A blood stained show is normal. Can stay home) |
| Q18 | - |  |  | SI | SROM |
| Q19 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | Time |
| Q21 | - |  |  | SI | Are you having normal foetal movements? |
| Q22 | - |  |  | SI | (Any change from normal pattern of movements for t... |
| Q23 | - |  |  | SI | Foetal monitoring attended recently? |
| Q24 | - |  |  | SI | (If any concerns, advise the woman to come into th... |
| Q25 | - |  |  | SI | Contractions |
| Q26 | - |  |  | SI | Onset date |
| Q27 | - |  |  | SI | Onset time |
| Q28 | - |  |  | SI | Action advised |
| Q29 | - |  |  | SI | Caller's name |
| Q30 | - |  |  | SI | Return phone number |
| Q31 | - |  |  | SI | Has this woman called before? |
| Q32 | - |  |  | SI | Gestation in weeks |
| Q33 | - |  |  | SI | Past obstetric history |
| Q34 | - |  |  | SI | Call detail notes |
| Q35 | - |  |  | SI | (Please enter PN  if postnatal) |
| Q36 | - |  |  | SI | Other complaints |
| Q37 | - |  |  | SI | Relationship to patient |
| Q38 | - |  |  | SI | Travel time to hospital |
| Q39 | - |  |  | SI | Strength |
| Q40 | - |  |  | SI | Frequency - 1 in |
| Q41 | - |  |  | SI | Duration (seconds) |
| Q42 | - |  |  | SI | PV discharge |
| Q43 | - |  |  | SI | Are you rhesus negative? |
| Q44 | - |  |  | SI | Headache |
| Q45 | - |  |  | SI | Oedema |
| Q46 | - |  |  | SI | Urinary symptoms |
| Q47 | - |  |  | SI | Visual disturbance |
| Q48 | - |  |  | SI | Abdominal pain |
| Q49 | - |  |  | SI | Anxiety or distress |
| Q50 | - |  |  | SI | Date of delivery |
| Q51 | - |  |  | SI | Days postnatal |
| Q52 | - |  |  | SI | Type of delivery |
| Q52B | - |  |  | SI | Type of delivery |
| Q52C | - |  |  | SI | Method of birth |
| Q53 | - |  |  | SI | Postnatal problems |
| Q54 | - |  |  | SI | Clinical note |
| Q55 | - |  |  | SI | Advice given |
| Q56 | - |  |  | SI | Assessment |
| Q57 | - |  |  | SI | Request to attend unit |
| Q58 | - |  |  | SI | Hospital on divert |
| Q59 | - |  |  | SI | Follow up |
| Q60 | - |  |  | SI | ml |
| Q61 | - |  |  | SI | Was the woman happy with the advice and informatio... |
| Q62 | - |  |  | SI | Comments |
| Q63 | - |  |  | SI | Time to attend or call back |
| Q64 | - |  |  | SI | Action advised |
| Q65 | - |  |  | SI | Date |
| Q66 | - |  |  | SI | Time |
| Q67 | - |  |  | SI | Reason for call |
| Q68 | - |  |  | SI | Has this woman called before? |
| Q69 | - |  |  | SI | Gravida |
| Q70 | - |  |  | SI | Para |
| Q71 | - |  |  | SI | Telephone consult |
| Q72 | - |  |  | SI | Current gestation |
| Q73 | - |  |  | SI | weeks |
| Q74 | - |  |  | SI | days |
| Q75 | - |  |  | SI | Current gestation (weeks) |
| Q76 | - |  |  | SI | Current gestation (days) |
| Q77 | - |  |  | SI | Comments related to relevant medical & obstetric h... |
| Q78 | - |  |  | SI | Current obstetric complications |
| Q79 | - |  |  | SI | Contractions |
| Q80 | - |  |  | SI | Contractions |
| Q81 | - |  |  | SI | Onset date |
| Q82 | - |  |  | SI | Onset time |
| Q83 | - |  |  | SI | Strength |
| Q84 | - |  |  | SI | Frequency (per 10 minutes) |
| Q85 | - |  |  | SI | Regularity |
| Q86 | - |  |  | SI | Duration (seconds) |
| Q87 | - |  |  | SI | Per Vaginam (PV) loss |
| Q88 | - |  |  | SI | Amount and colour |
| Q89 | - |  |  | SI | Membranes ruptured |
| Q90 | - |  |  | SI | Date / Time membranes ruptured |
| Q91 | - |  |  | SI | Time membranes ruptured |
| Q92 | - |  |  | SI | Fetal movements felt |
| Q93 | - |  |  | SI | Patient required to present for assessment |
| Q94 | - |  |  | SI | Duration of reduced movements |
| Q95 | - |  |  | SI | Time factor |
| Q96 | - |  |  | SI | Fetal movement notes |
| Q97 | - |  |  | SI | Postnatal age |
| Q98 | - |  |  | SI | months |
| Q99 | - |  |  | SI | days |
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