# SQLUser.LBC_InstrumentAntibioticTrans

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINAT_ParRef | bigint | PK |  | NO | Parent instrument DR |
| LBCINAT_Antibiotic_DR | bigint |  | FK | SI | Internal antibiotic |
| LBCINAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINAT_DateFrom | date |  |  | SI | Date From |
| LBCINAT_DateTo | date |  |  | SI | Date To |
| LBCINAT_InstrumentAntibiotic | varchar |  |  | SI | Instrument antibiotic |
| LBCINAT_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Intent to discharge documented in medical record |
| Q04 | - |  |  | SI | Relevant Multidisciplinary Teams (MTD) supports pa... |
| Q05 | - |  |  | SI | Contact appropriate specialty / clinician |
| Q06 | - |  |  | SI | MDT details |
| Q07 | - |  |  | SI | Next of kin / Relevant person / Guardianship / Cas... |
| Q08 | - |  |  | SI | Transport arranged |
| Q09 | - |  |  | SI | Discharge medications explained to patient / famil... |
| Q10 | - |  |  | SI | Discharge medications given to patient / family / ... |
| Q11 | - |  |  | SI | Patients own medications have been returned to the... |
| Q12 | - |  |  | SI | Outpatient prescription given to patient |
| Q13 | - |  |  | SI | All personal items returned to the patient |
| Q14 | - |  |  | SI | Personal items returned details |
| Q15 | - |  |  | SI | Equipment and supplies given to the patient |
| Q16 | - |  |  | SI | Reviewed all invasive devices and removed as requi... |
| Q17 | - |  |  | SI | Medical certificate provided / received |
| Q18 | - |  |  | SI | Medical discharge summary provided / received |
| Q19 | - |  |  | SI | Post discharge instructions provided to patient / ... |
| Q20 | - |  |  | SI | Patient / carer aware of follow up appointments an... |
| Q21 | - |  |  | SI | Patient able to wait in transit lounge |
| Q22 | - |  |  | SI | Waiting for |
| Q23 | - |  |  | SI | Adapted from the NSW Health Nepean Blue Mountains ... |
| Q24 | - |  |  | SI | Have Community Services / Providers / General Prac... |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*