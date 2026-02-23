# questionnaire.QTCEFRVIV

> Antecedentes Sociales, de la Vivienda y el Entorno

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Antecedentes Sociales, de la Vivienda y el Entorno

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ17 | varchar |  |  | SI | - |
| CQ18 | varchar |  |  | SI | - |
| Q1 | varchar |  |  | SI | Tipo de vivienda |
| Q10 | varchar |  |  | SI | ¿Cómo llega el agua para ser ocupada? |
| Q11 | varchar |  |  | SI | Sistema de eliminación de excretas |
| Q12 | varchar |  |  | SI | Sistema de disposición de basuras |
| Q13 | varchar |  |  | SI | Sistema eléctrico |
| Q14 | varchar |  |  | SI | Combustible que usa |
| Q15 | varchar |  |  | SI | Sistema de calefaccion |
| Q16 | varchar |  |  | SI | ¿Tiene animales domésticos? |
| Q17 | varchar |  |  | SI | Animales domésticos |
| Q18 | varchar |  |  | SI | Vectores |
| Q19 | varchar |  |  | SI | ¿Qué problemas de contaminación o deterioro del en... |
| Q2 | varchar |  |  | SI | Tenencia de la vivienda |
| Q20 | numeric |  |  | SI | Ingreso Familiar |
| Q21 | varchar |  |  | SI | Ingreso Per Cápita |
| Q22 | varchar |  |  | SI | Conexión al Cableado Eléctrico |
| Q23 | varchar |  |  | SI | Distancia al Paradero |
| Q24 | bit |  |  | SI | Conexion Telefonica: Fijo |
| Q25 | bit |  |  | SI | Celular |
| Q26 | varchar |  |  | SI | Tipo Trabajo del Jefe de Hogar |
| Q27 | varchar |  |  | SI | Comunicaciones |
| Q28 | numeric |  |  | SI | Número de Integrantes o Miembros de la Familia |
| Q29 | varchar |  |  | SI | Tipo de Establecimiento Educativo de uno o más int... |
| Q3 | numeric |  |  | SI | N° de Habitaciones (Total) |
| Q30 | varchar |  |  | SI | Matdrial de la Vivienda |
| Q31 | varchar |  |  | SI | Higiene General |
| Q4 | numeric |  |  | SI | N° de dormitorios |
| Q5 | numeric |  |  | SI | N° de camas |
| Q6 | varchar |  |  | SI | ¿Baño dentro de la casa? |
| Q7 | varchar |  |  | SI | ¿Cocina dentro de la casa? |
| Q8 | varchar |  |  | SI | Conservación de la vivienda |
| Q9 | varchar |  |  | SI | Fuente de origen del agua |
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