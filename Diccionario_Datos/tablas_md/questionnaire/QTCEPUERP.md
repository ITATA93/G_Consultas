# questionnaire.QTCEPUERP

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Embarazo Controlado |
| Q02 | varchar | PK |  | SI | Recibió preparación para el parto |
| Q03 | varchar | PK |  | SI | Trabajo de parto acompañada |
| Q04 | varchar | PK |  | SI | Parto acompañada |
| Q05 | date | PK |  | SI | Fecha Término embarazo |
| Q06 | varchar | PK |  | SI | Muerte Intrauterina |
| Q07 | varchar | PK |  | SI | Parto |
| Q08 | varchar | PK |  | SI | Tipo Parto |
| Q09 | varchar | PK |  | SI | Episiotomía |
| Q10 | varchar | PK |  | SI | Desgarro |
| Q11 | varchar | PK |  | SI | Inicio de trabajo de Parto |
| Q12 | varchar | PK |  | SI | Revisión Instrumental |
| Q13 | varchar | PK |  | SI | Indicaciones parto operatorio |
| Q14 | varchar | PK |  | SI | Esterilización Quirúrgica |
| Q15 | varchar | PK |  | SI | 4° VDRL |
| Q16 | varchar | PK |  | SI | Atención Parto |
| Q17 | varchar | PK |  | SI | Anestesia |
| Q18 | varchar | PK |  | SI | Medicamentos |
| Q19 | varchar | PK |  | SI | Especifique Medicamentos |
| Q20 | varchar | PK |  | SI | Recien Nacido |
| Q21 | varchar | PK |  | SI | Peso al Nacer |
| Q22 | varchar | PK |  | SI | Contacto inmediato con la madre en sala de partos: |
| Q23 | varchar | PK |  | SI | Diagnostico RN |
| Q24 | date | PK |  | SI | Fecha de Egreso de la Madre |
| Q25 | varchar | PK |  | SI | Diagnóstico de Egreso |
| Q26 | varchar | PK |  | SI | Derivada a |
| Q27 | date | PK |  | SI | Fecha de Control |
| Q28 | varchar | PK |  | SI | Diagnóstico al Control |
| Q29 | varchar | PK |  | SI | Lactancia Materna |
| Q30 | varchar | PK |  | SI | Indicaciones / Observaciones |
| Q31 | varchar | PK |  | SI | 4° RPR |
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