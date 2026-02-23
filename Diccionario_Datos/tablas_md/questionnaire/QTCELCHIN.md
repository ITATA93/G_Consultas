# questionnaire.QTCELCHIN

> Lista de Chequeo para Seguridad en Cirugía: Pausa Quirúrgica (previa incisión)

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lista de Chequeo para Seguridad en Cirugía: Pausa Quirúrgica (previa incisión)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Asistente confirma que todos los miembros del equi... |
| Q02 | varchar |  |  | SI | Paciente correcto (Nombre, Primer y Segundo Apelli... |
| Q03 | varchar |  |  | SI | Área Operatoria |
| Q04 | varchar |  |  | SI | Procedimiento  / Intervención Quirúrgica |
| Q05 | varchar |  |  | SI | Algún punto crítico a considerar / Escenarios Impr... |
| Q06 | varchar |  |  | SI | Duración estimada de la Intervención |
| Q07 | varchar |  |  | SI | Pérdidas de sangres estimadas |
| Q08 | varchar |  |  | SI | Otros |
| Q09 | varchar |  |  | SI | Alguna condición de riesgo que pueda cambiar plan ... |
| Q10 | varchar |  |  | SI | Instrumental |
| Q11 | varchar |  |  | SI | Funcionamiento correcto de equipos |
| Q12 | varchar |  |  | SI | Administración de profilaxis quirúrgica con antimi... |
| Q13 | varchar |  |  | SI | Imágenes esenciales, disponibles e instaladas |
| Q14 | varchar |  |  | SI | Ropa |
| Q15 | varchar |  |  | SI | Observación |
| Q16 | varchar |  |  | SI | Comentario01 |
| Q17 | varchar |  |  | SI | comentario 02 |
| Q18 | varchar |  |  | SI | comentario 03 |
| Q19 | varchar |  |  | SI | Cometario 04 |
| Q20 | varchar |  |  | SI | Comentario 05 |
| Q21 | varchar |  |  | SI | comentario 06 |
| Q22 | varchar |  |  | SI | Lateralidad Cirugía Principal |
| Q23 | varchar |  |  | SI | comentario 07 |
| Q24 | varchar |  |  | SI | comentario 08 |
| Q25 | varchar |  |  | SI | comentario 09 |
| Q26 | varchar |  |  | SI | comentario 10 |
| Q27 | varchar |  |  | SI | comentario 11 |
| Q28 | varchar |  |  | SI | comentario 12 |
| Q29 | varchar |  |  | SI | comentario 13 |
| Q30 | varchar |  |  | SI | comentario 14 |
| Q31 | varchar |  |  | SI | comentario 15 |
| Q32 | varchar |  |  | SI | Otros |
| Q33 | varchar |  |  | SI | Lateralidad Cirugía Secundaria  |
| Q34 | varchar |  |  | SI | Lateralidad Cirugía Terciaria  |
| Q35 | varchar |  |  | SI | comentario lateralidad 2 |
| Q36 | varchar |  |  | SI | comentario lateralidad 3 |
| Q37 | varchar |  |  | SI | Comentarios/Observaciones |
| Q38 | varchar |  |  | SI | Riesgo de sangrado o embolia, protección de puntos... |
| Q39 | varchar |  |  | SI | Comentarios riesgo de sangrado o embolia |
| Q40 | varchar |  |  | SI | Esterilidad del Instrumental  |
| Q41 | varchar |  |  | SI | Comentarios esterilidad del Instrumental  |
| Q42 | varchar |  |  | SI | Disponibilidad de Implantes |
| Q43 | varchar |  |  | SI | Comentarios disponibilidad de Implantes |
| Q44 | varchar |  |  | SI | Recuento inicial correcto |
| Q45 | varchar |  |  | SI | Comentarios recuento inicial correcto |
| Q46 | varchar |  |  | SI | Lateralidad Cirugía Secundaria |
| Q47 | varchar |  |  | SI | Comentario Lateralidad Cirugía Secundaria |
| Q48 | varchar |  |  | SI | Prevención de Enfermedad Tromboembólica |
| Q49 | varchar |  |  | SI | Comentario Prevención de Enfermedad Tromboembólica |
| Q50 | varchar |  |  | SI | Destino Post-operatorio probable |
| Q51 | varchar |  |  | SI | Comentario Destino Post-operatorio probable |
| Q52 | varchar |  |  | SI | Indicadores que aprueban esterilización del materi... |
| Q53 | varchar |  |  | SI | Comentario Indicadores que aprueban esterilización... |
| Q54 | varchar |  |  | SI | Aspectos del material correctos |
| Q55 | varchar |  |  | SI | Comentarios Aspectos del material correctos  |
| Q56 | varchar |  |  | SI | Alguna otra preocupación a considerar |
| Q57 | varchar |  |  | SI | Comentario Alguna otra preocupación a considerar |
| Q58 | varchar |  |  | SI | Profesional Responsable de la Medición |
| Q59 | varchar |  |  | SI | Cirugía / Procedimiento Principal |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*