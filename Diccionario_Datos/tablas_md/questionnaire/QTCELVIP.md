# questionnaire.QTCELVIP

> Lista de Verificación de Información Necesaria para el Paciente

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lista de Verificación de Información Necesaria para el Paciente

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Información General de Epilepsia |
| Q02 | varchar |  |  | SI | ¿Que es la Epilepsia? |
| Q03 | varchar |  |  | SI | Causas Probables |
| Q04 | varchar |  |  | SI | Explicación de procedimientos investigativos |
| Q05 | varchar |  |  | SI | Clasificación de la crisis |
| Q06 | varchar |  |  | SI | Síndrome |
| Q07 | varchar |  |  | SI | Epidemiología |
| Q08 | varchar |  |  | SI | Pronóstico |
| Q09 | varchar |  |  | SI | Genética |
| Q10 | varchar |  |  | SI | Muerte súbita en epilepsia |
| Q11 | varchar |  |  | SI | Drogas antiepilépticas |
| Q12 | varchar |  |  | SI | Elección de la droga |
| Q13 | varchar |  |  | SI | Eficacia |
| Q14 | varchar |  |  | SI | Efectos colaterales |
| Q15 | varchar |  |  | SI | Adherencia |
| Q16 | varchar |  |  | SI | Interacción con las drogas |
| Q17 | varchar |  |  | SI | Factores Gatillantes de Crisis |
| Q18 | varchar |  |  | SI | Falta de Sueño |
| Q19 | varchar |  |  | SI | Alcohol |
| Q20 | varchar |  |  | SI | Stress |
| Q21 | varchar |  |  | SI | Fotosensibilidad |
| Q22 | varchar |  |  | SI | Primeros Auxilios |
| Q23 | varchar |  |  | SI | Guía General |
| Q24 | varchar |  |  | SI | Status Epiléptico |
| Q25 | varchar |  |  | SI | Mujer con Epilepsia |
| Q26 | varchar |  |  | SI | Contracepción |
| Q27 | varchar |  |  | SI | Pre Concepción |
| Q28 | varchar |  |  | SI | Embarazo y lactancia |
| Q29 | varchar |  |  | SI | Menopausia |
| Q30 | varchar |  |  | SI | Estilos de Vida |
| Q31 | varchar |  |  | SI | Conducción de vehículos |
| Q32 | varchar |  |  | SI | Empleo |
| Q33 | varchar |  |  | SI | Educación (por ej. Guías para profesores) |
| Q34 | varchar |  |  | SI | Seguridad en casa |
| Q35 | varchar |  |  | SI | Descanso |
| Q36 | varchar |  |  | SI | Vida social |
| Q37 | varchar |  |  | SI | Posibles Consecuencias Psicosociales |
| Q38 | varchar |  |  | SI | Estigma |
| Q39 | varchar |  |  | SI | Pérdida de la memoria |
| Q40 | varchar |  |  | SI | Depresión |
| Q41 | varchar |  |  | SI | Ansiedad |
| Q42 | varchar |  |  | SI | Autoestima |
| Q43 | varchar |  |  | SI | Dificultades sexuales |
| Q44 | varchar |  |  | SI | Organización y Apoyo |
| Q45 | varchar |  |  | SI | Direcciones y números de teléfono de organizacione... |
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