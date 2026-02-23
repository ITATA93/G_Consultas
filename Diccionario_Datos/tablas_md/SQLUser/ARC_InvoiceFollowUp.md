# SQLUser.ARC_InvoiceFollowUp

**Schema:** SQLUser
**Columnas:** 194
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INVF_RowId | bigint | PK |  | NO | - |
| INVF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INVF_CreatedDate | date |  |  | SI | Created Date |
| INVF_CreatedTime | time |  |  | SI | Created Time |
| INVF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INVF_DateFrom | date |  |  | SI | Date From |
| INVF_DateTo | date |  |  | SI | Date To |
| INVF_Owner | varchar |  |  | SI | Owner |
| INVF_Rep1BillProgStatus_DR | bigint |  | FK | SI | Report 1 Bill Progress Status |
| INVF_Rep1CollectDays | date |  |  | SI | Report 1 Collection Days |
| INVF_Rep2BillProgStatus_DR | bigint |  | FK | SI | Report 2 Bill Progress Status |
| INVF_Rep2CollectDays | date |  |  | SI | Report 2 Collection Days |
| INVF_Rep3BillProgStatus_DR | bigint |  | FK | SI | Report 3 Bill Progress Status |
| INVF_Rep3CollectDays | date |  |  | SI | Report 3 Collection Days |
| INVF_Rep4BillProgStatus_DR | bigint |  | FK | SI | Report 4 Bill Progress Status |
| INVF_Rep4CollectDays | date |  |  | SI | Report 4 Collection Days |
| INVF_Report1_DR | bigint |  | FK | NO | Report 1 |
| INVF_Report2_DR | bigint |  | FK | SI | Report 2 |
| INVF_Report3_DR | bigint |  | FK | SI | Report 3 |
| INVF_Report4_DR | bigint |  | FK | SI | Report 4 |
| INVF_UpdatedDate | date |  |  | SI | Updated Date |
| INVF_UpdatedTime | time |  |  | SI | Updated Time |
| INVF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nivel de Conciencia |
| Q02 | - |  |  | SI | Orientacion en el tiempo |
| Q03 | - |  |  | SI | Orientacion en el Espacio |
| Q04 | - |  |  | SI | Reconocimiento de Personas |
| Q05 | - |  |  | SI | Capacidad para comprender preguntas simples |
| Q06 | - |  |  | SI | Capacidad para responder en forma inteligente |
| Q07 | - |  |  | SI | Capacidad para nombrar objetos |
| Q08 | - |  |  | SI | Capacidad para leer |
| Q09 | - |  |  | SI | Capacidad para escribir |
| Q10 | - |  |  | SI | De hechos remotos |
| Q100 | - |  |  | SI | obs |
| Q101 | - |  |  | SI | obs |
| Q102 | - |  |  | SI | obs |
| Q103 | - |  |  | SI | obs |
| Q104 | - |  |  | SI | obs |
| Q105 | - |  |  | SI | obs |
| Q106 | - |  |  | SI | obs |
| Q107 | - |  |  | SI | obs |
| Q108 | - |  |  | SI | obs |
| Q109 | - |  |  | SI | obs |
| Q10a | - |  |  | SI | Obs_De hechos remotos |
| Q11 | - |  |  | SI | De hechos recientes |
| Q110 | - |  |  | SI | obs |
| Q111 | - |  |  | SI | obs |
| Q112 | - |  |  | SI | obs |
| Q113 | - |  |  | SI | obs |
| Q114 | - |  |  | SI | obs |
| Q115 | - |  |  | SI | obs |
| Q116 | - |  |  | SI | obs |
| Q117 | - |  |  | SI | obs |
| Q118 | - |  |  | SI | Observaciones (Conciencia y Ex. Mental) |
| Q119 | - |  |  | SI | Observaciones (Lenguaje) |
| Q11a | - |  |  | SI | Obs_De hechos recientes |
| Q12 | - |  |  | SI | Capacidad para aprender cosas nuevas |
| Q120 | - |  |  | SI | Observaciones (Memoria) |
| Q121 | - |  |  | SI | Observaciones (Funciones Cognitivas Superiores) |
| Q122 | - |  |  | SI | Observaciones (Nervios Craneanos) |
| Q123 | - |  |  | SI | Observaciones (Motor) |
| Q124 | - |  |  | SI | Observaciones (Sensorial) |
| Q125 | - |  |  | SI | Area:CONCIENCIA Y EXAMEN MENTAL |
| Q126 | - |  |  | SI | Area: LENGUAJE |
| Q127 | - |  |  | SI | Area: MEMORIA |
| Q128 | - |  |  | SI | Area: FUNCIONES COGNITIVAS SUPERIORES |
| Q129 | - |  |  | SI | Area: NERVIOS CRANEANOS |
| Q12a | - |  |  | SI | Obs_Capacidad para aprender cosas nuevas |
| Q13 | - |  |  | SI | Pensamiento abstracto (comparaciones, diferencias,... |
| Q130 | - |  |  | SI | Area: MOTOR |
| Q131 | - |  |  | SI | Area: SENSORIAL |
| Q13a | - |  |  | SI | Obs_Pensamiento abstracto (comparaciones, diferenc... |
| Q14 | - |  |  | SI | Calculo aritmetico y series invertidas |
| Q14a | - |  |  | SI | obs calculo aritmetico y series invertidas |
| Q15 | - |  |  | SI | Capacidad para reproducir un dibujo |
| Q15a | - |  |  | SI | obs_capacidad para reproducir un dibujo |
| Q16 | - |  |  | SI | Estructuración del pensamiento y percepciones (est... |
| Q16a | - |  |  | SI | obs_estructuracion del pensamiento |
| Q17 | - |  |  | SI | Estado anímico y personalidad |
| Q17a | - |  |  | SI | obs_Estado anímico y personalidad |
| Q18 | - |  |  | SI | Olfatorio |
| Q18a | - |  |  | SI | obs_Olfatorio |
| Q19 | - |  |  | SI | Optico |
| Q19a | - |  |  | SI | obs_Optico |
| Q20 | - |  |  | SI | Oculomotor |
| Q20a | - |  |  | SI | obs_Oculomotor |
| Q21 | - |  |  | SI | Troclear |
| Q21a | - |  |  | SI | obs_Troclear |
| Q22 | - |  |  | SI | Trigemino |
| Q22a | - |  |  | SI | obs_Trigemino |
| Q23 | - |  |  | SI | Abducente |
| Q23a | - |  |  | SI | obs_Abducente |
| Q24 | - |  |  | SI | Facial |
| Q24a | - |  |  | SI | obs_Facial |
| Q25 | - |  |  | SI | Auditivo |
| Q25a | - |  |  | SI | obs_Auditivo |
| Q26 | - |  |  | SI | Glosofaringeo |
| Q26a | - |  |  | SI | obs_Glosofaringeo |
| Q27 | - |  |  | SI | Vago |
| Q27a | - |  |  | SI | obs_Vago |
| Q28 | - |  |  | SI | Espinal Accesorio |
| Q28a | - |  |  | SI | obs_Espinal Accesorio |
| Q29 | - |  |  | SI | Hipogloso |
| Q29a | - |  |  | SI | observacion |
| Q2a | - |  |  | SI | Obs orientacion en el tiempo |
| Q30 | - |  |  | SI | Fuerzas |
| Q30a | - |  |  | SI | obs_Fuerzas |
| Q31 | - |  |  | SI | Tono muscular |
| Q31a | - |  |  | SI | obs_Tono muscular |
| Q32 | - |  |  | SI | Reflejos tendíneos profundos y cutáneos |
| Q32a | - |  |  | SI | obs_Reflejos tendíneos profundos y cutáneos |
| Q33 | - |  |  | SI | Coordinación de los movimientos |
| Q33a | - |  |  | SI | obs_Coordinación de los movimientos |
| Q34 | - |  |  | SI | Masas musculares |
| Q34a | - |  |  | SI | obs_Masas musculares |
| Q35 | - |  |  | SI | Movimientos involuntarios |
| Q35a | - |  |  | SI | obs_Movimientos involuntarios |
| Q36 | - |  |  | SI | Dolor y temperatura |
| Q36a | - |  |  | SI | obs_Dolor y temperatura |
| Q37 | - |  |  | SI | Posición y vibración |
| Q37a | - |  |  | SI | obs_posicion y vibracion |
| Q38 | - |  |  | SI | Tacto superficial |
| Q38a | - |  |  | SI | obs_tacto superficial |
| Q39 | - |  |  | SI | Discriminación de distintos estímulos |
| Q39a | - |  |  | SI | obs_discriminacion de distintos estimulos |
| Q3a | - |  |  | SI | Obs orientacion en el espacio |
| Q40 | - |  |  | SI | Signos de irritación meníngea |
| Q4a | - |  |  | SI | Obs_reconocimiento de personas |
| Q5a | - |  |  | SI | Obs_Capacidad para comprender preguntas simples |
| Q6a | - |  |  | SI | Obs_Capacidad para responder en forma inteligente |
| Q79 | - |  |  | SI | obs |
| Q7a | - |  |  | SI | Obs_Capacidad para nombrar objetos |
| Q80 | - |  |  | SI | obs |
| Q81 | - |  |  | SI | obs |
| Q82 | - |  |  | SI | obs |
| Q83 | - |  |  | SI | obs |
| Q84 | - |  |  | SI | obs |
| Q85 | - |  |  | SI | obs |
| Q86 | - |  |  | SI | obs |
| Q87 | - |  |  | SI | obs |
| Q88 | - |  |  | SI | obs |
| Q89 | - |  |  | SI | obs |
| Q8a | - |  |  | SI | Obs_Capacidad para leer |
| Q90 | - |  |  | SI | obs |
| Q91 | - |  |  | SI | obs |
| Q92 | - |  |  | SI | obs |
| Q93 | - |  |  | SI | obs |
| Q94 | - |  |  | SI | obs |
| Q95 | - |  |  | SI | obs |
| Q96 | - |  |  | SI | obs |
| Q97 | - |  |  | SI | obs |
| Q98 | - |  |  | SI | obs |
| Q99 | - |  |  | SI | obs |
| Q9a | - |  |  | SI | Obs_Capacidad para escribir |
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