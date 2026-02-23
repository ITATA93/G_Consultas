# questionnaire.QTCETPVBR

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar | PK |  | SI | Peso |
| Q01ObsDR | varchar | PK | FK | SI | Peso DR |
| Q02 | varchar | PK |  | SI | Talla  |
| Q02ObsDR | varchar | PK | FK | SI | Talla  DR |
| Q03 | date | PK |  | SI | Fecha |
| Q04 | varchar | PK |  | SI | Diagnostico |
| Q05 | numeric | PK |  | SI | VEF 1 Esperando (Knudson) |
| Q06 | numeric | PK |  | SI | VEF 1 Basal |
| Q07 | numeric | PK |  | SI | VEF 1 Control Salino |
| Q08 | numeric | PK |  | SI | VEF 1 80% del Valor Control  |
| Q09 | numeric | PK |  | SI | VEF 1 Última Concentración  |
| Q10 | varchar | PK |  | SI | (mg/ml) |
| Q11 | numeric | PK |  | SI | VEF 1 80% del Valor Control  |
| Q12 | numeric | PK |  | SI | VEF 1 Post BD |
| Q13 | numeric | PK |  | SI | PC20  |
| Q14 | varchar | PK |  | SI | (mg/ml) |
| Q15 | varchar | PK |  | SI | Percepción de Obstrucción  |
| Q16 | varchar | PK |  | SI | Paciente |
| Q17 | varchar | PK |  | SI | Médico |
| Q18 | varchar | PK |  | SI | Observaciones |
| Q19 | varchar | PK |  | SI | Conclusión |
| Q20 | varchar | PK |  | SI | Profesional Informante  |
| Q21 | varchar | PK |  | SI | (L) |
| Q22 | varchar | PK |  | SI | (L) |
| Q23 | varchar | PK |  | SI | (L) |
| Q24 | varchar | PK |  | SI | (L) |
| Q25 | varchar | PK |  | SI | (L) |
| Q26 | varchar | PK |  | SI | (L) |
| Q27 | varchar | PK |  | SI | Edad |
| Q28 | varchar | PK |  | SI | Dias |
| Q29 | varchar | PK |  | SI | Meses |
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