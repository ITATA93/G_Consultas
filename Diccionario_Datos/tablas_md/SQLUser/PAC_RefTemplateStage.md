# SQLUser.PAC_RefTemplateStage

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STG_ParRef | bigint | PK |  | NO | PAC_RefTemplate Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of starting Peritoneal Dialysis (PD) |
| Q04 | - |  |  | SI | Type of dialysis |
| Q05 | - |  |  | SI | Number of exchanges |
| Q06 | - |  |  | SI | Total volume (ml) |
| Q07 | - |  |  | SI | Type of PD solutions |
| Q08 | - |  |  | SI | Type |
| Q09 | - |  |  | SI | Total volume (ml) |
| Q10 | - |  |  | SI | If on tidal specify % |
| Q11 | - |  |  | SI | Duration of night therapy |
| Q12 | - |  |  | SI | Number of night cycles |
| Q13 | - |  |  | SI | Total volume (ml) |
| Q14 | - |  |  | SI | Volume / solution of last fill |
| Q15 | - |  |  | SI | Volume / solution of day exchange (if applicable) |
| Q17 | - |  |  | SI | PD: compliance |
| Q18 | - |  |  | SI | If compliance poor (specify) |
| Q19 | - |  |  | SI | PD: bowel movements |
| Q20 | - |  |  | SI | If bowel movements Poor (specify) |
| Q21 | - |  |  | SI | PD: catheter status |
| Q22 | - |  |  | SI | PD: catheter dressing |
| Q23 | - |  |  | SI | If catheter dressing wet and dirty (describe) |
| Q24 | - |  |  | SI | PD: titanium adapter |
| Q25 | - |  |  | SI | If titanium adapter poor (specify) |
| Q26 | - |  |  | SI | Symptoms of peritonitis |
| Q27 | - |  |  | SI | If peritonitis present (describe) |
| Q28 | - |  |  | SI | PD: extension set well maintained |
| Q29 | - |  |  | SI | PD: extension set last time changed |
| Q30 | - |  |  | SI | PD: extension set poor |
| Q31 | - |  |  | SI | PD: exit site |
| Q33 | - |  |  | SI | Comments |
| Q34 | - |  |  | SI | If catheter dressing wet and dirty (describe) |
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
| STG_Childsub | double |  |  | NO | Childsub |
| STG_CreatedDate | date |  |  | SI | Created Date |
| STG_CreatedTime | time |  |  | SI | Created Time |
| STG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STG_RowId | varchar |  |  | NO | - |
| STG_SequenceNumber | double |  |  | SI | SequenceNumber  |
| STG_StartUponEndOf_DR | varchar |  | FK | SI | Start Upon End Of - DO NOT USE - replaced by PARef... |
| STG_Template_DR | bigint |  | FK | SI | Des Ref Template |
| STG_UpdatedDate | date |  |  | SI | Updated Date |
| STG_UpdatedTime | time |  |  | SI | Updated Time |
| STG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*