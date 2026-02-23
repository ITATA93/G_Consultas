# questionnaire.QTCPDCIC

> Peritoneal Dialysis Catheter Insertion and Care

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Catheter Insertion and Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Informed consent obtained from patient |
| Q04 | varchar |  |  | SI | Assembled all necessary equipment |
| Q05 | varchar |  |  | SI | Insertion site assessed and marked if appropriate |
| Q06 | varchar |  |  | SI | Barrier precautions used |
| Q07 | varchar |  |  | SI | Patient positioned correctly |
| Q08 | varchar |  |  | SI | Skin disinfected correctly |
| Q09 | varchar |  |  | SI | Hair removal, if required, using disposable clippe... |
| Q10 | varchar |  |  | SI | Skin preparation used |
| Q11 | varchar |  |  | SI | Catheter flushed before insertion |
| Q12 | varchar |  |  | SI | Pre-procedure notes |
| Q13 | date |  |  | SI | Date inserted |
| Q14 | time |  |  | SI | Time inserted |
| Q15 | varchar |  |  | SI | Insertion technique |
| Q16 | varchar |  |  | SI | Peritoneal Dialysis (PD) catheter type |
| Q17 | varchar |  |  | SI | PD catheter length |
| Q18 | numeric |  |  | SI | Other PD catheter length (cm) |
| Q19 | varchar |  |  | SI | Laterality of exit site |
| Q20 | varchar |  |  | SI | Anaesthesia |
| Q21 | varchar |  |  | SI | Pneumoperitoneum needle |
| Q22 | numeric |  |  | SI | Other needle (g) |
| Q23 | varchar |  |  | SI | Guidewire |
| Q24 | numeric |  |  | SI | Other guidewire (inch) |
| Q25 | varchar |  |  | SI | Exit site dressing attended to |
| Q26 | varchar |  |  | SI | Flush completed |
| Q27 | varchar |  |  | SI | Complications |
| Q28 | varchar |  |  | SI | Other complication notes |
| Q29 | varchar |  |  | SI | Procedure outcome	 |
| Q30 | varchar |  |  | SI | Insertion notes |
| Q31 | varchar |  |  | SI | Inserted by |
| Q33 | date |  |  | SI | Date of removal |
| Q34 | time |  |  | SI | Time of removal |
| Q35 | varchar |  |  | SI | Reason for removal	 |
| Q36 | varchar |  |  | SI | Removal notes |
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