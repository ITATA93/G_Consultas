# SQLUser.MR_ICUValues

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ICUV_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ICUV_Childsub | double |  |  | NO | Childsub |
| ICUV_DateCreated | date |  |  | SI | Date Created |
| ICUV_ICU_DR | bigint |  | FK | SI | Des Ref to MRC ICU |
| ICUV_RowId | varchar |  |  | NO | - |
| ICUV_TimeCreated | time |  |  | SI | Time Created |
| ICUV_UserCreated | bigint |  |  | SI | User Created |
| ICUV_Value | varchar |  |  | SI | Value |
| Q01 | - |  |  | SI | Stomatitis |
| Q01N | - |  |  | SI | Note |
| Q01NTxtOnly | - |  |  | SI | Note Plain Text Only |
| Q01ObsDR | - |  |  | SI | Stomatitis DR |
| Q03 | - |  |  | SI | Face |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Face DR |
| Q05 | - |  |  | SI | Neck |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Neck DR |
| Q07 | - |  |  | SI | Nose |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Nose DR |
| Q09 | - |  |  | SI | Oral Cavity |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Oral Cavity DR |
| Q11 | - |  |  | SI | Lips |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Lips DR |
| Q13 | - |  |  | SI | Larynx |
| Q13N | - |  |  | SI | Note |
| Q13ObsDR | - |  |  | SI | Larynx DR |
| Q15 | - |  |  | SI | Right ear |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Right ear DR |
| Q17 | - |  |  | SI | Left ear |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Left ear DR |
| Q18 | - |  |  | SI | Other |
| Q20 | - |  |  | SI | View |
| Q20TxtOnly | - |  |  | SI | View Plain Text Only |
| Q21 | - |  |  | SI | Head and face anterior |
| Q22 | - |  |  | SI | Eyes |
| Q22N | - |  |  | SI | Note |
| Q22ObsDR | - |  |  | SI | Eyes DR |
| Q23 | - |  |  | SI | Pupil difference |
| Q23N | - |  |  | SI | Note |
| Q23ObsDR | - |  |  | SI | Pupil difference DR |
| Q26 | - |  |  | SI | Neck range of motion |
| Q26N | - |  |  | SI | Note |
| Q26ObsDR | - |  |  | SI | Neck range of motion DR |
| Q28 | - |  |  | SI | Thyroid Exam |
| Q28N | - |  |  | SI | Note |
| Q28ObsDR | - |  |  | SI | Thyroid Exam DR |
| Q30 | - |  |  | SI | Lymph nodes |
| Q30N | - |  |  | SI | Note |
| Q30ObsDR | - |  |  | SI | Lymph nodes DR |
| Q32 | - |  |  | SI | Jugular venous distention |
| Q32N | - |  |  | SI | Note |
| Q32ObsDR | - |  |  | SI | Jugular venous distention DR |
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