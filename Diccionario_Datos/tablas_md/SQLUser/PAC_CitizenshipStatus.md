# SQLUser.PAC_CitizenshipStatus

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CITSTA_RowId | bigint | PK |  | NO | - |
| CITSTA_Code | varchar |  |  | NO | Code |
| CITSTA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CITSTA_CreatedDate | date |  |  | SI | Created Date |
| CITSTA_CreatedTime | time |  |  | SI | Created Time |
| CITSTA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CITSTA_DateFrom | date |  |  | SI | DateFrom |
| CITSTA_DateTo | date |  |  | SI | DateTo |
| CITSTA_Desc | varchar |  |  | NO | Description |
| CITSTA_Owner | varchar |  |  | SI | Owner |
| CITSTA_UpdatedDate | date |  |  | SI | Updated Date |
| CITSTA_UpdatedTime | time |  |  | SI | Updated Time |
| CITSTA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q10 | - |  |  | SI | Tongue |
| Q11 | - |  |  | SI | Gums |
| Q12 | - |  |  | SI | Natural teeth |
| Q13 | - |  |  | SI | Dentures |
| Q14 | - |  |  | SI | Diet |
| Q15 | - |  |  | SI | Respiratory support |
| Q16 | - |  |  | SI | Sepsis |
| Q17 | - |  |  | SI | Mobility |
| Q18 | - |  |  | SI | Initial oral assessment score |
| Q19 | - |  |  | SI | Review risk |
| Q20 | - |  |  | SI | Other |
| Q21 | - |  |  | SI | Care plan guidance |
| Q22 | - |  |  | SI | Low risk care plan: 12 hourly care |
| Q23 | - |  |  | SI | Twice daily teeth cleaning (with assistance if req... |
| Q24 | - |  |  | SI | Moisturiser to moisten lips if required |
| Q25 | - |  |  | SI | Ensure dentures fit and are in good condition. cle... |
| Q26 | - |  |  | SI | Clean and soak dentures overnight in sterile water |
| Q27 | - |  |  | SI | Any suspected infection move to medium risk |
| Q28 | - |  |  | SI | Medium risk care plan: 6 hourly care |
| Q29 | - |  |  | SI | Assist or clean teeth with low foaming toothpaste ... |
| Q3 | - |  |  | SI | Initial assessment or reassessment date |
| Q30 | - |  |  | SI | Apply moisturiser to moisten lips |
| Q31 | - |  |  | SI | Ensure access to unsweetened fluids |
| Q32 | - |  |  | SI | Ensure adequate fluid intake |
| Q33 | - |  |  | SI | High risk care plan: 4 hourly care |
| Q34 | - |  |  | SI | Brush teeth with low foaming toothpaste for 2-3 mi... |
| Q35 | - |  |  | SI | Apply moisturiser to moisten lips |
| Q36 | - |  |  | SI | Provide oral hygiene with water using toothbrush o... |
| Q37 | - |  |  | SI | If intubated 4 hourly cuff pressure check and Endo... |
| Q38 | - |  |  | SI | Pharyngeal and subglottic suctioning 4 hourly, soo... |
| Q39 | - |  |  | SI | This process is also part of the Ventilator Care B... |
| Q4 | - |  |  | SI | Time |
| Q40 | - |  |  | SI | Complete assessment or oral cavity and mucosa, est... |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Time |
| Q43 | - |  |  | SI | The Inpatient Oral Assessment Tool was designed to... |
| Q5 | - |  |  | SI | Category / risk |
| Q6 | - |  |  | SI | Expectorate |
| Q7 | - |  |  | SI | Oral pain |
| Q8 | - |  |  | SI | Lips |
| Q9 | - |  |  | SI | Mucosa |
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