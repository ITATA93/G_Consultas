# SQLUser.LB_WorksheetEntryTestSetItem

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBWSETSI_ParRef | varchar | PK |  | NO | - |
| ChildQ35DR | - |  |  | SI | Child Reference: Pulmonar |
| LBWSETSI_QCStatus | varchar |  |  | SI | QC Status
The display status of a qc test item on... |
| LBWSETSI_QCTestItem_DR | varchar |  | FK | SI | - |
| LBWSETSI_RowID | varchar |  |  | NO | - |
| LBWSETSI_Sequence | double |  |  | SI | - |
| LBWSETSI_TestSetItem_DR | varchar |  | FK | SI | - |
| Q01 | - |  |  | SI | Fecha de Ingreso |
| Q02 | - |  |  | SI | Hora de Ingreso |
| Q03 | - |  |  | SI | Información entregada por |
| Q04 | - |  |  | SI | Procedencia |
| Q05 | - |  |  | SI | Procedencia (otra) |
| Q06 | - |  |  | SI | Anamnesis Próxima |
| Q07 | - |  |  | SI | Factores de Riesgo Quirúrgico |
| Q08 | - |  |  | SI | Condición funcional basal |
| Q09 | - |  |  | SI | Utiliza red de salud |
| Q10 | - |  |  | SI | Pérdida significativa de peso |
| Q11 | - |  |  | SI | Medicamentos de uso habitual |
| Q12 | - |  |  | SI | Chequeo evaluación preoperatoria |
| Q13 | - |  |  | SI | Observación, medicamentos |
| Q14 | - |  |  | SI | Estado psíquico |
| Q15 | - |  |  | SI | Estado de conciencia |
| Q16 | - |  |  | SI | Paciente conciente, lúcido y orientado en tiempo y... |
| Q17 | - |  |  | SI | Hemodinamia estable, bien hidratado y perfundido. ... |
| Q18 | - |  |  | SI | Piel |
| Q19 | - |  |  | SI | P. Arterial Sistólica |
| Q19ObsDR | - |  |  | SI | P. Arterial Sistólica DR |
| Q20 | - |  |  | SI | P. Arterial Diastólica |
| Q20ObsDR | - |  |  | SI | P. Arterial Diastólica DR |
| Q21 | - |  |  | SI | Frecuencia cardíaca |
| Q21ObsDR | - |  |  | SI | Frecuencia cardíaca DR |
| Q22 | - |  |  | SI | Frecuencia Respiratoria |
| Q22ObsDR | - |  |  | SI | Frecuencia Respiratoria DR |
| Q23 | - |  |  | SI | Temperatura axilar |
| Q23ObsDR | - |  |  | SI | Temperatura axilar DR |
| Q24 | - |  |  | SI | Saturación O2 (%) |
| Q24ObsDR | - |  |  | SI | Saturación O2 (%) DR |
| Q25 | - |  |  | SI | FiO2 (%) |
| Q25ObsDR | - |  |  | SI | FiO2 (%) DR |
| Q26 | - |  |  | SI | Escala de dolor (EVA) |
| Q26ObsDR | - |  |  | SI | Escala de dolor (EVA) DR |
| Q27 | - |  |  | SI | Cabeza normal. Yugulares no ingurgitadas, pulso ca... |
| Q28 | - |  |  | SI | Cabeza y cuello |
| Q29 | - |  |  | SI | Descripción, cabeza y cuello |
| Q30 | - |  |  | SI | Resto del examen realizado, sin alteraciones (cyc) |
| Q31 | - |  |  | SI | Auscultación (<3) |
| Q32 | - |  |  | SI | Descripción, <3 |
| Q33 | - |  |  | SI | Ritmo regular en dos tiempos, sin soplos. |
| Q34 | - |  |  | SI | Resto del examen realizado, sin alteraciones (<3) |
| Q36 | - |  |  | SI | Resto del examen realizado sin alteraciones (pl) |
| Q37 | - |  |  | SI | Murmullo pulmonar simétrico normal, sin ruidos agr... |
| Q38 | - |  |  | SI | Descripción, pulmonar |
| Q40 | - |  |  | SI | Resto del examen realizado, sin alteraciones |
| Q41 | - |  |  | SI | Abdomen blando, depresible, indoloro. Ruidos hidro... |
| Q42 | - |  |  | SI | Descripción, abdomen |
| Q43 | - |  |  | SI | Región anogenital normal |
| Q44 | - |  |  | SI | Descripción, región anogenital |
| Q47 | - |  |  | SI | Extremidades normales, sin lesiones. Edema (-). Ar... |
| Q48 | - |  |  | SI | Descripción, extremidades |
| Q49 | - |  |  | SI | Exámenes de laboratorio |
| Q50 | - |  |  | SI | Exámenes de imagenología |
| Q51 | - |  |  | SI | Conclusión |
| Q52 | - |  |  | SI | Plan al Ingreso |
| Q53 | - |  |  | SI | Profesional de salud |
| Q54 | - |  |  | SI | Resto del examen realizado, sin alteraciones (ext) |
| Q55 | - |  |  | SI | Descripción examen físico general |
| Q56 | - |  |  | SI | Pulsos simétricos, amplitud normal. |
| Q57 | - |  |  | SI | Descripción Examen físico simple |
| Q58 | - |  |  | SI | Resto del examen realizado, sin alteraciones (anog... |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*