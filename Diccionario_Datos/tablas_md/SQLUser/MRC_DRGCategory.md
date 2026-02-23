# SQLUser.MRC_DRGCategory

**Schema:** SQLUser
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGCAT_RowId | bigint | PK |  | NO | - |
| DRGCAT_Code | varchar |  |  | NO | Code |
| DRGCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGCAT_CreatedDate | date |  |  | SI | Created Date |
| DRGCAT_CreatedTime | time |  |  | SI | Created Time |
| DRGCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGCAT_Desc | varchar |  |  | NO | Description |
| DRGCAT_Owner | varchar |  |  | SI | Owner |
| DRGCAT_UpdatedDate | date |  |  | SI | Updated Date |
| DRGCAT_UpdatedTime | time |  |  | SI | Updated Time |
| DRGCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Antecedentes/Historia Clínica |
| Q01a | - |  |  | SI | Flexión |
| Q01b | - |  |  | SI | Flexión |
| Q02 | - |  |  | SI | Escala de EVA |
| Q02a | - |  |  | SI | Extensión |
| Q02b | - |  |  | SI | Extensión |
| Q03 | - |  |  | SI | Localización |
| Q03a | - |  |  | SI | Abducción |
| Q03b | - |  |  | SI | Abducción |
| Q04a | - |  |  | SI | Aducción |
| Q04b | - |  |  | SI | Aducción |
| Q05a | - |  |  | SI | Rot interna |
| Q05b | - |  |  | SI | Rot interna |
| Q06a | - |  |  | SI | Rot externa |
| Q06b | - |  |  | SI | Rot externa |
| Q07 | - |  |  | SI | Comentarios |
| Q08a | - |  |  | SI | Flexión |
| Q08b | - |  |  | SI | Flexión |
| Q09a | - |  |  | SI | Extensión |
| Q09b | - |  |  | SI | Extensión |
| Q10a | - |  |  | SI | Pronación |
| Q10b | - |  |  | SI | Pronación |
| Q11a | - |  |  | SI | Supinación |
| Q11b | - |  |  | SI | Supinación |
| Q12 | - |  |  | SI | Comentarios |
| Q13a | - |  |  | SI | Flexión |
| Q13b | - |  |  | SI | Flexión |
| Q14a | - |  |  | SI | Extensión |
| Q14b | - |  |  | SI | Extensión |
| Q15a | - |  |  | SI | Desv cubital |
| Q15b | - |  |  | SI | Desv cubital |
| Q16a | - |  |  | SI | Desv Radial |
| Q16b | - |  |  | SI | Desv Radial |
| Q17 | - |  |  | SI | Comentarios |
| Q18 | - |  |  | SI | Puño |
| Q19a | - |  |  | SI | Fuerza de Garra |
| Q19b | - |  |  | SI | Fuerza de Garra |
| Q20a | - |  |  | SI | Fuerza de Pinza |
| Q20b | - |  |  | SI | Fuerza de Pinza |
| Q21 | - |  |  | SI | Movilidad de EESS |
| Q22 | - |  |  | SI | Alineación Postural |
| Q23 | - |  |  | SI | Equilibrio Estático y Dinámico |
| Q24 | - |  |  | SI | Prehensiones Gruesas y Pinzas |
| Q25 | - |  |  | SI | Tono |
| Q26 | - |  |  | SI | Sensibilidad Superficial/Profundo |
| Q27 | - |  |  | SI | Movilidad de EEII |
| Q28 | - |  |  | SI | Deformidad y Calidad de Piel |
| Q28a | - |  |  | SI | Fibrosis |
| Q28a1 | - |  |  | SI | Hiperplasia |
| Q28a2 | - |  |  | SI | Coloración |
| Q28a3 | - |  |  | SI | Temperatura |
| Q28a4 | - |  |  | SI | Adherencias |
| Q29 | - |  |  | SI | Centímetros |
| Q30 | - |  |  | SI | Localización |
| Q31 | - |  |  | SI | Uso de AT o adaptaciones |
| Q32 | - |  |  | SI | Básicas |
| Q33 | - |  |  | SI | Instrumentales |
| Q34 | - |  |  | SI | Independencia (Barthel/Otra) |
| Q35 | - |  |  | SI | Descripción |
| Q36 | - |  |  | SI | Se Reincorpora a Misma u Otra Actividad |
| Q37 | - |  |  | SI | Tiempo Transcurrido |
| Q38 | - |  |  | SI | Manejo en el Hogar/Cuidado de Otros |
| Q39 | - |  |  | SI | Tipo de Actividades |
| Q40 | - |  |  | SI | Reincorporación a Actividades Anteriores |
| Q41 | - |  |  | SI | Nuevas Actividades |
| Q42 | - |  |  | SI | Observaciones / Grado de Satisfacción con Proceso |
| Q67 | - |  |  | SI | Puño |
| Q68 | - |  |  | SI | Movimientos de Hombro |
| Q69 | - |  |  | SI | Movimientos de Codo |
| Q70 | - |  |  | SI | Movimientos de Muñeca |
| Q71 | - |  |  | SI | Movimientos Funcionales de Mano |
| Q72 | - |  |  | SI | Evaluación General |
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