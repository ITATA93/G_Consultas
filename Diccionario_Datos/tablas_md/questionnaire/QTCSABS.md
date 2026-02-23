# questionnaire.QTCSABS

> Staphylococcus Aureus Bacteraemia Summary

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Staphylococcus Aureus Bacteraemia Summary

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Please add Staphylococcus aureus bacteraemia (SAB)... |
| Q04 | varchar |  |  | SI | Staphylococcus Aureus Bacteraemia (SAB) Examinatio... |
| Q05 | date |  |  | SI | Date of first positive blood culture |
| Q06 | varchar |  |  | SI | Methicillin-Resistant Staphylococcus Aureus (MRSA) |
| Q07 | varchar |  |  | SI | Susceptibilities |
| Q08 | varchar |  |  | SI | Presentation |
| Q09 | varchar |  |  | SI | Intravenous (IV) drug use |
| Q10 | varchar |  |  | SI | Please ensure patients social history has been upd... |
| Q11 | varchar |  |  | SI | IV drug use details |
| Q12 | varchar |  |  | SI | Source of Infection |
| Q13 | varchar |  |  | SI | Source of infection |
| Q14 | varchar |  |  | SI | Source of infection details |
| Q15 | varchar |  |  | SI | First SAB positive blood culture was collected mor... |
| Q16 | varchar |  |  | SI | First SAB positive blood culture was collected les... |
| Q17 | varchar |  |  | SI | Indwelling medical device associated infection |
| Q18 | varchar |  |  | SI | Type of indwelling device |
| Q19 | varchar |  |  | SI | Other type of indwelling device |
| Q20 | varchar |  |  | SI | SAB occurring within 30 days of a surgical procedu... |
| Q21 | varchar |  |  | SI | Surgical procedure / device details |
| Q22 | varchar |  |  | SI | Invasive instrumentation or incision related to th... |
| Q23 | varchar |  |  | SI | Invasive instrumentation / incision details |
| Q24 | varchar |  |  | SI | SAB is associated with neutropaenia contributed to... |
| Q25 | varchar |  |  | SI | Neutropaenia / Cytotoxic therapy details |
| Q27 | varchar |  |  | SI | Removable focus (eg cannula) |
| Q28 | varchar |  |  | SI | Details of removal |
| Q29 | date |  |  | SI | Date of removal |
| Q30 | varchar |  |  | SI | History examination findings |
| Q31 | varchar |  |  | SI | Skin examination findings |
| Q32 | varchar |  |  | SI | Relevant investigations |
| Q33 | varchar |  |  | SI | Summary of relevant investigations |
| Q34 | varchar |  |  | SI | Diagnosed with infective endocarditis |
| Q35 | varchar |  |  | SI | Complete Infective Endocarditis Summary questionna... |
| Q36 | varchar |  |  | SI | Uncomplicated SAB (no metastatic focus of infectio... |
| Q37 | varchar |  |  | SI | Complicated SAB |
| Q38 | varchar |  |  | SI | Complicated SAB |
| Q39 | varchar |  |  | SI | Complicated SAB details |
| Q40 | varchar |  |  | SI | Evidence of metastatic foci |
| Q41 | varchar |  |  | SI | Metastatic foci details |
| Q42 | varchar |  |  | SI | Presence of prosthetic material |
| Q43 | varchar |  |  | SI | Prosthetic material details |
| Q44 | varchar |  |  | SI | Antibiotic management plan and duration of treatme... |
| Q45 | varchar |  |  | SI | Recommended post treatment investigations |
| Q46 | varchar |  |  | SI | Guidelines |
| Q47 | varchar |  |  | SI | Please refer to the SAB management protocol |
| Q48 | varchar |  |  | SI | Dummy1 |
| Q49 | varchar |  |  | SI | Dummy2 |
| Q50 | varchar |  |  | SI | Dummy3 |
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