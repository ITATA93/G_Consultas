# SQLUser.ORC_OperationTypes

**Schema:** SQLUser
**Columnas:** 111
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPETYP_RowId | bigint | PK |  | NO | - |
| OPETYP_Code | varchar |  |  | NO | Code |
| OPETYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPETYP_CreatedDate | date |  |  | SI | Created Date |
| OPETYP_CreatedTime | time |  |  | SI | Created Time |
| OPETYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPETYP_DateFrom | date |  |  | SI | Date From |
| OPETYP_DateTo | date |  |  | SI | Date To |
| OPETYP_Desc | varchar |  |  | NO | Description |
| OPETYP_Owner | varchar |  |  | SI | Owner |
| OPETYP_UpdatedDate | date |  |  | SI | Updated Date |
| OPETYP_UpdatedTime | time |  |  | SI | Updated Time |
| OPETYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | This form is intended to be used for single pregna... |
| Q04 | - |  |  | SI | This form is intended for nulliparous patients at ... |
| Q05 | - |  |  | SI | Gravida |
| Q06 | - |  |  | SI | Para |
| Q07 | - |  |  | SI | Gestation |
| Q08 | - |  |  | SI | weeks |
| Q09 | - |  |  | SI | Gestation (days) |
| Q10 | - |  |  | SI | days |
| Q11 | - |  |  | SI | Blood group - Rhesus |
| Q12 | - |  |  | SI | Blood group - Rhesus |
| Q14 | - |  |  | SI | Were maternal observations normal pre-ECV |
| Q15 | - |  |  | SI | Normal maternal observation pre-ECV notes |
| Q16 | - |  |  | SI | Was the cardiotocograph (CTG) normal pre-ECV |
| Q17 | - |  |  | SI | CTG normal pre-ECV notes |
| Q18 | - |  |  | SI | Is patient eligible for ECV |
| Q19 | - |  |  | SI | Patient eligible for ECV notes |
| Q20 | - |  |  | SI | Has ECV information been provided to the patient |
| Q21 | - |  |  | SI | Type of ECV information provided |
| Q22 | - |  |  | SI | Patient consent been gained |
| Q23 | - |  |  | SI | Patient consent notes |
| Q24 | - |  |  | SI | Has the patient been fasted |
| Q25 | - |  |  | SI | Fasted notes |
| Q26 | - |  |  | SI | Last food intake |
| Q27 | - |  |  | SI | Last food intake |
| Q28 | - |  |  | SI | Last food intake notes |
| Q29 | - |  |  | SI | Last fluid intake |
| Q30 | - |  |  | SI | Last fluid intake |
| Q31 | - |  |  | SI | Last fluid intake notes |
| Q32 | - |  |  | SI | Has a tocolytic been administered |
| Q33 | - |  |  | SI | Tocolytic notes |
| Q34 | - |  |  | SI | Pre-procedure notes |
| Q35 | - |  |  | SI | Procedure performed by |
| Q36 | - |  |  | SI | Role |
| Q37 | - |  |  | SI | Assistance provided by |
| Q38 | - |  |  | SI | Role |
| Q39 | - |  |  | SI | ECV start time |
| Q40 | - |  |  | SI | ECV end time |
| Q41 | - |  |  | SI | ECV outcome |
| Q42 | - |  |  | SI | Other presentation, if applicable |
| Q43 | - |  |  | SI | Number of attempts |
| Q44 | - |  |  | SI | Complications details |
| Q45 | - |  |  | SI | Specify other complication details |
| Q46 | - |  |  | SI | Complication notes |
| Q47 | - |  |  | SI | Are maternal observations normal post-ECV |
| Q48 | - |  |  | SI | Maternal observations normal post-ECV notes |
| Q49 | - |  |  | SI | Is the cardiotocograph (CTG) normal post-ECV |
| Q50 | - |  |  | SI | CTC normal post-ECV notes |
| Q51 | - |  |  | SI | Has Anti-D been administered |
| Q52 | - |  |  | SI | Anti-D administered notes |
| Q53 | - |  |  | SI | Post-procedures notes |
| Q54 | - |  |  | SI | Birth plan, if cephalic |
| Q55 | - |  |  | SI | Birth plan, if breech |
| Q56 | - |  |  | SI | Follow-up plan |
| Q57 | - |  |  | SI | Gravida |
| Q58 | - |  |  | SI | Para |
| Q59 | - |  |  | SI | Blood group - Rhesus |
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