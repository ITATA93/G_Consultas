# SQLUser.ARC_BillSequence

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLSEQ_RowId | bigint | PK |  | NO | - |
| BLSEQ_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| BLSEQ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLSEQ_CreatedDate | date |  |  | SI | Created Date |
| BLSEQ_CreatedTime | time |  |  | SI | Created Time |
| BLSEQ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLSEQ_DateFrom | date |  |  | SI | Date From |
| BLSEQ_DateTo | date |  |  | SI | Date To |
| BLSEQ_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| BLSEQ_Owner | varchar |  |  | SI | Owner |
| BLSEQ_Sequence | integer |  |  | SI | Sequence |
| BLSEQ_UpdatedDate | date |  |  | SI | Updated Date |
| BLSEQ_UpdatedTime | time |  |  | SI | Updated Time |
| BLSEQ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CQGRU | - |  |  | SI | (null) |
| Q17 | - |  |  | SI | Ubicación de la lesión |
| Q18 | - |  |  | SI | Extremidad |
| QAPC | - |  |  | SI | Apósito o cobertura |
| QAS | - |  |  | SI | Aspecto |
| QAU | - |  |  | SI | Agente Utilizado |
| QCLE | - |  |  | SI | Calidad exudado |
| QCNE | - |  |  | SI | Cantidad exudado |
| QCOM | - |  |  | SI | Comentarios |
| QDI | - |  |  | SI | Mayor extensión |
| QDO | - |  |  | SI | Dolor |
| QDSU | - |  |  | SI | Descripción de úlcera |
| QED | - |  |  | SI | Edema |
| QFC | - |  |  | SI | Frecuencia de cambio |
| QGRU | - |  |  | SI | Grado de la Úlcera |
| QGU | - |  |  | SI | Label |
| QPC | - |  |  | SI | Piel Circundante |
| QPF | - |  |  | SI | Profundidad |
| QTF | - |  |  | SI | Tipo de Fijación |
| QTG | - |  |  | SI | Tejido granulatorio |
| QTN | - |  |  | SI | Tejido esfacelado o necrótico |
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