# SQLUser.INC_SterileCategory

**Schema:** SQLUser
**Columnas:** 129
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCAT_RowId | bigint | PK |  | NO | - |
| ChildQ35DR | - |  |  | SI | Child Reference: INSPECCIÓN |
| Q01 | - |  |  | SI | FECHA DE INGRESO |
| Q02 | - |  |  | SI | HORA |
| Q03 | - |  |  | SI | INFORMACIÓN ENTREGADA POR |
| Q04 | - |  |  | SI | PROCEDENCIA |
| Q05 | - |  |  | SI | PROCEDENCIA |
| Q06 | - |  |  | SI | ANAMNESIS PRÓXIMA |
| Q07 | - |  |  | SI | FACTORES DE RIESGO |
| Q08 | - |  |  | SI | GRADO DE ACTIVIDAD |
| Q09 | - |  |  | SI | LUGAR DE CONSULTA FRECUENTE |
| Q10 | - |  |  | SI | DIETA Y NUTRICIÓN |
| Q11 | - |  |  | SI | PÉRDIDA RECIENTE DE PESO |
| Q12 | - |  |  | SI | MEDICAMIENTOS DE USO REGULAR |
| Q13 | - |  |  | SI | CONDICIONES FAMILIARES O SOCIALES PARA EL CUIDADO |
| Q14 | - |  |  | SI | CHEQUEO PREOPERATORIO |
| Q15 | - |  |  | SI | OBSERVACIONES |
| Q16 | - |  |  | SI | Paciente consciente, lúcido, orientado en tiempo y... |
| Q17 | - |  |  | SI | Paciente hemodinámicamiente estable, bien hidratad... |
| Q18 | - |  |  | SI | ESTADO PSÏQUICO / CONCIENCIA |
| Q19 | - |  |  | SI | PIEL |
| Q20 | - |  |  | SI | RESPIRACIÓN |
| Q21 | - |  |  | SI | OBSERVACIONES |
| Q22 | - |  |  | SI | TALLA |
| Q22ObsDR | - |  |  | SI | TALLA DR |
| Q23 | - |  |  | SI | PESO |
| Q23ObsDR | - |  |  | SI | PESO DR |
| Q24 | - |  |  | SI | TEMPERATURA |
| Q24ObsDR | - |  |  | SI | TEMPERATURA DR |
| Q25 | - |  |  | SI | FRECUENCIA CARDIACA |
| Q25ObsDR | - |  |  | SI | FRECUENCIA CARDIACA DR |
| Q26 | - |  |  | SI | FRECUENCIA RESPIRATORIA |
| Q26ObsDR | - |  |  | SI | FRECUENCIA RESPIRATORIA DR |
| Q27 | - |  |  | SI | PRESIÓN ARTERIAL SISTÓLICA |
| Q27ObsDR | - |  |  | SI | PRESIÓN ARTERIAL SISTÓLICA DR |
| Q28 | - |  |  | SI | PRESIÓN ARTERIAL DIASTÓLICA |
| Q28ObsDR | - |  |  | SI | PRESIÓN ARTERIAL DIASTÓLICA DR |
| Q29 | - |  |  | SI | PRESIÓN ARTERIAL MEDIA |
| Q29ObsDR | - |  |  | SI | PRESIÓN ARTERIAL MEDIA DR |
| Q30 | - |  |  | SI | Cabeza normal. Yugulares no ingurgitadas, pulso ca... |
| Q31 | - |  |  | SI | CABEZA Y CUELLO |
| Q32 | - |  |  | SI | OBSERVACIONES |
| Q33 | - |  |  | SI | Resto del examen de cabeza y cuello realizado y si... |
| Q34 | - |  |  | SI | Murmullo vesicular bilateral presente, sin ruidos ... |
| Q36 | - |  |  | SI | PERCUSIÓN |
| Q37 | - |  |  | SI | AUSCULTACIÓN |
| Q38 | - |  |  | SI | LOCALIZACIÓN DE LAS PRINCIPALES ANORMALIDADES |
| Q39 | - |  |  | SI | Resto del examen respiratorio realizado y sin alte... |
| Q40 | - |  |  | SI | Ritmo regular en dos tiempos, sin soplos. |
| Q41 | - |  |  | SI | CARDIOVASCULAR |
| Q42 | - |  |  | SI | HALLAZGO(S) |
| Q43 | - |  |  | SI | Resto del examen cardiovascular realizado y sin al... |
| Q44 | - |  |  | SI | Abdomen blando, depresible, indoloro, sin vicerome... |
| Q45 | - |  |  | SI | INSPECCIÓN |
| Q46 | - |  |  | SI | PALPACIÓN |
| Q47 | - |  |  | SI | PERCUSIÓN |
| Q48 | - |  |  | SI | AUSCULTACIÓN |
| Q49 | - |  |  | SI | LOCALIZACIÓN PRINCIPAL DE LAS ALTERACIONES |
| Q50 | - |  |  | SI | OBSERVACIONES |
| Q51 | - |  |  | SI | Resto de examen abdominal realizado, sin alteracio... |
| Q52 | - |  |  | SI | Región anogenital sin alteraciones. |
| Q53 | - |  |  | SI | OBSERVACIONES |
| Q54 | - |  |  | SI | Mamas normales |
| Q55 | - |  |  | SI | OBSERVACIONES |
| Q56 | - |  |  | SI | Extremidades con movilidad normal, sin lesiones ni... |
| Q57 | - |  |  | SI | EXTREMIDADES INFERIORES |
| Q58 | - |  |  | SI | LATERALIDAD DE LAS ALTERACIONES |
| Q59 | - |  |  | SI | OBSERVACIONES |
| Q60 | - |  |  | SI | Resto del examen de miembros realizado y sin alter... |
| Q61 | - |  |  | SI | Marcha normal,habla normal, sin asimetrias faciale... |
| Q62 | - |  |  | SI | NEUROLÓGICO |
| Q63 | - |  |  | SI | Resto del examen neurológico realizado, sin altera... |
| Q64 | - |  |  | SI | CONCLUSIÓN |
| Q65 | - |  |  | SI | PLAN |
| Q66 | - |  |  | SI | PLAN |
| Q67 | - |  |  | SI | HTML1 |
| Q67TxtOnly | - |  |  | SI | HTML1 Plain Text Only |
| Q68 | - |  |  | SI | HTML2 |
| Q68TxtOnly | - |  |  | SI | HTML2 Plain Text Only |
| Q69 | - |  |  | SI | IMAGEN |
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
| SCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SCAT_CreatedDate | date |  |  | SI | Created Date |
| SCAT_CreatedTime | time |  |  | SI | Created Time |
| SCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SCAT_Desc | varchar |  |  | NO | Description |
| SCAT_Owner | varchar |  |  | SI | Owner |
| SCAT_UpdatedDate | date |  |  | SI | Updated Date |
| SCAT_UpdatedTime | time |  |  | SI | Updated Time |
| SCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*