# SQLUser.CT_ShiftDetails

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | CT_Shift Parent Reference |
| DATE_Assigned | varchar |  |  | SI | Assigned |
| DATE_DateFrom | date |  |  | SI | Date From |
| DATE_DateTo | date |  |  | SI | Date To |
| DATE_Length | double |  |  | SI | Length |
| DATE_LoadLevel | double |  |  | SI | LoadLevel |
| DATE_Overbook | double |  |  | SI | Overbook |
| DATE_TimeFrom | time |  |  | SI | Time From |
| DATE_TimeTo | time |  |  | SI | Time To |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_RowId | varchar |  |  | NO | - |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q22 | - |  |  | SI | 0 - 13: minimal depression |
| Q23 | - |  |  | SI | 14 - 19: mild depression |
| Q24 | - |  |  | SI | 20 - 28: moderate depression |
| Q25 | - |  |  | SI | 29 - 63: severe depression |
| Q26 | - |  |  | SI | The Beck Depression Inventory BDI is a self-report... |
| Q27 | - |  |  | SI | BDI-II contains 21 questions, each answer being sc... |
| Q28 | - |  |  | SI | Date |
| Q29 | - |  |  | SI | Time |
| Q30 | - |  |  | SI | Beck, A.T., Ward, C. H., Mendelson, M., Mock, J., ... |
| Q31 | - |  |  | SI | Beck, A. T., Steer, R.A., and Garbin, M.G. (1988) ... |
| Q32 | - |  |  | SI | Groth-Marnat G. (1990). The handbook of psychologi... |
| Q33 | - |  |  | SI | Hojat, M., Shapurian, R., Mehrya, A.H., (1986). Ps... |
| Q34 | - |  |  | SI | Steer, R. A., Rissmiller, D. J. and Beck, A.T., (2... |
| QApp | - |  |  | SI | Appearance |
| QAppe | - |  |  | SI | Appetite |
| QCry | - |  |  | SI | Crying |
| QDec | - |  |  | SI | Decisions |
| QDis | - |  |  | SI | Discouragement |
| QDisa | - |  |  | SI | Disappointment |
| QFai | - |  |  | SI | Failure |
| QGui | - |  |  | SI | Guilt |
| QInt | - |  |  | SI | Interest |
| QIrr | - |  |  | SI | Irritation |
| QPun | - |  |  | SI | Punishment |
| QSad | - |  |  | SI | Sadness |
| QSat | - |  |  | SI | Satisfaction |
| QSex | - |  |  | SI | Sex |
| QSle | - |  |  | SI | Sleep |
| QSui | - |  |  | SI | Suicide |
| QTir | - |  |  | SI | Tiredness |
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
| QWea | - |  |  | SI | Weakness |
| QWei | - |  |  | SI | Weight |
| QWor | - |  |  | SI | Work |
| QWorr | - |  |  | SI | Worry |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*