# questionnaire.QTCEIRPO

> Ingreso Recuperación

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Recuperación

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Estado Mental/Emocional |
| Q02 | varchar |  |  | SI | Nivel de sedación |
| Q03 | varchar |  |  | SI | Estado de la Piel |
| Q04 | varchar |  |  | SI | Localización y Tipo de Lesión |
| Q05 | varchar |  |  | SI | Dispositivo Vía Aérea |
| Q06 | varchar |  |  | SI | Otro  |
| Q07 | varchar |  |  | SI | Comentario Uso Bomba de Infusión |
| Q08 | varchar |  |  | SI | Monitorización Traslado |
| Q09 | varchar |  |  | SI | Otro |
| Q10 | varchar |  |  | SI | Transportado en: |
| Q11 | varchar |  |  | SI | Destino Post-operatorio  |
| Q12 | varchar |  |  | SI | Responsable del traslado  |
| Q13 | varchar |  |  | SI | Estado Mental /Emocional |
| Q14 | varchar |  |  | SI | Estado de piel  (otra) |
| Q15 | varchar |  |  | SI | Recuperacion de la Anestesia |
| Q16 | varchar |  |  | SI | Evaluación Zona Operatoria |
| Q17 | varchar |  |  | SI | Comentario Uso Medias Antiembólicas |
| Q18 | varchar |  |  | SI | Uso  Medias Antiembólicas |
| Q19 | varchar |  |  | SI | Uso de Compresion Neumática |
| Q20 | varchar |  |  | SI | Comentario Uso de Compresión Neumática |
| Q21 | varchar |  |  | SI | Uso Bomba de  Infusión |
| Q22 | varchar |  |  | SI | Uso  Bomba Infusión |
| Q23 | varchar |  |  | SI | Procedencia |
| Q24 | varchar |  |  | SI | estado de la piel |
| Q25 | varchar |  |  | SI | Temporalidad Recuperación |
| Q26 | varchar |  |  | SI | Vía Aérea |
| Q27 | varchar |  |  | SI | Respiración |
| Q28 | varchar |  |  | SI | Cardiaco |
| Q29 | bit |  |  | SI | Emocional |
| Q30 | bit |  |  | SI | Ambiental |
| Q31 | bit |  |  | SI | Farmacológico |
| Q32 | bit |  |  | SI | Mecánica |
| Q33 | varchar |  |  | SI | Comentarios Emocional |
| Q34 | varchar |  |  | SI | Comentarios Ambiental |
| Q35 | varchar |  |  | SI | Comentarios Farmacológicos  |
| Q36 | varchar |  |  | SI | Comentarios Mecánica |
| Q37 | varchar |  |  | SI | Termorregulación |
| Q38 | varchar |  |  | SI | Comentarios Termorregulación |
| Q39 | varchar |  |  | SI | Comentarios Evaluación General |
| Q40 | varchar |  |  | SI | Cama Baja |
| Q41 | varchar |  |  | SI | Comentarios |
| Q42 | varchar |  |  | SI | Barandas en Alto |
| Q43 | varchar |  |  | SI | Comentarios |
| Q44 | varchar |  |  | SI | Paciente Vigilado |
| Q45 | varchar |  |  | SI | Comentarios |
| Q46 | varchar |  |  | SI | Freno Activado |
| Q47 | varchar |  |  | SI | Comentarios |
| Q48 | varchar |  |  | SI | Timbre a Mano |
| Q49 | varchar |  |  | SI | Comentarios |
| Q50 | varchar |  |  | SI | Observaciones Generales |
| Q51 | varchar |  |  | SI | Prevención de Caídas |
| Q52 | varchar |  |  | SI | Razón de no evaluación  |
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