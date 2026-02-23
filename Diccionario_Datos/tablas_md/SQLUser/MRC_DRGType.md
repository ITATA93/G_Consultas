# SQLUser.MRC_DRGType

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGTYP_RowId | bigint | PK |  | NO | - |
| DRGTYP_Code | varchar |  |  | NO | Code |
| DRGTYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGTYP_CostWeightEditDR | bigint |  | FK | SI | Cost Weight Edition DR |
| DRGTYP_CreatedDate | date |  |  | SI | Created Date |
| DRGTYP_CreatedTime | time |  |  | SI | Created Time |
| DRGTYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGTYP_DRGVersion | bigint |  |  | SI | DRG Version DR |
| DRGTYP_Desc | varchar |  |  | NO | Description |
| DRGTYP_LongDescription | varchar |  |  | SI | LongDescription |
| DRGTYP_Owner | varchar |  |  | SI | Owner |
| DRGTYP_UpdatedDate | date |  |  | SI | Updated Date |
| DRGTYP_UpdatedTime | time |  |  | SI | Updated Time |
| DRGTYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Disminuir o erradicar el dolor |
| Q02 | - |  |  | SI | Disminuir o eliminar compromiso de movilidad |
| Q03 | - |  |  | SI | Mejorar la independencia en AVD |
| Q04 | - |  |  | SI | Reincorporar al trabajo o la Escuela |
| Q05 | - |  |  | SI | Apoyo al cuidador |
| Q06 | - |  |  | SI | Prevenir pèrdida de funcionalidad |
| Q07 | - |  |  | SI | Prevenir complicaciones secundarias |
| Q08 | - |  |  | SI | Disminuir o erradicar el dolor |
| Q09 | - |  |  | SI | Disminuir o eliminar compromiso de movilidad |
| Q10 | - |  |  | SI | Mejorar la independencia en AVD |
| Q11 | - |  |  | SI | Reincorporar al trabajo o la escuela |
| Q12 | - |  |  | SI | Apoyo al cuidador |
| Q13 | - |  |  | SI | Prevenir perdida de funcionalidad |
| Q14 | - |  |  | SI | Prevenir complicaciones secundarias |
| Q15 | - |  |  | SI | ¿Cuales? |
| Q16 | - |  |  | SI | Ejercicios Terapèuticos |
| Q17 | - |  |  | SI | Favorecer inclusion social |
| Q18 | - |  |  | SI | Consejeria |
| Q19 | - |  |  | SI | Entrenamiento AVD (Instrumentales y Bàsicas) |
| Q20 | - |  |  | SI | Taller para personas con Parkinson |
| Q21 | - |  |  | SI | Otros |
| Q22 | - |  |  | SI | ¿Cuales? |
| Q23 | - |  |  | SI | Observaciones |
| Q7a | - |  |  | SI | ¿Cuales? |
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