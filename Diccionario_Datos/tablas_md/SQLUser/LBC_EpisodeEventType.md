# SQLUser.LBC_EpisodeEventType

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCEET_RowID | bigint | PK |  | NO | - |
| ChildQ37DR | - |  |  | SI | Child Reference: Horario |
| LBCEET_Code | varchar |  |  | SI | Code |
| LBCEET_CreatedDate | date |  |  | SI | Event Group
Created Date |
| LBCEET_CreatedTime | time |  |  | SI | Created Time |
| LBCEET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCEET_DateFrom | date |  |  | SI | Effective date for the record |
| LBCEET_DateTo | date |  |  | SI | Last day the record is active  |
| LBCEET_Desc | varchar |  |  | SI | Description |
| LBCEET_DisplayInSpecimenRecord | varchar |  |  | SI | Display in Specimen Record |
| LBCEET_EventTypeGroup_DR | bigint |  | FK | SI | - |
| LBCEET_UpdatedDate | date |  |  | SI | Updated Date |
| LBCEET_UpdatedTime | time |  |  | SI | Updated Time |
| LBCEET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Producto |
| Q01ObsDR | - |  |  | SI | Producto DR |
| Q02 | - |  |  | SI | Producto 2 |
| Q02ObsDR | - |  |  | SI | Producto 2 DR |
| Q03 | - |  |  | SI | Producto 3 |
| Q03ObsDR | - |  |  | SI | Producto 3 DR |
| Q04 | - |  |  | SI | Producto 4 |
| Q04ObsDR | - |  |  | SI | Producto 4 DR |
| Q05 | - |  |  | SI | Producto 5 |
| Q05ObsDR | - |  |  | SI | Producto 5 DR |
| Q06 | - |  |  | SI | Porcentaje |
| Q07 | - |  |  | SI | Porcentaje 2 |
| Q08 | - |  |  | SI | Porcentaje 3 |
| Q09 | - |  |  | SI | Porcentaje 4 |
| Q10 | - |  |  | SI | Porcentaje 5 |
| Q11 | - |  |  | SI | Vol / Unidad cc |
| Q12 | - |  |  | SI | Vol / Unidad cc 2 |
| Q13 | - |  |  | SI | Vol / Unidad cc 3 |
| Q14 | - |  |  | SI | Vol / Unidad cc 4 |
| Q15 | - |  |  | SI | Vol / Unidad cc 5 |
| Q16 | - |  |  | SI | Nº Veces |
| Q17 | - |  |  | SI | Nº Veces 2 |
| Q18 | - |  |  | SI | Nº Veces 3 |
| Q19 | - |  |  | SI | Nº Veces 4 |
| Q20 | - |  |  | SI | Nº Veces 5 |
| Q21 | - |  |  | SI | Vol. Total cc |
| Q22 | - |  |  | SI | Vol. Total cc 2 |
| Q23 | - |  |  | SI | Vol. Total cc 3 |
| Q24 | - |  |  | SI | Vol. Total cc 4 |
| Q25 | - |  |  | SI | Vol. Total cc 5 |
| Q40 | - |  |  | SI | Via de administración |
| Q41 | - |  |  | SI | Observación |
| Q42 | - |  |  | SI | Hora de Termino |
| Q43 | - |  |  | SI | Vol / Unidad cc |
| Q44 | - |  |  | SI | Gr. Unidad 1 |
| Q45 | - |  |  | SI | Gr. Totales 1 |
| Q46 | - |  |  | SI | Gr. Unidad 2 |
| Q47 | - |  |  | SI | Gr. Unidad 3 |
| Q48 | - |  |  | SI | Gr. Unidad 4 |
| Q49 | - |  |  | SI | Gr. Unidad 5 |
| Q50 | - |  |  | SI | Gr. Totales 2 |
| Q51 | - |  |  | SI | Gr. Totales 3 |
| Q52 | - |  |  | SI | Gr. Totales 4 |
| Q53 | - |  |  | SI | Gr. Totales 5 |
| QNUT050 | - |  |  | SI | Fecha Despacho |
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