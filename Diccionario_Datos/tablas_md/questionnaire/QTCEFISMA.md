# questionnaire.QTCEFISMA

> Formulario Ingreso - Egreso Salud Mental Adulto (20 años y mas)

**Schema:** questionnaire
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario Ingreso - Egreso Salud Mental Adulto (20 años y mas)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | VICTIMA |
| Q02 | varchar |  |  | SI | AGRESOR |
| Q03 | varchar |  |  | SI | VIOLENCIA HACIA EL ADULTO MAYOR |
| Q04 | varchar |  |  | SI | ABUSO SEXUAL |
| Q08 | varchar |  |  | SI | CONSUMO RIESGOSO DE DROGAS |
| Q09 | date |  |  | SI | Fecha Ingreso Depresión Moderada |
| Q10 | date |  |  | SI | Fecha Egreso Depresión Leve |
| Q100 | varchar |  |  | SI | Egreso Trastornos conductuales asociados a Demenci... |
| Q101 | date |  |  | SI | Fecha Ingreso Depresión Refractaria |
| Q102 | date |  |  | SI | Fecha Egreso Depresión Refractaria |
| Q103 | date |  |  | SI | Fecha Ingreso Depresión Grave con Psicosis  |
| Q104 | date |  |  | SI | Fecha Egreso Depresión Grave con Psicos |
| Q105 | date |  |  | SI | Fecha Ingreso Depresión con Alto Riesgo Suicida |
| Q106 | date |  |  | SI | Fecha Egreso Depresión con Alto Riesgo Suicida |
| Q107 | varchar |  |  | SI | Motivo Egreso Depresión Refractaria  |
| Q108 | varchar |  |  | SI | Motivo Egreso Depresión Grave con Psicosis  |
| Q109 | varchar |  |  | SI | Motivo Egreso Depresión con Alto Riesgo Suicida |
| Q11 | date |  |  | SI | Fecha Ingreso Depresión Leve |
| Q110 | date |  |  | SI | Fecha Ingreso Primer Episodio Esquizofrenia con Oc... |
| Q111 | date |  |  | SI | Fecha Egreso Primer Episodio Esquizofrenia con Ocu... |
| Q112 | varchar |  |  | SI | Motivo Egreso Primer Episodio Esquizofrenia con Oc... |
| Q113 | varchar |  |  | SI | Tipo de Ingreso (Alcohol y Drogas) |
| Q114 | date |  |  | SI | Plan Ambulatorio Intensivo |
| Q115 | date |  |  | SI | Fecha Egreso Plan Ambulatorio Intensivo |
| Q116 | varchar |  |  | SI | Egreso Plan Ambulatorio Intensivo |
| Q12 | date |  |  | SI | Fecha Egreso Depresión Moderada |
| Q13 | date |  |  | SI | Fecha Ingreso Depresión Grave |
| Q14 | date |  |  | SI | Fecha Egreso Depresión Grave |
| Q15 | date |  |  | SI | Fecha Ingreso Depresión Post Parto |
| Q16 | date |  |  | SI | Fecha Egreso Depresión Post Parto |
| Q17 | date |  |  | SI | Fecha Ingreso Trastorno Bipolar |
| Q18 | date |  |  | SI | Fecha Egreso Trastorno Bipolar |
| Q19 | date |  |  | SI | Fecha Ingreso consumo perjudicial o dependencia de... |
| Q20 | date |  |  | SI | Fecha Egreso  consumo perjudicial o dependencia de... |
| Q21 | date |  |  | SI | Fecha Ingreso  Consumo perjudicial o dependencia c... |
| Q22 | date |  |  | SI | Fecha Egreso  Consumo perjudicial o dependencia co... |
| Q23 | date |  |  | SI | Fecha Ingreso Policonsumo |
| Q24 | date |  |  | SI | Fecha Egreso Policonsumo |
| Q25 | date |  |  | SI | Fecha Ingreso Trastorno de Ansiedad |
| Q26 | date |  |  | SI | Fecha Egreso Trastorno de Ansiedad |
| Q27 | date |  |  | SI | Fecha Ingreso Alzheimer y otras Demencias |
| Q28 | date |  |  | SI | Fecha Egreso Alzheimer y otras Demencias |
| Q29 | date |  |  | SI | Fecha Ingreso Esquizofrenia |
| Q30 | date |  |  | SI | Fecha Egreso Esquizofrenia |
| Q31 | date |  |  | SI | Fecha Ingreso Trastornos de la conducta Alimentari... |
| Q32 | date |  |  | SI | Fecha Egreso Trastornos de la conducta Alimentaria |
| Q33 | date |  |  | SI | Fecha Ingreso Retraso Mental |
| Q34 | date |  |  | SI | Fecha Egreso Retraso Mental |
| Q35 | date |  |  | SI | Fecha Ingreso Trastorno de Personalidad |
| Q36 | date |  |  | SI | Fecha Egreso Trastorno de Personalidad |
| Q37 | date |  |  | SI | Fecha Ingreso Trastorno Generalizados del Desarrol... |
| Q38 | date |  |  | SI | Fecha Egreso Trastornos Generalizados del Desarrol... |
| Q39 | date |  |  | SI | Fecha Ingreso Plan Ambulatorio Básico |
| Q40 | date |  |  | SI | Fecha Egreso Plan Ambulatorio Básico |
| Q41 | date |  |  | SI | Fecha Ingreso Intervención Preventiva |
| Q42 | date |  |  | SI | Fecha Egreso Intervención Preventiva |
| Q43 | date |  |  | SI | Fecha Ingreso Intervención Terapeutica |
| Q44 | date |  |  | SI | Fecha Egreso Intervención Terapeutica |
| Q45 | date |  |  | SI | Fecha Ingreso Trastornos conductuales asociados a ... |
| Q46 | date |  |  | SI | Fecha Egreso Trastornos conductuales asociados a D... |
| Q57 | varchar |  |  | SI | Resultado AUDIT |
| Q57ObsDR | varchar |  | FK | SI | Resultado AUDIT DR |
| Q59 | varchar |  |  | SI | Resultado AUDIT-C |
| Q59ObsDR | varchar |  | FK | SI | Resultado AUDIT-C DR |
| Q78 | date |  |  | SI | Fecha Ingreso Otra |
| Q79 | date |  |  | SI | Fecha Egreso Otra |
| Q80 | varchar |  |  | SI | Motivo de Egreso Otra |
| Q81 | varchar |  |  | SI | Describa |
| Q82 | varchar |  |  | SI | Egreso Depresión Leve |
| Q83 | varchar |  |  | SI | Egreso Depresión Moderada |
| Q84 | varchar |  |  | SI | Egreso Depresión Grave |
| Q85 | varchar |  |  | SI | Egreso Depresión Post Parto |
| Q86 | varchar |  |  | SI | Egreso Trastorno Bipolar |
| Q87 | varchar |  |  | SI | Egreso Posible consumo Perjudicial o Dependencia d... |
| Q88 | varchar |  |  | SI | Egreso Otra Sustancia como Droga Principal |
| Q89 | varchar |  |  | SI | Egreso Policonsumo |
| Q90 | varchar |  |  | SI | Egreso Trastornos de Ansiedad |
| Q91 | varchar |  |  | SI | Egreso Alzheirmer y otras Demencias |
| Q92 | varchar |  |  | SI | Egreso Esquizofrenia |
| Q93 | varchar |  |  | SI | Egreso Trastornos de la Conducta Alimentaria |
| Q94 | varchar |  |  | SI | Egreso Retraso Mental |
| Q95 | varchar |  |  | SI | Egreso Trastorno de Personalidad |
| Q96 | varchar |  |  | SI | Egreso Trastorno Generalizados del Desarrollo |
| Q97 | varchar |  |  | SI | Egreso Plan Ambulatorio Básico |
| Q98 | varchar |  |  | SI | Egreso Intervención Preventiva |
| Q99 | varchar |  |  | SI | Egreso Intervención Terapeutica |
| QMIM2 | varchar |  |  | SI | Mujer con Infante Menor de 2 Años |
| QMIM2ObsDR | varchar |  | FK | SI | Mujer con Infante Menor de 2 Años DR |
| QMIM5 | varchar |  |  | SI | Mujer con Infante Menor de 5 años |
| QMIM5ObsDR | varchar |  | FK | SI | Mujer con Infante Menor de 5 años DR |
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