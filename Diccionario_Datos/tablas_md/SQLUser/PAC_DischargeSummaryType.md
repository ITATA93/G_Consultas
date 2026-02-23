# SQLUser.PAC_DischargeSummaryType

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISCST_RowId | bigint | PK |  | NO | - |
| DISCST_Chart | varchar |  |  | SI | Chart |
| DISCST_Code | varchar |  |  | NO | Code |
| DISCST_CreatedDate | date |  |  | SI | Created Date |
| DISCST_CreatedTime | time |  |  | SI | Created Time |
| DISCST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISCST_DateFrom | date |  |  | SI | Date From |
| DISCST_DateTo | date |  |  | SI | Date To |
| DISCST_Desc | varchar |  |  | NO | Description |
| DISCST_DocumentName | varchar |  |  | SI | Document Name |
| DISCST_DocumentType | varchar |  |  | SI | Document Type |
| DISCST_EpisodeType | varchar |  |  | SI | EpisodeType |
| DISCST_MultipleVersions | varchar |  |  | SI | Multiple Versions |
| DISCST_UpdatedDate | date |  |  | SI | Updated Date |
| DISCST_UpdatedTime | time |  |  | SI | Updated Time |
| DISCST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type of assessment |
| Q04 | - |  |  | SI | Age 65+ |
| Q05 | - |  |  | SI | Diagnosis (3 or more co-existing) |
| Q06 | - |  |  | SI | Includes only documented medical diagnosis |
| Q07 | - |  |  | SI | Prior history of falls within 3 months |
| Q08 | - |  |  | SI | An unintentional change in position resulting in c... |
| Q09 | - |  |  | SI | Incontinence |
| Q10 | - |  |  | SI | Inability to make it to the bathroom or commode in... |
| Q11 | - |  |  | SI | Visual impairment |
| Q12 | - |  |  | SI | Includes but not limited to, macular degeneration,... |
| Q13 | - |  |  | SI | Impaired functional mobility |
| Q14 | - |  |  | SI | May include patients who need help with instrument... |
| Q15 | - |  |  | SI | Environmental hazards |
| Q16 | - |  |  | SI | May include but not limited to, poor illumination,... |
| Q17 | - |  |  | SI | Polypharmacy (4 or more prescriptions any type) |
| Q18 | - |  |  | SI | All prescriptions including prescriptions for over... |
| Q19 | - |  |  | SI | Pain affecting level of function |
| Q20 | - |  |  | SI | Pain often affects an individuals desire or abilit... |
| Q21 | - |  |  | SI | Cognitive impairment |
| Q22 | - |  |  | SI | Could include patients with dementia, Alzheimer's ... |
| Q23 | - |  |  | SI | 1. MAHC 10 – Fall Risk Assessment Tool. Missouri A... |
| Q24 | - |  |  | SI | visual field loss, age related changes, decline in... |
| Q25 | - |  |  | SI | or Activities of Daily Living (ADLs) or have gait ... |
| Q26 | - |  |  | SI | Drugs highly associated with fall risk include, bu... |
| Q27 | - |  |  | SI | Consider patients ability to adhere to the plan of... |
| Q28 | - |  |  | SI | 2. Calys M, Gagnon K, Jernigan S. A Validation Stu... |
| Q29 | - |  |  | SI | The Missouri Alliance For Home Cares Fall Risk Ass... |
| Q30 | - |  |  | SI | anticholinergic drugs. |
| Q31 | - |  |  | SI | or improper use of assistive devices. |
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