# questionnaire.QCLXXPSCY

> Cuestionario Para Estudiantes PSC-Y

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cuestionario Para Estudiantes PSC-Y

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tiene malestar y dolores. |
| Q02 | varchar |  |  | SI | Te aíslas y prefieres estar solo(a). |
| Q03 | varchar |  |  | SI | Tienes poca energia / Te cansa fácilmente. |
| Q04 | varchar |  |  | SI | Te cuesta estar tranquilo(a). |
| Q05 | varchar |  |  | SI | Tienes malas relaciones con tu profesor(a). |
| Q06 | varchar |  |  | SI | * Tienes interes por la escuela. |
| Q07 | varchar |  |  | SI | Eres inquieto(a). |
| Q08 | varchar |  |  | SI | Sueñas despierto(a), estás en tu propio mundo. |
| Q09 | varchar |  |  | SI | Te distraes fácilmente. |
| Q10 | varchar |  |  | SI | Temes a las situaciones nuevas. |
| Q11 | varchar |  |  | SI | Te sientes triste. |
| Q12 | varchar |  |  | SI | Eres irritable, enojón / enojona. |
| Q13 | varchar |  |  | SI | Te sientes pesimista / Piensas que las cosas van a... |
| Q14 | varchar |  |  | SI | Te cuesta concentrarte. |
| Q15 | varchar |  |  | SI | No te interesan los amigos(a). |
| Q16 | varchar |  |  | SI | Peleas con otros(as) compañeros(as). |
| Q17 | varchar |  |  | SI | Tienes malas notas. |
| Q18 | varchar |  |  | SI | Te sientes poca cosa. |
| Q19 | varchar |  |  | SI | Vas al médico por malestares y no te encuentran na... |
| Q20 | varchar |  |  | SI | Te cuesta quedarte dormido / Duermes mal. |
| Q21 | varchar |  |  | SI | Te cuesta separarte de tus padres. |
| Q22 | varchar |  |  | SI | Sientes que eres malo(a) |
| Q23 | varchar |  |  | SI | Eres arriesgado(a). |
| Q24 | varchar |  |  | SI | Sufres heridas frecuentemente. |
| Q25 | varchar |  |  | SI | Te aburres. |
| Q26 | varchar |  |  | SI | Actuas como si fueras mas chico(a). |
| Q27 | varchar |  |  | SI | Ignoras las órdenes que te dan. |
| Q28 | varchar |  |  | SI | * Expresas tus sentimientos. |
| Q29 | varchar |  |  | SI | * Comprendes los sentimientos de los demás. |
| Q30 | varchar |  |  | SI | Molestas a los demás. |
| Q31 | varchar |  |  | SI | Culpas a los demás de tus problemas. |
| Q32 | varchar |  |  | SI | Tomas cosas ajenas. |
| Q33 | varchar |  |  | SI | Te cuesta mucho compartir. |
| Q34 | varchar |  |  | SI | Toma cosas que no le pertenecen |
| Q35 | varchar |  |  | SI | Se rehusa a compartir |
| Q36 | varchar |  |  | SI | Nombre |
| Q37 | varchar |  |  | SI | Apellido Paterno |
| Q38 | varchar |  |  | SI | Apellido Materno |
| Q39 | varchar |  |  | SI | Fecha de Nacimiento |
| Q40 | varchar |  |  | SI | Resultado |
| Q41 | varchar |  |  | SI | Necesita ayuda con problemas de comportamiento, em... |
| Q42 | varchar |  |  | SI | Responde |
| Q43 | varchar |  |  | SI | Nombre Completo Padre/Madre/Otro |
| Q44 | date |  |  | SI | Fecha de Aplicación |
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