# SQLUser.PA_AdmWardAttend

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WAT_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| Q01 | - |  |  | SI | Is the patient eating any health foods regularly (... |
| Q02 | - |  |  | SI | Regular foods |
| Q03 | - |  |  | SI | During the last 6 months, has the patient had any ... |
| Q04 | - |  |  | SI | Special X-ray or CT examination	 |
| Q05 | - |  |  | SI | Weight changes |
| Q06 | - |  |  | SI | Palpitations |
| Q07 | - |  |  | SI | Tremors |
| Q08 | - |  |  | SI | Sweating / Heat intolerance |
| Q09 | - |  |  | SI | Irregular bowel movements	 |
| Q10 | - |  |  | SI | Irregular periods	 |
| Q11 | - |  |  | SI | Eye symptoms	 |
| Q12 | - |  |  | SI | Appetite pattern changes |
| Q13 | - |  |  | SI | Hair loss |
| Q14 | - |  |  | SI | Neck pain |
| Q15 | - |  |  | SI | Recent history of fever |
| Q16 | - |  |  | SI | Surgery |
| Q17 | - |  |  | SI | Family history |
| Q18 | - |  |  | SI | Ultrasound |
| Q19 | - |  |  | SI | Fine Needle Aspiration Cytology  (FNAC) |
| Q20 | - |  |  | SI | Abnormal Blood test (FT3, FT4, TSH) |
| Q21 | - |  |  | SI | Isotope scan |
| Q22 | - |  |  | SI | Iodine therapy |
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
| WAT_AdminCategory_DR | bigint |  | FK | SI | Des Ref PACAccountClass |
| WAT_AttendanceDetails | varchar |  |  | SI | Attendance Details |
| WAT_CTCPType_DR | bigint |  | FK | SI | Des Ref CTCPType |
| WAT_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| WAT_CTLOCSeen_DR | bigint |  | FK | SI | Des Ref CTLOCSeen |
| WAT_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WAT_Childsub | double |  |  | NO | Childsub |
| WAT_Date | date |  |  | SI | Date |
| WAT_DateUpdate | date |  |  | SI | Date Update |
| WAT_FirstAttendance | varchar |  |  | SI | First Attendance |
| WAT_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| WAT_Outcome_DR | bigint |  | FK | SI | Des Ref Outcome |
| WAT_PatSeeInLoc | varchar |  |  | SI | Patient See In Loc |
| WAT_RowId | varchar |  |  | NO | - |
| WAT_Time | time |  |  | SI | Time |
| WAT_TimeUpdate | time |  |  | SI | Time Update |
| WAT_UserHospitalUpdate_DR | bigint |  | FK | SI | Des Ref UserHospitalUpdate |
| WAT_User_DR | bigint |  | FK | SI | Des Ref User |
| WAT_Ward_DR | bigint |  | FK | SI | Des Ref Ward |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*