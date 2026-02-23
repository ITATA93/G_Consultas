# questionnaire.QTCEEVINT

> Evaluación Integral de Adultos Mayores con Indicación de Endoprótesis Total de Cadera GES

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Integral de Adultos Mayores con Indicación de Endoprótesis Total de Cadera GES

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1.- El Adulto Mayor (AM): ¿Tiene pérdidas importan... |
| Q02 | varchar |  |  | SI | 2.- ¿Tiene Dificultad para expresarse de forma ver... |
| Q03 | varchar |  |  | SI | 3.- ¿La alteración cognitiva dificulta la realizac... |
| Q04 | varchar |  |  | SI | 4.- ¿Posee un Minimental abreviado bajo los 13 pun... |
| Q05 | varchar |  |  | SI | 5.- ¿Se ha sentido deprimido o angustiado en el úl... |
| Q06 | varchar |  |  | SI | 6.- El Cuidador: ¿Podrá ayudarlo(a) en actividades... |
| Q07 | varchar |  |  | SI | 7.- ¿Podrá acompañarlo(a) a rehabilitación 1 a 3 v... |
| Q08 | varchar |  |  | SI | 8.- ¿El cuidador, es una persona activa e independ... |
| Q09 | varchar |  |  | SI | 9.- Usted: ¿Vive con su cuidadora(or)? |
| Q10 | varchar |  |  | SI | 10.- ¿Posee dinero para asistir a sesiones de reha... |
| Q11 | varchar |  |  | SI | 11.- ¿Reside en segundos pisos (o superiores), cer... |
| Q12 | varchar |  |  | SI | 12.-¿Tiene sensación de perder equilibrio, inestab... |
| Q13 | varchar |  |  | SI | 13.- ¿Ha sufrido 2 o más caídas en los últimos 6 m... |
| Q14 | varchar |  |  | SI | 14.- ¿Tiene dificultad para usar bastón o andador ... |
| Q15 | varchar |  |  | SI | 15.- ¿ Usa usted bastones ortopédicos? |
| Q16 | varchar |  |  | SI | 16.- ¿ El o los bastones otopédicos o su andador s... |
| Q17 | varchar |  |  | SI | 17.- ¿Tiene Obesidad (IMC > a 32), HTA y/o Diabete... |
| Q18 | varchar |  |  | SI | 18.- ¿Sus enfermedades crónicas están en control y... |
| Q19 | varchar |  |  | SI | 19.- ¿Ha bajado más de 4 Kg. de peso en los último... |
| Q20 | varchar |  |  | SI | 20.- ¿Puede mover los brazos normalmente? |
| Q21 | varchar |  |  | SI | 21.- ¿Presenta dolor intenso en los brazos que dif... |
| Q22 | varchar |  |  | SI | 22.- Aparte de la cadera con artrosis ¿ Tiene otra... |
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