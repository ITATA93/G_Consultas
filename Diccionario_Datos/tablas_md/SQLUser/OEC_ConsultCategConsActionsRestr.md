# SQLUser.OEC_ConsultCategConsActionsRestr

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESTR_ParRef | varchar | PK |  | NO | OEC_ConsultCateg Parent Reference |
| Q01 | - |  |  | SI | Weakness |
| Q01N | - |  |  | SI | Note |
| Q01Y | - |  |  | SI | If yes |
| Q03 | - |  |  | SI | Numbness or paresthesia |
| Q03N | - |  |  | SI | Note |
| Q03Y | - |  |  | SI | If yes |
| Q05 | - |  |  | SI | Impaired speech |
| Q05N | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Nausea or Vomiting |
| Q07N | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Headaches |
| Q09N | - |  |  | SI | Note |
| Q09Y | - |  |  | SI | If yes |
| Q11 | - |  |  | SI | Head injury |
| Q11N | - |  |  | SI | Note |
| Q11Y | - |  |  | SI | If yes |
| Q13 | - |  |  | SI | Fever |
| Q13N | - |  |  | SI | Note |
| Q15 | - |  |  | SI | Confusion |
| Q15N | - |  |  | SI | Note |
| Q17 | - |  |  | SI | Abnormal behaviour |
| Q17N | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Delusions or hallucinations |
| Q19N | - |  |  | SI | Note |
| Q21 | - |  |  | SI | Altered mood |
| Q21N | - |  |  | SI | Note |
| Q23 | - |  |  | SI | Syncope or loss of consciousness |
| Q23N | - |  |  | SI | Note |
| Q25 | - |  |  | SI | Seizure |
| Q25N | - |  |  | SI | Note |
| Q27 | - |  |  | SI | Gait abnormality |
| Q27N | - |  |  | SI | Note |
| Q29 | - |  |  | SI | Impaired memory |
| Q29N | - |  |  | SI | Note |
| Q31 | - |  |  | SI | Recent falls |
| Q31N | - |  |  | SI | Note |
| Q33 | - |  |  | SI | Excessive bleeding / bruising |
| Q33N | - |  |  | SI | Note |
| Q35 | - |  |  | SI | Taking aspirin or platelet inhibitor |
| Q35N | - |  |  | SI | Note |
| Q37 | - |  |  | SI | Taking anticoagulant |
| Q37N | - |  |  | SI | Note |
| Q43 | - |  |  | SI | Dizziness |
| Q43N | - |  |  | SI | Note |
| Q45 | - |  |  | SI | Date |
| Q46 | - |  |  | SI | Time |
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
| RESTR_AgeFrom | varchar |  |  | SI | Age From |
| RESTR_AgeTo | varchar |  |  | SI | AgeTo |
| RESTR_Childsub | double |  |  | NO | Childsub |
| RESTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESTR_CreatedDate | date |  |  | SI | Created Date |
| RESTR_CreatedTime | time |  |  | SI | Created Time |
| RESTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESTR_RowId | varchar |  |  | NO | - |
| RESTR_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| RESTR_UpdatedDate | date |  |  | SI | Updated Date |
| RESTR_UpdatedTime | time |  |  | SI | Updated Time |
| RESTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*