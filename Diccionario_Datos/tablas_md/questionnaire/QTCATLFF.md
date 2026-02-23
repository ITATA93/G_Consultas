# questionnaire.QTCATLFF

> Assessment Tool For Lingual Frenulum Function (ATLFF)

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Assessment Tool For Lingual Frenulum Function (ATLFF)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Lateralisation |
| Q04 | varchar |  |  | SI | Lift of tongue |
| Q05 | varchar |  |  | SI | Extension of tongue |
| Q06 | varchar |  |  | SI | Spread of anterior tongue |
| Q07 | varchar |  |  | SI | Cupping of tongue |
| Q08 | varchar |  |  | SI | Peristalsis |
| Q09 | varchar |  |  | SI | Function Items Score |
| Q10 | varchar |  |  | SI | Appearance of tongue when lifted |
| Q11 | varchar |  |  | SI | Length of lingual frenulum when tongue lifted |
| Q12 | varchar |  |  | SI | Attachment of lingual frenulum to inferior  alveol... |
| Q13 | varchar |  |  | SI | Elasticity of frenulum |
| Q14 | varchar |  |  | SI | Attachment of lingual frenulum to tongue |
| Q15 | varchar |  |  | SI | Appearance Score |
| Q16 | varchar |  |  | SI | Scoring / Frenotomy Decision Rule |
| Q17 | varchar |  |  | SI | • 14 = Perfect Function score regardless of Appear... |
| Q18 | varchar |  |  | SI | • 11 = Acceptable Function score only if Appearanc... |
| Q19 | varchar |  |  | SI | • < 11 = Function Score indicates function impaire... |
| Q20 | varchar |  |  | SI | • Hazelbaker AK. Assessment tool for lingual frenu... |
| Q21 | varchar |  |  | SI | Snap back |
| Q22 | varchar |  |  | SI | Documents the assessment of the frenulum function ... |
| Q23 | varchar |  |  | SI | The ATLFF™© remains the only valid and reliable to... |
| Q24 | varchar |  |  | SI | Total Score |
| Q25 | varchar |  |  | SI | Function Items Score |
| Q26 | varchar |  |  | SI | Appearance Score |
| Q27 | varchar |  |  | SI | 14 = Perfect Function score regardless of Appearan... |
| Q28 | varchar |  |  | SI | 11 = Acceptable Function score only if Appearance ... |
| Q29 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q30 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q31 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q32 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q33 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q34 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q35 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q36 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q37 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q38 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q39 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q40 | varchar |  |  | SI | < 11 = Function Score indicates function impaired.... |
| Q41 | varchar |  |  | SI | Hazelbaker AK. Assessment tool for lingual frenulu... |
| Q42 | varchar |  |  | SI | Documents the assessment of the frenulum function ... |
| Q43 | varchar |  |  | SI | Appearance Items Score |
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