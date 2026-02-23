# SQLUser.LBC_ModeOfTransport

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCMOT_RowID | bigint | PK |  | NO | - |
| LBCMOT_Code | varchar |  |  | NO | Code |
| LBCMOT_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCMOT_CreatedDate | date |  |  | SI | Created Date |
| LBCMOT_CreatedTime | time |  |  | SI | Created Time |
| LBCMOT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCMOT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCMOT_DateTo | date |  |  | SI | Last day the record is active |
| LBCMOT_Desc | varchar |  |  | NO | Description |
| LBCMOT_Owner | varchar |  |  | SI | Owner |
| LBCMOT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCMOT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCMOT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Parents |
| Q04 | - |  |  | SI | Cognition |
| Q05 | - |  |  | SI | Language |
| Q06 | - |  |  | SI | Other |
| Q07 | - |  |  | SI | Observations / Comments |
| Q08 | - |  |  | SI | I. Sensorimotor–Exploratory (emerging 2 to 4 month... |
| Q09 | - |  |  | SI | • Reaching, grasping, holding, rubbing, mouthing o... |
| Q10 | - |  |  | SI | • Holding and looking at objects |
| Q11 | - |  |  | SI | • Repetitive pounding / hitting of objects |
| Q12 | - |  |  | SI | II. Relational–Non-functional (emerging 6 to 10 mo... |
| Q13 | - |  |  | SI | • Relating objects one to another without regard f... |
| Q14 | - |  |  | SI | • Holding two or more objects |
| Q15 | - |  |  | SI | • Stacking, bumping, nesting, touching, pushing ob... |
| Q16 | - |  |  | SI | • Offering objects to, and taking objects from, ot... |
| Q17 | - |  |  | SI | III. Functional–Conventional (emerging 10 to 12 mo... |
| Q18 | - |  |  | SI | • Relating objects one to another in a social–conv... |
| Q19 | - |  |  | SI | • Typical, functional, conventional, social use of... |
| Q20 | - |  |  | SI | (e.g., drinking from a cup, pushing a toy car, fee... |
| Q21 | - |  |  | SI | IV. symbolic (emerging 12 to 18 months) |
| Q22 | - |  |  | SI | Agent |
| Q23 | - |  |  | SI | Self (emerging 12 to 18 months) |
| Q24 | - |  |  | SI | • Child is the initiating agent of the play action... |
| Q25 | - |  |  | SI | Passive-Other (emerging 18 to 24 months) |
| Q26 | - |  |  | SI | • Child acts on nonanimated substitute agents—puts... |
| Q27 | - |  |  | SI | puts telephone up to doll’s or teddy bear’s ear an... |
| Q28 | - |  |  | SI | Active-Other (emerging 24 to 30 months) |
| Q29 | - |  |  | SI | • Child adds animacy to substitute agents—puts cup... |
| Q30 | - |  |  | SI | may make “drinking” sounds for the substitute agen... |
| Q31 | - |  |  | SI | Instrument |
| Q32 | - |  |  | SI | Realistic Object (emerging 10 to 12 months) |
| Q33 | - |  |  | SI | • Typical, functional, conventional, social use of... |
| Q34 | - |  |  | SI | (e.g., drinking from cup, pushing a toy car, feedi... |
| Q35 | - |  |  | SI | Substitute Object (emerging 18 to 24 months) |
| Q36 | - |  |  | SI | • Use of another object as a substitute for the st... |
| Q37 | - |  |  | SI | Imaginary Object (emerging 24 to 30 months) |
| Q38 | - |  |  | SI | • Performance of an object-action scheme without t... |
| Q39 | - |  |  | SI | Scheme |
| Q40 | - |  |  | SI | Single (emerging 12 to 18 months) |
| Q41 | - |  |  | SI | • Child carries out a single play act, such as put... |
| Q42 | - |  |  | SI | Multiple (emerging 18 to 24 months) |
| Q43 | - |  |  | SI | • Child carries out a sequence of two or more play... |
| Q44 | - |  |  | SI | pretending to drink from a cup and eat off of a pl... |
| Q45 | - |  |  | SI | Complex / Planned (emerging 30 months) |
| Q46 | - |  |  | SI | Other comments |
| Q47 | - |  |  | SI | Laying out the dishes and doll for a pretend snack... |
| Q48 | - |  |  | SI | Casby MW. Developmental Assessment of Play. Commun... |
| Q49 | - |  |  | SI | • Relating objects one to another in a social–conv... |
| Q50 | - |  |  | SI | I. Sensorimotor–Exploratory (emerging 2 to 4 month... |
| Q51 | - |  |  | SI | II. Relational–Non-functional (emerging 6 to 10 mo... |
| Q52 | - |  |  | SI | III. Functional–Conventional (emerging 10 to 12 mo... |
| Q53 | - |  |  | SI | Agent |
| Q54 | - |  |  | SI | Instrument |
| Q55 | - |  |  | SI | Scheme |
| Q56 | - |  |  | SI | Other comments |
| Q57 | - |  |  | SI | Other comments |
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