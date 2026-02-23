# SQLUser.ARC_ItemProcActivityModif

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MOD_ParRef | varchar | PK |  | NO | ARC_EpisodicBilling Parent Reference |
| MOD_ActivityModif_DR | bigint |  | FK | SI | Des Ref ActivityModif |
| MOD_Childsub | double |  |  | NO | Childsub |
| MOD_CreatedDate | date |  |  | SI | Created Date |
| MOD_CreatedTime | time |  |  | SI | Created Time |
| MOD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MOD_RowId | varchar |  |  | NO | - |
| MOD_UpdatedDate | date |  |  | SI | Updated Date |
| MOD_UpdatedTime | time |  |  | SI | Updated Time |
| MOD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Ley de Urgencia |
| Q02 | - |  |  | SI | CAEC ISAPRE |
| Q03 | - |  |  | SI | Derivación GRD |
| Q04 | - |  |  | SI | Derivación UGCC |
| Q05 | - |  |  | SI | Fecha Inicio&nbsp |
| Q06 | - |  |  | SI | Hora Inicio Ley de Urgencia |
| Q07 | - |  |  | SI | Cierre Ley de Urgencia |
| Q08 | - |  |  | SI | Fecha Término Ley de Urgencia |
| Q09 | - |  |  | SI | Hora Término Ley de Urgencia |
| Q10 | - |  |  | SI | Fecha Inicio CAEC ISAPRE |
| Q11 | - |  |  | SI | Hora Inicio CAEC ISAPRE |
| Q12 | - |  |  | SI | Cierre CAEC ISAPRE |
| Q13 | - |  |  | SI | Fecha Término CAEC ISAPRE |
| Q14 | - |  |  | SI | Hora Término CAEC ISAPRE |
| Q15 | - |  |  | SI | Fecha Inicio Derivación GRD |
| Q16 | - |  |  | SI | Hora&nbsp |
| Q17 | - |  |  | SI | Cierre&nbsp |
| Q18 | - |  |  | SI | Fecha&nbsp |
| Q19 | - |  |  | SI | Hora Término&nbsp |
| Q20 | - |  |  | SI | Fecha Inicio Derivación UGCC |
| Q21 | - |  |  | SI | Hora Inicio Derivación UGCC |
| Q22 | - |  |  | SI | Cierre Derivación UGCC |
| Q23 | - |  |  | SI | Fecha Término Derivación UGCC |
| Q24 | - |  |  | SI | Hora Término Derivación UGCC |
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