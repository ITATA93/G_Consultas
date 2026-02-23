# SQLUser.ARC_OrdSetDate

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DATE_ParRef | varchar | PK |  | NO | ARC_OrdSets Parent Reference |
| DATE_AllowInPathways | varchar |  |  | SI | Allow Order Set to be Used in Existing Clinical Pa... |
| DATE_Childsub | double |  |  | NO | Childsub |
| DATE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DATE_CreatedDate | date |  |  | SI | Created Date |
| DATE_CreatedTime | time |  |  | SI | Created Time |
| DATE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DATE_DateFrom | date |  |  | NO | Date From |
| DATE_DateTo | date |  |  | SI | Date To |
| DATE_Duration | varchar |  |  | SI | Sequence Plan Duration |
| DATE_IsInUse | bit |  |  | SI | Version Is In Use |
| DATE_IsInUseDate | date |  |  | SI | Date of Version Use |
| DATE_Notes | varchar |  |  | SI | Notes for Version |
| DATE_Number | double |  |  | SI | Version Number |
| DATE_RowId | varchar |  |  | NO | - |
| DATE_Source_DR | bigint |  | FK | SI | Vendor Source |
| DATE_TimeFrom | time |  |  | SI | Time From |
| DATE_TimeTo | time |  |  | SI | Time To |
| DATE_UpdatedDate | date |  |  | SI | Updated Date |
| DATE_UpdatedTime | time |  |  | SI | Updated Time |
| DATE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DATE_Version | varchar |  |  | SI | Vendor Version ID |
| Q01 | - |  |  | SI | Se queja de malestares y dolores. |
| Q02 | - |  |  | SI | El niño o niña tiende a aislarse y estar solo(a). |
| Q03 | - |  |  | SI | Tiene poca energía/se cansa fácilmente |
| Q04 | - |  |  | SI | Le cuesta estar tranquilo(a). |
| Q05 | - |  |  | SI | Tiene malas relaciones con su profesor(a). |
| Q06 | - |  |  | SI | * Manifiesta interés por la lectura. |
| Q07 | - |  |  | SI | Es inquieto(a). |
| Q08 | - |  |  | SI | Sueña despierto(a), está en su propio mundo. |
| Q09 | - |  |  | SI | Se distrae fácilmente. |
| Q10 | - |  |  | SI | Teme a las situaciones nuevas. |
| Q11 | - |  |  | SI | Se siente triste. |
| Q12 | - |  |  | SI | Es irritable y enojón(a). |
| Q13 | - |  |  | SI | Se siente pesimista, piensa que las cosas son difí... |
| Q14 | - |  |  | SI | Le cuesta concentrarse. |
| Q15 | - |  |  | SI | Está desinteresado(a) de los amigos(as). |
| Q16 | - |  |  | SI | Pelea con otros niños(as). |
| Q17 | - |  |  | SI | Tiene malas notas. |
| Q18 | - |  |  | SI | Se siente poca cosa. |
| Q19 | - |  |  | SI | Consulta a médico y no le encuentra(n) nada. |
| Q20 | - |  |  | SI | Le cuesta quedarse dormido(a)/duerme mal. |
| Q21 | - |  |  | SI | Le cuesta separarse de usted. |
| Q22 | - |  |  | SI | El niño o la niña piensa que es malo(a). |
| Q23 | - |  |  | SI | Es arriesgado(a). |
| Q24 | - |  |  | SI | Sufre heridas frecuentemente. |
| Q25 | - |  |  | SI | Se aburre. |
| Q26 | - |  |  | SI | Actúa como si fuera más chico(a)/llora con facilid... |
| Q27 | - |  |  | SI | Ignora las órdenes. |
| Q28 | - |  |  | SI | * Expresa sus sentimientos. |
| Q29 | - |  |  | SI | * Comprende los sentimientos de los demás. |
| Q30 | - |  |  | SI | Molesta a los demás. |
| Q31 | - |  |  | SI | Culpa a los demás de sus problemas. |
| Q32 | - |  |  | SI | Toma cosas ajenas. |
| Q33 | - |  |  | SI | Es egoísta. |
| Q34 | - |  |  | SI | Toma cosas que no le pertenecen |
| Q35 | - |  |  | SI | Se rehusa a compartir |
| Q36 | - |  |  | SI | Nombre |
| Q37 | - |  |  | SI | Apellido Paterno |
| Q38 | - |  |  | SI | Apellido Materno |
| Q39 | - |  |  | SI | Fecha de Nacimiento |
| Q40 | - |  |  | SI | Resultado |
| Q41 | - |  |  | SI | Necesita ayuda con problemas de comportamiento, em... |
| Q42 | - |  |  | SI | Fecha de Aplicación |
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