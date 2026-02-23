# questionnaire.QTCAHPAUACH

> Adult Audiology Case History

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Adult Audiology Case History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | General information |
| Q02 | varchar |  |  | SI | Marital status |
| Q03 | numeric |  |  | SI | Number of children |
| Q04 | varchar |  |  | SI | Occupation |
| Q05 | varchar |  |  | SI | Noise exposure |
| Q06 | varchar |  |  | SI | Primary reason for referral |
| Q07 | varchar |  |  | SI | Medical history |
| Q08 | varchar |  |  | SI | How long have you had this problem? |
| Q09 | varchar |  |  | SI | Have you previously consulted an Audiologist / ENT... |
| Q10 | date |  |  | SI | When |
| Q11 | varchar |  |  | SI | Where |
| Q12 | varchar |  |  | SI | Have you had any of the following in the last 90 d... |
| Q13 | varchar |  |  | SI | Are (were) you regularly exposed to loud noise?  |
| Q14 | varchar |  |  | SI | Are (were) you taking any of the following medicat... |
| Q15 | varchar |  |  | SI | Do (did) you have any of the following medical con... |
| Q16 | varchar |  |  | SI | Do you have a family history of hearing loss and/o... |
| Q17 | varchar |  |  | SI | Do you have an allergy towards any of the followin... |
| Q18 | varchar |  |  | SI | Hearing Loss and Communication |
| Q19 | varchar |  |  | SI | Do you have a known hearing loss? |
| Q20 | varchar |  |  | SI | Which ear is the better ear? |
| Q21 | varchar |  |  | SI | Do you currently use Hearing Aids? |
| Q22 | varchar |  |  | SI | Do they help? |
| Q23 | varchar |  |  | SI | Please specify |
| Q24 | varchar |  |  | SI | Does your difficulty in hearing restrict you from ... |
| Q25 | varchar |  |  | SI | How does your hearing difficulty affect others? (F... |
| Q26 | varchar |  |  | SI | Do you have a problem in the following situations? |
| Q27 | varchar |  |  | SI | Additional comments |
| Q28 | varchar |  |  | SI | Do you have known hearing loss? |
| Q29 | varchar |  |  | SI | Was the onset of hearing loss gradual or sudden? |
| Q30 | varchar |  |  | SI | Any blocked feeling / pressure inside the ear? |
| Q31 | varchar |  |  | SI | Any dizziness or vertigo? |
| Q32 | varchar |  |  | SI | Any ringing inside the ear? |
| Q33 | varchar |  |  | SI | Which ear? |
| Q34 | date |  |  | SI | Date |
| Q35 | time |  |  | SI | Time |
| Q36 | varchar |  |  | SI | Which ear is the better ear? |
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