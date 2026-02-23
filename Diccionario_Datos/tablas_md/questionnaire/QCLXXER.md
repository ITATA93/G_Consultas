# questionnaire.QCLXXER

> Egreso Recuperación Procedimiento / Cirugía Menor

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Egreso Recuperación Procedimiento / Cirugía Menor

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | time |  |  | SI | Hora Egreso / Alta |
| Q02 | varchar |  |  | SI | Estado del Paciente |
| Q03 | varchar |  |  | SI | Signos Vitales |
| Q04 | varchar |  |  | SI | Frecuencia Cardiaca |
| Q04ObsDR | varchar |  | FK | SI | Frecuencia Cardiaca DR |
| Q05 | varchar |  |  | SI | Presión Arterial Sistólica |
| Q05ObsDR | varchar |  | FK | SI | Presión Arterial Sistólica DR |
| Q06 | varchar |  |  | SI | Presión Arterial Diastólica |
| Q06ObsDR | varchar |  | FK | SI | Presión Arterial Diastólica DR |
| Q07 | varchar |  |  | SI | Presión Arterial Media |
| Q08 | varchar |  |  | SI | Frecuencia Respiratoria |
| Q08ObsDR | varchar |  | FK | SI | Frecuencia Respiratoria DR |
| Q09 | varchar |  |  | SI | Saturación O2 |
| Q09ObsDR | varchar |  | FK | SI | Saturación O2 DR |
| Q10 | varchar |  |  | SI | Hemoglucotest  |
| Q10ObsDR | varchar |  | FK | SI | Hemoglucotest  DR |
| Q11 | varchar |  |  | SI | Escala del Dolor (EVA) |
| Q11ObsDR | varchar |  | FK | SI | Escala del Dolor (EVA) DR |
| Q12 | varchar |  |  | SI | Entrega Pertenencias Paciente / Acompañante |
| Q13 | varchar |  |  | SI | Entrega de Exámenes Previos al Paciente/Acompañant... |
| Q14 | varchar |  |  | SI | Comentarios |
| Q15 | varchar |  |  | SI | Pertenencias y Accesorios |
| Q16 | varchar |  |  | SI | Comentarios |
| Q17 | varchar |  |  | SI | Instrucciones para retiro resultado de biopsia |
| Q18 | varchar |  |  | SI | Comentarios |
| Q19 | varchar |  |  | SI | Indicaciones al Alta (verbal o escrita) |
| Q20 | varchar |  |  | SI | Comentarios |
| Q21 | varchar |  |  | SI | Responsables |
| Q22 | varchar |  |  | SI | Médico / Odontólogo |
| Q23 | varchar |  |  | SI | Enfermera(o) |
| Q24 | varchar |  |  | SI | TENS / TONS |
| Q25 | varchar |  |  | SI | Observaciones Generales |
| Q26 | varchar |  |  | SI | FiO2 |
| Q26ObsDR | varchar |  | FK | SI | FiO2 DR |
| Q27 | varchar |  |  | SI | Escala de nivel de sedación (Ramsay) |
| Q28 | varchar |  |  | SI | ALD: Actividad |
| Q28ObsDR | varchar |  | FK | SI | ALD: Actividad DR |
| Q29 | varchar |  |  | SI | ALD: Respiración |
| Q29ObsDR | varchar |  | FK | SI | ALD: Respiración DR |
| Q30 | varchar |  |  | SI | ALD: Circulación |
| Q30ObsDR | varchar |  | FK | SI | ALD: Circulación DR |
| Q31 | varchar |  |  | SI | ALD: Nivel de Consciencia |
| Q31ObsDR | varchar |  | FK | SI | ALD: Nivel de Consciencia DR |
| Q32 | varchar |  |  | SI | ALD: Saturación de oxígeno |
| Q32ObsDR | varchar |  | FK | SI | ALD: Saturación de oxígeno DR |
| Q33 | varchar |  |  | SI | ALD: Puntaje |
| Q34 | varchar |  |  | SI | Escala de Aldrete Modificada |
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