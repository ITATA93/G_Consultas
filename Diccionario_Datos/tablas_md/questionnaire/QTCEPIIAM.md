# questionnaire.QTCEPIIAM

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric | PK |  | SI | Nº DAU |
| Q02 | numeric | PK |  | SI | Tiempo de evolución de síntomas previo ingreso a U... |
| Q03 | date | PK |  | SI | Ingreso del paciente |
| Q05 | varchar | PK |  | SI | 1 |
| Q05A | time | PK |  | SI | 1 |
| Q07 | varchar | PK |  | SI | 2 |
| Q07A | time | PK |  | SI | 2 |
| Q09 | varchar | PK |  | SI | 3 |
| Q09A | time | PK |  | SI | 3 |
| Q11 | varchar | PK |  | SI | 1T |
| Q11A | time | PK |  | SI | 1T |
| Q13 | varchar | PK |  | SI | 2T |
| Q13A | time | PK |  | SI | 2T |
| Q15 | varchar | PK |  | SI | 3T |
| Q15A | time | PK |  | SI | 3T |
| Q17 | varchar | PK |  | SI | IAM con elevación ST: |
| Q18 | varchar | PK |  | SI | IAM sin elevación ST: |
| Q19 | varchar | PK |  | SI | ANGOR INESTABLE |
| Q20 | varchar | PK |  | SI | OTRO IAM |
| Q20A | varchar | PK |  | SI | (Escriba diagnostico) |
| Q22 | varchar | PK |  | SI | Dolor torácico no IAM: |
| Q23 | varchar | PK |  | SI | (Escribir diagnostico) |
| Q24 | varchar | PK |  | SI | Trombolisis |
| Q24A | time | PK |  | SI | (en 30'de confirmación con ECG) |
| Q26 | varchar | PK |  | SI | Nitroglicerina |
| Q27 | varchar | PK |  | SI | Heparina |
| Q28 | varchar | PK |  | SI | Otros (especificar) |
| Q29 | varchar | PK |  | SI | Medidas generales en IAM con SDTS |
| Q29A | time | PK |  | SI | Hora de inicio  |
| Q31 | varchar | PK |  | SI | Hospitalización en H. Talagante |
| Q31A | date | PK |  | SI | Fecha |
| Q31B | time | PK |  | SI | Hora |
| Q34 | varchar | PK |  | SI | Traslado a serv. de mayor complejidad |
| Q34A | time | PK |  | SI | Hora |
| Q34B | varchar | PK |  | SI | Lugar |
| Q37 | varchar | PK |  | SI | Domicilio |
| Q37A | varchar | PK |  | SI | Comuna |
| Q39 | varchar | PK |  | SI | Observaciones |
| Q3A | time | PK |  | SI | Hora atención médica |
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