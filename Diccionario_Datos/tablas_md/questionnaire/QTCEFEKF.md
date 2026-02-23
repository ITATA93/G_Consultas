# questionnaire.QTCEFEKF

> Evaluación Kinésica Funcional

**Schema:** questionnaire
**Columnas:** 166
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Evaluación Kinésica Funcional

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Test Apley Derecha |
| Q02 | varchar |  |  | SI | Test Apley Izquierda |
| Q03 | numeric |  |  | SI | Test Mano-Espalda Derecha&nbsp;cms. |
| Q04 | numeric |  |  | SI | Test Mano-Espalda Izquierda&nbsp;cms. |
| Q05 | numeric |  |  | SI | DISTANCIA ENTRE DEDOS MEDIOS A NIVEL DE ESPALDA DE... |
| Q06 | numeric |  |  | SI | DISTANCIA ENTRE DEDOS MEDIOS A NIVEL DE ESPALDA IZ... |
| Q07 | varchar |  |  | SI | Codo Flexión&nbsp;Derecha |
| Q08 | varchar |  |  | SI | Codo Flexión Izquierda |
| Q09 | varchar |  |  | SI | Codo Extersión&nbsp;Derecha |
| Q10 | varchar |  |  | SI | Codo Extersión Izquierda |
| Q100 | varchar |  |  | SI | TOBILLO |
| Q101 | varchar |  |  | SI | IZQUIERDO |
| Q102 | varchar |  |  | SI | FLEXIÓN |
| Q103 | varchar |  |  | SI | EXTENSIÓN |
| Q104 | varchar |  |  | SI | PRUEBA DE SENTARSE EN LA SILLA Y ALCANZAR LA PUNTA... |
| Q105 | varchar |  |  | SI | ESTACIÓN UNIPODAL |
| Q106 | varchar |  |  | SI | TIMED UP AND GO |
| Q107 | varchar |  |  | SI | EV. ENF. DE PARKINSON |
| Q108 | varchar |  |  | SI | ANTECEDENTES PSICOSOCIALES Y REDES |
| Q109 | varchar |  |  | SI | DIAGNÓSTICO KINÉSICO FUNCIONAL |
| Q11 | varchar |  |  | SI | Codo Supinación Derecha |
| Q110 | varchar |  |  | SI | PLANO DE TRATAMENTO |
| Q111 | varchar |  |  | SI | HOMBRO |
| Q112 | varchar |  |  | SI | COLUMNA |
| Q113 | varchar |  |  | SI | CADERA |
| Q114 | varchar |  |  | SI | RODILLA |
| Q115 | varchar |  |  | SI | Resultado Evaluación Funcional Cadera |
| Q115ObsDR | varchar |  | FK | SI | Resultado Evaluación Funcional Cadera DR |
| Q116 | varchar |  |  | SI | Resultado Evaluación Cadera Harris Modificado |
| Q116ObsDR | varchar |  | FK | SI | Resultado Evaluación Cadera Harris Modificado DR |
| Q12 | varchar |  |  | SI | Codo Supinación Izquierda |
| Q13 | varchar |  |  | SI | Codo Pronación Derecha |
| Q14 | varchar |  |  | SI | Codo Pronación Izquierda |
| Q15 | varchar |  |  | SI | Mano Oposición Derecha |
| Q16 | varchar |  |  | SI | Mano Oposición Izquierda |
| Q17 | varchar |  |  | SI | Mano Prensión Derecha |
| Q18 | varchar |  |  | SI | Mano Prensión Izquierda |
| Q19 | varchar |  |  | SI | Cadera Test de Piernas Cruzadas Derecha |
| Q20 | varchar |  |  | SI | Cadera Test de Piernas Cruzadas Izquierda |
| Q21 | varchar |  |  | SI | Rodilla Flexión&nbsp;Derecha |
| Q22 | varchar |  |  | SI | Rodilla Flexión Izquierda |
| Q23 | varchar |  |  | SI | Rodilla Extersión Derecha |
| Q24 | varchar |  |  | SI | Rodilla Extersión Izquierda |
| Q25 | numeric |  |  | SI | Fuerza de Cuadriceps&nbsp;Izquierdo (%) |
| Q26 | numeric |  |  | SI | Fuerza de Cuadriceps&nbsp;Derecho (%) |
| Q27 | varchar |  |  | SI | Tobillo Flexión Derecho |
| Q28 | varchar |  |  | SI | Tobillo Flexión Izquierdo |
| Q29 | varchar |  |  | SI | Tobillo Extersión Derecho |
| Q30 | varchar |  |  | SI | Tobillo Extersión&nbsp;Izquierdo |
| Q31 | numeric |  |  | SI | Sentarse en una silla y tocar la punta del pie, Di... |
| Q32 | numeric |  |  | SI | Sentarse en una silla y tocar la punta del pie, Di... |
| Q33 | varchar |  |  | SI | Caidas |
| Q34 | numeric |  |  | SI | Cantidad |
| Q35 | numeric |  |  | SI | Estación Unipodal Izquierda&nbsp;(Seg.) |
| Q36 | numeric |  |  | SI | Estación Unipodal Derecha&nbsp;(Seg.) |
| Q37 | numeric |  |  | SI | Timed Up and Go (Seg.) |
| Q38 | varchar |  |  | SI | Ayudas Técnicas |
| Q39 | bit |  |  | SI | Bastón |
| Q40 | bit |  |  | SI | Andador |
| Q41 | bit |  |  | SI | Silla de Ruedas |
| Q42 | varchar |  |  | SI | Otro |
| Q43 | varchar |  |  | SI | Bradicinesia&nbsp;(Signo Obligado) |
| Q44 | varchar |  |  | SI | Rigidez (Flexión y Extensión de Muñeca y Codo) |
| Q45 | varchar |  |  | SI | Temblor de Reposo&nbsp;(Mov. Pulgar - Indice Recíp... |
| Q46 | varchar |  |  | SI | Alt. Reflejos Posturales&nbsp;(Test del Empujón) |
| Q47 | varchar |  |  | SI | Realiza Actividad Física |
| Q48 | numeric |  |  | SI | Veces&nbsp;por Semana |
| Q49 | varchar |  |  | SI | Arrastra un Pié |
| Q50 | varchar |  |  | SI | Ev.Función Respiratoria |
| Q51 | varchar |  |  | SI | Compensado |
| Q52 | varchar |  |  | SI | ¿Se siente acompañado(a)? |
| Q53 | varchar |  |  | SI | ¿Siente que las personas de casa se preocupan de u... |
| Q54 | varchar |  |  | SI | ¿Le agrada participar en actividades de grupo? |
| Q55 | varchar |  |  | SI | ¿Presenta alteraciones del sueño? |
| Q56 | varchar |  |  | SI | Diagnóstico Kinésico Funcional |
| Q57 | varchar |  |  | SI | Prestaciones Kinesicas |
| Q58 | varchar |  |  | SI | Otros |
| Q59 | varchar |  |  | SI | PLAN DE TRATAMIENTO |
| Q60 | numeric |  |  | SI | Individual / N° Sesiones |
| Q61 | numeric |  |  | SI | Grupal / N° Sesiones |
| Q62 | varchar |  |  | SI | FICHA DE EVALUACION KINÉSICA FUNCIONAL |
| Q63 | varchar |  |  | SI | DOLOR OSTEOARTICULAR: Utilice Escala Visual Análog... |
| Q64 | varchar |  |  | SI | DERECHA |
| Q65 | varchar |  |  | SI | HOMBRO |
| Q66 | varchar |  |  | SI | IZQUIERDA |
| Q67 | varchar |  |  | SI | Eva Hombro Derecho |
| Q67ObsDR | varchar |  | FK | SI | Eva Hombro Derecho DR |
| Q68 | varchar |  |  | SI | Eva Hombro Izquierdo |
| Q68ObsDR | varchar |  | FK | SI | Eva Hombro Izquierdo DR |
| Q69 | varchar |  |  | SI | Eva Columna |
| Q69ObsDR | varchar |  | FK | SI | Eva Columna DR |
| Q70 | varchar |  |  | SI | Eva Cadera Derecha |
| Q70ObsDR | varchar |  | FK | SI | Eva Cadera Derecha DR |
| Q71 | varchar |  |  | SI | Eva Cadera Izquierda |
| Q71ObsDR | varchar |  | FK | SI | Eva Cadera Izquierda DR |
| Q72 | varchar |  |  | SI | Eva Rodilla Derecha |
| Q72ObsDR | varchar |  | FK | SI | Eva Rodilla Derecha DR |
| Q73 | varchar |  |  | SI | Eva Rodilla Izquierda |
| Q73ObsDR | varchar |  | FK | SI | Eva Rodilla Izquierda DR |
| Q74 | varchar |  |  | SI | TEST APLEY |
| Q75 | varchar |  |  | SI | TEST MANO-ESPALDA |
| Q76 | varchar |  |  | SI | DISTANCIA ENTRE DEDOS MEDIOS A NIVEL DE ESPALDA |
| Q77 | varchar |  |  | SI | DERECHA |
| Q78 | varchar |  |  | SI | CODO |
| Q79 | varchar |  |  | SI | IZQUIERDA |
| Q80 | varchar |  |  | SI | FLEXIÓN |
| Q81 | varchar |  |  | SI | EXTENSIÓN |
| Q82 | varchar |  |  | SI | SUPINACIÓN |
| Q83 | varchar |  |  | SI | PRONACIÓN |
| Q84 | varchar |  |  | SI | DERECHA |
| Q85 | varchar |  |  | SI | MANO |
| Q86 | varchar |  |  | SI | IZQUIERDA |
| Q87 | varchar |  |  | SI | OPOSICIÓN |
| Q88 | varchar |  |  | SI | PRENSIÓN |
| Q89 | varchar |  |  | SI | DERECHA |
| Q90 | varchar |  |  | SI | CADERA |
| Q91 | varchar |  |  | SI | IZQUIERDA |
| Q92 | varchar |  |  | SI | TEST PIERNAS CRUZADAS |
| Q93 | varchar |  |  | SI | DERECHA |
| Q94 | varchar |  |  | SI | RODILLA |
| Q95 | varchar |  |  | SI | IZQUIERDA |
| Q96 | varchar |  |  | SI | FLEXIÓN |
| Q97 | varchar |  |  | SI | EXTENSIÓN |
| Q98 | varchar |  |  | SI | FUERZA DE CUADRICEPS |
| Q99 | varchar |  |  | SI | DERECHO |
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