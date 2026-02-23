# SQLUser.ARC_PayAgreemDetails

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| DET_ARCIM1_DR | varchar |  | FK | SI | Des Ref ARCIM1 |
| DET_ARCIM2_DR | varchar |  | FK | SI | Des Ref ARCIM2 |
| DET_AdmissionType | varchar |  |  | SI | AdmissionType |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| DET_Number1 | double |  |  | SI | Number1 |
| DET_Number10 | double |  |  | SI | Number10 |
| DET_Number11 | double |  |  | SI | Number11 |
| DET_Number12 | double |  |  | SI | Number12 |
| DET_Number13 | double |  |  | SI | Number13 |
| DET_Number14 | double |  |  | SI | Number14 |
| DET_Number15 | double |  |  | SI | Number15 |
| DET_Number16 | double |  |  | SI | Number16 |
| DET_Number17 | double |  |  | SI | Number17 |
| DET_Number18 | double |  |  | SI | Number18 |
| DET_Number19 | double |  |  | SI | Number19 |
| DET_Number2 | double |  |  | SI | Number2 |
| DET_Number20 | double |  |  | SI | Number20 |
| DET_Number3 | double |  |  | SI | Number3 |
| DET_Number4 | double |  |  | SI | Number4 |
| DET_Number5 | double |  |  | SI | Number5 |
| DET_Number6 | double |  |  | SI | Number6 |
| DET_Number7 | double |  |  | SI | Number7 |
| DET_Number8 | double |  |  | SI | Number8 |
| DET_Number9 | double |  |  | SI | Number9 |
| DET_RowId | varchar |  |  | NO | - |
| DET_Text1 | varchar |  |  | SI | Text1 |
| DET_Text2 | varchar |  |  | SI | Text2 |
| DET_Text3 | varchar |  |  | SI | Text3 |
| DET_Text4 | varchar |  |  | SI | Text4 |
| DET_Text5 | varchar |  |  | SI | Text5 |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DET_YesNo1 | varchar |  |  | SI | YesNo1 |
| DET_YesNo2 | varchar |  |  | SI | YesNo2 |
| DET_YesNo3 | varchar |  |  | SI | YesNo3 |
| DET_YesNo4 | varchar |  |  | SI | YesNo4 |
| DET_YesNo5 | varchar |  |  | SI | YesNo5 |
| Q01 | - |  |  | SI | Indicador |
| Q02 | - |  |  | SI | Tiempo de Observación |
| Q03 | - |  |  | SI | Gestación |
| Q04 | - |  |  | SI | Comportamiento |
| Q05 | - |  |  | SI | 15 segundos |
| Q06 | - |  |  | SI | Aumento de FC |
| Q07 | - |  |  | SI | 30 segundos |
| Q08 | - |  |  | SI | Disminución de saturación de O2 |
| Q09 | - |  |  | SI | 30 segundos |
| Q10 | - |  |  | SI | Entrecejo fruncido |
| Q11 | - |  |  | SI | 30 segundos |
| Q12 | - |  |  | SI | Ojos apretados |
| Q13 | - |  |  | SI | Surco nasolabial |
| Q14 | - |  |  | SI | 30 segundos |
| Q15 | - |  |  | SI | 30 segundos |
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