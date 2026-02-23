# questionnaire.QCLXXPSC

> Cuestionario Para Padres PSC

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cuestionario Para Padres PSC

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Se queja de malestares y dolores. |
| Q02 | varchar |  |  | SI | El niño o niña tiende a aislarse y estar solo(a).  |
| Q03 | varchar |  |  | SI | Tiene poca energía/se cansa fácilmente |
| Q04 | varchar |  |  | SI | Le cuesta estar tranquilo(a). |
| Q05 | varchar |  |  | SI | Tiene malas relaciones con su profesor(a). |
| Q06 | varchar |  |  | SI | * Manifiesta interés por la lectura. |
| Q07 | varchar |  |  | SI | Es inquieto(a). |
| Q08 | varchar |  |  | SI | Sueña despierto(a), está en su propio mundo. |
| Q09 | varchar |  |  | SI | Se distrae fácilmente. |
| Q10 | varchar |  |  | SI | Teme a las situaciones nuevas. |
| Q11 | varchar |  |  | SI | Se siente triste. |
| Q12 | varchar |  |  | SI | Es irritable y enojón(a). |
| Q13 | varchar |  |  | SI | Se siente pesimista, piensa que las cosas son difí... |
| Q14 | varchar |  |  | SI | Le cuesta concentrarse. |
| Q15 | varchar |  |  | SI | Está desinteresado(a) de los amigos(as). |
| Q16 | varchar |  |  | SI | Pelea con otros niños(as). |
| Q17 | varchar |  |  | SI | Tiene malas notas. |
| Q18 | varchar |  |  | SI | Se siente poca cosa. |
| Q19 | varchar |  |  | SI | Consulta a médico y no le encuentra(n) nada. |
| Q20 | varchar |  |  | SI | Le cuesta quedarse dormido(a)/duerme mal. |
| Q21 | varchar |  |  | SI | Le cuesta separarse de usted. |
| Q22 | varchar |  |  | SI | El niño o la niña piensa que es malo(a). |
| Q23 | varchar |  |  | SI | Es arriesgado(a). |
| Q24 | varchar |  |  | SI | Sufre heridas frecuentemente.  |
| Q25 | varchar |  |  | SI | Se aburre. |
| Q26 | varchar |  |  | SI | Actúa como si fuera más chico(a)/llora con facilid... |
| Q27 | varchar |  |  | SI | Ignora las órdenes. |
| Q28 | varchar |  |  | SI | * Expresa sus sentimientos. |
| Q29 | varchar |  |  | SI | * Comprende los sentimientos de los demás. |
| Q30 | varchar |  |  | SI | Molesta a los demás. |
| Q31 | varchar |  |  | SI | Culpa a los demás de sus problemas.  |
| Q32 | varchar |  |  | SI | Toma cosas ajenas. |
| Q33 | varchar |  |  | SI | Es egoísta. |
| Q34 | varchar |  |  | SI | Toma cosas que no le pertenecen |
| Q35 | varchar |  |  | SI | Se rehusa a compartir |
| Q36 | varchar |  |  | SI | Nombre |
| Q37 | varchar |  |  | SI | Apellido Paterno |
| Q38 | varchar |  |  | SI | Apellido Materno |
| Q39 | varchar |  |  | SI | Fecha de Nacimiento |
| Q40 | varchar |  |  | SI | Resultado |
| Q41 | varchar |  |  | SI | Necesita ayuda con problemas de comportamiento, em... |
| Q42 | date |  |  | SI | Fecha de Aplicación |
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