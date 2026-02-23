# questionnaire.QTCECPTAR

> Tarjeton Alivio del dolor y cuidados paliativos.

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Tarjeton Alivio del dolor y cuidados paliativos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Fecha de Ingreso a Programa |
| Q10 | bit |  |  | SI | Permanente |
| Q11 | bit |  |  | SI | Esporádico |
| Q12 | bit |  |  | SI | Anorexia |
| Q13 | bit |  |  | SI | Enflaquecido |
| Q14 | bit |  |  | SI | Caquexico |
| Q15 | bit |  |  | SI | Ansiedad |
| Q16 | bit |  |  | SI | Mareos |
| Q17 | bit |  |  | SI | Temblor |
| Q18 | bit |  |  | SI | Fatiga |
| Q19 | bit |  |  | SI | Ictericia |
| Q2 | varchar |  |  | SI | Año Diagnóstico enfermedad |
| Q20 | bit |  |  | SI | Linfidema |
| Q21 | bit |  |  | SI | Edema |
| Q22 | bit |  |  | SI | Ascitis |
| Q23 | bit |  |  | SI | Náuseas |
| Q24 | bit |  |  | SI | Vómitos |
| Q25 | bit |  |  | SI | Hipo |
| Q26 | bit |  |  | SI | Estreñimiento |
| Q27 | bit |  |  | SI | Diarrea |
| Q28 | bit |  |  | SI | Gastralgia |
| Q29 | bit |  |  | SI | Disfagia |
| Q3 | varchar |  |  | SI | Centro Derivador |
| Q30 | bit |  |  | SI | Cefalea |
| Q31 | bit |  |  | SI | Disnea |
| Q32 | bit |  |  | SI | Tos |
| Q33 | bit |  |  | SI | Insomnio |
| Q34 | bit |  |  | SI | Somnolencia |
| Q35 | bit |  |  | SI | Letargo |
| Q36 | bit |  |  | SI | Desorientacion |
| Q37 | bit |  |  | SI | Prurito |
| Q38 | bit |  |  | SI | Fistula |
| Q39 | bit |  |  | SI | Ostomia |
| Q4 | date |  |  | SI | Fecha |
| Q40 | bit |  |  | SI | Hemorragias |
| Q41 | bit |  |  | SI | Disuria |
| Q48 | varchar |  |  | SI | Incontinencia |
| Q49 | varchar |  |  | SI | Localización del Dolor |
| Q5 | varchar |  |  | SI | Paciente |
| Q50 | varchar |  |  | SI | Quimioterapia |
| Q51 | varchar |  |  | SI | Radioterapia |
| Q52 | varchar |  |  | SI | Adiccion |
| Q53 | varchar |  |  | SI | Oxigenoterapia |
| Q54 | date |  |  | SI | Fecha |
| Q55 | date |  |  | SI | Fecha |
| Q56 | date |  |  | SI | Fecha |
| Q57 | date |  |  | SI | Fecha |
| Q6 | varchar |  |  | SI | Familia |
| Q7 | varchar |  |  | SI | EVA |
| Q8 | varchar |  |  | SI | Tipo de Dolor |
| Q9 | varchar |  |  | SI | Mixto |
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