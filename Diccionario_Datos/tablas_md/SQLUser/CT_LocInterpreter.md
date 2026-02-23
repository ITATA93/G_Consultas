# SQLUser.CT_LocInterpreter

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INTERP_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| INTERP_Childsub | double |  |  | NO | Childsub |
| INTERP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INTERP_CreatedDate | date |  |  | SI | Created Date |
| INTERP_CreatedTime | time |  |  | SI | Created Time |
| INTERP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INTERP_DateFrom | date |  |  | SI | Date From |
| INTERP_DateTo | date |  |  | SI | Date To |
| INTERP_Interpreter_DR | bigint |  | FK | SI | Des Ref Interpreter |
| INTERP_RowId | varchar |  |  | NO | - |
| INTERP_UpdatedDate | date |  |  | SI | Updated Date |
| INTERP_UpdatedTime | time |  |  | SI | Updated Time |
| INTERP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Is the patient receiving anticoagulants? |
| Q02 | - |  |  | SI | Ensure this is documented on Medications chart |
| Q03 | - |  |  | SI | Current Treatment	 |
| Q04 | - |  |  | SI | Problems with Appetite 	 |
| Q05 | - |  |  | SI | Issues / Concerns 	 |
| Q06 | - |  |  | SI | Problems with Breathlessness |
| Q07 | - |  |  | SI | Issues / Concerns 	 |
| Q08 | - |  |  | SI | Problems with Bowels / Urine	 |
| Q09 | - |  |  | SI | Issues / Concerns 	 |
| Q10 | - |  |  | SI | Problems with Nausea and Vomiting |
| Q11 | - |  |  | SI | Issues / Concerns |
| Q12 | - |  |  | SI | Problems with Pain |
| Q13 | - |  |  | SI | Issues / Concerns |
| Q14 | - |  |  | SI | Problems with Sleep |
| Q15 | - |  |  | SI | Issues / Concerns 	 |
| Q16 | - |  |  | SI | Problems with Fatigue |
| Q17 | - |  |  | SI | Issues / Concerns |
| Q18 | - |  |  | SI | General Assessment / Key Concerns	 |
| Q19 | - |  |  | SI | Document patients understanding of Ascites	 |
| Q20 | - |  |  | SI | Date of Admission 	 |
| Q21 | - |  |  | SI | Reason for Admission	 |
| Q22 | - |  |  | SI | Plan |
| Q23 | - |  |  | SI | Home Circumstances 	 |
| Q24 | - |  |  | SI | Support At Home |
| Q25 | - |  |  | SI | Key Concerns	 |
| Q26 | - |  |  | SI | Referrals needed	 |
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