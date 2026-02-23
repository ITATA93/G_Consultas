# questionnaire.QTCAFHD

> Escala de Riesgo de Caídas Pediátrica Humpty Dumpty

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Riesgo de Caídas Pediátrica Humpty Dumpty

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Edad |
| Q02 | varchar |  |  | SI | Género |
| Q03 | varchar |  |  | SI | Diagnóstico |
| Q04 | varchar |  |  | SI | Deterioro cognitivo |
| Q05 | varchar |  |  | SI | Factores ambientales |
| Q06 | varchar |  |  | SI | Cirugía / sedación / anestesia |
| Q07 | varchar |  |  | SI | Medicación |
| Q08 | varchar |  |  | SI | Indicación para la evaluación |
| Q09 | varchar |  |  | SI | Intervenciones |
| Q10 | varchar |  |  | SI | 7-11: Bajo riesgo |
| Q11 | varchar |  |  | SI | >=12: Alto riesgo |
| Q12 | varchar |  |  | SI | Permite al equipo clínico evaluar rápida y fácilme... |
| Q13 | varchar |  |  | SI | 7 - 11 |
| Q14 | varchar |  |  | SI | Bajo riesgo |
| Q15 | varchar |  |  | SI | ≥12 |
| Q16 | varchar |  |  | SI | Alto riesgo |
| Q17 | varchar |  |  | SI | Puntaje |
| Q18 | varchar |  |  | SI | Clasificación |
| Q19 | varchar |  |  | SI | * Medicamentos: Sedantes (excluyendo pacientes de ... |
| Q20 | date |  |  | SI | Fecha |
| Q21 | time |  |  | SI | Hora |
| Q22 | varchar |  |  | SI | Other indication |
| Q23 | varchar |  |  | SI | Guidelines |
| Q24 | varchar |  |  | SI | Assess and periodically reassess each  patient’s r... |
| Q25 | varchar |  |  | SI | Educate child / parent / guardian / boarder on : |
| Q26 | varchar |  |  | SI | * potential falls risk and interventions |
| Q27 | varchar |  |  | SI | * call bell and light use |
| Q28 | varchar |  |  | SI | * bed side/cot rails use |
| Q29 | varchar |  |  | SI | * appropriate clothing and non-slip footwear |
| Q30 | varchar |  |  | SI | Place child in appropriately sized bed with brakes... |
| Q31 | varchar |  |  | SI | Ensure mobility aids and call bell within reach. |
| Q32 | varchar |  |  | SI | Routine Care Instructions : |
| Q33 | varchar |  |  | SI | * Assess toileting and assist as needed |
| Q34 | varchar |  |  | SI | * Head and foot ends placed on beds |
| Q35 | varchar |  |  | SI | * If child mobilises with IV pole, ensure equipmen... |
| Q36 | varchar |  |  | SI | * Environment is clear of clutter and trip hazards |
| Q37 | varchar |  |  | SI | * Curtains and room door open, unless otherwise in... |
| Q38 | varchar |  |  | SI | * Ensure adequate lighting and leave nightlight on... |
| Q39 | varchar |  |  | SI | Additional considerations for high risk patients (... |
| Q40 | varchar |  |  | SI | * Paediatric High Falls sign added to bedside |
| Q41 | varchar |  |  | SI | * Hourly visual checks on patient |
| Q42 | varchar |  |  | SI | * Assist with ambulation |
| Q43 | varchar |  |  | SI | * Consider moving child closer to nurses' station |
| Q44 | varchar |  |  | SI | * Assess need for 1:1 supervision |
| Q45 | varchar |  |  | SI | Assess need for 1:1 supervision |
| Q46 | varchar |  |  | SI | * Review medication administration times |
| Q47 | varchar |  |  | SI | * Engage parents / carers / boarders in falls prev... |
| Q48 | varchar |  |  | SI | Age |
| Q49 | varchar |  |  | SI | In the 2009 study (J Spec Pediatr Nurs 2009;14:22–... |
| Q50 | varchar |  |  | SI |  and a negative predictive value of 63% for the pr... |
| Q51 | varchar |  |  | SI | References |
| Q52 | varchar |  |  | SI | 1. Hill‐Rodriguez D, Messmer PR, Williams PD, Zell... |
| Q53 | varchar |  |  | SI | 1. Hill-Rodriguez D, Messmer PR, Wood ML. Humpty D... |
| Q54 | varchar |  |  | SI | 2. Hill‐Rodriguez D, Messmer PR, Williams PD, Zell... |
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