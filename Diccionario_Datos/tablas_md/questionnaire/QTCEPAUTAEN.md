# questionnaire.QTCEPAUTAEN

> Detección de la progresión de la enfermedad renal crónica

**Schema:** questionnaire
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Detección de la progresión de la enfermedad renal crónica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Diabetes |
| Q02 | varchar |  |  | SI | Hipertensión o enfermedad cardiovascular |
| Q03 | varchar |  |  | SI | Antecedentes nefrourológicos: |
| Q04 | varchar |  |  | SI | Familiares 1º grado con ERC |
| Q05 | numeric |  |  | SI | Peso |
| Q06 | numeric |  |  | SI | Presión Sistólica |
| Q07 | numeric |  |  | SI | Presión Diastólica |
| Q08 | numeric |  |  | SI | Creatinina |
| Q09 | varchar |  |  | SI | Velocidad Filtración Glomerular (VFG) informada po... |
| Q10 | varchar |  |  | SI | Proteinura Confirmada: |
| Q11 | varchar |  |  | SI | Hematuria Opción |
| Q12 | varchar |  |  | SI | Otras alteraciones: |
| Q13 | varchar |  |  | SI | Otras alteraciones: |
| Q14 | varchar |  |  | SI | Paciente diabético: |
| Q15 | varchar |  |  | SI | Paciente no diabético: |
| Q17 | varchar |  |  | SI | Etapa Enfermedad Renal Crónica |
| Q17ObsDR | varchar |  | FK | SI | Etapa Enfermedad Renal Crónica DR |
| Q18 | varchar |  |  | SI | Conducta Final |
| Q19 | numeric |  |  | SI | Infomdo Lab |
| Q20 | numeric |  |  | SI | Hombre |
| Q21Mujer | numeric |  |  | SI | Mujer |
| Q23 | varchar |  |  | SI | Microalbuminuría Opción |
| Q24 | varchar |  |  | SI | Proteinuría |
| Q24ObsDR | varchar |  | FK | SI | Proteinuría DR |
| Q25 | varchar |  |  | SI | Microalbuminuría |
| Q25ObsDR | varchar |  | FK | SI | Microalbuminuría DR |
| Q26 | varchar |  |  | SI | RAC |
| Q26ObsDR | varchar |  | FK | SI | RAC DR |
| Q27 | numeric |  |  | SI | Hombre Raza |
| Q28 | numeric |  |  | SI | Mujer Raza |
| Q29 | varchar |  |  | SI | Velocidad de Filtración Glomerular Estimada |
| Q29ObsDR | varchar |  | FK | SI | Velocidad de Filtración Glomerular Estimada DR |
| Q30 | varchar |  |  | SI | Velocidad de Filtración Glomerular (Cockcroft - Ga... |
| Q30ObsDR | varchar |  | FK | SI | Velocidad de Filtración Glomerular (Cockcroft - Ga... |
| Q31 | varchar |  |  | SI | Categoría de Albuminuria |
| Q31ObsDR | varchar |  | FK | SI | Categoría de Albuminuria DR |
| Q32 | numeric |  |  | SI | Creatinuria |
| Q33 | varchar |  |  | SI | Proteinuria Opción |
| Q34 | date |  |  | SI | Hematuria Fecha |
| Q35 | date |  |  | SI | Proteinuria  Fecha |
| Q36 | varchar |  |  | SI | Microalbuminuria Opción |
| Q37 | varchar |  |  | SI | Creatininuria Opción |
| Q38 | varchar |  |  | SI | Creatinemia Opción |
| Q39 | varchar |  |  | SI | Razón albuminuria-Creatininuria Opción |
| Q40 | date |  |  | SI | Microalbuminuría Fecha |
| Q41 | date |  |  | SI | Creatinemia Fecha |
| Q42 | date |  |  | SI | Creatininuria Fecha |
| Q43 | date |  |  | SI | Razón albuminuria-Creatininuria Fecha |
| Q44 | varchar |  |  | SI | Hematuria |
| Q44ObsDR | varchar |  | FK | SI | Hematuria DR |
| Q45 | varchar |  |  | SI | Proteinuria |
| Q45ObsDR | varchar |  | FK | SI | Proteinuria DR |
| Q46 | date |  |  | SI | Fecha del Examen |
| QEdadPacinte | varchar |  |  | SI | Edad del Paciente |
| QRPERC | varchar |  |  | SI | Resultado Pauta de Enfermedad Renal Crónica |
| QRPERCObsDR | varchar |  | FK | SI | Resultado Pauta de Enfermedad Renal Crónica DR |
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