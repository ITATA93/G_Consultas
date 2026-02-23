# questionnaire.QTCEDIALMED

**Schema:** questionnaire
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric | PK |  | SI | Peso Seco |
| Q02 | varchar | PK |  | SI | Filtro |
| Q03 | varchar | PK |  | SI | Acceso Vascular |
| Q04 | numeric | PK |  | SI | QB (FS) |
| Q05 | numeric | PK |  | SI | QD (FD) |
| Q06 | numeric | PK |  | SI | QT (TD en minutos) |
| Q07 | numeric | PK |  | SI | NA+ |
| Q08 | numeric | PK |  | SI | K+ (meq / litro) |
| Q09 | numeric | PK |  | SI | Ca+ (meq / litro) |
| Q10 | varchar | PK |  | SI | Bicarbonato |
| Q11 | varchar | PK |  | SI | Concentrado |
| Q12 | numeric | PK |  | SI | Heparina Inicio (en miles de unidades) |
| Q13 | numeric | PK |  | SI | Heparina Mantención (en miles de unidades) |
| Q14 | date | PK |  | SI | Fecha de Sesión |
| Q15 | numeric | PK |  | SI | Programación (Peso en gramos) |
| Q16 | numeric | PK |  | SI | Ingreso Colación |
| Q17 | numeric | PK |  | SI | Ingreso Suero (Cebado) |
| Q18 | numeric | PK |  | SI | Suero |
| Q19 | numeric | PK |  | SI | Sangre |
| Q20 | numeric | PK |  | SI | Albúmina |
| Q21 | numeric | PK |  | SI | Fierro |
| Q22 | varchar | PK |  | SI | Total Programación |
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