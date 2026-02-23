# questionnaire.QTCECONEPIN

> Control Programa Epilepsia Niños 1 a 15 Años

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Control Programa Epilepsia Niños 1 a 15 Años

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Crisis Epilépticas |
| Q02 | date |  |  | SI | Fecha Última Crisis |
| Q03 | numeric |  |  | SI | Peso Anterior |
| Q04 | varchar |  |  | SI | Peso Actual |
| Q04ObsDR | varchar |  | FK | SI | Peso Actual DR |
| Q05 | varchar |  |  | SI | P/E |
| Q06 | varchar |  |  | SI | T/E |
| Q07 | varchar |  |  | SI | P/T |
| Q08 | numeric |  |  | SI | IMC |
| Q09 | varchar |  |  | SI | Consumo de Drogas |
| Q10 | varchar |  |  | SI | Cual Droga |
| Q11 | varchar |  |  | SI | Escolaridad |
| Q12 | varchar |  |  | SI | Derivación |
| Q13 | varchar |  |  | SI | GOT |
| Q13ObsDR | varchar |  | FK | SI | GOT DR |
| Q14 | varchar |  |  | SI | GPT |
| Q14ObsDR | varchar |  | FK | SI | GPT DR |
| Q15 | varchar |  |  | SI | Creatinemia |
| Q15ObsDR | varchar |  | FK | SI | Creatinemia DR |
| Q16 | varchar |  |  | SI | Hemograma |
| Q16ObsDR | varchar |  | FK | SI | Hemograma DR |
| Q17 | varchar |  |  | SI | Sodio |
| Q17ObsDR | varchar |  | FK | SI | Sodio DR |
| Q18 | varchar |  |  | SI | Potasio |
| Q18ObsDR | varchar |  | FK | SI | Potasio DR |
| Q19 | varchar |  |  | SI | Cloro |
| Q19ObsDR | varchar |  | FK | SI | Cloro DR |
| Q20 | varchar |  |  | SI | Exámenes al Día |
| Q21 | varchar |  |  | SI | Tratamiento Farmacológico |
| Q22 | varchar |  |  | SI | Fármacos |
| Q23 | varchar |  |  | SI | Otro Fármaco |
| Q24 | varchar |  |  | SI | Adherencia |
| Q25 | varchar |  |  | SI | Efectos Adversos |
| Q26 | varchar |  |  | SI | Mencione Efecto Adversos |
| Q27 | varchar |  |  | SI | Intervención Psicológica |
| Q28 | varchar |  |  | SI | Educación a la Familia |
| Q29 | varchar |  |  | SI | Adherencia al Tratamiento |
| Q30 | varchar |  |  | SI | Efectos Colaterales del Tratamiento |
| Q31 | varchar |  |  | SI | Asistencia a Controles |
| Q32 | varchar |  |  | SI | Dieta Cetogénica |
| Q33 | varchar |  |  | SI | Otra Intervención |
| Q34 | date |  |  | SI | Médico |
| Q35 | date |  |  | SI | Enfermera |
| Q36 | date |  |  | SI | Neurólogo |
| Q37 | varchar |  |  | SI | TP |
| Q37ObsDR | varchar |  | FK | SI | TP DR |
| Q38 | varchar |  |  | SI | Electrolitos Plasmáticos |
| Q39 | varchar |  |  | SI | Tratamiento Anticonceptivo |
| Q40 | varchar |  |  | SI | Derivación Neurólogo |
| Q41 | varchar |  |  | SI | Control de Embarazo |
| Q42 | varchar |  |  | SI | Uso de Drogas Ilícitas |
| Q43 | varchar |  |  | SI | Nombre Tto Aco |
| Q44 | varchar |  |  | SI | Nombre de Droga |
| Q45 | numeric |  |  | SI | N° de Crisis |
| Q46 | varchar |  |  | SI | Centil Peso/Edad |
| Q47 | varchar |  |  | SI | Centil Talla/Edad |
| Q48 | varchar |  |  | SI | Centil Peso/Talla |
| Q49 | varchar |  |  | SI | Control con neurólogo |
| Q50 | date |  |  | SI | Fecha último control neurólogo |
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