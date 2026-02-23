# SQLUser.LB_EpisodeGroupTestSet

**Schema:** SQLUser
**Columnas:** 142
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPGTS_RowID | bigint | PK |  | NO | - |
| LBEPGTS_EpisodeGroup_DR | bigint |  | FK | NO | LBRequest Reference |
| LBEPGTS_SpecimenContainers | varchar |  |  | SI | The associated specimen containers |
| LBEPGTS_TestSet_DR | bigint |  | FK | NO | TestSet CodeTable Reference |
| Q04 | - |  |  | SI | VICTIMA |
| Q05 | - |  |  | SI | AGRESOR |
| Q06 | - |  |  | SI | MALTRATO NIÑOS, NIÑAS Y ADOLESCENTES |
| Q07 | - |  |  | SI | ABUSO SEXUAL |
| Q102 | - |  |  | SI | Egreso Trastorno Disocial Desafiante y Oposicionis... |
| Q103 | - |  |  | SI | Egreso Trastorno de Ansiedad de separación en la i... |
| Q104 | - |  |  | SI | Fecha Ingreso Depresión Refractaria |
| Q105 | - |  |  | SI | Fecha Egreso Depresión Refractaria |
| Q106 | - |  |  | SI | Fecha Ingreso Depresión Grave con Psicosis |
| Q107 | - |  |  | SI | Fecha Egreso Depresión Grave con Psicosis |
| Q108 | - |  |  | SI | Fecha Ingreso Depresión con Alto Riesgo Suicida |
| Q109 | - |  |  | SI | Fecha Egreso Depresión con Alto Riesgo Suicida |
| Q110 | - |  |  | SI | Motivo Egreso Depresión Refractaria |
| Q111 | - |  |  | SI | Motivo Egreso Depresión Grave con Psicosis |
| Q112 | - |  |  | SI | Motivo Egreso Depresión con Alto Riesgo Suicida |
| Q113 | - |  |  | SI | Fecha Ingreso Otros Trastornos del comportamiento ... |
| Q114 | - |  |  | SI | Fecha Egreso Otros Trastornos del comportamiento y... |
| Q115 | - |  |  | SI | Motivo Egreso Otros Trastornos del comportamiento ... |
| Q116 | - |  |  | SI | Fecha Ingreso Primer Episodio Esquizofrenia con Oc... |
| Q117 | - |  |  | SI | Fecha Egreso Primer Episodio Esquizofrenia con Ocu... |
| Q118 | - |  |  | SI | Motivo Egreso  Primer Episodio Esquizofrenia con O... |
| Q119 | - |  |  | SI | Fecha Ingreso Otra |
| Q12 | - |  |  | SI | Resultado AUDIT |
| Q120 | - |  |  | SI | Fecha Egreso Otra |
| Q121 | - |  |  | SI | Motivo de Egreso Otra |
| Q122 | - |  |  | SI | Describa |
| Q123 | - |  |  | SI | Tipo de Ingreso (sólo Alcohol y Drogas) |
| Q124 | - |  |  | SI | Plan ambulatorio intensivo |
| Q125 | - |  |  | SI | Fecha Egreso Plan ambulatorio intensivo |
| Q126 | - |  |  | SI | Egreso Plan Ambulatorio Intensivo |
| Q12ObsDR | - |  |  | SI | Resultado AUDIT DR |
| Q16 | - |  |  | SI | Fecha Ingreso Depresión Leve |
| Q17 | - |  |  | SI | Fecha Egreso Depresión Leve |
| Q19 | - |  |  | SI | Fecha Ingreso Depresión Moderada |
| Q20 | - |  |  | SI | Fecha Egreso Depresión Moderada |
| Q22 | - |  |  | SI | Fecha Ingreso Depresión Grave |
| Q23 | - |  |  | SI | Fecha Egreso Depresión Grave |
| Q25 | - |  |  | SI | Fecha Ingreso Post Parto |
| Q26 | - |  |  | SI | Fecha Egreso Post Parto |
| Q28 | - |  |  | SI | Fecha Ingreso Trastorno Bipolar |
| Q29 | - |  |  | SI | Fecha Egreso Trastorno Bipolar |
| Q32 | - |  |  | SI | Fecha Ingreso consumo perjudicial o dependencia de... |
| Q33 | - |  |  | SI | Fecha Egreso  consumo perjudicial o dependencia de... |
| Q35 | - |  |  | SI | Fecha Ingreso Consumo perjudicial o dependencia co... |
| Q36 | - |  |  | SI | Fecha Egreso  Consumo perjudicial o dependencia co... |
| Q38 | - |  |  | SI | Fecha Ingreso Policonsumo |
| Q39 | - |  |  | SI | Fecha Egreso Policonsumo |
| Q41 | - |  |  | SI | Fecha Ingreso Trastorno de Ansiedad |
| Q42 | - |  |  | SI | Fecha Egreso Trastorno de Ansiedad |
| Q44 | - |  |  | SI | Fecha Ingreso Esquizofrenia |
| Q45 | - |  |  | SI | Fecha Egreso Esquizofrenia |
| Q47 | - |  |  | SI | Fecha Ingreso Trastornos de la conducta alimentari... |
| Q48 | - |  |  | SI | Fecha Egreso Trastornos de la conducta alimentaria |
| Q50 | - |  |  | SI | Fecha Ingreso Trastornos Hipercineticos de la acti... |
| Q51 | - |  |  | SI | Fecha Egreso Trastornos Hipercineticos de la activ... |
| Q53 | - |  |  | SI | Fecha Ingreso Trastornos emocionales y del comport... |
| Q54 | - |  |  | SI | Fecha Egreso Trastornos emocionales y del comporta... |
| Q56 | - |  |  | SI | Fecha Ingreso Retraso Mental |
| Q57 | - |  |  | SI | Fecha Egreso Retraso Mental |
| Q59 | - |  |  | SI | Fecha Ingreso Trastorno de personalidad |
| Q60 | - |  |  | SI | Fecha Egreso Trastorno de personalidad |
| Q62 | - |  |  | SI | Fecha Ingreso Trastornos generalizados del desarro... |
| Q63 | - |  |  | SI | Fecha Egreso Generalizado del Desarrollo |
| Q65 | - |  |  | SI | Fecha Ingreso Plan ambulatorio básico |
| Q66 | - |  |  | SI | Fecha Egreso Plan ambulatorio básico |
| Q68 | - |  |  | SI | Fecha Ingreso Intervención Preventiva |
| Q69 | - |  |  | SI | Fecha Egreso Intervención Preventiva |
| Q71 | - |  |  | SI | Fecha Ingreso Intervención Terapeutica |
| Q72 | - |  |  | SI | Fecha Egreso Intervención Terapeutica |
| Q73 | - |  |  | SI | Egreso Depresión Leve |
| Q74 | - |  |  | SI | Egreso Depresión Moderada |
| Q75 | - |  |  | SI | Egreso Depresión Grave |
| Q76 | - |  |  | SI | Egreso Post Parto |
| Q77 | - |  |  | SI | Egreso Trastorno Bipolar |
| Q78 | - |  |  | SI | Egreso Posible consumo Perjudicial o Dependencia d... |
| Q79 | - |  |  | SI | Egreso Otra Sustancia como Droga Principal |
| Q80 | - |  |  | SI | Egreso Policonsumo |
| Q81 | - |  |  | SI | Egreso Trastornos de Ansiedad |
| Q82 | - |  |  | SI | Egreso Esquizofrenia |
| Q83 | - |  |  | SI | Egreso Trastorno de la Conducta Alimentaria |
| Q84 | - |  |  | SI | Egreso Retraso Mental |
| Q85 | - |  |  | SI | Egreso Trastorno de Personalidad |
| Q86 | - |  |  | SI | Egreso Trastorno Generalizado del Desarrollo |
| Q87 | - |  |  | SI | Egreso Plan Ambulatorio Básico |
| Q88 | - |  |  | SI | Egreso Intervención Preventiva |
| Q89 | - |  |  | SI | Egreso Intervención Terapeutica |
| Q90 | - |  |  | SI | Egreso Trastornos Emocionales y del comportamiento... |
| Q91 | - |  |  | SI | Egreso Trastornos Hipercinéticos, de la actividad ... |
| Q92 | - |  |  | SI | Resultado AUDIT - C |
| Q92ObsDR | - |  |  | SI | Resultado AUDIT - C DR |
| Q94 | - |  |  | SI | Fecha Ingreso Trastorno Disocial Desafiante y Opos... |
| Q95 | - |  |  | SI | Fecha Ingreso Trastorno de Ansiedad de separación ... |
| Q98 | - |  |  | SI | Fecha Egreso Trastorno Disocial Desafiante y Oposi... |
| Q99 | - |  |  | SI | Fecha Egreso Trastorno de Ansiedad de separación e... |
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