# questionnaire.QTCDAP

> Developmental Assessment of Play

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Developmental Assessment of Play

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Parents |
| Q04 | varchar |  |  | SI | Cognition |
| Q05 | varchar |  |  | SI | Language |
| Q06 | varchar |  |  | SI | Other |
| Q07 | varchar |  |  | SI | Observations / Comments |
| Q08 | varchar |  |  | SI | I. Sensorimotor–Exploratory (emerging 2 to 4 month... |
| Q09 | varchar |  |  | SI | • Reaching, grasping, holding, rubbing, mouthing o... |
| Q10 | varchar |  |  | SI | • Holding and looking at objects |
| Q11 | varchar |  |  | SI | • Repetitive pounding / hitting of objects |
| Q12 | varchar |  |  | SI | II. Relational–Non-functional (emerging 6 to 10 mo... |
| Q13 | varchar |  |  | SI | • Relating objects one to another without regard f... |
| Q14 | varchar |  |  | SI | • Holding two or more objects |
| Q15 | varchar |  |  | SI | • Stacking, bumping, nesting, touching, pushing ob... |
| Q16 | varchar |  |  | SI | • Offering objects to, and taking objects from, ot... |
| Q17 | varchar |  |  | SI | III. Functional–Conventional (emerging 10 to 12 mo... |
| Q18 | varchar |  |  | SI | • Relating objects one to another in a social–conv... |
| Q19 | varchar |  |  | SI | • Typical, functional, conventional, social use of... |
| Q20 | varchar |  |  | SI | (e.g., drinking from a cup, pushing a toy car, fee... |
| Q21 | varchar |  |  | SI | IV. symbolic (emerging 12 to 18 months) |
| Q22 | varchar |  |  | SI | Agent |
| Q23 | varchar |  |  | SI | Self (emerging 12 to 18 months) |
| Q24 | varchar |  |  | SI | • Child is the initiating agent of the play action... |
| Q25 | varchar |  |  | SI | Passive-Other (emerging 18 to 24 months) |
| Q26 | varchar |  |  | SI | • Child acts on nonanimated substitute agents—puts... |
| Q27 | varchar |  |  | SI | puts telephone up to doll’s or teddy bear’s ear an... |
| Q28 | varchar |  |  | SI | Active-Other (emerging 24 to 30 months) |
| Q29 | varchar |  |  | SI | • Child adds animacy to substitute agents—puts cup... |
| Q30 | varchar |  |  | SI | may make “drinking” sounds for the substitute agen... |
| Q31 | varchar |  |  | SI | Instrument |
| Q32 | varchar |  |  | SI | Realistic Object (emerging 10 to 12 months) |
| Q33 | varchar |  |  | SI | • Typical, functional, conventional, social use of... |
| Q34 | varchar |  |  | SI | (e.g., drinking from cup, pushing a toy car, feedi... |
| Q35 | varchar |  |  | SI | Substitute Object (emerging 18 to 24 months) |
| Q36 | varchar |  |  | SI | • Use of another object as a substitute for the st... |
| Q37 | varchar |  |  | SI | Imaginary Object (emerging 24 to 30 months) |
| Q38 | varchar |  |  | SI | • Performance of an object-action scheme without t... |
| Q39 | varchar |  |  | SI | Scheme |
| Q40 | varchar |  |  | SI | Single (emerging 12 to 18 months) |
| Q41 | varchar |  |  | SI | • Child carries out a single play act, such as put... |
| Q42 | varchar |  |  | SI | Multiple (emerging 18 to 24 months) |
| Q43 | varchar |  |  | SI | • Child carries out a sequence of two or more play... |
| Q44 | varchar |  |  | SI | pretending to drink from a cup and eat off of a pl... |
| Q45 | varchar |  |  | SI | Complex / Planned (emerging 30 months) |
| Q46 | varchar |  |  | SI | Other comments |
| Q47 | varchar |  |  | SI | Laying out the dishes and doll for a pretend snack... |
| Q48 | varchar |  |  | SI | Casby MW. Developmental Assessment of Play. Commun... |
| Q49 | varchar |  |  | SI | • Relating objects one to another in a social–conv... |
| Q50 | varchar |  |  | SI | I. Sensorimotor–Exploratory (emerging 2 to 4 month... |
| Q51 | varchar |  |  | SI | II. Relational–Non-functional (emerging 6 to 10 mo... |
| Q52 | varchar |  |  | SI | III. Functional–Conventional (emerging 10 to 12 mo... |
| Q53 | varchar |  |  | SI | Agent |
| Q54 | varchar |  |  | SI | Instrument |
| Q55 | varchar |  |  | SI | Scheme |
| Q56 | varchar |  |  | SI | Other comments |
| Q57 | varchar |  |  | SI | Other comments |
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