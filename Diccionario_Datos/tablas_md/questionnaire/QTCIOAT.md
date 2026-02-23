# questionnaire.QTCIOAT

> Inpatient Oral Assessment Tool

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Inpatient Oral Assessment Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q10 | varchar |  |  | SI | Tongue |
| Q11 | varchar |  |  | SI | Gums |
| Q12 | varchar |  |  | SI | Natural teeth |
| Q13 | varchar |  |  | SI | Dentures |
| Q14 | varchar |  |  | SI | Diet |
| Q15 | varchar |  |  | SI | Respiratory support |
| Q16 | varchar |  |  | SI | Sepsis |
| Q17 | varchar |  |  | SI | Mobility |
| Q18 | varchar |  |  | SI | Initial oral assessment score |
| Q19 | varchar |  |  | SI | Review risk |
| Q20 | varchar |  |  | SI | Other |
| Q21 | varchar |  |  | SI | Care plan guidance |
| Q22 | varchar |  |  | SI | Low risk care plan: 12 hourly care |
| Q23 | varchar |  |  | SI | Twice daily teeth cleaning (with assistance if req... |
| Q24 | varchar |  |  | SI | Moisturiser to moisten lips if required |
| Q25 | varchar |  |  | SI | Ensure dentures fit and are in good condition. cle... |
| Q26 | varchar |  |  | SI | Clean and soak dentures overnight in sterile water |
| Q27 | varchar |  |  | SI | Any suspected infection move to medium risk |
| Q28 | varchar |  |  | SI | Medium risk care plan: 6 hourly care |
| Q29 | varchar |  |  | SI | Assist or clean teeth with low foaming toothpaste ... |
| Q3 | date |  |  | SI | Initial assessment or reassessment date |
| Q30 | varchar |  |  | SI | Apply moisturiser to moisten lips |
| Q31 | varchar |  |  | SI | Ensure access to unsweetened fluids |
| Q32 | varchar |  |  | SI | Ensure adequate fluid intake |
| Q33 | varchar |  |  | SI | High risk care plan: 4 hourly care |
| Q34 | varchar |  |  | SI | Brush teeth with low foaming toothpaste for 2-3 mi... |
| Q35 | varchar |  |  | SI | Apply moisturiser to moisten lips |
| Q36 | varchar |  |  | SI | Provide oral hygiene with water using toothbrush o... |
| Q37 | varchar |  |  | SI | If intubated 4 hourly cuff pressure check and Endo... |
| Q38 | varchar |  |  | SI | Pharyngeal and subglottic suctioning 4 hourly, soo... |
| Q39 | varchar |  |  | SI | This process is also part of the Ventilator Care B... |
| Q4 | time |  |  | SI | Time |
| Q40 | varchar |  |  | SI | Complete assessment or oral cavity and mucosa, est... |
| Q41 | date |  |  | SI | Date |
| Q42 | time |  |  | SI | Time |
| Q43 | varchar |  |  | SI | The Inpatient Oral Assessment Tool was designed to... |
| Q5 | varchar |  |  | SI | Category / risk |
| Q6 | varchar |  |  | SI | Expectorate |
| Q7 | varchar |  |  | SI | Oral pain |
| Q8 | varchar |  |  | SI | Lips |
| Q9 | varchar |  |  | SI | Mucosa |
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