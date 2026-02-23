# SQLUser.PAC_Transport

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANSP_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Education discussed with |
| Q04 | - |  |  | SI | Cot sides and bed rails |
| Q05 | - |  |  | SI | Safe sleeping - Sudden Infant Death Syndrom (SIDS) |
| Q06 | - |  |  | SI | Supervised play activity |
| Q07 | - |  |  | SI | Mobility restrictions |
| Q08 | - |  |  | SI | Safety notes |
| Q09 | - |  |  | SI | Diagnosis |
| Q10 | - |  |  | SI | Investigations and consent |
| Q11 | - |  |  | SI | Therapeutic treatments |
| Q12 | - |  |  | SI | Isolation requirements |
| Q13 | - |  |  | SI | Frequency of weight checks |
| Q14 | - |  |  | SI | Diagnosis and treatment notes |
| Q15 | - |  |  | SI | Reason for PIVC |
| Q16 | - |  |  | SI | How to identify signs of infection / dislodgement |
| Q17 | - |  |  | SI | Care of PIVC |
| Q18 | - |  |  | SI | PIVC notes |
| Q19 | - |  |  | SI | Appropriate foods for age |
| Q20 | - |  |  | SI | Accurate records and informing staff of intake and... |
| Q21 | - |  |  | SI | Breastfeeding mothers aware of the need for extra ... |
| Q22 | - |  |  | SI | Nutrition notes |
| Q23 | - |  |  | SI | Oral care |
| Q24 | - |  |  | SI | Personal hygiene |
| Q25 | - |  |  | SI | Handwashing |
| Q26 | - |  |  | SI | Pressure care |
| Q27 | - |  |  | SI | Cares notes |
| Q28 | - |  |  | SI | Hot drinks guideline |
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
| TRANSP_Address | varchar |  |  | SI | Address |
| TRANSP_Code | varchar |  |  | NO | Code |
| TRANSP_ContactMethod | varchar |  |  | SI | Contact Method |
| TRANSP_CreatedDate | date |  |  | SI | Created Date |
| TRANSP_CreatedTime | time |  |  | SI | Created Time |
| TRANSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRANSP_DateFrom | date |  |  | SI | Date From |
| TRANSP_DateTo | date |  |  | SI | Date To |
| TRANSP_Desc | varchar |  |  | NO | Description |
| TRANSP_Email | varchar |  |  | SI | Email |
| TRANSP_Fax | varchar |  |  | SI | Fax |
| TRANSP_Phone | varchar |  |  | SI | Phone |
| TRANSP_UpdatedDate | date |  |  | SI | Updated Date |
| TRANSP_UpdatedTime | time |  |  | SI | Updated Time |
| TRANSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*