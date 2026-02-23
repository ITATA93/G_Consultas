# questionnaire.QTCOPKHQ

> Outpatient Pre Procedure Key Health Questions

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Outpatient Pre Procedure Key Health Questions

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Is your gender identity the same as you were assig... |
| Q04 | varchar |  |  | SI | If no please detail |
| Q05 | varchar |  |  | SI | What are your preferred pronouns? |
| Q06 | varchar |  |  | SI | Key health questions |
| Q07 | varchar |  |  | SI | Do you have any implants e.g shunt, orthopaedic im... |
| Q08 | varchar |  |  | SI | Proposed procedure and laterality |
| Q09 | varchar |  |  | SI | Have you ever experienced any significant problems... |
| Q10 | varchar |  |  | SI | Family history of problems with anaesthesia or int... |
| Q11 | varchar |  |  | SI | Any back, neck, breathing problems, cramps, panic ... |
| Q12 | varchar |  |  | SI | Personal or family history of any blood, bleeding ... |
| Q13 | varchar |  |  | SI | Do you have any dietary requirements? |
| Q14 | varchar |  |  | SI | Dizziness, vertigo, epilepsy fit and seizures? |
| Q15 | varchar |  |  | SI | Do you have any specific individual needs, learnin... |
| Q16 | varchar |  |  | SI | Is there a possibility you could be pregnant? |
| Q17 | varchar |  |  | SI | Please state the date of your last menstrual perio... |
| Q18 | varchar |  |  | SI | Is there anything in your medical history that has... |
| Q19 | varchar |  |  | SI | If yes to any of the above please detail |
| Q20 | varchar |  |  | SI | Permission to discuss treatment with next of kin |
| Q21 | varchar |  |  | SI | Permission to access a summary of your medical his... |
| Q22 | varchar |  |  | SI | Patient consent obtained for information to be sha... |
| Q23 | varchar |  |  | SI | Infection prevention |
| Q24 | varchar |  |  | SI | Are you immuno-compromised, or have you previously... |
| Q25 | varchar |  |  | SI | Have you had any symptoms of infection (E.g. cough... |
| Q26 | varchar |  |  | SI | Have you taken antibiotics within the last 3 month... |
| Q27 | varchar |  |  | SI | Do you have any exfoliating skin conditions such a... |
| Q28 | varchar |  |  | SI | Do you have any body piercings? |
| Q29 | varchar |  |  | SI | Do you have MRSA or have you previously been ident... |
| Q30 | varchar |  |  | SI | Have you ever been treated for or advised you have... |
| Q31 | varchar |  |  | SI | Have you had diarrhoea (loose stools) in the last ... |
| Q32 | varchar |  |  | SI | Have you, or anyone in your family, been diagnosed... |
| Q33 | varchar |  |  | SI | Have you anything in your medical, personal or soc... |
| Q34 | varchar |  |  | SI | If yes to any of the above please detail |
| Q35 | varchar |  |  | SI | To my knowledge the above information is accurate |
| Q36 | longvarbinary |  |  | SI | Patient signature area |
| Q36UDt | date |  |  | SI | Patient signature area Last Updated Date |
| Q36UTm | time |  |  | SI | Patient signature area Last Updated Time |
| Q37 | varchar |  |  | SI | Is the patient taking blood thinners? |
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