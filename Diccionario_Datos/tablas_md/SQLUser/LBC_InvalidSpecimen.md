# SQLUser.LBC_InvalidSpecimen

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCISP_RowID | bigint | PK |  | NO | - |
| LBCISP_Code | varchar |  |  | NO | Code |
| LBCISP_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCISP_DateFrom | date |  |  | SI | Effective date for the record |
| LBCISP_DateTo | date |  |  | SI | Last day the record is active |
| LBCISP_DefaultAction | varchar |  |  | SI | Default Action
For screens like Specimen Rejectio... |
| LBCISP_Desc | varchar |  |  | NO | Description |
| LBCISP_Owner | varchar |  |  | SI | Owner |
| LBCISP_Types | varchar |  |  | SI | List of type of the reasons. E.g. use before colle... |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Previous skin cancer |
| Q04 | - |  |  | SI | Type of skin cancer |
| Q05 | - |  |  | SI | Please specify |
| Q06 | - |  |  | SI | Family history of melanoma |
| Q07 | - |  |  | SI | Please ensure this is documented in the patient's ... |
| Q08 | - |  |  | SI | Additional risk factors |
| Q09 | - |  |  | SI | Other risks |
| Q10 | - |  |  | SI | Fitzpatrick skin type |
| Q10ObsDR | - |  |  | SI | Fitzpatrick skin type DR |
| Q11 | - |  |  | SI | Full skin surveillance examination |
| Q12 | - |  |  | SI | Patient-directed examination |
| Q13 | - |  |  | SI | Scalp |
| Q14 | - |  |  | SI | Scalp notes |
| Q15 | - |  |  | SI | Face |
| Q16 | - |  |  | SI | Face notes |
| Q17 | - |  |  | SI | Trunk |
| Q18 | - |  |  | SI | Trunk notes |
| Q19 | - |  |  | SI | Arms / Hands |
| Q20 | - |  |  | SI | Arms / Hands notes |
| Q21 | - |  |  | SI | Legs / Feet |
| Q22 | - |  |  | SI | Legs / Feet notes |
| Q23 | - |  |  | SI | Lymph Node Basins Examined |
| Q24 | - |  |  | SI | Cervical nodes |
| Q25 | - |  |  | SI | Findings |
| Q26 | - |  |  | SI | Axillary |
| Q27 | - |  |  | SI | Findings |
| Q28 | - |  |  | SI | Inguinal |
| Q29 | - |  |  | SI | Findings |
| Q30 | - |  |  | SI | Abdominal palpation |
| Q31 | - |  |  | SI | Findings |
| Q32 | - |  |  | SI | Other findings / Issues |
| Q33 | - |  |  | SI | Education given about sun protection / Sunscreen u... |
| Q34 | - |  |  | SI | Education details |
| Q35 | - |  |  | SI | Breslow thickness (mm) |
| Q36 | - |  |  | SI | Type of skin cancer |
| Q37 | - |  |  | SI | Previous skin cancer |
| Q38 | - |  |  | SI | Family history of melanoma |
| Q39 | - |  |  | SI | Prevention |
| Q40 | - |  |  | SI | Other prevention |
| Q41 | - |  |  | SI | Fitzpatrick skin type |
| Q41ObsDR | - |  |  | SI | Fitzpatrick skin type DR |
| Q42 | - |  |  | SI | Type of examination |
| Q43 | - |  |  | SI | Solar keratoses notes |
| Q44 | - |  |  | SI | Findings |
| Q45 | - |  |  | SI | Findings |
| Q46 | - |  |  | SI | Findings |
| Q47 | - |  |  | SI | Findings |
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