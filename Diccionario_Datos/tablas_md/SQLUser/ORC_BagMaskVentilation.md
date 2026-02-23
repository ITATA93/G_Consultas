# SQLUser.ORC_BagMaskVentilation

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BAGMVENT_RowId | bigint | PK |  | NO | - |
| BAGMVENT_Code | varchar |  |  | NO | Code |
| BAGMVENT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BAGMVENT_CreatedDate | date |  |  | SI | Created Date |
| BAGMVENT_CreatedTime | time |  |  | SI | Created Time |
| BAGMVENT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BAGMVENT_DateFrom | date |  |  | SI | Date From |
| BAGMVENT_DateTo | date |  |  | SI | Date To |
| BAGMVENT_Desc | varchar |  |  | NO | Description |
| BAGMVENT_Owner | varchar |  |  | SI | Owner |
| BAGMVENT_UpdatedDate | date |  |  | SI | Updated Date |
| BAGMVENT_UpdatedTime | time |  |  | SI | Updated Time |
| BAGMVENT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | INTENSIDAD Y DURACIÓN DE LA PRESIÓN |
| Q02 | - |  |  | SI | Condición física general |
| Q03 | - |  |  | SI | MOVILIDAD |
| Q04 | - |  |  | SI | ACTIVIDAD |
| Q05 | - |  |  | SI | PERCEPCIÓN SENSORIAL |
| Q06 | - |  |  | SI | TOLERANCIA DE LA PIEL Y LA ESTRUCTURA DE SOPORTE |
| Q07 | - |  |  | SI | HUMEDAD |
| Q08 | - |  |  | SI | FRICCIÓN Y CIZALLA |
| Q09 | - |  |  | SI | NUTRICIÓN |
| Q10 | - |  |  | SI | Perfusión tisular y oxigenación |
| Q11 | - |  |  | SI | Comentarios |
| Q12 | - |  |  | SI | > 16 |
| Q13 | - |  |  | SI | Riesgo bajo |
| Q14 | - |  |  | SI | ≤ 16 |
| Q15 | - |  |  | SI | En riesgo |
| Q16 | - |  |  | SI | La escala Braden Q para predecir el riesgo de úlce... |
| Q17 | - |  |  | SI | Puntaje |
| Q18 | - |  |  | SI | Clasificación |
| Q19 | - |  |  | SI | > 16: riesgo bajo |
| Q20 | - |  |  | SI | ≤ 16: riesgo alto |
| Q21 | - |  |  | SI | Revise la interpretación de la puntuación a contin... |
| Q22 | - |  |  | SI | Fecha |
| Q23 | - |  |  | SI | Hora |
| Q24 | - |  |  | SI | Comentarios |
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