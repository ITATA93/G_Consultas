# SQLUser.PA_ConsultFactors

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONSFACT_RowID | bigint | PK |  | NO | - |
| CONSFACT_Code | varchar |  |  | NO | - |
| CONSFACT_CreatedDate | date |  |  | SI | CreatedDate |
| CONSFACT_CreatedTime | time |  |  | SI | CreatedTime |
| CONSFACT_CreatedUser_DR | bigint |  | FK | SI | Des Ref CreatedUser |
| CONSFACT_DateFrom | date |  |  | SI | From Date |
| CONSFACT_DateTo | date |  |  | SI | To Date |
| CONSFACT_Desc | varchar |  |  | SI | - |
| CONSFACT_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| CONSFACT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| CONSFACT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| CONSFACT_MRAdm_DR | bigint |  | FK | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Presence of uterus |
| Q03ObsDR | - |  |  | SI | Presence of uterus DR |
| Q04 | - |  |  | SI | POP-Q: Point Aa |
| Q04ObsDR | - |  |  | SI | POP-Q: Point Aa DR |
| Q05 | - |  |  | SI | POP-Q: Point Ba |
| Q05ObsDR | - |  |  | SI | POP-Q: Point Ba DR |
| Q06 | - |  |  | SI | POP-Q: Point C |
| Q06ObsDR | - |  |  | SI | POP-Q: Point C DR |
| Q07 | - |  |  | SI | POP-Q: Point D |
| Q07ObsDR | - |  |  | SI | POP-Q: Point D DR |
| Q08 | - |  |  | SI | POP-Q: Point Bp |
| Q08ObsDR | - |  |  | SI | POP-Q: Point Bp DR |
| Q09 | - |  |  | SI | POP-Q: Point Ap |
| Q09ObsDR | - |  |  | SI | POP-Q: Point Ap DR |
| Q10 | - |  |  | SI | POP-Q: Total vaginal length |
| Q10ObsDR | - |  |  | SI | POP-Q: Total vaginal length DR |
| Q11 | - |  |  | SI | POP-Q: Genital hiatus |
| Q11ObsDR | - |  |  | SI | POP-Q: Genital hiatus DR |
| Q12 | - |  |  | SI | POP-Q: Perineal body |
| Q12ObsDR | - |  |  | SI | POP-Q: Perineal body DR |
| Q13 | - |  |  | SI | POP-Q: Staging of pelvic organ prolapse |
| Q13ObsDR | - |  |  | SI | POP-Q: Staging of pelvic organ prolapse DR |
| Q14 | - |  |  | SI | POP-Q notes |
| Q15 | - |  |  | SI | Baden - Walker |
| Q16 | - |  |  | SI | BW: Anterior vagina |
| Q16ObsDR | - |  |  | SI | BW: Anterior vagina DR |
| Q17 | - |  |  | SI | BW: Posterior vagina |
| Q17ObsDR | - |  |  | SI | BW: Posterior vagina DR |
| Q18 | - |  |  | SI | BW: Cervico / uterine (or vaginal cuff, post hyste... |
| Q18ObsDR | - |  |  | SI | BW: Cervico / uterine (or vaginal cuff, post hyste... |
| Q19 | - |  |  | SI | Baden-Walker notes |
| Q20 | - |  |  | SI | Prolapse / Pelvic Floor Assessment |
| Q21 | - |  |  | SI | Cough stress test |
| Q22 | - |  |  | SI | Cough stress test notes |
| Q23 | - |  |  | SI | Evidence of vaginal atrophy |
| Q24 | - |  |  | SI | Vaginal atrophy notes |
| Q25 | - |  |  | SI | Digital assessment pelvic floor strength |
| Q26 | - |  |  | SI | Maximum duration of squeeze - before fatigue (seco... |
| Q27 | - |  |  | SI | Pelvic floor strength notes |
| Q28 | - |  |  | SI | Anal sphincter tone |
| Q29 | - |  |  | SI | Anal sphincter strength |
| Q30 | - |  |  | SI | Anal sphincter notes |
| Q31 | - |  |  | SI | Lateral vaginal wall detachments |
| Q32 | - |  |  | SI | Detachments notes |
| Q33 | - |  |  | SI | Notes |
| Q34 | - |  |  | SI | Pelvic Organ Prolapse Quantification System (POP-Q... |
| Q35 | - |  |  | SI | Bump RC, Mattiasson A, Bø K, Brubaker LP, DeLancey... |
| Q36 | - |  |  | SI | Baden-Walker system |
| Q37 | - |  |  | SI | Baden WF, Walker T. Surgical Repair of Vaginal Def... |
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