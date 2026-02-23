# questionnaire.QGXXXOPHSED

> Sedation

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(Sedation)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | time |  |  | SI | Ultrasound - start  |
| Q02 | time |  |  | SI | Ultrasound - finish |
| Q03 | time |  |  | SI | VER/ERG - start |
| Q04 | time |  |  | SI | VER/ERG - finsh |
| Q06 | time |  |  | SI | Photos - start |
| Q07 | time |  |  | SI | Photos - finish |
| Q08 | time |  |  | SI | CT Scan/MRI - start |
| Q09 | time |  |  | SI | CT Scan/MRI - finish |
| Q10 | time |  |  | SI | Contact Lens Fitting - start |
| Q11 | time |  |  | SI | Contact Lens Fitting - finish |
| Q12 | varchar |  |  | SI | EUS |
| Q13 | varchar |  |  | SI | Slit lamp |
| Q14 | varchar |  |  | SI | Suture removal |
| Q15 | varchar |  |  | SI | Fundus exam |
| Q16 | varchar |  |  | SI | Intraocular pressure |
| Q17 | varchar |  |  | SI | Refraction |
| Q18 | varchar |  |  | SI | Other |
| Q19 | numeric |  |  | SI | Number of previous Sedations |
| Q20 | varchar |  |  | SI | Previous Failed Sedations |
| Q21 | time |  |  | SI | NPO - Milk / Solids |
| Q22 | time |  |  | SI | NPO - Fluids |
| Q23 | bit |  |  | SI | Not applicable |
| Q24 | time |  |  | SI | NPO Breast Milk |
| Q25 | varchar |  |  | SI | Ramsay Sedation Scale |
| Q26 | varchar |  |  | SI | Post Anaesthesia Recovery Score for Ambulatory Pat... |
| Q27 | varchar |  |  | SI | Instructions: to enter data , fill in the fields, ... |
| Q28 | time |  |  | SI | Sign out time |
| Q29 | date |  |  | SI | Date |
| Q30 | varchar |  |  | SI | Follow Up Apointment Given |
| Q31 | varchar |  |  | SI | Medication instructions |
| Q32 | varchar |  |  | SI | Removal of Eye pad |
| Q33 | varchar |  |  | SI | Feeding instructions |
| Q34 | varchar |  |  | SI | Discharge destination |
| Q35 | varchar |  |  | SI | ASA level |
| Q36 | time |  |  | SI | NPO Breast milk |
| Q37 | varchar |  |  | SI | Given to and verbalised by (name)  |
| Q38 | varchar |  |  | SI | Relationship |
| Q39 | varchar |  |  | SI | Mode of transport |
| Q40 | varchar |  |  | SI | Notes |
| Q41 | varchar |  |  | SI | Sedation History |
| Q42 | varchar |  |  | SI | Fasting |
| Q43 | varchar |  |  | SI | Start time |
| Q44 | varchar |  |  | SI | Finish time |
| Q45 | varchar |  |  | SI | Ultrasound |
| Q46 | varchar |  |  | SI | VER / ERG |
| Q47 | varchar |  |  | SI | Photos |
| Q48 | varchar |  |  | SI | CT Scan / MRI |
| Q49 | varchar |  |  | SI | Contact lens fitting |
| Q50 | varchar |  |  | SI | NPO - Breast Milk |
| Q51 | varchar |  |  | SI | Notes |
| Q52 | varchar |  |  | SI | Ultrasound |
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