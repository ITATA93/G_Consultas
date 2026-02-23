# questionnaire.QCLXXEVOST

> Registro Evaluación de Ostomía

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Registro Evaluación de Ostomía

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo de Ostomía |
| Q02 | varchar |  |  | SI | Localización |
| Q03 | varchar |  |  | SI | Otros elementos |
| Q04 | varchar |  |  | SI | Baguetas |
| Q05 | varchar |  |  | SI | Tutores |
| Q06 | varchar |  |  | SI | N° Tutores |
| Q07 | varchar |  |  | SI | Comentario Otros Elementos |
| Q08 | varchar |  |  | SI | Valoración de abdomen |
| Q09 | varchar |  |  | SI | Tamaño del estoma |
| Q10 | varchar |  |  | SI | Coloración del estoma |
| Q11 | varchar |  |  | SI | Elevación del estoma |
| Q12 | varchar |  |  | SI | Estado de la unión muco-cutánea |
| Q13 | varchar |  |  | SI | Forma del estoma |
| Q14 | varchar |  |  | SI | Orientación ángulo del drenaje |
| Q15 | varchar |  |  | SI | Estado de la piel periostomal: Sana |
| Q16 | varchar |  |  | SI | Características del efluente |
| Q17 | varchar |  |  | SI | Descripción Otro efluente |
| Q18 | varchar |  |  | SI | Volumen del efluente |
| Q19 | varchar |  |  | SI | Aspectos de la orina |
| Q20 | varchar |  |  | SI | Aspecto de las deposiciones |
| Q21 | varchar |  |  | SI | Acciones realizadas en la herida |
| Q22 | bit |  |  | SI | Limpieza con agua destilada estéril |
| Q23 | varchar |  |  | SI | Cantidad utilizada |
| Q24 | varchar |  |  | SI | Otra |
| Q25 | bit |  |  | SI | Limpieza con suero fisiológico 0,9% |
| Q26 | varchar |  |  | SI | Cantidad utilizada |
| Q27 | varchar |  |  | SI | Otra |
| Q28 | bit |  |  | SI | Limpieza con Prontosan |
| Q29 | varchar |  |  | SI | Cantidad utilizada |
| Q30 | varchar |  |  | SI | Otra |
| Q31 | bit |  |  | SI | Limpieza con Vashe |
| Q32 | varchar |  |  | SI | Cantidad utilizada |
| Q33 | varchar |  |  | SI | Otra |
| Q34 | varchar |  |  | SI | Otras acciones realizadas en la herida |
| Q35 | varchar |  |  | SI | Cobertura utilizada |
| Q36 | varchar |  |  | SI | Otra cobertura utilizada |
| Q37 | varchar |  |  | SI | Apósito interactivo |
| Q38 | varchar |  |  | SI | Otro apósito interactivo |
| Q39 | varchar |  |  | SI | Apósito bioactivo |
| Q40 | varchar |  |  | SI | Otro apósito bioactivo |
| Q41 | varchar |  |  | SI | Apósito mixto |
| Q42 | varchar |  |  | SI | Otro apósito mixto |
| Q43 | varchar |  |  | SI | Protector cutáneo |
| Q44 | varchar |  |  | SI | Otro protector cutáneo |
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