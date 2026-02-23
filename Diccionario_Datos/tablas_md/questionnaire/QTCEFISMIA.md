# questionnaire.QTCEFISMIA

> Formulario Ingreso - Egreso Salud Mental Infanto - Adolescente

**Schema:** questionnaire
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Formulario Ingreso - Egreso Salud Mental Infanto - Adolescente

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q04 | varchar |  |  | SI | VICTIMA |
| Q05 | varchar |  |  | SI | AGRESOR |
| Q06 | varchar |  |  | SI | MALTRATO NIÑOS, NIÑAS Y ADOLESCENTES |
| Q07 | varchar |  |  | SI | ABUSO SEXUAL |
| Q102 | varchar |  |  | SI | Egreso Trastorno Disocial Desafiante y Oposicionis... |
| Q103 | varchar |  |  | SI | Egreso Trastorno de Ansiedad de separación en la i... |
| Q104 | date |  |  | SI | Fecha Ingreso Depresión Refractaria |
| Q105 | date |  |  | SI | Fecha Egreso Depresión Refractaria |
| Q106 | date |  |  | SI | Fecha Ingreso Depresión Grave con Psicosis |
| Q107 | date |  |  | SI | Fecha Egreso Depresión Grave con Psicosis |
| Q108 | date |  |  | SI | Fecha Ingreso Depresión con Alto Riesgo Suicida |
| Q109 | date |  |  | SI | Fecha Egreso Depresión con Alto Riesgo Suicida |
| Q110 | varchar |  |  | SI | Motivo Egreso Depresión Refractaria |
| Q111 | varchar |  |  | SI | Motivo Egreso Depresión Grave con Psicosis |
| Q112 | varchar |  |  | SI | Motivo Egreso Depresión con Alto Riesgo Suicida |
| Q113 | date |  |  | SI | Fecha Ingreso Otros Trastornos del comportamiento ... |
| Q114 | date |  |  | SI | Fecha Egreso Otros Trastornos del comportamiento y... |
| Q115 | varchar |  |  | SI | Motivo Egreso Otros Trastornos del comportamiento ... |
| Q116 | date |  |  | SI | Fecha Ingreso Primer Episodio Esquizofrenia con Oc... |
| Q117 | date |  |  | SI | Fecha Egreso Primer Episodio Esquizofrenia con Ocu... |
| Q118 | varchar |  |  | SI | Motivo Egreso  Primer Episodio Esquizofrenia con O... |
| Q119 | date |  |  | SI | Fecha Ingreso Otra |
| Q12 | varchar |  |  | SI | Resultado AUDIT |
| Q120 | date |  |  | SI | Fecha Egreso Otra |
| Q121 | varchar |  |  | SI | Motivo de Egreso Otra |
| Q122 | varchar |  |  | SI | Describa |
| Q123 | varchar |  |  | SI | Tipo de Ingreso (sólo Alcohol y Drogas) |
| Q124 | date |  |  | SI | Plan ambulatorio intensivo |
| Q125 | date |  |  | SI | Fecha Egreso Plan ambulatorio intensivo |
| Q126 | varchar |  |  | SI | Egreso Plan Ambulatorio Intensivo |
| Q12ObsDR | varchar |  | FK | SI | Resultado AUDIT DR |
| Q16 | date |  |  | SI | Fecha Ingreso Depresión Leve |
| Q17 | date |  |  | SI | Fecha Egreso Depresión Leve |
| Q19 | date |  |  | SI | Fecha Ingreso Depresión Moderada |
| Q20 | date |  |  | SI | Fecha Egreso Depresión Moderada |
| Q22 | date |  |  | SI | Fecha Ingreso Depresión Grave |
| Q23 | date |  |  | SI | Fecha Egreso Depresión Grave |
| Q25 | date |  |  | SI | Fecha Ingreso Post Parto |
| Q26 | date |  |  | SI | Fecha Egreso Post Parto |
| Q28 | date |  |  | SI | Fecha Ingreso Trastorno Bipolar |
| Q29 | date |  |  | SI | Fecha Egreso Trastorno Bipolar |
| Q32 | date |  |  | SI | Fecha Ingreso consumo perjudicial o dependencia de... |
| Q33 | date |  |  | SI | Fecha Egreso  consumo perjudicial o dependencia de... |
| Q35 | date |  |  | SI | Fecha Ingreso Consumo perjudicial o dependencia co... |
| Q36 | date |  |  | SI | Fecha Egreso  Consumo perjudicial o dependencia co... |
| Q38 | date |  |  | SI | Fecha Ingreso Policonsumo |
| Q39 | date |  |  | SI | Fecha Egreso Policonsumo |
| Q41 | date |  |  | SI | Fecha Ingreso Trastorno de Ansiedad |
| Q42 | date |  |  | SI | Fecha Egreso Trastorno de Ansiedad |
| Q44 | date |  |  | SI | Fecha Ingreso Esquizofrenia |
| Q45 | date |  |  | SI | Fecha Egreso Esquizofrenia |
| Q47 | date |  |  | SI | Fecha Ingreso Trastornos de la conducta alimentari... |
| Q48 | date |  |  | SI | Fecha Egreso Trastornos de la conducta alimentaria |
| Q50 | date |  |  | SI | Fecha Ingreso Trastornos Hipercineticos de la acti... |
| Q51 | date |  |  | SI | Fecha Egreso Trastornos Hipercineticos de la activ... |
| Q53 | date |  |  | SI | Fecha Ingreso Trastornos emocionales y del comport... |
| Q54 | date |  |  | SI | Fecha Egreso Trastornos emocionales y del comporta... |
| Q56 | date |  |  | SI | Fecha Ingreso Retraso Mental |
| Q57 | date |  |  | SI | Fecha Egreso Retraso Mental |
| Q59 | date |  |  | SI | Fecha Ingreso Trastorno de personalidad |
| Q60 | date |  |  | SI | Fecha Egreso Trastorno de personalidad |
| Q62 | date |  |  | SI | Fecha Ingreso Trastornos generalizados del desarro... |
| Q63 | date |  |  | SI | Fecha Egreso Generalizado del Desarrollo |
| Q65 | date |  |  | SI | Fecha Ingreso Plan ambulatorio básico |
| Q66 | date |  |  | SI | Fecha Egreso Plan ambulatorio básico |
| Q68 | date |  |  | SI | Fecha Ingreso Intervención Preventiva |
| Q69 | date |  |  | SI | Fecha Egreso Intervención Preventiva |
| Q71 | date |  |  | SI | Fecha Ingreso Intervención Terapeutica |
| Q72 | date |  |  | SI | Fecha Egreso Intervención Terapeutica |
| Q73 | varchar |  |  | SI | Egreso Depresión Leve |
| Q74 | varchar |  |  | SI | Egreso Depresión Moderada |
| Q75 | varchar |  |  | SI | Egreso Depresión Grave |
| Q76 | varchar |  |  | SI | Egreso Post Parto |
| Q77 | varchar |  |  | SI | Egreso Trastorno Bipolar |
| Q78 | varchar |  |  | SI | Egreso Posible consumo Perjudicial o Dependencia d... |
| Q79 | varchar |  |  | SI | Egreso Otra Sustancia como Droga Principal |
| Q80 | varchar |  |  | SI | Egreso Policonsumo |
| Q81 | varchar |  |  | SI | Egreso Trastornos de Ansiedad |
| Q82 | varchar |  |  | SI | Egreso Esquizofrenia |
| Q83 | varchar |  |  | SI | Egreso Trastorno de la Conducta Alimentaria |
| Q84 | varchar |  |  | SI | Egreso Retraso Mental |
| Q85 | varchar |  |  | SI | Egreso Trastorno de Personalidad |
| Q86 | varchar |  |  | SI | Egreso Trastorno Generalizado del Desarrollo |
| Q87 | varchar |  |  | SI | Egreso Plan Ambulatorio Básico |
| Q88 | varchar |  |  | SI | Egreso Intervención Preventiva |
| Q89 | varchar |  |  | SI | Egreso Intervención Terapeutica |
| Q90 | varchar |  |  | SI | Egreso Trastornos Emocionales y del comportamiento... |
| Q91 | varchar |  |  | SI | Egreso Trastornos Hipercinéticos, de la actividad ... |
| Q92 | varchar |  |  | SI | Resultado AUDIT - C |
| Q92ObsDR | varchar |  | FK | SI | Resultado AUDIT - C DR |
| Q94 | date |  |  | SI | Fecha Ingreso Trastorno Disocial Desafiante y Opos... |
| Q95 | date |  |  | SI | Fecha Ingreso Trastorno de Ansiedad de separación ... |
| Q98 | date |  |  | SI | Fecha Egreso Trastorno Disocial Desafiante y Oposi... |
| Q99 | date |  |  | SI | Fecha Egreso Trastorno de Ansiedad de separación e... |
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