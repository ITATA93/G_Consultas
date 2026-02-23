# SQLUser.LBC_InstrumentTestItemResultTrans

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCINTIT_ParRef | varchar | PK |  | NO | Parent instrument DR |
| LBCINTIT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCINTIT_DateFrom | date |  |  | SI | Date From |
| LBCINTIT_DateTo | date |  |  | SI | Date To |
| LBCINTIT_InstrumentResult | varchar |  |  | SI | Instrument result |
| LBCINTIT_InstrumentResultFrom | varchar |  |  | SI | Instrument Result From |
| LBCINTIT_InstrumentResultTo | varchar |  |  | SI | Instrument Result To |
| LBCINTIT_Result | varchar |  |  | SI | Internal result |
| LBCINTIT_RowID | varchar |  |  | NO | - |
| Q1 | - |  |  | SI | ¿Se considera satisfecho de su vida? |
| Q10 | - |  |  | SI | ¿Siente que tiene más problemas con su memoria que... |
| Q11 | - |  |  | SI | ¿Piensa que es maravilloso estar vivo? |
| Q12 | - |  |  | SI | ¿Se siente muy inútil como está en este momento? |
| Q13 | - |  |  | SI | ¿Se siente lleno de energías? |
| Q14 | - |  |  | SI | ¿Siente su situación como sin esperanzas? |
| Q15 | - |  |  | SI | ¿Cree que la mayoría está mejor que usted? |
| Q17 | - |  |  | SI | Resultado de Escala de Depresión Geriátrica |
| Q17ObsDR | - |  |  | SI | Resultado de Escala de Depresión Geriátrica DR |
| Q2 | - |  |  | SI | ¿Ha ido abandonando muchas de sus actividades e in... |
| Q3 | - |  |  | SI | ¿Se aburre a menudo? |
| Q4 | - |  |  | SI | ¿Siente que su vida está vacía? |
| Q5 | - |  |  | SI | ¿Está de buen ánimo la mayor parte del tiempo? |
| Q6 | - |  |  | SI | ¿Tiene miedo que le pueda ocurrir algo malo? |
| Q7 | - |  |  | SI | ¿Está contento la mayor parte del tiempo? |
| Q8 | - |  |  | SI | ¿Se siente a menudo desvalido? |
| Q9 | - |  |  | SI | ¿Prefiere quedarse en casa en vez de hacer otras c... |
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