# questionnaire.QCLXXTDINSU

> Taller de Insulinoterapia

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Taller de Insulinoterapia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tipo de Atención |
| Q02 | varchar |  |  | SI | ANAMNESIS |
| Q03 | varchar |  |  | SI | Motivo de Inicio de Insulina |
| Q04 | varchar |  |  | SI | Acude con Acompañado |
| Q05 | varchar |  |  | SI | Relación del Acompañante |
| Q06 | varchar |  |  | SI | Nombre del Acompañante |
| Q07 | varchar |  |  | SI | Principal red de apoyo  |
| Q08 | varchar |  |  | SI | Trabaja |
| Q09 | varchar |  |  | SI | Tipo de trabajo |
| Q10 | varchar |  |  | SI | Turnos  |
| Q11 | varchar |  |  | SI | Comidas al día |
| Q12 | varchar |  |  | SI | TIPO INSULINA INDICADA |
| Q13 | varchar |  |  | SI | Insulina Lentas |
| Q14 | varchar |  |  | SI | Insulina Rápidas |
| Q15 | varchar |  |  | SI | Otra Insulina |
| Q16 | varchar |  |  | SI | Dosis y Esquema Indicado |
| Q17 | varchar |  |  | SI | Horario Insulina |
| Q18 | varchar |  |  | SI | Tipo de Administración |
| Q19 | varchar |  |  | SI | Nombre de un Tercero |
| Q20 | varchar |  |  | SI | Signos de Lipodistrofia |
| Q21 | varchar |  |  | SI | Sitio Lipodistrofia |
| Q23 | varchar |  |  | SI | Presencia de Hipoglicemias sobre todo nocturna y c... |
| Q24 | varchar |  |  | SI | Necesidad de ajuste  |
| Q25 | varchar |  |  | SI | Descripción del Ajuste |
| Q26 | varchar |  |  | SI | INDICACIONES |
| Q27 | bit |  |  | SI | Automonitoreo de glicemias en ayunas-precena y con... |
| Q28 | bit |  |  | SI | Mantener controles de salud cardiovascular |
| Q29 | bit |  |  | SI | Mantener el tratamiento farmacológico y reforzar e... |
| Q30 | bit |  |  | SI | Médico/Urgencia SOS |
| Q31 | bit |  |  | SI | Educación |
| Q32 | bit |  |  | SI | Agregar imagen con sitio de punción |
| Q33 | bit |  |  | SI | Ajuste Insulina |
| Q34 | varchar |  |  | SI | Otra red de Apoyo |
| Q35 | varchar |  |  | SI | Con quien Vive |
| Q36 | varchar |  |  | SI | Horarios y otros de Comida |
| Q37 | varchar |  |  | SI | Colación al día |
| Q38 | varchar |  |  | SI | Horarios y otros de Colación |
| Q39 | varchar |  |  | SI | Educación en particular |
| Q40 | varchar |  |  | SI | Opciones Ajuste insulina  |
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