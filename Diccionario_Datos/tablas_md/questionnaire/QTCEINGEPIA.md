# questionnaire.QTCEINGEPIA

> Ingreso Epilepsia Adultos

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Epilepsia Adultos

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Antecedentes de Enfermedades Concomitantes |
| Q02 | varchar |  |  | SI | Derivación desde APS para Diagnóstico en Nivel Sec... |
| Q03 | varchar |  |  | SI | Control con Neurólogo |
| Q04 | varchar |  |  | SI | Última Crisis de Epilepsia |
| Q05 | date |  |  | SI | Fecha Última Crisis |
| Q06 | numeric |  |  | SI | N° de Episodios |
| Q07 | varchar |  |  | SI | GOT |
| Q07ObsDR | varchar |  | FK | SI | GOT DR |
| Q08 | varchar |  |  | SI | GPT |
| Q08ObsDR | varchar |  | FK | SI | GPT DR |
| Q09 | varchar |  |  | SI | Creatinina |
| Q09ObsDR | varchar |  | FK | SI | Creatinina DR |
| Q10 | varchar |  |  | SI | Hemograma |
| Q10ObsDR | varchar |  | FK | SI | Hemograma DR |
| Q11 | varchar |  |  | SI | Sodio |
| Q11ObsDR | varchar |  | FK | SI | Sodio DR |
| Q12 | varchar |  |  | SI | Potasio |
| Q12ObsDR | varchar |  | FK | SI | Potasio DR |
| Q13 | varchar |  |  | SI | Cloro |
| Q13ObsDR | varchar |  | FK | SI | Cloro DR |
| Q14 | varchar |  |  | SI | INR |
| Q14ObsDR | varchar |  | FK | SI | INR DR |
| Q15 | varchar |  |  | SI | Otro Examen |
| Q16 | varchar |  |  | SI | Tratamiento Farmacológico |
| Q17 | varchar |  |  | SI | Fármacos |
| Q18 | varchar |  |  | SI | Efectos Secundarios al Tratamiento |
| Q19 | varchar |  |  | SI | Descriva Efectos Secundarios |
| Q20 | varchar |  |  | SI | Adherencia |
| Q21 | varchar |  |  | SI | Tratamiento Anticonceptivo |
| Q22 | varchar |  |  | SI | Describa Tratamiento Anticonceptivo |
| Q23 | varchar |  |  | SI | Tratamiento Adicional |
| Q24 | varchar |  |  | SI | Describa Tratamiento |
| Q25 | varchar |  |  | SI | Derivación Neurólogo |
| Q26 | varchar |  |  | SI | Control de Embarazo |
| Q27 | varchar |  |  | SI | Tratamiento Ácido Fólico |
| Q28 | varchar |  |  | SI | Laborales |
| Q29 | varchar |  |  | SI | Económicos |
| Q30 | varchar |  |  | SI | Psicológicos |
| Q31 | varchar |  |  | SI | Familiares |
| Q32 | varchar |  |  | SI | Consumo de Tabaco |
| Q33 | varchar |  |  | SI | Consumo de Alcohol |
| Q34 | varchar |  |  | SI | Consumo de Drogas |
| Q35 | varchar |  |  | SI | Trastorno de Sueño |
| Q36 | varchar |  |  | SI | Otro Fármaco |
| Q37 | varchar |  |  | SI | Frecuencia de Consumo |
| Q38 | varchar |  |  | SI | Tipo de Droga |
| Q39 | varchar |  |  | SI | TP |
| Q39ObsDR | varchar |  | FK | SI | TP DR |
| Q40 | varchar |  |  | SI | Electrolitos Plasmáticos |
| Q41 | date |  |  | SI | Fecha Último Control Neurólogo |
| Q42 | date |  |  | SI | Fecha de Diagnóstico de Epilepsia |
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