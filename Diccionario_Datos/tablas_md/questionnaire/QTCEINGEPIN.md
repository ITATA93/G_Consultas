# questionnaire.QTCEINGEPIN

> Ingreso Programa Epilepsia Niños 1 a 15 Años

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Programa Epilepsia Niños 1 a 15 Años

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Control Neurológico |
| Q02 | date |  |  | SI | Fecha Control Neurológico |
| Q03 | varchar |  |  | SI | Crisis Epilépticas |
| Q04 | date |  |  | SI | Fecha Última Crísis |
| Q05 | varchar |  |  | SI | GOT |
| Q05ObsDR | varchar |  | FK | SI | GOT DR |
| Q06 | varchar |  |  | SI | GPT |
| Q06ObsDR | varchar |  | FK | SI | GPT DR |
| Q07 | varchar |  |  | SI | Creatinina |
| Q07ObsDR | varchar |  | FK | SI | Creatinina DR |
| Q08 | varchar |  |  | SI | Hemograma |
| Q08ObsDR | varchar |  | FK | SI | Hemograma DR |
| Q09 | varchar |  |  | SI | Sodio |
| Q09ObsDR | varchar |  | FK | SI | Sodio DR |
| Q10 | varchar |  |  | SI | Potasio |
| Q10ObsDR | varchar |  | FK | SI | Potasio DR |
| Q11 | varchar |  |  | SI | Cloro |
| Q11ObsDR | varchar |  | FK | SI | Cloro DR |
| Q12 | varchar |  |  | SI | Tratamiento Farmacológico |
| Q13 | varchar |  |  | SI | Fármacos |
| Q14 | varchar |  |  | SI | Otro |
| Q15 | varchar |  |  | SI | Adherencia |
| Q16 | varchar |  |  | SI | Síntomas Autonómicos |
| Q17 | varchar |  |  | SI | Síntomas Psíquicos |
| Q18 | varchar |  |  | SI | Otro Síntoma Autonómico |
| Q19 | varchar |  |  | SI | Escolaridad |
| Q20 | varchar |  |  | SI | Derivación |
| Q21 | numeric |  |  | SI | Peso Anterior |
| Q22 | varchar |  |  | SI | Peso Actual |
| Q22ObsDR | varchar |  | FK | SI | Peso Actual DR |
| Q23 | varchar |  |  | SI | P/E |
| Q24 | varchar |  |  | SI | T/E |
| Q25 | varchar |  |  | SI | P/T |
| Q26 | varchar |  |  | SI | IMC |
| Q27 | varchar |  |  | SI | Tratamiento Anticonceptivo |
| Q28 | varchar |  |  | SI | Cual Tratamiento Anticonceptivo |
| Q29 | varchar |  |  | SI | Derivación Neurólogo |
| Q30 | varchar |  |  | SI | Control Embarazo |
| Q31 | varchar |  |  | SI | Uso de Drogas Ilícitas |
| Q32 | varchar |  |  | SI | ¿Cuál? |
| Q33 | varchar |  |  | SI | Intervención Psicológica |
| Q34 | varchar |  |  | SI | Educación a la Familia |
| Q35 | varchar |  |  | SI | Adherencia al Tratamiento |
| Q36 | varchar |  |  | SI | Efectos Colaterales del Tratamiento |
| Q37 | varchar |  |  | SI | Asistencia a Controles |
| Q38 | varchar |  |  | SI | Dieta Cetogénica |
| Q39 | varchar |  |  | SI | Otra Intervención |
| Q40 | varchar |  |  | SI | TP |
| Q40ObsDR | varchar |  | FK | SI | TP DR |
| Q41 | varchar |  |  | SI | Electrolitos Plasmáticos |
| Q42 | numeric |  |  | SI | N° de Crisis |
| Q43 | varchar |  |  | SI | Centil Peso/Edad |
| Q44 | varchar |  |  | SI | Centil Talla/Edad |
| Q45 | varchar |  |  | SI | Centil Peso/Talla |
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