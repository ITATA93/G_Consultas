# SQLUser.MRC_MedicalCertifType

**Schema:** SQLUser
**Columnas:** 143
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEDCT_RowId | bigint | PK |  | NO | - |
| MEDCT_Code | varchar |  |  | NO | Code |
| MEDCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MEDCT_CreatedDate | date |  |  | SI | Created Date |
| MEDCT_CreatedTime | time |  |  | SI | Created Time |
| MEDCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEDCT_DateFrom | date |  |  | SI | DateFrom |
| MEDCT_DateTo | date |  |  | SI | DateTo |
| MEDCT_Desc | varchar |  |  | NO | Description |
| MEDCT_Owner | varchar |  |  | SI | Owner |
| MEDCT_UpdatedDate | date |  |  | SI | Updated Date |
| MEDCT_UpdatedTime | time |  |  | SI | Updated Time |
| MEDCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | VICTIMA |
| Q02 | - |  |  | SI | AGRESOR |
| Q03 | - |  |  | SI | VIOLENCIA HACIA EL ADULTO MAYOR |
| Q04 | - |  |  | SI | ABUSO SEXUAL |
| Q08 | - |  |  | SI | CONSUMO RIESGOSO DE DROGAS |
| Q09 | - |  |  | SI | Fecha Ingreso Depresión Moderada |
| Q10 | - |  |  | SI | Fecha Egreso Depresión Leve |
| Q100 | - |  |  | SI | Egreso Trastornos conductuales asociados a Demenci... |
| Q101 | - |  |  | SI | Fecha Ingreso Depresión Refractaria |
| Q102 | - |  |  | SI | Fecha Egreso Depresión Refractaria |
| Q103 | - |  |  | SI | Fecha Ingreso Depresión Grave con Psicosis |
| Q104 | - |  |  | SI | Fecha Egreso Depresión Grave con Psicos |
| Q105 | - |  |  | SI | Fecha Ingreso Depresión con Alto Riesgo Suicida |
| Q106 | - |  |  | SI | Fecha Egreso Depresión con Alto Riesgo Suicida |
| Q107 | - |  |  | SI | Motivo Egreso Depresión Refractaria |
| Q108 | - |  |  | SI | Motivo Egreso Depresión Grave con Psicosis |
| Q109 | - |  |  | SI | Motivo Egreso Depresión con Alto Riesgo Suicida |
| Q11 | - |  |  | SI | Fecha Ingreso Depresión Leve |
| Q110 | - |  |  | SI | Fecha Ingreso Primer Episodio Esquizofrenia con Oc... |
| Q111 | - |  |  | SI | Fecha Egreso Primer Episodio Esquizofrenia con Ocu... |
| Q112 | - |  |  | SI | Motivo Egreso Primer Episodio Esquizofrenia con Oc... |
| Q113 | - |  |  | SI | Tipo de Ingreso (Alcohol y Drogas) |
| Q114 | - |  |  | SI | Plan Ambulatorio Intensivo |
| Q115 | - |  |  | SI | Fecha Egreso Plan Ambulatorio Intensivo |
| Q116 | - |  |  | SI | Egreso Plan Ambulatorio Intensivo |
| Q12 | - |  |  | SI | Fecha Egreso Depresión Moderada |
| Q13 | - |  |  | SI | Fecha Ingreso Depresión Grave |
| Q14 | - |  |  | SI | Fecha Egreso Depresión Grave |
| Q15 | - |  |  | SI | Fecha Ingreso Depresión Post Parto |
| Q16 | - |  |  | SI | Fecha Egreso Depresión Post Parto |
| Q17 | - |  |  | SI | Fecha Ingreso Trastorno Bipolar |
| Q18 | - |  |  | SI | Fecha Egreso Trastorno Bipolar |
| Q19 | - |  |  | SI | Fecha Ingreso consumo perjudicial o dependencia de... |
| Q20 | - |  |  | SI | Fecha Egreso  consumo perjudicial o dependencia de... |
| Q21 | - |  |  | SI | Fecha Ingreso  Consumo perjudicial o dependencia c... |
| Q22 | - |  |  | SI | Fecha Egreso  Consumo perjudicial o dependencia co... |
| Q23 | - |  |  | SI | Fecha Ingreso Policonsumo |
| Q24 | - |  |  | SI | Fecha Egreso Policonsumo |
| Q25 | - |  |  | SI | Fecha Ingreso Trastorno de Ansiedad |
| Q26 | - |  |  | SI | Fecha Egreso Trastorno de Ansiedad |
| Q27 | - |  |  | SI | Fecha Ingreso Alzheimer y otras Demencias |
| Q28 | - |  |  | SI | Fecha Egreso Alzheimer y otras Demencias |
| Q29 | - |  |  | SI | Fecha Ingreso Esquizofrenia |
| Q30 | - |  |  | SI | Fecha Egreso Esquizofrenia |
| Q31 | - |  |  | SI | Fecha Ingreso Trastornos de la conducta Alimentari... |
| Q32 | - |  |  | SI | Fecha Egreso Trastornos de la conducta Alimentaria |
| Q33 | - |  |  | SI | Fecha Ingreso Retraso Mental |
| Q34 | - |  |  | SI | Fecha Egreso Retraso Mental |
| Q35 | - |  |  | SI | Fecha Ingreso Trastorno de Personalidad |
| Q36 | - |  |  | SI | Fecha Egreso Trastorno de Personalidad |
| Q37 | - |  |  | SI | Fecha Ingreso Trastorno Generalizados del Desarrol... |
| Q38 | - |  |  | SI | Fecha Egreso Trastornos Generalizados del Desarrol... |
| Q39 | - |  |  | SI | Fecha Ingreso Plan Ambulatorio Básico |
| Q40 | - |  |  | SI | Fecha Egreso Plan Ambulatorio Básico |
| Q41 | - |  |  | SI | Fecha Ingreso Intervención Preventiva |
| Q42 | - |  |  | SI | Fecha Egreso Intervención Preventiva |
| Q43 | - |  |  | SI | Fecha Ingreso Intervención Terapeutica |
| Q44 | - |  |  | SI | Fecha Egreso Intervención Terapeutica |
| Q45 | - |  |  | SI | Fecha Ingreso Trastornos conductuales asociados a ... |
| Q46 | - |  |  | SI | Fecha Egreso Trastornos conductuales asociados a D... |
| Q57 | - |  |  | SI | Resultado AUDIT |
| Q57ObsDR | - |  |  | SI | Resultado AUDIT DR |
| Q59 | - |  |  | SI | Resultado AUDIT-C |
| Q59ObsDR | - |  |  | SI | Resultado AUDIT-C DR |
| Q78 | - |  |  | SI | Fecha Ingreso Otra |
| Q79 | - |  |  | SI | Fecha Egreso Otra |
| Q80 | - |  |  | SI | Motivo de Egreso Otra |
| Q81 | - |  |  | SI | Describa |
| Q82 | - |  |  | SI | Egreso Depresión Leve |
| Q83 | - |  |  | SI | Egreso Depresión Moderada |
| Q84 | - |  |  | SI | Egreso Depresión Grave |
| Q85 | - |  |  | SI | Egreso Depresión Post Parto |
| Q86 | - |  |  | SI | Egreso Trastorno Bipolar |
| Q87 | - |  |  | SI | Egreso Posible consumo Perjudicial o Dependencia d... |
| Q88 | - |  |  | SI | Egreso Otra Sustancia como Droga Principal |
| Q89 | - |  |  | SI | Egreso Policonsumo |
| Q90 | - |  |  | SI | Egreso Trastornos de Ansiedad |
| Q91 | - |  |  | SI | Egreso Alzheirmer y otras Demencias |
| Q92 | - |  |  | SI | Egreso Esquizofrenia |
| Q93 | - |  |  | SI | Egreso Trastornos de la Conducta Alimentaria |
| Q94 | - |  |  | SI | Egreso Retraso Mental |
| Q95 | - |  |  | SI | Egreso Trastorno de Personalidad |
| Q96 | - |  |  | SI | Egreso Trastorno Generalizados del Desarrollo |
| Q97 | - |  |  | SI | Egreso Plan Ambulatorio Básico |
| Q98 | - |  |  | SI | Egreso Intervención Preventiva |
| Q99 | - |  |  | SI | Egreso Intervención Terapeutica |
| QMIM2 | - |  |  | SI | Mujer con Infante Menor de 2 Años |
| QMIM2ObsDR | - |  |  | SI | Mujer con Infante Menor de 2 Años DR |
| QMIM5 | - |  |  | SI | Mujer con Infante Menor de 5 años |
| QMIM5ObsDR | - |  |  | SI | Mujer con Infante Menor de 5 años DR |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*