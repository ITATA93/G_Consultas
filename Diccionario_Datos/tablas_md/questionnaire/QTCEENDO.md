# questionnaire.QTCEENDO

> Endodoncia

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(Endodoncia)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tratamiento Endodóntico |
| Q02 | varchar |  |  | SI | Piezas |
| Q03 | varchar |  |  | SI | 1. Preparación de conducto(s) e instrumentos biome... |
| Q04 | varchar |  |  | SI | Longitud Aparente del Diente |
| Q05 | varchar |  |  | SI | Radiografía de Control de Longitud |
| Q06 | varchar |  |  | SI | Longitud Real del Diente |
| Q07 | varchar |  |  | SI | 2. Irrigación y acondicionamiento |
| Q10 | bit |  |  | SI | Imprimir Indicaciones |
| Q11 | varchar |  |  | SI | Radiografia de Control |
| Q12 | varchar |  |  | SI | Observaciones |
| Q17 | varchar |  |  | SI | Pronostico |
| Q18 | varchar |  |  | SI | Conductor |
| Q19 | varchar |  |  | SI | Conducto 2 |
| Q20 | varchar |  |  | SI | Conducto 3 |
| Q21 | varchar |  |  | SI | Conducto 4 |
| Q22 | varchar |  |  | SI | Longitud Aparente del Diente 2 |
| Q23 | varchar |  |  | SI | Longitud Aparente del Diente 3 |
| Q24 | varchar |  |  | SI | Longitud Aparente del Diente 4 |
| Q25 | varchar |  |  | SI | Radiografía de Control de Longitud 2 |
| Q26 | varchar |  |  | SI | Radiografía de Control de Longitud 3 |
| Q27 | varchar |  |  | SI | Radiografía de Control de Longitud 4 |
| Q28 | longvarbinary |  |  | SI | Imprimir |
| Q28UDt | date |  |  | SI | Imprimir Last Updated Date |
| Q28UTm | time |  |  | SI | Imprimir Last Updated Time |
| Q29 | varchar |  |  | SI | 3. Sellando de Conducto |
| Q32 | varchar |  |  | SI | observacion 1 |
| Q39 | varchar |  |  | SI | Categoria de la carta  |
| Q41 | varchar |  |  | SI | Digitado Por |
| Q50 | varchar |  |  | SI | Longitud Real del Diente 2 |
| Q51 | varchar |  |  | SI | Longitud Real del Diente 3 |
| Q52 | varchar |  |  | SI | Longitud Real del Diente 4 |
| QRem1 | date |  |  | SI | Instalación/Alta |
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