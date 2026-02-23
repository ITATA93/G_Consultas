# SQLUser.PAC_Question

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUES_RowId | bigint | PK |  | NO | - |
| ChildQ09DR | - |  |  | SI | Child Reference: Diathermy Plate	 |
| Q01 | - |  |  | SI | Procedure |
| Q02 | - |  |  | SI | Intravenous fluid warmer used	 |
| Q03 | - |  |  | SI | Forced air heater used	 |
| Q04 | - |  |  | SI | Specify |
| Q05 | - |  |  | SI | Specify	 |
| Q06 | - |  |  | SI | Under patient warming used	 |
| Q07 | - |  |  | SI | Specify |
| Q08 | - |  |  | SI | Specify	 |
| Q10 | - |  |  | SI | Date |
| Q11 | - |  |  | SI | Time |
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
| QUES_AgeFrom | double |  |  | SI | Age From |
| QUES_AgeTo | double |  |  | SI | Age To |
| QUES_AllowFormatDescForLabel | varchar |  |  | SI | Allow formatted description for label |
| QUES_AtomicTestResult | varchar |  |  | SI | Atomic Test Result |
| QUES_Code | varchar |  |  | NO | Code |
| QUES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QUES_ControlType | varchar |  |  | SI | Control Type |
| QUES_CreatedDate | date |  |  | SI | Created Date |
| QUES_CreatedTime | time |  |  | SI | Created Time |
| QUES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QUES_CustomType | varchar |  |  | SI | Custom Type |
| QUES_DBField | varchar |  |  | SI | Database Field |
| QUES_DateFrom | date |  |  | SI | Date From |
| QUES_DateTo | date |  |  | SI | Date To |
| QUES_Decimal | varchar |  |  | SI | Decimal |
| QUES_DefaultAnswer | varchar |  |  | SI | DefaultAnswer |
| QUES_Desc | varchar |  |  | NO | Description |
| QUES_FieldType | varchar |  |  | SI | Field Type |
| QUES_ForSpecimenCollection | varchar |  |  | SI | ForSpecimenCollection |
| QUES_NumberOfDays | double |  |  | SI | Number Of Days |
| QUES_ObsItem_DR | bigint |  | FK | SI | Des Ref ObsItem |
| QUES_Other | varchar |  |  | SI | Other |
| QUES_Owner | varchar |  |  | SI | Owner |
| QUES_PositiveOnly | varchar |  |  | SI | PositiveOnly |
| QUES_PrintOnLabDoctorReport | varchar |  |  | SI | Print On Lab Doctor's Report |
| QUES_RespAnsCont | varchar |  |  | SI | Response Answer Control |
| QUES_RespAnsDepth | varchar |  |  | SI | Depth From Root Response Answer Question |
| QUES_Sequence | double |  |  | SI | Sequence |
| QUES_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| QUES_TextLength | double |  |  | SI | Text Length |
| QUES_UpdatedDate | date |  |  | SI | Updated Date |
| QUES_UpdatedTime | time |  |  | SI | Updated Time |
| QUES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QUES_Values | varchar |  |  | SI | Values |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*