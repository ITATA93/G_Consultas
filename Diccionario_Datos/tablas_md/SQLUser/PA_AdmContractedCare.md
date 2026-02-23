# SQLUser.PA_AdmContractedCare

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTCARE_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| CONTCARE_Childsub | double |  |  | NO | Childsub |
| CONTCARE_ContRole_DR | bigint |  | FK | SI | Des Ref ContRole |
| CONTCARE_ContType_DR | bigint |  | FK | SI | Des Ref ContType |
| CONTCARE_DateFrom | date |  |  | SI | Date From |
| CONTCARE_DateTo | date |  |  | SI | Date To |
| CONTCARE_RowId | varchar |  |  | NO | - |
| CONTCARE_TimeFrom | time |  |  | SI | Time From |
| CONTCARE_TimeTo | time |  |  | SI | Time To |
| CONTCARE_UpdateDate | date |  |  | SI | Update Date |
| CONTCARE_UpdateTime | time |  |  | SI | Update Time |
| CONTCARE_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| CONTCARE_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| ChildQ30DR | - |  |  | SI | Child Reference: Reasons for care not delivered |
| Q1 | - |  |  | SI | Frequency of SSKIN bundle |
| Q10 | - |  |  | SI | Date |
| Q11 | - |  |  | SI | Cushion type |
| Q12 | - |  |  | SI | Cushion changed to |
| Q13 | - |  |  | SI | Date |
| Q14 | - |  |  | SI | Mattress / cushion functioning correctly |
| Q15 | - |  |  | SI | Heal protectors used |
| Q16 | - |  |  | SI | Bed rest |
| Q17 | - |  |  | SI | Bed rest positioning |
| Q18 | - |  |  | SI | Right side |
| Q19 | - |  |  | SI | Left side |
| Q20 | - |  |  | SI | Back |
| Q21 | - |  |  | SI | Prone |
| Q22 | - |  |  | SI | Wheelchair pressure relief (please record dependen... |
| Q23 | - |  |  | SI | Incontinence related skin case regime implemented |
| Q24 | - |  |  | SI | Dry and clean |
| Q25 | - |  |  | SI | Perineal skin healthy |
| Q26 | - |  |  | SI | Nutritional screening |
| Q27 | - |  |  | SI | Nutritional supplements prescribed |
| Q28 | - |  |  | SI | Nutritional supplements taken |
| Q29 | - |  |  | SI | Care delivered |
| Q3 | - |  |  | SI | All pressure areas checked |
| Q31 | - |  |  | SI | Waterlow score |
| Q32 | - |  |  | SI | Date of waterlow |
| Q33 | - |  |  | SI | Time of waterlow |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | Time |
| Q36 | - |  |  | SI | Hourly |
| Q4 | - |  |  | SI | Pressure injury present |
| Q5 | - |  |  | SI | If pressure injury present (please record on wound... |
| Q6 | - |  |  | SI | New redness |
| Q7 | - |  |  | SI | If yes, please specify location |
| Q8 | - |  |  | SI | Mattress type |
| Q9 | - |  |  | SI | Mattress changed to |
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