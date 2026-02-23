# questionnaire.QTCEINGPRE

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Alfabeta |
| Q02 | varchar | PK |  | SI | Estudios |
| Q03 | numeric | PK |  | SI | Años Aprobados |
| Q04 | varchar | PK |  | SI | Evaluación Nutricional de la Embarazada |
| Q04ObsDR | varchar | PK | FK | SI | Evaluación Nutricional de la Embarazada DR |
| Q05 | varchar | PK |  | SI | Antecedentes Familiares |
| Q06 | varchar | PK |  | SI | Diabetes |
| Q07 | varchar | PK |  | SI | TBC Pulmonar |
| Q08 | varchar | PK |  | SI | Hipertensión Arterial |
| Q09 | varchar | PK |  | SI | CIE |
| Q10 | varchar | PK |  | SI | Peso habitual |
| Q10ObsDR | varchar | PK | FK | SI | Peso habitual DR |
| Q11 | varchar | PK |  | SI | Talla |
| Q11ObsDR | varchar | PK | FK | SI | Talla DR |
| Q12 | varchar | PK |  | SI | Examen Clínico Normal |
| Q13 | varchar | PK |  | SI | Examen Odontológico Normal |
| Q14 | varchar | PK |  | SI | Pelvis Normal |
| Q15 | varchar | PK |  | SI | Cervix Normal |
| Q16 | varchar | PK |  | SI | Tabaquismo |
| Q17 | numeric | PK |  | SI | Cigarrillos por Día |
| Q18 | varchar | PK |  | SI | Alcohol |
| Q19 | varchar | PK |  | SI | Pasta Base |
| Q20 | varchar | PK |  | SI | Cocaína |
| Q21 | varchar | PK |  | SI | Otras Adicciones |
| Q22 | varchar | PK |  | SI | ¿Embarazo planificado? |
| Q23 | varchar | PK |  | SI | Embarazo No Planificado |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*