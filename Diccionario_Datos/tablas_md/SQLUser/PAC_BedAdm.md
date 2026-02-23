# SQLUser.PAC_BedAdm

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADM_ParRef | varchar | PK |  | NO | PAC_Bed Parent Reference |
| ADM_BookedStatus | varchar |  |  | SI | Booked Status |
| ADM_Childsub | double |  |  | NO | Childsub |
| ADM_CreatedDate | date |  |  | SI | Created Date |
| ADM_CreatedTime | time |  |  | SI | Created Time |
| ADM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADM_Location_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ADM_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| ADM_RowId | varchar |  |  | NO | - |
| ADM_Trans_DR | varchar |  | FK | SI | Des Ref PAADM Trans |
| ADM_UpdatedDate | date |  |  | SI | Updated Date |
| ADM_UpdatedTime | time |  |  | SI | Updated Time |
| ADM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Discharge agreed by Intensivist |
| Q02 | - |  |  | SI | Active medications reviewed |
| Q03 | - |  |  | SI | Patients regular preop medications reviewed / reco... |
| Q04 | - |  |  | SI | Paper order forms for ward completed if required |
| Q05 | - |  |  | SI | Admitting accredited practioner aware of D/C |
| Q06 | - |  |  | SI | Other relevant accredited practioners notified of ... |
| Q07 | - |  |  | SI | Apache form completed |
| Q08 | - |  |  | SI | Critical care form completed |
| Q09 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Time |
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