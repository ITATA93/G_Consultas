# SQLUser.ORC_OperationItemLink

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINK_ParRef | bigint | PK |  | NO | ORC_Operation Parent Reference |
| LINK_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| LINK_Childsub | double |  |  | NO | Childsub |
| LINK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LINK_CreatedDate | date |  |  | SI | Created Date |
| LINK_CreatedTime | time |  |  | SI | Created Time |
| LINK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LINK_MinAmt | double |  |  | SI | MinAmt |
| LINK_MinValueMainItem | varchar |  |  | SI | Min Value of Main Item |
| LINK_OfCode | varchar |  |  | SI | Of Code |
| LINK_Percent | double |  |  | SI | Percent |
| LINK_RowId | varchar |  |  | NO | - |
| LINK_UpdatedDate | date |  |  | SI | Updated Date |
| LINK_UpdatedTime | time |  |  | SI | Updated Time |
| LINK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Diagnóstico Principal |
| Q04 | - |  |  | SI | Otros |
| Q05 | - |  |  | SI | Razón principal |
| Q06 | - |  |  | SI | Fase |
| Q07 | - |  |  | SI | Protocolo |
| Q08 | - |  |  | SI | Otros |
| Q09 | - |  |  | SI | Procedimientos / Intervenciones |
| Q10 | - |  |  | SI | Otros |
| Q11 | - |  |  | SI | Terapia |
| Q12 | - |  |  | SI | Número de examen |
| Q13 | - |  |  | SI | Fecha del examen |
| Q14 | - |  |  | SI | Fecha inicial |
| Q15 | - |  |  | SI | Ritmo basal |
| Q16 | - |  |  | SI | Otros |
| Q17 | - |  |  | SI | Conducción intraventricular (IV) |
| Q18 | - |  |  | SI | Arritmia ventricular |
| Q19 | - |  |  | SI | Arritmia supraventricular |
| Q20 | - |  |  | SI | Presión arterial sistólica basal (mmHg) |
| Q21 | - |  |  | SI | Presión arterial diastólica basal (mmHg) |
| Q22 | - |  |  | SI | Frecuencia cardíaca basal (FC) (lpm) |
| Q23 | - |  |  | SI | Producto doble basal (DP)(lpm*mmHg) |
| Q24 | - |  |  | SI | Datos máximos |
| Q25 | - |  |  | SI | Duración del ejercicio |
| Q26 | - |  |  | SI | Razón de finalización |
| Q27 | - |  |  | SI | Presión arterial sistólica máxima (mmHg) |
| Q28 | - |  |  | SI | Presión arterial diastólica máxima (mmHg) |
| Q29 | - |  |  | SI | Frecuencia cardíaca máxima (lpm) |
| Q30 | - |  |  | SI | Producto doble máximo (DP) (lpm*mmHg) |
| Q31 | - |  |  | SI | Presión arterial sistólica de recuperación (mmHg) |
| Q32 | - |  |  | SI | Presión arterial diastólica de recuperación (mmHg) |
| Q33 | - |  |  | SI | Frecuencia cardíaca de recuperación (lpm) |
| Q34 | - |  |  | SI | Producto doble de recuperación (DP) (lpm*mmHg) |
| Q35 | - |  |  | SI | Resultado |
| Q36 | - |  |  | SI | Resultado |
| Q37 | - |  |  | SI | Angina |
| Q38 | - |  |  | SI | En el minuto |
| Q39 | - |  |  | SI | Escala de Borg |
| Q39ObsDR | - |  |  | SI | Escala de Borg DR |
| Q40 | - |  |  | SI | Presión arterial sistólica (mmHg) |
| Q40ObsDR | - |  |  | SI | Presión arterial sistólica (mmHg) DR |
| Q41 | - |  |  | SI | Presión arterial diastólica (mmHg) |
| Q41ObsDR | - |  |  | SI | Presión arterial diastólica (mmHg) DR |
| Q42 | - |  |  | SI | Frecuencia cardíaca (lpm) |
| Q42ObsDR | - |  |  | SI | Frecuencia cardíaca (lpm) DR |
| Q43 | - |  |  | SI | Producto doble (DP) (lpm*mmHg) |
| Q44 | - |  |  | SI | Otras variaciones en el ECG |
| Q45 | - |  |  | SI | Arritmia por estrés |
| Q46 | - |  |  | SI | Arritmia ventricular |
| Q47 | - |  |  | SI | Arritmia supraventricular |
| Q48 | - |  |  | SI | Arritmia de Recuperación |
| Q49 | - |  |  | SI | Arritmia ventricular |
| Q50 | - |  |  | SI | Arritmia supraventricular |
| Q51 | - |  |  | SI | Conclusión |
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