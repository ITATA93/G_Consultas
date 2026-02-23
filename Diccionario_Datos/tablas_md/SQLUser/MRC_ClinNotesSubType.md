# SQLUser.MRC_ClinNotesSubType

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBT_ParRef | bigint | PK |  | NO | MRC_ClinNotesType Parent Reference |
| CQ06 | - |  |  | SI | (null) |
| CQ1 | - |  |  | SI | (null) |
| CQ2 | - |  |  | SI | (null) |
| CQ3 | - |  |  | SI | (null) |
| CQ4 | - |  |  | SI | (null) |
| CQ5 | - |  |  | SI | (null) |
| CQ7 | - |  |  | SI | (null) |
| CQ8 | - |  |  | SI | (null) |
| CQ9 | - |  |  | SI | (null) |
| Q06 | - |  |  | SI | Aplique Minimental Abreviado |
| Q1 | - |  |  | SI | ¿Puede bañarse o ducharse? |
| Q10 | - |  |  | SI | Resultado EFAM A |
| Q10ObsDR | - |  |  | SI | Resultado EFAM A DR |
| Q11 | - |  |  | SI | Con los brazos extendidos lo máximo posible sobre ... |
| Q12 | - |  |  | SI | De pie y derecho, agáchese, tomar un objeto desde ... |
| Q13 | - |  |  | SI | MMSE |
| Q14 | - |  |  | SI | Con los brazos extendidos lo máximo posible sobre ... |
| Q15 | - |  |  | SI | Recuerde Ingresar Resultado en Forma Manual en Cue... |
| Q2 | - |  |  | SI | ¿Es Ud, Capaz de manejar su propio dinero? |
| Q3 | - |  |  | SI | ¿Puede Ud. tomar sus medicamentos? |
| Q4 | - |  |  | SI | ¿Prepara Ud. su comida? |
| Q5 | - |  |  | SI | ¿Puede hacer las tareas de la casa? |
| Q7 | - |  |  | SI | Escolaridad. Pregunte por los años de escolaridad ... |
| Q8 | - |  |  | SI | El adulto mayor de pie intentará tomar un objeto r... |
| Q9 | - |  |  | SI | En posición de pie, encuclillese, tome el objeto d... |
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
| SUBT_Childsub | double |  |  | NO | Childsub |
| SUBT_Code | varchar |  |  | NO | Code |
| SUBT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUBT_CreatedDate | date |  |  | SI | Created Date |
| SUBT_CreatedTime | time |  |  | SI | Created Time |
| SUBT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUBT_DateFrom | date |  |  | SI | Date From |
| SUBT_DateTo | date |  |  | SI | Date To |
| SUBT_Desc | varchar |  |  | NO | Description |
| SUBT_RowId | varchar |  |  | NO | - |
| SUBT_UpdatedDate | date |  |  | SI | Updated Date |
| SUBT_UpdatedTime | time |  |  | SI | Updated Time |
| SUBT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*