# questionnaire.QTCRAIC

> Regional Anaesthesia Insertion and Care

**Schema:** questionnaire
**Columnas:** 127
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Regional Anaesthesia Insertion and Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Regional anaesthetic type |
| Q04 | varchar |  |  | SI | Indication |
| Q05 | varchar |  |  | SI | Other indication |
| Q06 | varchar |  |  | SI | Relevant history |
| Q07 | varchar |  |  | SI | Patient identified |
| Q08 | varchar |  |  | SI | Procedure, risks, benefits and alternatives discus... |
| Q09 | varchar |  |  | SI | Informed consent obtained |
| Q10 | varchar |  |  | SI | Intravascular access in situ |
| Q11 | varchar |  |  | SI | Site marked |
| Q12 | varchar |  |  | SI | Barrier precautions in place |
| Q13 | varchar |  |  | SI | Skin preparation |
| Q14 | varchar |  |  | SI | Other skin preparation |
| Q15 | varchar |  |  | SI | Monitoring in situ |
| Q16 | varchar |  |  | SI | Other monitoring |
| Q17 | varchar |  |  | SI | Level of sedation  |
| Q18 | varchar |  |  | SI | Pre-procedure notes |
| Q19 | date |  |  | SI | Date of insertion |
| Q20 | time |  |  | SI | Time of insertion |
| Q21 | varchar |  |  | SI | Patient position |
| Q22 | varchar |  |  | SI | Other position |
| Q23 | varchar |  |  | SI | Level of insertion |
| Q24 | varchar |  |  | SI | Other level of insertion |
| Q25 | varchar |  |  | SI | Peripheral nerve block type |
| Q26 | varchar |  |  | SI | Peripheral nerve block details |
| Q27 | varchar |  |  | SI | Laterality |
| Q28 | varchar |  |  | SI | Surface landmark |
| Q29 | varchar |  |  | SI | Technique used |
| Q30 | varchar |  |  | SI | Other technique |
| Q31 | numeric |  |  | SI | Current (mA) |
| Q32 | varchar |  |  | SI | Technique details |
| Q33 | varchar |  |  | SI | Ultrasound guidance used |
| Q34 | varchar |  |  | SI | Epidural needle type |
| Q35 | varchar |  |  | SI | Other epidural needle type  |
| Q36 | varchar |  |  | SI | Epidural needle size |
| Q37 | varchar |  |  | SI | Other epidural needle size |
| Q38 | numeric |  |  | SI | Epidural needle length (mm) |
| Q39 | numeric |  |  | SI | Depth of space (cm) |
| Q40 | varchar |  |  | SI | Loss of resistance |
| Q41 | varchar |  |  | SI | Spinal needle type |
| Q42 | varchar |  |  | SI | Other spinal needle type  |
| Q43 | varchar |  |  | SI | Spinal needle size |
| Q44 | varchar |  |  | SI | Other spinal needle size |
| Q45 | numeric |  |  | SI | Catheter depth at skin (cm) |
| Q46 | varchar |  |  | SI | Test Dose |
| Q47 | varchar |  |  | SI | The following local anaesthetic documentation does... |
| Q48 | varchar |  |  | SI | Test dose anaesthetic |
| Q49 | varchar |  |  | SI | Other test dose anaesthetic |
| Q50 | varchar |  |  | SI | Vasoconstrictor added |
| Q51 | numeric |  |  | SI | Test dose concentration (%) |
| Q52 | numeric |  |  | SI | Test dose volume (mLs) |
| Q53 | varchar |  |  | SI | Test dose notes |
| Q54 | varchar |  |  | SI | Insertion and block performed by |
| Q55 | varchar |  |  | SI | Insertion notes |
| Q56 | varchar |  |  | SI | Assessment |
| Q57 | varchar |  |  | SI | This section is for documenting assessment of the ... |
| Q59 | date |  |  | SI | Removal date |
| Q60 | time |  |  | SI | Removal time |
| Q61 | varchar |  |  | SI | Removal reason |
| Q62 | varchar |  |  | SI | Other removal reason |
| Q63 | varchar |  |  | SI | Catheter tip intact on removal |
| Q64 | varchar |  |  | SI | Catheter tip sent for microbiology culture |
| Q65 | varchar |  |  | SI | Removal notes |
| Q66 | varchar |  |  | SI | Removed by  |
| Q67 | varchar |  |  | SI | Complications |
| Q68 | varchar |  |  | SI | Other complications  |
| Q69 | varchar |  |  | SI | Complication notes |
| Q70 | varchar |  |  | SI | Removal Details |
| Q71 | varchar |  |  | SI | Risks explained |
| Q72 | varchar |  |  | SI | Other risks |
| Q73 | varchar |  |  | SI | Barrier precautions in place |
| Q74 | varchar |  |  | SI | Local anaesthetic notes |
| Q75 | varchar |  |  | SI | If yes to above, vasoconstrictor added via |
| Q76 | varchar |  |  | SI | Level of insertion -  spinal |
| Q77 | numeric |  |  | SI | Spinal needle length (mm) |
| Q78 | varchar |  |  | SI | Other peripheral nerve block |
| Q79 | numeric |  |  | SI | Depth to target (cm) |
| Q80 | numeric |  |  | SI | Number of passes |
| Q81 | varchar |  |  | SI | Assisted by |
| Q82 | varchar |  |  | SI | Supervising consultant |
| Q83 | varchar |  |  | SI | Block outcome |
| Q84 | varchar |  |  | SI | Removal checked by |
| Q85 | varchar |  |  | SI | Nerve group blocks |
| Q86 | varchar |  |  | SI | Interfascial blocks |
| Q87 | varchar |  |  | SI | Plexus nerve blocks |
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