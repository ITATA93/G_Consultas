# questionnaire.QTCVPPFA

> Vaginal Prolapse and Pelvic Floor Assessment

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Vaginal Prolapse and Pelvic Floor Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Presence of uterus |
| Q03ObsDR | varchar |  | FK | SI | Presence of uterus DR |
| Q04 | varchar |  |  | SI | POP-Q: Point Aa |
| Q04ObsDR | varchar |  | FK | SI | POP-Q: Point Aa DR |
| Q05 | varchar |  |  | SI | POP-Q: Point Ba |
| Q05ObsDR | varchar |  | FK | SI | POP-Q: Point Ba DR |
| Q06 | varchar |  |  | SI | POP-Q: Point C |
| Q06ObsDR | varchar |  | FK | SI | POP-Q: Point C DR |
| Q07 | varchar |  |  | SI | POP-Q: Point D |
| Q07ObsDR | varchar |  | FK | SI | POP-Q: Point D DR |
| Q08 | varchar |  |  | SI | POP-Q: Point Bp |
| Q08ObsDR | varchar |  | FK | SI | POP-Q: Point Bp DR |
| Q09 | varchar |  |  | SI | POP-Q: Point Ap |
| Q09ObsDR | varchar |  | FK | SI | POP-Q: Point Ap DR |
| Q10 | varchar |  |  | SI | POP-Q: Total vaginal length |
| Q10ObsDR | varchar |  | FK | SI | POP-Q: Total vaginal length DR |
| Q11 | varchar |  |  | SI | POP-Q: Genital hiatus |
| Q11ObsDR | varchar |  | FK | SI | POP-Q: Genital hiatus DR |
| Q12 | varchar |  |  | SI | POP-Q: Perineal body |
| Q12ObsDR | varchar |  | FK | SI | POP-Q: Perineal body DR |
| Q13 | varchar |  |  | SI | POP-Q: Staging of pelvic organ prolapse |
| Q13ObsDR | varchar |  | FK | SI | POP-Q: Staging of pelvic organ prolapse DR |
| Q14 | varchar |  |  | SI | POP-Q notes |
| Q15 | varchar |  |  | SI | Baden - Walker |
| Q16 | varchar |  |  | SI | BW: Anterior vagina |
| Q16ObsDR | varchar |  | FK | SI | BW: Anterior vagina DR |
| Q17 | varchar |  |  | SI | BW: Posterior vagina |
| Q17ObsDR | varchar |  | FK | SI | BW: Posterior vagina DR |
| Q18 | varchar |  |  | SI | BW: Cervico / uterine (or vaginal cuff, post hyste... |
| Q18ObsDR | varchar |  | FK | SI | BW: Cervico / uterine (or vaginal cuff, post hyste... |
| Q19 | varchar |  |  | SI | Baden-Walker notes |
| Q20 | varchar |  |  | SI | Prolapse / Pelvic Floor Assessment |
| Q21 | varchar |  |  | SI | Cough stress test |
| Q22 | varchar |  |  | SI | Cough stress test notes |
| Q23 | varchar |  |  | SI | Evidence of vaginal atrophy |
| Q24 | varchar |  |  | SI | Vaginal atrophy notes |
| Q25 | varchar |  |  | SI | Digital assessment pelvic floor strength |
| Q26 | numeric |  |  | SI | Maximum duration of squeeze - before fatigue (seco... |
| Q27 | varchar |  |  | SI | Pelvic floor strength notes |
| Q28 | varchar |  |  | SI | Anal sphincter tone |
| Q29 | varchar |  |  | SI | Anal sphincter strength |
| Q30 | varchar |  |  | SI | Anal sphincter notes |
| Q31 | varchar |  |  | SI | Lateral vaginal wall detachments |
| Q32 | varchar |  |  | SI | Detachments notes |
| Q33 | varchar |  |  | SI | Notes |
| Q34 | varchar |  |  | SI | Pelvic Organ Prolapse Quantification System (POP-Q... |
| Q35 | varchar |  |  | SI | Bump RC, Mattiasson A, Bø K, Brubaker LP, DeLancey... |
| Q36 | varchar |  |  | SI | Baden-Walker system |
| Q37 | varchar |  |  | SI | Baden WF, Walker T. Surgical Repair of Vaginal Def... |
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