# SQLUser.CT_TaskAssignGroupUsers

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| USER_ParRef | bigint | PK |  | NO | CT_TaskAssignGroup Parent Reference |
| Q01 | - |  |  | SI | Facility |
| Q02 | - |  |  | SI | Department |
| Q03 | - |  |  | SI | Admission diagnosis |
| Q04 | - |  |  | SI | Date admitted |
| Q05 | - |  |  | SI | Date readmitted |
| Q06 | - |  |  | SI | Date of discharge |
| Q07 | - |  |  | SI | Date of onset |
| Q08 | - |  |  | SI | Attending physician |
| Q09 | - |  |  | SI | Infection detected on |
| Q10 | - |  |  | SI | Location |
| Q11 | - |  |  | SI | Central line |
| Q12 | - |  |  | SI | Central line type |
| Q13 | - |  |  | SI | Central line (including umbilical catheter) |
| Q14 | - |  |  | SI | Birth weight (g) |
| Q15 | - |  |  | SI | Reason for device insertion |
| Q16 | - |  |  | SI | Location of device Insertion |
| Q16ObsDR | - |  |  | SI | Location of device Insertion DR |
| Q17 | - |  |  | SI | Hemodialysis catheter present |
| Q18 | - |  |  | SI | Date of device insertion |
| Q19 | - |  |  | SI | Date device removed |
| Q20 | - |  |  | SI | Event details |
| Q21 | - |  |  | SI | Criteria used |
| Q22 | - |  |  | SI | Any patient |
| Q23 | - |  |  | SI | ≤ 1 year old |
| Q24 | - |  |  | SI | Laboratory |
| Q25 | - |  |  | SI | Clinical diagnosis |
| Q26 | - |  |  | SI | Pathogens identified |
| Q27 | - |  |  | SI | Patient status |
| Q28 | - |  |  | SI | HAI confirmed by the attending physician |
| Q29 | - |  |  | SI | Investigation |
| Q30 | - |  |  | SI | • Bloodstream infection is a serious infection req... |
| Q31 | - |  |  | SI | • Bloodstream Infection Surveillance allows clinic... |
| Q32 | - |  |  | SI | • The questionnaire allows documentation of when t... |
| Q33 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Time |
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
| USER_Childsub | double |  |  | NO | Childsub |
| USER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| USER_CreatedDate | date |  |  | SI | Created Date |
| USER_CreatedTime | time |  |  | SI | Created Time |
| USER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| USER_RowId | varchar |  |  | NO | - |
| USER_UpdatedDate | date |  |  | SI | Updated Date |
| USER_UpdatedTime | time |  |  | SI | Updated Time |
| USER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| USER_User_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*