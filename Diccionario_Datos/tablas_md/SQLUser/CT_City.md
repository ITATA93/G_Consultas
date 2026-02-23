# SQLUser.CT_City

**Schema:** SQLUser
**Columnas:** 126
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCIT_RowId | bigint | PK |  | NO | - |
| CTCIT_Code | varchar |  |  | NO | City Code |
| CTCIT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTCIT_CreatedDate | date |  |  | SI | Created Date |
| CTCIT_CreatedTime | time |  |  | SI | Created Time |
| CTCIT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTCIT_DateFrom | date |  |  | SI | Date From |
| CTCIT_DateTo | date |  |  | SI | Date To |
| CTCIT_Desc | varchar |  |  | NO | City Description |
| CTCIT_FiscalPrefix | varchar |  |  | SI | Fiscal Prefix |
| CTCIT_LocalityType | varchar |  |  | SI | Locality Type |
| CTCIT_LocalityType_DR | bigint |  | FK | SI | Des Ref LocalityType |
| CTCIT_NationalCode | varchar |  |  | SI | National Code |
| CTCIT_Owner | varchar |  |  | SI | Owner |
| CTCIT_Province_DR | bigint |  | FK | SI | Des Ref Province |
| CTCIT_Region_DR | bigint |  | FK | SI | Des Ref Region  |
| CTCIT_UpdatedDate | date |  |  | SI | Updated Date |
| CTCIT_UpdatedTime | time |  |  | SI | Updated Time |
| CTCIT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tipo de Evaluación |
| Q02 | - |  |  | SI | Fecha Evaluación |
| Q03 | - |  |  | SI | Evaluador |
| Q04 | - |  |  | SI | Puntaje Obtenido Parte I |
| Q05 | - |  |  | SI | /24 |
| Q06 | - |  |  | SI | Use solamente cuadrados y círculos grandes (6 fich... |
| Q07 | - |  |  | SI | Puntaje Obtenido Parte II |
| Q08 | - |  |  | SI | /24 |
| Q09 | - |  |  | SI | Use cuadrados y círculos grandes y chicos (12 fich... |
| Q10 | - |  |  | SI | Puntaje Obtenido Parte III |
| Q11 | - |  |  | SI | /24 |
| Q12 | - |  |  | SI | Use los cuadrados y círculos grandes (6 fichas) |
| Q13 | - |  |  | SI | Puntaje Obtenido Parte IV |
| Q14 | - |  |  | SI | /24 |
| Q15 | - |  |  | SI | Use cuadrados y círculos grandes y chicos (12 fich... |
| Q16 | - |  |  | SI | Parte I (Use solamente cuadrados y círculos grande... |
| Q17 | - |  |  | SI | Toque el círculo rojo |
| Q18 | - |  |  | SI | Observación |
| Q19 | - |  |  | SI | Toque el cuadrado azul |
| Q20 | - |  |  | SI | Observación |
| Q21 | - |  |  | SI | Toque el cuadrado rojo |
| Q22 | - |  |  | SI | Observación |
| Q23 | - |  |  | SI | Toque el círculo amarillo |
| Q24 | - |  |  | SI | Observación |
| Q25 | - |  |  | SI | Toque el círculo azul |
| Q26 | - |  |  | SI | Observación |
| Q27 | - |  |  | SI | Toque el cuadrado amarillo |
| Q28 | - |  |  | SI | Observación |
| Q29 | - |  |  | SI | Parte II (Use cuadrados y círculos grandes y chico... |
| Q30 | - |  |  | SI | Toque el círculo amarillo chico |
| Q31 | - |  |  | SI | Observación |
| Q32 | - |  |  | SI | Toque el círculo azul grande |
| Q33 | - |  |  | SI | Observación |
| Q34 | - |  |  | SI | Toque el círculo amarillo grande |
| Q35 | - |  |  | SI | Observación |
| Q36 | - |  |  | SI | Toque el cuadrado rojo grande |
| Q37 | - |  |  | SI | Observación |
| Q38 | - |  |  | SI | Toque el círculo azul chico |
| Q39 | - |  |  | SI | Observación |
| Q40 | - |  |  | SI | Toque el cuadrado amarillo chico |
| Q41 | - |  |  | SI | Observación |
| Q42 | - |  |  | SI | Parte III (Use los cuadrados y círculos grandes (6... |
| Q43 | - |  |  | SI | Toque el círculo amarillo y el cuadrado azul |
| Q44 | - |  |  | SI | Observación |
| Q45 | - |  |  | SI | Toque el cuadrado azul y el cuadrado amarillo |
| Q46 | - |  |  | SI | Observación |
| Q47 | - |  |  | SI | Toque el cuadrado rojo y el círculo azul |
| Q48 | - |  |  | SI | Observación |
| Q49 | - |  |  | SI | Toque el círculo rojo y el cuadrado amarillo |
| Q50 | - |  |  | SI | Observación |
| Q51 | - |  |  | SI | Toque el círculo azul y el cuadrado rojo |
| Q52 | - |  |  | SI | Observación |
| Q53 | - |  |  | SI | Toque el cuadrado amarillo y el cuadrado rojo |
| Q54 | - |  |  | SI | Observación |
| Q55 | - |  |  | SI | Parte IV (Use cuadrados y círculos grandes y chico... |
| Q56 | - |  |  | SI | Toque el círculo amarillo chico y el cuadrado rojo... |
| Q57 | - |  |  | SI | Observación |
| Q58 | - |  |  | SI | Toque el cuadrado azul chico y el círculo amarillo... |
| Q59 | - |  |  | SI | Observación |
| Q60 | - |  |  | SI | Toque el cuadrado azul grande y el cuadrado rojo c... |
| Q61 | - |  |  | SI | Observación |
| Q62 | - |  |  | SI | Toque el círculo rojo chico y el círculo amarillo ... |
| Q63 | - |  |  | SI | Observación |
| Q64 | - |  |  | SI | Toque el círculo amarillo grande y el círculo azul... |
| Q65 | - |  |  | SI | Observación |
| Q66 | - |  |  | SI | Toque el cuadrado rojo grande y el círculo amarill... |
| Q67 | - |  |  | SI | Observación |
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