# questionnaire.QTCECOPLFA

**Schema:** questionnaire
**Columnas:** 59
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Nombre del Fármaco |
| Q02 | varchar | PK |  | SI | Vía de Administración |
| Q03 | numeric | PK |  | SI | MG Totales / día |
| Q04 | time | PK |  | SI | Horario Medicación |
| Q05 | varchar | PK |  | SI | Acatamiento de la medicación |
| Q06 | varchar | PK |  | SI | Comentario Crisis |
| Q07 | varchar | PK |  | SI | Crisis |
| Q08 | varchar | PK |  | SI | Inicio de Tratamiento |
| Q09 | date | PK |  | SI | Fecha de Inicio |
| Q10 | varchar | PK |  | SI | Control de Tratamiento |
| Q11 | varchar | PK |  | SI | Sospecha de intoxicación |
| Q12 | numeric | PK |  | SI | Nivel Plasmático Previo mg/dl |
| Q13 | numeric | PK |  | SI | Última dosis: mg |
| Q14 | date | PK |  | SI | Fecha última dosis |
| Q15 | time | PK |  | SI | Hora última dosis |
| Q16 | date | PK |  | SI | Fecha Toma de muestra |
| Q17 | time | PK |  | SI | Hora toma de muestra |
| Q18 | varchar | PK |  | SI | Comentarios  Nombre Fármaco |
| Q19 | date | PK |  | SI | Fecha Nivel Plásmatico Previo |
| Q20 | numeric | PK |  | SI | Nivel Plasmático Actual mg/dl |
| Q21 | date | PK |  | SI | Fecha Nivel Plasmático Actual |
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