# questionnaire.QTCEARNER

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric | PK |  | SI | PESO |
| Q02 | numeric | PK |  | SI | TALLA |
| Q03 | varchar | PK |  | SI | C.CRANEANA  |
| Q04 | varchar | PK |  | SI | C. TORACICA |
| Q05 | varchar | PK |  | SI | EDAD GESTACIONAL POR FUR |
| Q06 | bit | PK |  | SI | RN POSTERMINO  |
| Q07 | bit | PK |  | SI | PEG |
| Q08 | numeric | PK |  | SI | EDAD GESTACIONAL POR ECO |
| Q09 | bit | PK |  | SI | RN TERMINO |
| Q10 | bit | PK |  | SI | AEG |
| Q11 | varchar | PK |  | SI | MADUREZ GESTIONAL POR EXAMEN |
| Q12 | bit | PK |  | SI | RN PRETERMINO |
| Q13 | bit | PK |  | SI | GEG |
| Q14 | varchar | PK |  | SI | PROFILAXIA OCULAR |
| Q15 | varchar | PK |  | SI | VITAMINA K |
| Q16 | varchar | PK |  | SI | IDENTIFICACION |
| Q17 | varchar | PK |  | SI | MUESTRA CORDON |
| Q18 | varchar | PK |  | SI | ASPIRACION GASTRICA |
| Q19 | varchar | PK |  | SI | ESFUERZO RESPIRATORIO |
| Q19A | varchar | PK |  | SI | ESFUERZO RESPIRATORIO |
| Q21 | varchar | PK |  | SI | TONICIDAD |
| Q21A | varchar | PK |  | SI | TONICIDAD |
| Q23 | varchar | PK |  | SI | IRRITABILIDAD REFLEJA |
| Q23A | varchar | PK |  | SI | IRRITABILIDAD REFLEJA |
| Q25 | varchar | PK |  | SI | COLOR |
| Q25A | varchar | PK |  | SI | COLOR |
| Q27 | numeric | PK |  | SI | TOTAL |
| Q28 | varchar | PK |  | SI | METODO  |
| Q29 | varchar | PK |  | SI | MEDICAMENTOS USADOS EN RNI |
| Q30 | varchar | PK |  | SI | VACUNA |
| Q31 | date | PK |  | SI | FECHA |
| Q32 | varchar | PK |  | SI | total |
| Q33 | varchar | PK |  | SI | PULSO |
| Q34 | varchar | PK |  | SI | PULSO |
| Q35 | varchar | PK |  | SI | TOTAL |
| Q36 | varchar | PK |  | SI | TOTAL2 |
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