# SQLUser.MRC_PlaceOfBirth

**Schema:** SQLUser
**Columnas:** 174
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| POB_RowId | bigint | PK |  | NO | - |
| POB_Code | varchar |  |  | NO | Code |
| POB_CreatedDate | date |  |  | SI | Created Date |
| POB_CreatedTime | time |  |  | SI | Created Time |
| POB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| POB_Desc | varchar |  |  | NO | Description |
| POB_UpdatedDate | date |  |  | SI | Updated Date |
| POB_UpdatedTime | time |  |  | SI | Updated Time |
| POB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Test Apley Derecha |
| Q02 | - |  |  | SI | Test Apley Izquierda |
| Q03 | - |  |  | SI | Test Mano-Espalda Derecha&nbsp |
| Q04 | - |  |  | SI | Test Mano-Espalda Izquierda&nbsp |
| Q05 | - |  |  | SI | DISTANCIA ENTRE DEDOS MEDIOS A NIVEL DE ESPALDA DE... |
| Q06 | - |  |  | SI | DISTANCIA ENTRE DEDOS MEDIOS A NIVEL DE ESPALDA IZ... |
| Q07 | - |  |  | SI | Codo Flexión&nbsp |
| Q08 | - |  |  | SI | Codo Flexión Izquierda |
| Q09 | - |  |  | SI | Codo Extersión&nbsp |
| Q10 | - |  |  | SI | Codo Extersión Izquierda |
| Q100 | - |  |  | SI | TOBILLO |
| Q101 | - |  |  | SI | IZQUIERDO |
| Q102 | - |  |  | SI | FLEXIÓN |
| Q103 | - |  |  | SI | EXTENSIÓN |
| Q104 | - |  |  | SI | PRUEBA DE SENTARSE EN LA SILLA Y ALCANZAR LA PUNTA... |
| Q105 | - |  |  | SI | ESTACIÓN UNIPODAL |
| Q106 | - |  |  | SI | TIMED UP AND GO |
| Q107 | - |  |  | SI | EV. ENF. DE PARKINSON |
| Q108 | - |  |  | SI | ANTECEDENTES PSICOSOCIALES Y REDES |
| Q109 | - |  |  | SI | DIAGNÓSTICO KINÉSICO FUNCIONAL |
| Q11 | - |  |  | SI | Codo Supinación Derecha |
| Q110 | - |  |  | SI | PLANO DE TRATAMENTO |
| Q111 | - |  |  | SI | HOMBRO |
| Q112 | - |  |  | SI | COLUMNA |
| Q113 | - |  |  | SI | CADERA |
| Q114 | - |  |  | SI | RODILLA |
| Q115 | - |  |  | SI | Resultado Evaluación Funcional Cadera |
| Q115ObsDR | - |  |  | SI | Resultado Evaluación Funcional Cadera DR |
| Q116 | - |  |  | SI | Resultado Evaluación Cadera Harris Modificado |
| Q116ObsDR | - |  |  | SI | Resultado Evaluación Cadera Harris Modificado DR |
| Q12 | - |  |  | SI | Codo Supinación Izquierda |
| Q13 | - |  |  | SI | Codo Pronación Derecha |
| Q14 | - |  |  | SI | Codo Pronación Izquierda |
| Q15 | - |  |  | SI | Mano Oposición Derecha |
| Q16 | - |  |  | SI | Mano Oposición Izquierda |
| Q17 | - |  |  | SI | Mano Prensión Derecha |
| Q18 | - |  |  | SI | Mano Prensión Izquierda |
| Q19 | - |  |  | SI | Cadera Test de Piernas Cruzadas Derecha |
| Q20 | - |  |  | SI | Cadera Test de Piernas Cruzadas Izquierda |
| Q21 | - |  |  | SI | Rodilla Flexión&nbsp |
| Q22 | - |  |  | SI | Rodilla Flexión Izquierda |
| Q23 | - |  |  | SI | Rodilla Extersión Derecha |
| Q24 | - |  |  | SI | Rodilla Extersión Izquierda |
| Q25 | - |  |  | SI | Fuerza de Cuadriceps&nbsp |
| Q26 | - |  |  | SI | Fuerza de Cuadriceps&nbsp |
| Q27 | - |  |  | SI | Tobillo Flexión Derecho |
| Q28 | - |  |  | SI | Tobillo Flexión Izquierdo |
| Q29 | - |  |  | SI | Tobillo Extersión Derecho |
| Q30 | - |  |  | SI | Tobillo Extersión&nbsp |
| Q31 | - |  |  | SI | Sentarse en una silla y tocar la punta del pie, Di... |
| Q32 | - |  |  | SI | Sentarse en una silla y tocar la punta del pie, Di... |
| Q33 | - |  |  | SI | Caidas |
| Q34 | - |  |  | SI | Cantidad |
| Q35 | - |  |  | SI | Estación Unipodal Izquierda&nbsp |
| Q36 | - |  |  | SI | Estación Unipodal Derecha&nbsp |
| Q37 | - |  |  | SI | Timed Up and Go (Seg.) |
| Q38 | - |  |  | SI | Ayudas Técnicas |
| Q39 | - |  |  | SI | Bastón |
| Q40 | - |  |  | SI | Andador |
| Q41 | - |  |  | SI | Silla de Ruedas |
| Q42 | - |  |  | SI | Otro |
| Q43 | - |  |  | SI | Bradicinesia&nbsp |
| Q44 | - |  |  | SI | Rigidez (Flexión y Extensión de Muñeca y Codo) |
| Q45 | - |  |  | SI | Temblor de Reposo&nbsp |
| Q46 | - |  |  | SI | Alt. Reflejos Posturales&nbsp |
| Q47 | - |  |  | SI | Realiza Actividad Física |
| Q48 | - |  |  | SI | Veces&nbsp |
| Q49 | - |  |  | SI | Arrastra un Pié |
| Q50 | - |  |  | SI | Ev.Función Respiratoria |
| Q51 | - |  |  | SI | Compensado |
| Q52 | - |  |  | SI | ¿Se siente acompañado(a)? |
| Q53 | - |  |  | SI | ¿Siente que las personas de casa se preocupan de u... |
| Q54 | - |  |  | SI | ¿Le agrada participar en actividades de grupo? |
| Q55 | - |  |  | SI | ¿Presenta alteraciones del sueño? |
| Q56 | - |  |  | SI | Diagnóstico Kinésico Funcional |
| Q57 | - |  |  | SI | Prestaciones Kinesicas |
| Q58 | - |  |  | SI | Otros |
| Q59 | - |  |  | SI | PLAN DE TRATAMIENTO |
| Q60 | - |  |  | SI | Individual / N° Sesiones |
| Q61 | - |  |  | SI | Grupal / N° Sesiones |
| Q62 | - |  |  | SI | FICHA DE EVALUACION KINÉSICA FUNCIONAL |
| Q63 | - |  |  | SI | DOLOR OSTEOARTICULAR: Utilice Escala Visual Análog... |
| Q64 | - |  |  | SI | DERECHA |
| Q65 | - |  |  | SI | HOMBRO |
| Q66 | - |  |  | SI | IZQUIERDA |
| Q67 | - |  |  | SI | Eva Hombro Derecho |
| Q67ObsDR | - |  |  | SI | Eva Hombro Derecho DR |
| Q68 | - |  |  | SI | Eva Hombro Izquierdo |
| Q68ObsDR | - |  |  | SI | Eva Hombro Izquierdo DR |
| Q69 | - |  |  | SI | Eva Columna |
| Q69ObsDR | - |  |  | SI | Eva Columna DR |
| Q70 | - |  |  | SI | Eva Cadera Derecha |
| Q70ObsDR | - |  |  | SI | Eva Cadera Derecha DR |
| Q71 | - |  |  | SI | Eva Cadera Izquierda |
| Q71ObsDR | - |  |  | SI | Eva Cadera Izquierda DR |
| Q72 | - |  |  | SI | Eva Rodilla Derecha |
| Q72ObsDR | - |  |  | SI | Eva Rodilla Derecha DR |
| Q73 | - |  |  | SI | Eva Rodilla Izquierda |
| Q73ObsDR | - |  |  | SI | Eva Rodilla Izquierda DR |
| Q74 | - |  |  | SI | TEST APLEY |
| Q75 | - |  |  | SI | TEST MANO-ESPALDA |
| Q76 | - |  |  | SI | DISTANCIA ENTRE DEDOS MEDIOS A NIVEL DE ESPALDA |
| Q77 | - |  |  | SI | DERECHA |
| Q78 | - |  |  | SI | CODO |
| Q79 | - |  |  | SI | IZQUIERDA |
| Q80 | - |  |  | SI | FLEXIÓN |
| Q81 | - |  |  | SI | EXTENSIÓN |
| Q82 | - |  |  | SI | SUPINACIÓN |
| Q83 | - |  |  | SI | PRONACIÓN |
| Q84 | - |  |  | SI | DERECHA |
| Q85 | - |  |  | SI | MANO |
| Q86 | - |  |  | SI | IZQUIERDA |
| Q87 | - |  |  | SI | OPOSICIÓN |
| Q88 | - |  |  | SI | PRENSIÓN |
| Q89 | - |  |  | SI | DERECHA |
| Q90 | - |  |  | SI | CADERA |
| Q91 | - |  |  | SI | IZQUIERDA |
| Q92 | - |  |  | SI | TEST PIERNAS CRUZADAS |
| Q93 | - |  |  | SI | DERECHA |
| Q94 | - |  |  | SI | RODILLA |
| Q95 | - |  |  | SI | IZQUIERDA |
| Q96 | - |  |  | SI | FLEXIÓN |
| Q97 | - |  |  | SI | EXTENSIÓN |
| Q98 | - |  |  | SI | FUERZA DE CUADRICEPS |
| Q99 | - |  |  | SI | DERECHO |
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