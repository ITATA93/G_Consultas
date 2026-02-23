# questionnaire.QREMA32R

> REMA32 - Sección R - Actividades Programa Elige Vida Sana por Llamada Telefónica o Redes Sociales

**Schema:** questionnaire
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* REMA32 - Sección R - Actividades Programa Elige Vida Sana por Llamada Telefónica o Redes Sociales

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | N° de Mensajes 1 |
| Q02 | numeric |  |  | SI | N° de Mensajes 2 |
| Q03 | numeric |  |  | SI | N° de Mensajes 3 |
| Q04 | numeric |  |  | SI | N° de Participantes 1 |
| Q05 | numeric |  |  | SI | N° de Participantes 2 |
| Q06 | numeric |  |  | SI | N° de Participantes 3 |
| Q07 | numeric |  |  | SI | Menores de 1 año 1 |
| Q08 | numeric |  |  | SI | Menores de 1 año 2 |
| Q09 | numeric |  |  | SI | Menores de 1 año 3 |
| Q10 | numeric |  |  | SI | Niños 12 a 23 meses 1   |
| Q11 | numeric |  |  | SI | Niños 12 a 23 meses 2 |
| Q12 | numeric |  |  | SI | Niños 12 a 23 meses 3 |
| Q13 | numeric |  |  | SI | Menor de 2 años 1 |
| Q14 | numeric |  |  | SI | Menor de 2 años 2 |
| Q15 | numeric |  |  | SI | Menor de 2 años 3 |
| Q16 | numeric |  |  | SI | 2 a 4 años 1 |
| Q17 | numeric |  |  | SI | 2 a 4 años 2 |
| Q18 | numeric |  |  | SI | 2 a 4 años 3 |
| Q19 | numeric |  |  | SI | 5 a 9 años 1 |
| Q20 | numeric |  |  | SI | 5 a 9 años 2 |
| Q21 | numeric |  |  | SI | 5 a 9 años 3 |
| Q22 | numeric |  |  | SI | 10 a 14 años 1 |
| Q23 | numeric |  |  | SI | 10 a 14 años 2 |
| Q24 | numeric |  |  | SI | 10 a 14 años 3 |
| Q25 | numeric |  |  | SI | 15 a 19 años 1 |
| Q26 | numeric |  |  | SI | 15 a 19 años 2 |
| Q27 | numeric |  |  | SI | 15 a 19 años 3 |
| Q28 | numeric |  |  | SI | 20 -24 años 1 |
| Q29 | numeric |  |  | SI | 20 -24 años 2 |
| Q30 | numeric |  |  | SI | 20 -24 años 3 |
| Q31 | numeric |  |  | SI | 25 -29 años 1 |
| Q32 | numeric |  |  | SI | 25 -29 años 2 |
| Q33 | numeric |  |  | SI | 25 -29 años 3 |
| Q34 | numeric |  |  | SI | 30 - 34 años 1 |
| Q35 | numeric |  |  | SI | 30 - 34 años 2 |
| Q36 | numeric |  |  | SI | 30 - 34 años 3 |
| Q37 | numeric |  |  | SI | 35 - 39 años 1 |
| Q38 | numeric |  |  | SI | 35 - 39 años 2 |
| Q39 | numeric |  |  | SI | 35 - 39 años 3 |
| Q40 | numeric |  |  | SI | 40 - 44 años 1 |
| Q41 | numeric |  |  | SI | 40 - 44 años 2 |
| Q42 | numeric |  |  | SI | 40 - 44 años 3 |
| Q43 | numeric |  |  | SI | 45 - 49 años 1 |
| Q44 | numeric |  |  | SI | 45 - 49 años 2 |
| Q45 | numeric |  |  | SI | 45 - 49 años 3 |
| Q46 | numeric |  |  | SI | 50 - 54 años 1 |
| Q47 | numeric |  |  | SI | 50 - 54 años 2 |
| Q48 | numeric |  |  | SI | 50 - 54 años 3 |
| Q49 | numeric |  |  | SI | 55 - 59 años 1 |
| Q50 | numeric |  |  | SI | 55 - 59 años 2 |
| Q51 | numeric |  |  | SI | 55 - 59 años 3 |
| Q52 | numeric |  |  | SI | 60 - 64 años 1 |
| Q53 | numeric |  |  | SI | 60 - 64 años 2 |
| Q54 | numeric |  |  | SI | 60 - 64 años 3 |
| Q55 | numeric |  |  | SI | Gestantes 1 |
| Q56 | numeric |  |  | SI | Gestantes 2 |
| Q57 | numeric |  |  | SI | Gestantes 3 |
| Q58 | numeric |  |  | SI | Post Parto 1 |
| Q59 | numeric |  |  | SI | Post Parto 2 |
| Q60 | numeric |  |  | SI | Post Parto 3 |
| Q62 | varchar |  |  | SI | Mes |
| Q63 | numeric |  |  | SI | Año |
| QHD | varchar |  |  | SI | Establecimiento |
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