# SQLUser.PAC_ThirdStageOxy

**Schema:** SQLUser
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TSO_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | I have reviewed updated physician's order and rela... |
| Q04 | - |  |  | SI | General appearance |
| Q05 | - |  |  | SI | Level of consciousness |
| Q05ObsDR | - |  |  | SI | Level of consciousness DR |
| Q06 | - |  |  | SI | Muscle length examination |
| Q07 | - |  |  | SI | Muscle length summary |
| Q08 | - |  |  | SI | Muscle tone examination |
| Q09 | - |  |  | SI | Muscle tone summary |
| Q10 | - |  |  | SI | Muscle strength examination |
| Q11 | - |  |  | SI | Muscle strength summary |
| Q12 | - |  |  | SI | Limb muscle strength |
| Q13 | - |  |  | SI | Left upper extremities |
| Q13ObsDR | - |  |  | SI | Left upper extremities DR |
| Q14 | - |  |  | SI | Right upper extremities |
| Q14ObsDR | - |  |  | SI | Right upper extremities DR |
| Q15 | - |  |  | SI | Left lower extremities |
| Q15ObsDR | - |  |  | SI | Left lower extremities DR |
| Q16 | - |  |  | SI | Right lower extremities |
| Q16ObsDR | - |  |  | SI | Right lower extremities DR |
| Q17 | - |  |  | SI | Static sitting balance |
| Q17ObsDR | - |  |  | SI | Static sitting balance DR |
| Q18 | - |  |  | SI | Dynamic sitting balance |
| Q18ObsDR | - |  |  | SI | Dynamic sitting balance DR |
| Q19 | - |  |  | SI | Static standing balance |
| Q19ObsDR | - |  |  | SI | Static standing balance DR |
| Q20 | - |  |  | SI | Dynamic standing balance |
| Q20ObsDR | - |  |  | SI | Dynamic standing balance DR |
| Q21 | - |  |  | SI | Sensation examination |
| Q22 | - |  |  | SI | Sensation summary |
| Q23 | - |  |  | SI | Rolling |
| Q23ObsDR | - |  |  | SI | Rolling DR |
| Q24 | - |  |  | SI | Come to sit |
| Q24ObsDR | - |  |  | SI | Come to sit DR |
| Q25 | - |  |  | SI | Ambulatory status |
| Q25ObsDR | - |  |  | SI | Ambulatory status DR |
| Q26 | - |  |  | SI | Transferring |
| Q26ObsDR | - |  |  | SI | Transferring DR |
| Q27 | - |  |  | SI | Gait pattern |
| Q27ObsDR | - |  |  | SI | Gait pattern DR |
| Q28 | - |  |  | SI | Gait aid |
| Q28ObsDR | - |  |  | SI | Gait aid DR |
| Q29 | - |  |  | SI | Level of assistance |
| Q29ObsDR | - |  |  | SI | Level of assistance DR |
| Q30 | - |  |  | SI | Gait analysis summary |
| Q31 | - |  |  | SI | Other examination |
| Q32 | - |  |  | SI | To document specific examinations, please complete... |
| Q33 | - |  |  | SI | Examples: |
| Q34 | - |  |  | SI | Range of Motion |
| Q35 | - |  |  | SI | Manual Muscle Testing |
| Q36 | - |  |  | SI | Modified Tardieu Scale |
| Q37 | - |  |  | SI | Modified Ashworth Scale |
| Q38 | - |  |  | SI | Come to stand |
| Q38ObsDR | - |  |  | SI | Come to stand DR |
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
| TSO_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| TSO_Code | varchar |  |  | NO | Code |
| TSO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TSO_CreatedDate | date |  |  | SI | Created Date |
| TSO_CreatedTime | time |  |  | SI | Created Time |
| TSO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TSO_DateFrom | date |  |  | SI | DateFrom |
| TSO_DateTo | date |  |  | SI | DateTo |
| TSO_Desc | varchar |  |  | NO | Description |
| TSO_Owner | varchar |  |  | SI | Owner |
| TSO_UpdatedDate | date |  |  | SI | Updated Date |
| TSO_UpdatedTime | time |  |  | SI | Updated Time |
| TSO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*