# SQLUser.MRC_RiskEvalParam

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REP_RowId1 | varchar | PK |  | NO | - |
| ChildQ53DR | - |  |  | SI | Child Reference: Dispositivos Invasivos |
| Q01 | - |  |  | SI | Estado Mental/Emocional |
| Q02 | - |  |  | SI | Nivel de sedación |
| Q03 | - |  |  | SI | Estado de la Piel |
| Q04 | - |  |  | SI | Localización y Tipo de Lesión |
| Q05 | - |  |  | SI | Dispositivo Vía Aérea |
| Q06 | - |  |  | SI | Otro |
| Q07 | - |  |  | SI | Comentario Uso Bomba de Infusión |
| Q08 | - |  |  | SI | Monitorización Traslado |
| Q09 | - |  |  | SI | Otro |
| Q10 | - |  |  | SI | Transportado en: |
| Q11 | - |  |  | SI | Destino Post-operatorio |
| Q12 | - |  |  | SI | Responsable del traslado |
| Q13 | - |  |  | SI | Estado Mental /Emocional |
| Q14 | - |  |  | SI | Estado de piel  (otra) |
| Q15 | - |  |  | SI | Recuperacion de la Anestesia |
| Q16 | - |  |  | SI | Evaluación Zona Operatoria |
| Q17 | - |  |  | SI | Comentario Uso Medias Antiembólicas |
| Q18 | - |  |  | SI | Uso  Medias Antiembólicas |
| Q19 | - |  |  | SI | Uso de Compresion Neumática |
| Q20 | - |  |  | SI | Comentario Uso de Compresión Neumática |
| Q21 | - |  |  | SI | Uso Bomba de  Infusión |
| Q22 | - |  |  | SI | Uso  Bomba Infusión |
| Q23 | - |  |  | SI | Procedencia |
| Q24 | - |  |  | SI | estado de la piel |
| Q25 | - |  |  | SI | Temporalidad Recuperación |
| Q26 | - |  |  | SI | Vía Aérea |
| Q27 | - |  |  | SI | Respiración |
| Q28 | - |  |  | SI | Cardiaco |
| Q29 | - |  |  | SI | Emocional |
| Q30 | - |  |  | SI | Ambiental |
| Q31 | - |  |  | SI | Farmacológico |
| Q32 | - |  |  | SI | Mecánica |
| Q33 | - |  |  | SI | Comentarios Emocional |
| Q34 | - |  |  | SI | Comentarios Ambiental |
| Q35 | - |  |  | SI | Comentarios Farmacológicos |
| Q36 | - |  |  | SI | Comentarios Mecánica |
| Q37 | - |  |  | SI | Termorregulación |
| Q38 | - |  |  | SI | Comentarios Termorregulación |
| Q39 | - |  |  | SI | Comentarios Evaluación General |
| Q40 | - |  |  | SI | Cama Baja |
| Q41 | - |  |  | SI | Comentarios |
| Q42 | - |  |  | SI | Barandas en Alto |
| Q43 | - |  |  | SI | Comentarios |
| Q44 | - |  |  | SI | Paciente Vigilado |
| Q45 | - |  |  | SI | Comentarios |
| Q46 | - |  |  | SI | Freno Activado |
| Q47 | - |  |  | SI | Comentarios |
| Q48 | - |  |  | SI | Timbre a Mano |
| Q49 | - |  |  | SI | Comentarios |
| Q50 | - |  |  | SI | Observaciones Generales |
| Q51 | - |  |  | SI | Prevención de Caídas |
| Q52 | - |  |  | SI | Razón de no evaluación |
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
| REP_Code | varchar |  |  | NO | Code |
| REP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REP_CreatedDate | date |  |  | SI | Created Date |
| REP_CreatedTime | time |  |  | SI | Created Time |
| REP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REP_Desc | varchar |  |  | NO | Description |
| REP_Owner | varchar |  |  | SI | Owner |
| REP_RowId | varchar |  |  | NO | MRC_RiskEvalParam Row ID |
| REP_UpdatedDate | date |  |  | SI | Updated Date |
| REP_UpdatedTime | time |  |  | SI | Updated Time |
| REP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*