# SQLUser.MRC_DRGVersion

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGVER_RowId | bigint | PK |  | NO | - |
| DRGVER_Code | varchar |  |  | NO | Code |
| DRGVER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGVER_CostWeightEditDR | bigint |  | FK | SI | Cost Weight Edition DR |
| DRGVER_CreatedDate | date |  |  | SI | Created Date |
| DRGVER_CreatedTime | time |  |  | SI | Created Time |
| DRGVER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGVER_DateFrom | date |  |  | SI | Date From |
| DRGVER_DateTo | date |  |  | SI | Date To |
| DRGVER_Desc | varchar |  |  | NO | Description |
| DRGVER_Owner | varchar |  |  | SI | Owner |
| DRGVER_UpdatedDate | date |  |  | SI | Updated Date |
| DRGVER_UpdatedTime | time |  |  | SI | Updated Time |
| DRGVER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Asistente confirma que todos los miembros del equi... |
| Q02 | - |  |  | SI | Paciente correcto (Nombre, Primer y Segundo Apelli... |
| Q03 | - |  |  | SI | Área Operatoria |
| Q04 | - |  |  | SI | Procedimiento  / Intervención Quirúrgica |
| Q05 | - |  |  | SI | Algún punto crítico a considerar / Escenarios Impr... |
| Q06 | - |  |  | SI | Duración estimada de la Intervención |
| Q07 | - |  |  | SI | Pérdidas de sangres estimadas |
| Q08 | - |  |  | SI | Otros |
| Q09 | - |  |  | SI | Alguna condición de riesgo que pueda cambiar plan ... |
| Q10 | - |  |  | SI | Instrumental |
| Q11 | - |  |  | SI | Funcionamiento correcto de equipos |
| Q12 | - |  |  | SI | Administración de profilaxis quirúrgica con antimi... |
| Q13 | - |  |  | SI | Imágenes esenciales, disponibles e instaladas |
| Q14 | - |  |  | SI | Ropa |
| Q15 | - |  |  | SI | Observación |
| Q16 | - |  |  | SI | Comentario01 |
| Q17 | - |  |  | SI | comentario 02 |
| Q18 | - |  |  | SI | comentario 03 |
| Q19 | - |  |  | SI | Cometario 04 |
| Q20 | - |  |  | SI | Comentario 05 |
| Q21 | - |  |  | SI | comentario 06 |
| Q22 | - |  |  | SI | Lateralidad Cirugía Principal |
| Q23 | - |  |  | SI | comentario 07 |
| Q24 | - |  |  | SI | comentario 08 |
| Q25 | - |  |  | SI | comentario 09 |
| Q26 | - |  |  | SI | comentario 10 |
| Q27 | - |  |  | SI | comentario 11 |
| Q28 | - |  |  | SI | comentario 12 |
| Q29 | - |  |  | SI | comentario 13 |
| Q30 | - |  |  | SI | comentario 14 |
| Q31 | - |  |  | SI | comentario 15 |
| Q32 | - |  |  | SI | Otros |
| Q33 | - |  |  | SI | Lateralidad Cirugía Secundaria |
| Q34 | - |  |  | SI | Lateralidad Cirugía Terciaria |
| Q35 | - |  |  | SI | comentario lateralidad 2 |
| Q36 | - |  |  | SI | comentario lateralidad 3 |
| Q37 | - |  |  | SI | Comentarios/Observaciones |
| Q38 | - |  |  | SI | Riesgo de sangrado o embolia, protección de puntos... |
| Q39 | - |  |  | SI | Comentarios riesgo de sangrado o embolia |
| Q40 | - |  |  | SI | Esterilidad del Instrumental |
| Q41 | - |  |  | SI | Comentarios esterilidad del Instrumental |
| Q42 | - |  |  | SI | Disponibilidad de Implantes |
| Q43 | - |  |  | SI | Comentarios disponibilidad de Implantes |
| Q44 | - |  |  | SI | Recuento inicial correcto |
| Q45 | - |  |  | SI | Comentarios recuento inicial correcto |
| Q46 | - |  |  | SI | Lateralidad Cirugía Secundaria |
| Q47 | - |  |  | SI | Comentario Lateralidad Cirugía Secundaria |
| Q48 | - |  |  | SI | Prevención de Enfermedad Tromboembólica |
| Q49 | - |  |  | SI | Comentario Prevención de Enfermedad Tromboembólica |
| Q50 | - |  |  | SI | Destino Post-operatorio probable |
| Q51 | - |  |  | SI | Comentario Destino Post-operatorio probable |
| Q52 | - |  |  | SI | Indicadores que aprueban esterilización del materi... |
| Q53 | - |  |  | SI | Comentario Indicadores que aprueban esterilización... |
| Q54 | - |  |  | SI | Aspectos del material correctos |
| Q55 | - |  |  | SI | Comentarios Aspectos del material correctos |
| Q56 | - |  |  | SI | Alguna otra preocupación a considerar |
| Q57 | - |  |  | SI | Comentario Alguna otra preocupación a considerar |
| Q58 | - |  |  | SI | Profesional Responsable de la Medición |
| Q59 | - |  |  | SI | Cirugía / Procedimiento Principal |
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