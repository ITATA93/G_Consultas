# SQLUser.CT_LocHealthSpecCode

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HSPC_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| HSPC_Childsub | double |  |  | NO | Childsub |
| HSPC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HSPC_CreatedDate | date |  |  | SI | Created Date |
| HSPC_CreatedTime | time |  |  | SI | Created Time |
| HSPC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HSPC_DateFrom | date |  |  | SI | Date From |
| HSPC_DateTo | date |  |  | SI | Date To |
| HSPC_HealthSpecCode_DR | bigint |  | FK | NO | Des Ref CT_HealthSpecialtyCodes |
| HSPC_RowId | varchar |  |  | NO | - |
| HSPC_UpdatedDate | date |  |  | SI | Updated Date |
| HSPC_UpdatedTime | time |  |  | SI | Updated Time |
| HSPC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Systolic blood pressure |
| Q01ObsDR | - |  |  | SI | Systolic blood pressure DR |
| Q02 | - |  |  | SI | Diastolic blood pressure |
| Q02ObsDR | - |  |  | SI | Diastolic blood pressure DR |
| Q03 | - |  |  | SI | Urinalysis abnormalities |
| Q03ObsDR | - |  |  | SI | Urinalysis abnormalities DR |
| Q04 | - |  |  | SI | Oedema |
| Q04ObsDR | - |  |  | SI | Oedema DR |
| Q05 | - |  |  | SI | Urinalysis |
| Q05ObsDR | - |  |  | SI | Urinalysis DR |
| Q06 | - |  |  | SI | Presentation |
| Q06ObsDR | - |  |  | SI | Presentation DR |
| Q07 | - |  |  | SI | External cephalic version offered |
| Q07ObsDR | - |  |  | SI | External cephalic version offered DR |
| Q08 | - |  |  | SI | External cephalic version accepted |
| Q08ObsDR | - |  |  | SI | External cephalic version accepted DR |
| Q09 | - |  |  | SI | External cephalic version discussed / info given |
| Q09ObsDR | - |  |  | SI | External cephalic version discussed / info given D... |
| Q10 | - |  |  | SI | Details of external cephalic version procedure |
| Q11 | - |  |  | SI | Fundal height |
| Q11ObsDR | - |  |  | SI | Fundal height DR |
| Q12 | - |  |  | SI | Lie |
| Q12ObsDR | - |  |  | SI | Lie DR |
| Q13 | - |  |  | SI | Presentation / 5ths palpable |
| Q13ObsDR | - |  |  | SI | Presentation / 5ths palpable DR |
| Q14 | - |  |  | SI | Fetal heart rate |
| Q14ObsDR | - |  |  | SI | Fetal heart rate DR |
| Q15 | - |  |  | SI | Position |
| Q15ObsDR | - |  |  | SI | Position DR |
| Q16 | - |  |  | SI | Fetal movement felt |
| Q16ObsDR | - |  |  | SI | Fetal movement felt DR |
| Q17 | - |  |  | SI | Comments |
| Q18 | - |  |  | SI | Is follow-up to brief intervention required |
| Q18ObsDR | - |  |  | SI | Is follow-up to brief intervention required DR |
| Q19 | - |  |  | SI | Alcohol units per week - currently |
| Q19ObsDR | - |  |  | SI | Alcohol units per week - currently DR |
| Q20 | - |  |  | SI | Maximum units per day - currently |
| Q20ObsDR | - |  |  | SI | Maximum units per day - currently DR |
| Q21 | - |  |  | SI | Plans for care |
| Q22 | - |  |  | SI | Midwife countersigning |
| Q23 | - |  |  | SI | Gestation: Weeks |
| Q23ObsDR | - |  |  | SI | Gestation: Weeks DR |
| Q24 | - |  |  | SI | Weight in late pregnancy |
| Q24ObsDR | - |  |  | SI | Weight in late pregnancy DR |
| Q25 | - |  |  | SI | Has thrombosis risk changed |
| Q25ObsDR | - |  |  | SI | Has thrombosis risk changed DR |
| Q26 | - |  |  | SI | Urine Blood |
| Q26ObsDR | - |  |  | SI | Urine Blood DR |
| Q27 | - |  |  | SI | Urine Glucose |
| Q27ObsDR | - |  |  | SI | Urine Glucose DR |
| Q28 | - |  |  | SI | Urine Protein |
| Q28ObsDR | - |  |  | SI | Urine Protein DR |
| Q29 | - |  |  | SI | Urine Leukocytes |
| Q29ObsDR | - |  |  | SI | Urine Leukocytes DR |
| Q30 | - |  |  | SI | Urine Ketones |
| Q30ObsDR | - |  |  | SI | Urine Ketones DR |
| Q31 | - |  |  | SI | Gestation: Days |
| Q31ObsDR | - |  |  | SI | Gestation: Days DR |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
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