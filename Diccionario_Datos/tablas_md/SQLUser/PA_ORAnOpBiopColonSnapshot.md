# SQLUser.PA_ORAnOpBiopColonSnapshot

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAOBC_ParRef | bigint | PK |  | NO | PA_ORAnaestOper Parent Reference |
| ChildQ12DR | - |  |  | SI | Child Reference: CUELLO |
| PAOBC_Childsub | double |  |  | NO | Childsub |
| PAOBC_RowId | varchar |  |  | NO | - |
| PAOBC_Type_DR | bigint |  | FK | SI | Des Ref ORCDigestiveSystem |
| Q01 | - |  |  | SI | Fecha de Evaluación |
| Q02 | - |  |  | SI | Hora de Evaluación |
| Q03 | - |  |  | SI | I - MOMENTO DE LA VALORACIÓN |
| Q04 | - |  |  | SI | Momento de la Valoración |
| Q04a | - |  |  | SI | I.A. IDENTIFICACIÓN DEL TURNO |
| Q04b | - |  |  | SI | Identificación del Turno |
| Q05 | - |  |  | SI | II. EXAMEN FÍSICO PROMINENCIAS OSEAS |
| Q06 | - |  |  | SI | Alteraciones de la Piel en Cabeza y Cara |
| Q10 | - |  |  | SI | Comentarios de Cabeza y Cara |
| Q11 | - |  |  | SI | Alteraciones de la Piel en Cuello |
| Q13 | - |  |  | SI | Comentarios del Cuello |
| Q14 | - |  |  | SI | Alteraciones de la Piel en Tórax y Abdomen |
| Q16 | - |  |  | SI | Comentarios de Tórax y Abdomen |
| Q17 | - |  |  | SI | Alteraciones de la Piel en Extremidades |
| Q19 | - |  |  | SI | Comentarios de Extremidades |
| Q20 | - |  |  | SI | Alteraciones de la Piel en Pelvis-Genitales |
| Q22 | - |  |  | SI | Comentarios de Pelvis-Genitales |
| Q23 | - |  |  | SI | Alteraciones de la Piel en Dorso |
| Q25 | - |  |  | SI | Comentarios del Dorso |
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