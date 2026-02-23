# questionnaire.QCLXXMHPDI

> Proceso Diagnóstico Integral - Adicciones

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Proceso Diagnóstico Integral - Adicciones

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Edad de inicio de consumo |
| Q02 | varchar |  |  | SI | Sustancia o droga consumida |
| Q03 | varchar |  |  | SI | Frecuencia del consumo actual |
| Q04 | varchar |  |  | SI | Consumo Sostenido |
| Q05 | varchar |  |  | SI | Consumo socializado o no |
| Q06 | varchar |  |  | SI | Vía de Administración |
| Q07 | varchar |  |  | SI | Consecuencia de intensidad de consumo |
| Q08 | varchar |  |  | SI | Criterios de dependencia |
| Q09 | varchar |  |  | SI | Fisiológica1 |
| Q10 | varchar |  |  | SI | Fisiológica2 |
| Q11 | varchar |  |  | SI | Fisiológica3 |
| Q12 | varchar |  |  | SI | Emocionales1 |
| Q13 | varchar |  |  | SI | Emocionales2 |
| Q14 | varchar |  |  | SI | Emocionales3 |
| Q15 | varchar |  |  | SI | Desempeño y adaptacion1 |
| Q16 | varchar |  |  | SI | Desempeño y adaptacion2 |
| Q17 | varchar |  |  | SI | Desempeño y adaptacion3 |
| Q18 | varchar |  |  | SI | Diagnostico Dimensión Ligada al Consumo |
| Q18ObsDR | varchar |  | FK | SI | Diagnostico Dimensión Ligada al Consumo DR |
| Q19 | varchar |  |  | SI | Salud física y general |
| Q20 | varchar |  |  | SI | Salud sexual y reproductiva |
| Q21 | varchar |  |  | SI | Salud Mental |
| Q22 | varchar |  |  | SI | Capacidad Relacional |
| Q23 | varchar |  |  | SI | Familia |
| Q24 | varchar |  |  | SI | Aspectos Socioculturales |
| Q25 | varchar |  |  | SI | Conducta Infractora |
| Q26 | varchar |  |  | SI | Vida de calle |
| Q27 | varchar |  |  | SI | Escuela o liceo |
| Q28 | varchar |  |  | SI | Grupo de pares |
| Q29 | varchar |  |  | SI | Comunidad |
| Q30 | varchar |  |  | SI | Recreación y tiempo libre |
| Q31 | varchar |  |  | SI | Diagnostico CBPS |
| Q31ObsDR | varchar |  | FK | SI | Diagnostico CBPS DR |
| Q32 | time |  |  | SI | Hora |
| Q33 | date |  |  | SI | Fecha |
| Q34 | varchar |  |  | SI | Reparación |
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