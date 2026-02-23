# SQLUser.PAC_RefTemplateStageEvAlND

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NUMD_ParRef | varchar | PK |  | NO | PAC_RefTemplateStage Parent Reference |
| ChildQ32DR | - |  |  | SI | Child Reference: Line change details |
| NUMD_Childsub | double |  |  | NO | Childsub |
| NUMD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NUMD_CreatedDate | date |  |  | SI | Created Date |
| NUMD_CreatedTime | time |  |  | SI | Created Time |
| NUMD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NUMD_NumberOfDays | double |  |  | SI | NumberOfDays |
| NUMD_RowId | varchar |  |  | NO | - |
| NUMD_State_DR | bigint |  | FK | SI | Des Ref Sate |
| NUMD_UpdatedDate | date |  |  | SI | Updated Date |
| NUMD_UpdatedTime | time |  |  | SI | Updated Time |
| NUMD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Informed consent obtained from patient |
| Q04 | - |  |  | SI | Assembled all necessary equipment |
| Q05 | - |  |  | SI | Insertion site assessed and marked if appropriate |
| Q06 | - |  |  | SI | Barrier precautions used |
| Q07 | - |  |  | SI | Patient positioned correctly |
| Q08 | - |  |  | SI | Skin disinfected correctly |
| Q09 | - |  |  | SI | Hair removal, if required, using disposable clippe... |
| Q10 | - |  |  | SI | Skin preparation used |
| Q11 | - |  |  | SI | Catheter flushed before insertion |
| Q12 | - |  |  | SI | Pre-procedure notes |
| Q13 | - |  |  | SI | Date inserted |
| Q14 | - |  |  | SI | Time inserted |
| Q15 | - |  |  | SI | Insertion technique |
| Q16 | - |  |  | SI | Peritoneal Dialysis (PD) catheter type |
| Q17 | - |  |  | SI | PD catheter length |
| Q18 | - |  |  | SI | Other PD catheter length (cm) |
| Q19 | - |  |  | SI | Laterality of exit site |
| Q20 | - |  |  | SI | Anaesthesia |
| Q21 | - |  |  | SI | Pneumoperitoneum needle |
| Q22 | - |  |  | SI | Other needle (g) |
| Q23 | - |  |  | SI | Guidewire |
| Q24 | - |  |  | SI | Other guidewire (inch) |
| Q25 | - |  |  | SI | Exit site dressing attended to |
| Q26 | - |  |  | SI | Flush completed |
| Q27 | - |  |  | SI | Complications |
| Q28 | - |  |  | SI | Other complication notes |
| Q29 | - |  |  | SI | Procedure outcome	 |
| Q30 | - |  |  | SI | Insertion notes |
| Q31 | - |  |  | SI | Inserted by |
| Q33 | - |  |  | SI | Date of removal |
| Q34 | - |  |  | SI | Time of removal |
| Q35 | - |  |  | SI | Reason for removal	 |
| Q36 | - |  |  | SI | Removal notes |
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