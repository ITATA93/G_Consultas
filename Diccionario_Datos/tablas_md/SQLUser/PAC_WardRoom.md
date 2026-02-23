# SQLUser.PAC_WardRoom

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROOM_ParRef | bigint | PK |  | NO | PAC_Ward Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Are you interested in quitting, reducing your smok... |
| Q04 | - |  |  | SI | Please complete referral to appropriate person |
| Q05 | - |  |  | SI | Would you like Nicotine Replacement Therapy (NRT) ... |
| Q06 | - |  |  | SI | Review NRT dosing guidelines |
| Q07 | - |  |  | SI | Prior to your admission were you using NRT or quit... |
| Q08 | - |  |  | SI | Notify Medical Officer |
| Q09 | - |  |  | SI | Would you like information about smoking, reducing... |
| Q10 | - |  |  | SI | Supply information pack |
| Q11 | - |  |  | SI | Are you exposed to people smoking at home (second ... |
| Q12 | - |  |  | SI | Supply information regarding the effects of passiv... |
| Q13 | - |  |  | SI | On discharge would you like support to quit, reduc... |
| Q14 | - |  |  | SI | Ensure relevant referrals are completed |
| Q15 | - |  |  | SI | Comments |
| Q16 | - |  |  | SI | If the Fagerstrom Test for Nicotine Dependence ach... |
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
| ROOM_AccommodationTypeDR | bigint |  | FK | SI | Accommodation Type DR |
| ROOM_ActiveFlag | varchar |  |  | SI | Active for FloorPlan Flag |
| ROOM_ChildSub | double |  |  | NO | ChildSub |
| ROOM_CreatedDate | date |  |  | SI | Created Date |
| ROOM_CreatedTime | time |  |  | SI | Created Time |
| ROOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROOM_DateFrom | date |  |  | SI | Date From |
| ROOM_DateTo | date |  |  | SI | Date To |
| ROOM_PositionHeight | double |  |  | SI | Position Height |
| ROOM_PositionLeft | double |  |  | SI | Position Left |
| ROOM_PositionTop | double |  |  | SI | Position Top |
| ROOM_PositionWidth | double |  |  | SI | Position Width |
| ROOM_Room_DR | bigint |  | FK | SI | Des Ref Room |
| ROOM_RowId | varchar |  |  | NO | - |
| ROOM_UpdatedDate | date |  |  | SI | Updated Date |
| ROOM_UpdatedTime | time |  |  | SI | Updated Time |
| ROOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*