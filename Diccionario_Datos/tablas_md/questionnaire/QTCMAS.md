# questionnaire.QTCMAS

> Escala de Ashworth Modificada (MAS)

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Ashworth Modificada (MAS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Codo |
| Q02 | varchar |  |  | SI | Start position: Elbow fully flexed, forearm neutra... |
| Q03 | varchar |  |  | SI | Movement: Extend elbow from maximum possible flexi... |
| Q04 | varchar |  |  | SI | Wrist  |
| Q05 | varchar |  |  | SI | Start position: Elbow as straight as possible, for... |
| Q06 | varchar |  |  | SI | Movement: Extend the patient&#39;s wrist from maxi... |
| Q07 | varchar |  |  | SI | Fingers |
| Q08 | varchar |  |  | SI | Start position: Elbow as straight as possible, for... |
| Q09 | varchar |  |  | SI | Movement: Extend the patient&#39;s fingers from ma... |
| Q10 | varchar |  |  | SI | Thumb |
| Q11 | varchar |  |  | SI | Start position: Elbow as straight as possible, for... |
| Q12 | varchar |  |  | SI | Movement: Extend the thumb from maximum possible (... |
| Q13 | varchar |  |  | SI | Hamstrings |
| Q14 | varchar |  |  | SI | Start position: Prone so that ankle falls beyond e... |
| Q15 | varchar |  |  | SI | Movement: Extend the patient&#39;s knee from maxim... |
| Q16 | varchar |  |  | SI | Quadriceps |
| Q17 | varchar |  |  | SI | Start position: Prone so that ankle falls beyond e... |
| Q18 | varchar |  |  | SI | Movement: Flex the patient&#39;s limb from maximum... |
| Q19 | varchar |  |  | SI | Gastrocnemius |
| Q20 | varchar |  |  | SI | Start position: Supine, ankle plantarflexed, hip i... |
| Q21 | varchar |  |  | SI | Movement: Dorsiflex the patient&#39;s ankle from m... |
| Q22 | varchar |  |  | SI | Soleus |
| Q23 | varchar |  |  | SI | Start position: Supine, ankle plantarflexed, hip i... |
| Q24 | varchar |  |  | SI | Movement: Dorsiflex the patient&#39;s ankle from m... |
| Q25 | varchar |  |  | SI | Positions |
| Q26 | varchar |  |  | SI | Scoring |
| Q27 | varchar |  |  | SI | 0 = Normal tone, no increase in tone |
| Q28 | varchar |  |  | SI | 1 = Slight increase in muscle tone, manifested by ... |
| Q29 | varchar |  |  | SI | +1 = Slight increase in muscle tone, manifested by... |
| Q30 | varchar |  |  | SI | 2 = More marked increase in muscle tone through mo... |
| Q31 | varchar |  |  | SI | 3 = Considerable increase in muscle tone, passive ... |
| Q32 | varchar |  |  | SI | 4 = Affected part(s) rigid in flexion or extension |
| Q33 | varchar |  |  | SI | Elbow |
| Q34 | varchar |  |  | SI | Wrist |
| Q35 | varchar |  |  | SI | Finger |
| Q36 | varchar |  |  | SI | Pulgar |
| Q37 | varchar |  |  | SI | Hamstrings |
| Q38 | varchar |  |  | SI | Quadriceps |
| Q39 | varchar |  |  | SI | Gastrocnemius |
| Q40 | varchar |  |  | SI | Soleus |
| Q41 | date |  |  | SI | Date |
| Q42 | time |  |  | SI | Time |
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