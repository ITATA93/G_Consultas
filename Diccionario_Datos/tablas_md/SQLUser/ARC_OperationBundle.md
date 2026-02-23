# SQLUser.ARC_OperationBundle

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPBDL_RowId | bigint | PK |  | NO | - |
| OPBDL_Code | varchar |  |  | NO | Code |
| OPBDL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPBDL_CreatedDate | date |  |  | SI | Created Date |
| OPBDL_CreatedTime | time |  |  | SI | Created Time |
| OPBDL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPBDL_DateFrom | date |  |  | SI | Date From |
| OPBDL_DateTo | date |  |  | SI | Date To |
| OPBDL_Desc | varchar |  |  | NO | Description |
| OPBDL_Owner | varchar |  |  | SI | Owner |
| OPBDL_UpdatedDate | date |  |  | SI | Updated Date |
| OPBDL_UpdatedTime | time |  |  | SI | Updated Time |
| OPBDL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tiene malestar y dolores. |
| Q02 | - |  |  | SI | Te aíslas y prefieres estar solo(a). |
| Q03 | - |  |  | SI | Tienes poca energia / Te cansa fácilmente. |
| Q04 | - |  |  | SI | Te cuesta estar tranquilo(a). |
| Q05 | - |  |  | SI | Tienes malas relaciones con tu profesor(a). |
| Q06 | - |  |  | SI | * Tienes interes por la escuela. |
| Q07 | - |  |  | SI | Eres inquieto(a). |
| Q08 | - |  |  | SI | Sueñas despierto(a), estás en tu propio mundo. |
| Q09 | - |  |  | SI | Te distraes fácilmente. |
| Q10 | - |  |  | SI | Temes a las situaciones nuevas. |
| Q11 | - |  |  | SI | Te sientes triste. |
| Q12 | - |  |  | SI | Eres irritable, enojón / enojona. |
| Q13 | - |  |  | SI | Te sientes pesimista / Piensas que las cosas van a... |
| Q14 | - |  |  | SI | Te cuesta concentrarte. |
| Q15 | - |  |  | SI | No te interesan los amigos(a). |
| Q16 | - |  |  | SI | Peleas con otros(as) compañeros(as). |
| Q17 | - |  |  | SI | Tienes malas notas. |
| Q18 | - |  |  | SI | Te sientes poca cosa. |
| Q19 | - |  |  | SI | Vas al médico por malestares y no te encuentran na... |
| Q20 | - |  |  | SI | Te cuesta quedarte dormido / Duermes mal. |
| Q21 | - |  |  | SI | Te cuesta separarte de tus padres. |
| Q22 | - |  |  | SI | Sientes que eres malo(a) |
| Q23 | - |  |  | SI | Eres arriesgado(a). |
| Q24 | - |  |  | SI | Sufres heridas frecuentemente. |
| Q25 | - |  |  | SI | Te aburres. |
| Q26 | - |  |  | SI | Actuas como si fueras mas chico(a). |
| Q27 | - |  |  | SI | Ignoras las órdenes que te dan. |
| Q28 | - |  |  | SI | * Expresas tus sentimientos. |
| Q29 | - |  |  | SI | * Comprendes los sentimientos de los demás. |
| Q30 | - |  |  | SI | Molestas a los demás. |
| Q31 | - |  |  | SI | Culpas a los demás de tus problemas. |
| Q32 | - |  |  | SI | Tomas cosas ajenas. |
| Q33 | - |  |  | SI | Te cuesta mucho compartir. |
| Q34 | - |  |  | SI | Toma cosas que no le pertenecen |
| Q35 | - |  |  | SI | Se rehusa a compartir |
| Q36 | - |  |  | SI | Nombre |
| Q37 | - |  |  | SI | Apellido Paterno |
| Q38 | - |  |  | SI | Apellido Materno |
| Q39 | - |  |  | SI | Fecha de Nacimiento |
| Q40 | - |  |  | SI | Resultado |
| Q41 | - |  |  | SI | Necesita ayuda con problemas de comportamiento, em... |
| Q42 | - |  |  | SI | Responde |
| Q43 | - |  |  | SI | Nombre Completo Padre/Madre/Otro |
| Q44 | - |  |  | SI | Fecha de Aplicación |
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