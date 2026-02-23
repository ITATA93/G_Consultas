# SQLUser.LB_StorageContainerPosition

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBSTCP_ParRef | bigint | PK |  | NO | Parent Reference |
| ChildQ09DR | - |  |  | SI | Child Reference: Acuerdos y Responsables de cada i... |
| LBSTCP_Column | varchar |  |  | SI | Column
A label which identifies the column in the... |
| LBSTCP_Comment | varchar |  |  | SI | Comment |
| LBSTCP_DateChangeReason | varchar |  |  | SI | Date Change Reason |
| LBSTCP_DisposalDate | date |  |  | SI | Disposal Date |
| LBSTCP_NextReviewDate | date |  |  | SI | Next Review Date |
| LBSTCP_Position | varchar |  |  | SI | Position
A label which identifies the position in... |
| LBSTCP_ProtocolMaterial_DR | varchar |  | FK | SI | Protocol Material |
| LBSTCP_RequestBy_DR | bigint |  | FK | SI | Requested By DR |
| LBSTCP_ReserveForMaterial_DR | varchar |  | FK | SI | Reserve for Material |
| LBSTCP_ReviewCycle | numeric |  |  | SI | Review Cycle |
| LBSTCP_Row | varchar |  |  | SI | Row
A label which identifies the row in the conta... |
| LBSTCP_RowID | varchar |  |  | NO | - |
| LBSTCP_Sequence | numeric |  |  | SI | Sequence
Numeric value indicating the sequence in... |
| LBSTCP_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container DR |
| Q01 | - |  |  | SI | CESFAM |
| Q02 | - |  |  | SI | Territorio |
| Q03 | - |  |  | SI | Fecha |
| Q04 | - |  |  | SI | Riesgo Familiar |
| Q04ObsDR | - |  |  | SI | Riesgo Familiar DR |
| Q05 | - |  |  | SI | Caso Indice |
| Q06 | - |  |  | SI | Responsables |
| Q07 | - |  |  | SI | Motivo |
| Q10 | - |  |  | SI | Objetivos |
| Q11 | - |  |  | SI | Actividades |
| Q12 | - |  |  | SI | Tiempo de intervención |
| Q13 | - |  |  | SI | Observaciones |
| Q14 | - |  |  | SI | Inclusión Social |
| Q15 | - |  |  | SI | Trabajo |
| Q16 | - |  |  | SI | Escuela |
| Q17 | - |  |  | SI | Grupos Sociales |
| Q18 | - |  |  | SI | Organizaciones |
| Q19 | - |  |  | SI | Otras. Especifique: |
| Q22 | - |  |  | SI | Motivo de Egreso Familiar |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*