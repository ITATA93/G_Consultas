# questionnaire.QTCEEXAFMAM

> Examen Fisico de Mamas (EFM) y Autoexamen Mamario (AEM)

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Fisico de Mamas (EFM) y Autoexamen Mamario (AEM)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ01 | varchar |  |  | SI | - |
| CQ39 | varchar |  |  | SI | - |
| Q01 | varchar |  |  | SI | Establecimiento de Procedencia |
| Q02 | varchar |  |  | SI | Exclusiva EFM |
| Q03 | varchar |  |  | SI | Control Ginecologico |
| Q04 | varchar |  |  | SI | Morbilidad Ginecologica |
| Q05 | varchar |  |  | SI | Control Prenatal |
| Q06 | varchar |  |  | SI | Control Paternidad responsable |
| Q07 | varchar |  |  | SI | Examen de Salud del Adulto |
| Q08 | varchar |  |  | SI | Control Cronicos |
| Q09 | varchar |  |  | SI | Morbilidad adultos |
| Q10 | date |  |  | SI | Anterior EFM |
| Q11 | varchar |  |  | SI | Resultado  |
| Q12 | varchar |  |  | SI | Motivos del EFM |
| Q13 | varchar |  |  | SI | Especifique |
| Q14 | varchar |  |  | SI | Nodulo Palpable Der. |
| Q15 | varchar |  |  | SI | Nódulo Palpable Izq. |
| Q16 | varchar |  |  | SI | Nodulo Axilar Der. |
| Q17 | varchar |  |  | SI | Nodulo Axilar Izq. |
| Q18 | varchar |  |  | SI | Nodo Supraclavicular Der. |
| Q19 | varchar |  |  | SI | Nodo Supraclavicular Izq. |
| Q20 | varchar |  |  | SI | Derrame Hepatico Pezon Der. |
| Q21 | varchar |  |  | SI | Derrame Hepatico Pezon Izq. |
| Q22 | varchar |  |  | SI | Retraccion del Pezon Der. |
| Q23 | varchar |  |  | SI | Retraccion del Pezon Izq. |
| Q24 | varchar |  |  | SI | Eczema del Pezon Der. |
| Q25 | varchar |  |  | SI | Eczema del Pezon Izq. |
| Q26 | varchar |  |  | SI | Retraccion Piel Mama Der. |
| Q27 | varchar |  |  | SI | Retraccion Piel Mama Izq. |
| Q28 | varchar |  |  | SI | Ulceracion Piel Mama Der. |
| Q29 | varchar |  |  | SI | Ulceracion Piel Mama Izq. |
| Q30 | varchar |  |  | SI | Eritema Piel Mama Der. |
| Q31 | varchar |  |  | SI | Eritema Piel Mama Izq. |
| Q32 | varchar |  |  | SI | Edema Piel Mama Der. |
| Q33 | varchar |  |  | SI | Edema Piel Mama Izq. |
| Q34 | varchar |  |  | SI | Autoexamen Mamario (AEM) |
| Q35 | varchar |  |  | SI | Obs Imagen |
| Q38 | varchar |  |  | SI | Observaciones  |
| Q39 | varchar |  |  | SI | Derivado a |
| Q40 | varchar |  |  | SI | Especifique |
| Q41 | date |  |  | SI | PROXIMO EFM |
| Q42 | varchar |  |  | SI | Actividad Realizada |
| Q43 | varchar |  |  | SI | Examen Mamario |
| QRQuest | varchar |  |  | SI | Resultado Examen Físico Mamario |
| QRQuestObsDR | varchar |  | FK | SI | Resultado Examen Físico Mamario DR |
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