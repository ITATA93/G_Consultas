# questionnaire.QTCEPQL5

> Instrumento Medición Calidad de Vida Pacientes con Asma (5-7 Años): Reporte de Niños

**Schema:** questionnaire
**Columnas:** 58
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Instrumento Medición Calidad de Vida Pacientes con Asma (5-7 Años): Reporte de Niños

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Te duele el PECHO&nbsp;o lo sientes apretado |
| Q02 | varchar |  |  | SI | 2. Sientes que te silba el pecho |
| Q03 | varchar |  |  | SI | 3. Has tenido ataques de asma |
| Q04 | varchar |  |  | SI | 4. Te asustas cuando tienes ataques de asma |
| Q05 | varchar |  |  | SI | 5. Te ahogas |
| Q06 | varchar |  |  | SI | 6. Toses |
| Q07 | varchar |  |  | SI | 7. Te cuesta respirar profundo |
| Q08 | varchar |  |  | SI | 8. Tienes la nariz tapada o con secreción (mocos) |
| Q09 | varchar |  |  | SI | 9. Despiertas en la noche con dificultad para resp... |
| Q10 | varchar |  |  | SI | 10. Te cuesta jugar con mascotas |
| Q11 | varchar |  |  | SI | 11. Te cuesta jugar en el patio |
| Q12 | varchar |  |  | SI | 1. Los medicamentos te hacen sentir mal |
| Q13 | varchar |  |  | SI | 2. Tienes problemas para dormir debido a tus medic... |
| Q14 | varchar |  |  | SI | 3. Es dificil para ti usar los inhaladores |
| Q15 | varchar |  |  | SI | 4. No te gusta andar trayendo tus inhaladores |
| Q16 | varchar |  |  | SI | 5. Es dificil para ti hacerte responsable de tu tr... |
| Q17 | varchar |  |  | SI | 6. Te cuesta controlar tu asma |
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