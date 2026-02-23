# questionnaire.QTCECGST

> Prueba de Esfuerzo con Electrocardiograma (ECG)

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Prueba de Esfuerzo con Electrocardiograma (ECG)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha |
| Q02 | time |  |  | SI | Hora |
| Q03 | varchar |  |  | SI | Diagnóstico Principal |
| Q04 | varchar |  |  | SI | Otros |
| Q05 | varchar |  |  | SI | Razón principal |
| Q06 | varchar |  |  | SI | Fase |
| Q07 | varchar |  |  | SI | Protocolo |
| Q08 | varchar |  |  | SI | Otros |
| Q09 | varchar |  |  | SI | Procedimientos / Intervenciones |
| Q10 | varchar |  |  | SI | Otros |
| Q11 | varchar |  |  | SI | Terapia |
| Q12 | numeric |  |  | SI | Número de examen |
| Q13 | date |  |  | SI | Fecha del examen |
| Q14 | varchar |  |  | SI | Fecha inicial |
| Q15 | varchar |  |  | SI | Ritmo basal |
| Q16 | varchar |  |  | SI | Otros |
| Q17 | varchar |  |  | SI | Conducción intraventricular (IV) |
| Q18 | varchar |  |  | SI | Arritmia ventricular |
| Q19 | varchar |  |  | SI | Arritmia supraventricular |
| Q20 | numeric |  |  | SI | Presión arterial sistólica basal (mmHg) |
| Q21 | numeric |  |  | SI | Presión arterial diastólica basal (mmHg) |
| Q22 | numeric |  |  | SI | Frecuencia cardíaca basal (FC) (lpm) |
| Q23 | numeric |  |  | SI | Producto doble basal (DP)(lpm*mmHg) |
| Q24 | varchar |  |  | SI | Datos máximos |
| Q25 | numeric |  |  | SI | Duración del ejercicio |
| Q26 | varchar |  |  | SI | Razón de finalización |
| Q27 | numeric |  |  | SI | Presión arterial sistólica máxima (mmHg) |
| Q28 | numeric |  |  | SI | Presión arterial diastólica máxima (mmHg) |
| Q29 | numeric |  |  | SI | Frecuencia cardíaca máxima (lpm) |
| Q30 | numeric |  |  | SI | Producto doble máximo (DP) (lpm*mmHg) |
| Q31 | numeric |  |  | SI | Presión arterial sistólica de recuperación (mmHg) |
| Q32 | numeric |  |  | SI | Presión arterial diastólica de recuperación (mmHg) |
| Q33 | numeric |  |  | SI | Frecuencia cardíaca de recuperación (lpm) |
| Q34 | numeric |  |  | SI | Producto doble de recuperación (DP) (lpm*mmHg) |
| Q35 | varchar |  |  | SI | Resultado |
| Q36 | varchar |  |  | SI | Resultado |
| Q37 | varchar |  |  | SI | Angina |
| Q38 | numeric |  |  | SI | En el minuto |
| Q39 | varchar |  |  | SI | Escala de Borg |
| Q39ObsDR | varchar |  | FK | SI | Escala de Borg DR |
| Q40 | varchar |  |  | SI | Presión arterial sistólica (mmHg) |
| Q40ObsDR | varchar |  | FK | SI | Presión arterial sistólica (mmHg) DR |
| Q41 | varchar |  |  | SI | Presión arterial diastólica (mmHg) |
| Q41ObsDR | varchar |  | FK | SI | Presión arterial diastólica (mmHg) DR |
| Q42 | varchar |  |  | SI | Frecuencia cardíaca (lpm) |
| Q42ObsDR | varchar |  | FK | SI | Frecuencia cardíaca (lpm) DR |
| Q43 | numeric |  |  | SI | Producto doble (DP) (lpm*mmHg) |
| Q44 | varchar |  |  | SI | Otras variaciones en el ECG |
| Q45 | varchar |  |  | SI | Arritmia por estrés |
| Q46 | varchar |  |  | SI | Arritmia ventricular |
| Q47 | varchar |  |  | SI | Arritmia supraventricular |
| Q48 | varchar |  |  | SI | Arritmia de Recuperación |
| Q49 | varchar |  |  | SI | Arritmia ventricular |
| Q50 | varchar |  |  | SI | Arritmia supraventricular |
| Q51 | varchar |  |  | SI | Conclusión |
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