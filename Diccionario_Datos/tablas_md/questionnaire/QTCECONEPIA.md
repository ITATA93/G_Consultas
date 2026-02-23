# questionnaire.QTCECONEPIA

> Control Programa Epilepsia Adultos

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Control Programa Epilepsia Adultos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Control con Neurólogo |
| Q02 | varchar |  |  | SI | Adherencia a Controles APS |
| Q03 | varchar |  |  | SI | Adherencia a Indicaciones APS |
| Q04 | varchar |  |  | SI | GOT |
| Q04ObsDR | varchar |  | FK | SI | GOT DR |
| Q05 | varchar |  |  | SI | GPT |
| Q05ObsDR | varchar |  | FK | SI | GPT DR |
| Q06 | varchar |  |  | SI | Creatinina |
| Q06ObsDR | varchar |  | FK | SI | Creatinina DR |
| Q07 | varchar |  |  | SI | Hemograma |
| Q07ObsDR | varchar |  | FK | SI | Hemograma DR |
| Q08 | varchar |  |  | SI | Sodio |
| Q08ObsDR | varchar |  | FK | SI | Sodio DR |
| Q09 | varchar |  |  | SI | Potasio |
| Q09ObsDR | varchar |  | FK | SI | Potasio DR |
| Q10 | varchar |  |  | SI | Cloro |
| Q10ObsDR | varchar |  | FK | SI | Cloro DR |
| Q11 | varchar |  |  | SI | INR |
| Q11ObsDR | varchar |  | FK | SI | INR DR |
| Q12 | varchar |  |  | SI | Otro Examen |
| Q13 | varchar |  |  | SI | Tratamiento Farmacológico |
| Q14 | varchar |  |  | SI | Fármacos |
| Q15 | varchar |  |  | SI | Efectos Secundarios al Tratamiento |
| Q16 | varchar |  |  | SI | Describir Efectos Secundarios |
| Q17 | varchar |  |  | SI | Otro Fármaco |
| Q18 | varchar |  |  | SI | Adherencia |
| Q19 | varchar |  |  | SI | Laborales |
| Q20 | varchar |  |  | SI | Económicos |
| Q21 | varchar |  |  | SI | Psicológicos |
| Q22 | varchar |  |  | SI | Familiares |
| Q23 | varchar |  |  | SI | Consumo de Tabaco |
| Q24 | varchar |  |  | SI | Consumo de Alcohol |
| Q25 | varchar |  |  | SI | Consumo de Drogas |
| Q26 | varchar |  |  | SI | Trastorno de Sueño |
| Q27 | varchar |  |  | SI | Frecuencia de Consumo |
| Q28 | varchar |  |  | SI | Tipo de Droga |
| Q29 | varchar |  |  | SI | Observaciones del Trastorno del Sueño |
| Q30 | varchar |  |  | SI | Electrolitos Plasmáticos |
| Q31 | varchar |  |  | SI | TP |
| Q31ObsDR | varchar |  | FK | SI | TP DR |
| Q32 | varchar |  |  | SI | Tratamietno Anticonceptivo |
| Q33 | varchar |  |  | SI | Tratamiento Adicional |
| Q34 | varchar |  |  | SI | Control de Embarazo |
| Q35 | varchar |  |  | SI | Tratamiento Ácido Fólico |
| Q36 | varchar |  |  | SI | Derivación Neurólogo |
| Q37 | varchar |  |  | SI | Describa Tto ACO |
| Q38 | varchar |  |  | SI | Describa Tto Adicional |
| Q39 | date |  |  | SI | Fecha de Última Crísis |
| Q40 | numeric |  |  | SI | N° de Crisis |
| Q41 | date |  |  | SI | Fecha último control neurólogo |
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