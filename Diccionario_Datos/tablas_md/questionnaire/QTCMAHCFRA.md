# questionnaire.QTCMAHCFRA

> Missouri Alliance For Home Cares Fall Risk Assessment Tool

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Missouri Alliance For Home Cares Fall Risk Assessment Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Type of assessment |
| Q04 | varchar |  |  | SI | Age 65+ |
| Q05 | varchar |  |  | SI | Diagnosis (3 or more co-existing) |
| Q06 | varchar |  |  | SI | Includes only documented medical diagnosis |
| Q07 | varchar |  |  | SI | Prior history of falls within 3 months |
| Q08 | varchar |  |  | SI | An unintentional change in position resulting in c... |
| Q09 | varchar |  |  | SI | Incontinence |
| Q10 | varchar |  |  | SI | Inability to make it to the bathroom or commode in... |
| Q11 | varchar |  |  | SI | Visual impairment |
| Q12 | varchar |  |  | SI | Includes but not limited to, macular degeneration,... |
| Q13 | varchar |  |  | SI | Impaired functional mobility |
| Q14 | varchar |  |  | SI | May include patients who need help with instrument... |
| Q15 | varchar |  |  | SI | Environmental hazards |
| Q16 | varchar |  |  | SI | May include but not limited to, poor illumination,... |
| Q17 | varchar |  |  | SI | Polypharmacy (4 or more prescriptions any type) |
| Q18 | varchar |  |  | SI | All prescriptions including prescriptions for over... |
| Q19 | varchar |  |  | SI | Pain affecting level of function |
| Q20 | varchar |  |  | SI | Pain often affects an individuals desire or abilit... |
| Q21 | varchar |  |  | SI | Cognitive impairment |
| Q22 | varchar |  |  | SI | Could include patients with dementia, Alzheimer's ... |
| Q23 | varchar |  |  | SI | 1. MAHC 10 – Fall Risk Assessment Tool. Missouri A... |
| Q24 | varchar |  |  | SI | visual field loss, age related changes, decline in... |
| Q25 | varchar |  |  | SI | or Activities of Daily Living (ADLs) or have gait ... |
| Q26 | varchar |  |  | SI | Drugs highly associated with fall risk include, bu... |
| Q27 | varchar |  |  | SI | Consider patients ability to adhere to the plan of... |
| Q28 | varchar |  |  | SI | 2. Calys M, Gagnon K, Jernigan S. A Validation Stu... |
| Q29 | varchar |  |  | SI | The Missouri Alliance For Home Cares Fall Risk Ass... |
| Q30 | varchar |  |  | SI | anticholinergic drugs. |
| Q31 | varchar |  |  | SI | or improper use of assistive devices. |
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