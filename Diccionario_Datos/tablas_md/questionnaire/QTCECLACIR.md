# questionnaire.QTCECLACIR

> Cirugia Geral

**Schema:** questionnaire
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cirugia Geral

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | FECHA DE INGRESO |
| Q02 | time |  |  | SI | HORA |
| Q03 | varchar |  |  | SI | INFORMACIÓN ENTREGADA POR |
| Q04 | varchar |  |  | SI | PROCEDENCIA |
| Q05 | varchar |  |  | SI | PROCEDENCIA |
| Q06 | varchar |  |  | SI | ANAMNESIS PRÓXIMA |
| Q07 | varchar |  |  | SI | FACTORES DE RIESGO  |
| Q08 | varchar |  |  | SI | GRADO DE ACTIVIDAD |
| Q09 | varchar |  |  | SI | LUGAR DE CONSULTA FRECUENTE |
| Q10 | varchar |  |  | SI | DIETA Y NUTRICIÓN |
| Q11 | varchar |  |  | SI | PÉRDIDA RECIENTE DE PESO |
| Q12 | varchar |  |  | SI | MEDICAMIENTOS DE USO REGULAR |
| Q13 | varchar |  |  | SI | CONDICIONES FAMILIARES O SOCIALES PARA EL CUIDADO |
| Q14 | varchar |  |  | SI | CHEQUEO PREOPERATORIO |
| Q15 | varchar |  |  | SI | OBSERVACIONES |
| Q16 | bit |  |  | SI | Paciente consciente, lúcido, orientado en tiempo y... |
| Q17 | bit |  |  | SI | Paciente hemodinámicamiente estable, bien hidratad... |
| Q18 | varchar |  |  | SI | ESTADO PSÏQUICO / CONCIENCIA |
| Q19 | varchar |  |  | SI | PIEL |
| Q20 | varchar |  |  | SI | RESPIRACIÓN |
| Q21 | varchar |  |  | SI | OBSERVACIONES |
| Q22 | varchar |  |  | SI | TALLA |
| Q22ObsDR | varchar |  | FK | SI | TALLA DR |
| Q23 | varchar |  |  | SI | PESO |
| Q23ObsDR | varchar |  | FK | SI | PESO DR |
| Q24 | varchar |  |  | SI | TEMPERATURA |
| Q24ObsDR | varchar |  | FK | SI | TEMPERATURA DR |
| Q25 | varchar |  |  | SI | FRECUENCIA CARDIACA |
| Q25ObsDR | varchar |  | FK | SI | FRECUENCIA CARDIACA DR |
| Q26 | varchar |  |  | SI | FRECUENCIA RESPIRATORIA |
| Q26ObsDR | varchar |  | FK | SI | FRECUENCIA RESPIRATORIA DR |
| Q27 | varchar |  |  | SI | PRESIÓN ARTERIAL SISTÓLICA |
| Q27ObsDR | varchar |  | FK | SI | PRESIÓN ARTERIAL SISTÓLICA DR |
| Q28 | varchar |  |  | SI | PRESIÓN ARTERIAL DIASTÓLICA |
| Q28ObsDR | varchar |  | FK | SI | PRESIÓN ARTERIAL DIASTÓLICA DR |
| Q29 | varchar |  |  | SI | PRESIÓN ARTERIAL MEDIA |
| Q29ObsDR | varchar |  | FK | SI | PRESIÓN ARTERIAL MEDIA DR |
| Q30 | bit |  |  | SI | Cabeza normal. Yugulares no ingurgitadas, pulso ca... |
| Q31 | varchar |  |  | SI | CABEZA Y CUELLO |
| Q32 | varchar |  |  | SI | OBSERVACIONES |
| Q33 | bit |  |  | SI | Resto del examen de cabeza y cuello realizado y si... |
| Q34 | bit |  |  | SI | Murmullo vesicular bilateral presente, sin ruidos ... |
| Q36 | varchar |  |  | SI | PERCUSIÓN |
| Q37 | varchar |  |  | SI | AUSCULTACIÓN |
| Q38 | varchar |  |  | SI | LOCALIZACIÓN DE LAS PRINCIPALES ANORMALIDADES |
| Q39 | bit |  |  | SI | Resto del examen respiratorio realizado y sin alte... |
| Q40 | bit |  |  | SI | Ritmo regular en dos tiempos, sin soplos.  |
| Q41 | varchar |  |  | SI | CARDIOVASCULAR |
| Q42 | varchar |  |  | SI | HALLAZGO(S) |
| Q43 | bit |  |  | SI | Resto del examen cardiovascular realizado y sin al... |
| Q44 | bit |  |  | SI | Abdomen blando, depresible, indoloro, sin vicerome... |
| Q45 | varchar |  |  | SI | INSPECCIÓN |
| Q46 | varchar |  |  | SI | PALPACIÓN |
| Q47 | varchar |  |  | SI | PERCUSIÓN |
| Q48 | varchar |  |  | SI | AUSCULTACIÓN |
| Q49 | varchar |  |  | SI | LOCALIZACIÓN PRINCIPAL DE LAS ALTERACIONES |
| Q50 | varchar |  |  | SI | OBSERVACIONES |
| Q51 | bit |  |  | SI | Resto de examen abdominal realizado, sin alteracio... |
| Q52 | bit |  |  | SI | Región anogenital sin alteraciones. |
| Q53 | varchar |  |  | SI | OBSERVACIONES |
| Q54 | bit |  |  | SI | Mamas normales; axilas sin masas palpables o adeno... |
| Q55 | varchar |  |  | SI | OBSERVACIONES |
| Q56 | bit |  |  | SI | Extremidades con movilidad normal, sin lesiones ni... |
| Q57 | varchar |  |  | SI | EXTREMIDADES INFERIORES |
| Q58 | varchar |  |  | SI | LATERALIDAD DE LAS ALTERACIONES |
| Q59 | varchar |  |  | SI | OBSERVACIONES |
| Q60 | bit |  |  | SI | Resto del examen de miembros realizado y sin alter... |
| Q61 | bit |  |  | SI | Marcha normal,habla normal, sin asimetrias faciale... |
| Q62 | varchar |  |  | SI | NEUROLÓGICO |
| Q63 | bit |  |  | SI | Resto del examen neurológico realizado, sin altera... |
| Q64 | varchar |  |  | SI | CONCLUSIÓN |
| Q65 | varchar |  |  | SI | PLAN |
| Q66 | varchar |  |  | SI | PLAN |
| Q67 | bigint |  |  | SI | HTML1 |
| Q67TxtOnly | bigint |  |  | SI | HTML1 Plain Text Only |
| Q68 | bigint |  |  | SI | HTML2 |
| Q68TxtOnly | bigint |  |  | SI | HTML2 Plain Text Only |
| Q69 | varchar |  |  | SI | IMAGEN |
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