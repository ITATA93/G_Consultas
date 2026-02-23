# questionnaire.QCLXXREQ

> Registro Evaluación de Quemadura

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Evaluación de Quemadura

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo de quemadura |
| Q02 | varchar |  |  | SI | Porcentaje de quemadura |
| Q03 | varchar |  |  | SI | Cultivo |
| Q04 | varchar |  |  | SI | Resultado Cultivo |
| Q05 | varchar |  |  | SI | Valoración de Heridas / Úlceras |
| Q06 | varchar |  |  | SI | Aspecto de la herida |
| Q07 | varchar |  |  | SI | Profundidad |
| Q08 | varchar |  |  | SI | Exudado cantidad |
| Q09 | varchar |  |  | SI | Exudado calidad |
| Q10 | varchar |  |  | SI | Tejido esfacelado o necrótico |
| Q11 | varchar |  |  | SI | Tejido granulatorio |
| Q12 | varchar |  |  | SI | Edema |
| Q13 | varchar |  |  | SI | Escala del dolor |
| Q14 | varchar |  |  | SI | Piel circundante |
| Q15 | varchar |  |  | SI | Acciones realizadas en la quemadura |
| Q16 | bit |  |  | SI | Limpieza con agua destilada estéril |
| Q17 | bit |  |  | SI | Limpieza con suero fisiológico 0,9% |
| Q18 | bit |  |  | SI | Limpieza con Prontosan |
| Q19 | bit |  |  | SI | Limpieza con Vashe |
| Q20 | varchar |  |  | SI | cantidad utilizada |
| Q21 | varchar |  |  | SI | Curación Avanzada de Heridas |
| Q22 | varchar |  |  | SI | Detalle |
| Q23 | varchar |  |  | SI | Otras acciones realizadas en la quemadura |
| Q24 | varchar |  |  | SI | Cobertura utilizada |
| Q25 | varchar |  |  | SI | Otra cobertura utilizada |
| Q26 | varchar |  |  | SI | Apósito interactivo |
| Q27 | varchar |  |  | SI | Otro apósito interactivo |
| Q28 | varchar |  |  | SI | Apósito bioactivo |
| Q29 | varchar |  |  | SI | Otro apósito bioactivo |
| Q30 | varchar |  |  | SI | Apósito mixo |
| Q31 | varchar |  |  | SI | Otro apósito mixto |
| Q32 | varchar |  |  | SI | Protector cutáneo |
| Q33 | varchar |  |  | SI | Otro protector cutáneo |
| Q34 | varchar |  |  | SI | Vendaje de fijación |
| Q35 | varchar |  |  | SI | Otro vendaje de fijación |
| Q36 | varchar |  |  | SI | Terapia de Presión Negativa (TPN) /&nbsp;Vacuum As... |
| Q37 | varchar |  |  | SI | cantidad utilizada |
| Q38 | varchar |  |  | SI | Detalle |
| Q39 | varchar |  |  | SI | cantidad utilizada |
| Q40 | varchar |  |  | SI | Detalle |
| Q41 | varchar |  |  | SI | cantidad utilizada |
| Q42 | varchar |  |  | SI | Detalle |
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