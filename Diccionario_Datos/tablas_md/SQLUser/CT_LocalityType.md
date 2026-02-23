# SQLUser.CT_LocalityType

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCTYPE_RowId | bigint | PK |  | NO | - |
| LOCTYPE_Code | varchar |  |  | NO | Code |
| LOCTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOCTYPE_CreatedDate | date |  |  | SI | Created Date |
| LOCTYPE_CreatedTime | time |  |  | SI | Created Time |
| LOCTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOCTYPE_Desc | varchar |  |  | NO | Description |
| LOCTYPE_NationalCode | varchar |  |  | SI | NationalCode |
| LOCTYPE_Owner | varchar |  |  | SI | Owner |
| LOCTYPE_Type | varchar |  |  | SI | Type |
| LOCTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| LOCTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| LOCTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Tipo de posición quirúrgica |
| Q04 | - |  |  | SI | Tiempo de cirugía |
| Q05 | - |  |  | SI | Tipo de anestesia |
| Q06 | - |  |  | SI | Superficie de soporte |
| Q07 | - |  |  | SI | Posición de los miembros |
| Q08 | - |  |  | SI | Comorbilidades |
| Q09 | - |  |  | SI | Edad del paciente |
| Q10 | - |  |  | SI | La Escala de evaluación de riesgo de lesiones por ... |
| Q11 | - |  |  | SI | Referencias |
| Q12 | - |  |  | SI | • Lopes CM de M, Haas VJ, Dantas RAS, Oliveira CG ... |
| Q13 | - |  |  | SI | • 7 a 19: menor riesgo de lesiones |
| Q14 | - |  |  | SI | • 20 a 35: mayor riesgo de lesiones |
| Q15 | - |  |  | SI | • La Escala de evaluación de riesgo de lesiones po... |
| Q16 | - |  |  | SI | • Escala de evaluación de riesgo de lesiones por p... |
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