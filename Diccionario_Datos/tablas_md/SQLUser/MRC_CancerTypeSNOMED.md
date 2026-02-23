# SQLUser.MRC_CancerTypeSNOMED

**Schema:** SQLUser
**Columnas:** 152
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSNOMED_ParRef | bigint | PK |  | NO | Parent Reference |
| CTSNOMED_Childsub | double |  |  | NO | Childsub |
| CTSNOMED_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| CTSNOMED_CreatedDate | date |  |  | SI | Created Date |
| CTSNOMED_CreatedTime | time |  |  | SI | Created Time |
| CTSNOMED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTSNOMED_DateFrom | date |  |  | SI | Date From |
| CTSNOMED_DateTo | date |  |  | SI | Date To |
| CTSNOMED_RowId | varchar |  |  | NO | - |
| CTSNOMED_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| CTSNOMED_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| CTSNOMED_UpdatedDate | date |  |  | SI | Updated Date |
| CTSNOMED_UpdatedTime | time |  |  | SI | Updated Time |
| CTSNOMED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q107 | - |  |  | SI | Tronco |
| Q108 | - |  |  | SI | Tronco Flexión Activo |
| Q109 | - |  |  | SI | Tronco Flexión Pasivo |
| Q110 | - |  |  | SI | Extensión tronco activo |
| Q111 | - |  |  | SI | Extensión tronco pasivo |
| Q112 | - |  |  | SI | Flex lateral  tronco izquierda activo |
| Q113 | - |  |  | SI | Flex lateral tronco izquierda pasivo |
| Q114 | - |  |  | SI | Flex lateral tronco derecho activo |
| Q115 | - |  |  | SI | Flex lateral tronco derecho pasivo |
| Q116 | - |  |  | SI | Rotación tronco izquierdo activo |
| Q117 | - |  |  | SI | Rotación tronco izquierdo pasivo |
| Q118 | - |  |  | SI | Rotación tronco derecho activo |
| Q119 | - |  |  | SI | Rotación tronco derecho pasivo |
| Q120 | - |  |  | SI | Observaciones |
| Q230 | - |  |  | SI | eva tronco flexion |
| Q231 | - |  |  | SI | eva tronco extension |
| Q232 | - |  |  | SI | eva tronco flexion lateral izquierda |
| Q233 | - |  |  | SI | eva tronco flexion lateral derecha |
| Q234 | - |  |  | SI | eva tronco rotacion izquierda |
| Q235 | - |  |  | SI | eva tronco rotacion derecha |
| Q287 | - |  |  | SI | eva tobillo eversión derecha pasivo |
| Q288 | - |  |  | SI | Tronco Flexión Izquierda Pasivo |
| Q289 | - |  |  | SI | Tronco Flexión Izquierda Activo |
| Q290 | - |  |  | SI | eva tronco flex. lateral izquierdo pasivo |
| Q291 | - |  |  | SI | eva tronco flexión derecha pasivo |
| Q292 | - |  |  | SI | eva tronco flex. lateral derecha pasivo |
| Q293 | - |  |  | SI | eva tronco extensión derecha pasivo |
| Q294 | - |  |  | SI | eva tronco rotación izquierda pasivo |
| Q295 | - |  |  | SI | eva tronco rotación derecha pasivo |
| Q296 | - |  |  | SI | Cuello Flexión Derecha Activo |
| Q297 | - |  |  | SI | Cuello Flexión Derecha Pasivo |
| Q298 | - |  |  | SI | Cuello Flexión Izquierda Activo |
| Q299 | - |  |  | SI | Cuello Flexión Izquierda Pasivo |
| Q300 | - |  |  | SI | Cuello Extensión Derecha Activo |
| Q301 | - |  |  | SI | Cuello Extensión Derecha Pasivo |
| Q302 | - |  |  | SI | Cuello Extensión Izquierda Activo |
| Q303 | - |  |  | SI | Cuello Extensión Izquierda Pasivo |
| Q304 | - |  |  | SI | Cuello Flexión Lateral Derecha Activo |
| Q305 | - |  |  | SI | Cuello Flexión Lateral Derecha Pasivo |
| Q306 | - |  |  | SI | Cuello Flexión Lateral Izquierda Activo |
| Q307 | - |  |  | SI | Cuello Flexión Lateral Izquierda Pasivo |
| Q308 | - |  |  | SI | Cuello Rotación Derecha Activo |
| Q309 | - |  |  | SI | Cuello Rotación Derecha Pasivo |
| Q310 | - |  |  | SI | Cuello Rotación Izquierda Activo |
| Q311 | - |  |  | SI | Cuello Rotación Izquierda Pasivo |
| Q312 | - |  |  | SI | Cuello Flexión Fuerza Izquierda |
| Q313 | - |  |  | SI | Cuello Flexión Fuerza Derecha |
| Q314 | - |  |  | SI | Cuello Extensión Fuerza Izquierdo |
| Q315 | - |  |  | SI | Cuello Extensión Fuerza Derecha |
| Q316 | - |  |  | SI | Cuello Flexión Lateral Fuerza Izquierda |
| Q317 | - |  |  | SI | Cuello Flexión Lateral Fuerza Derecha |
| Q318 | - |  |  | SI | Cuello Rotación Fuerza Izquierda |
| Q319 | - |  |  | SI | Cuello Rotación Fuerza Derecha |
| Q320 | - |  |  | SI | Cuello Flexión Eva Izquierda Activo |
| Q321 | - |  |  | SI | Cuello Flexión Eva Izquierdo Pasivo |
| Q322 | - |  |  | SI | Cuello Flexión Eva Derecho Activo |
| Q323 | - |  |  | SI | Cuello Flexión Eva Derecho Pasivo |
| Q324 | - |  |  | SI | Cuello Extensión Eva Izquierdo Activo |
| Q325 | - |  |  | SI | Cuello Extensión Eva Izquierdo Pasivo |
| Q326 | - |  |  | SI | Cuello Extensión Eva Derecho Activo |
| Q327 | - |  |  | SI | Cuello Extensión Eva Derecho Pasivo |
| Q328 | - |  |  | SI | Cuello Flexión Lateral Eva Izquierdo Activo |
| Q329 | - |  |  | SI | Cuello Flexión Lateral Eva Izquierdo Pasivo |
| Q330 | - |  |  | SI | Cuello Flexión Lateral Eva Derecho Activo |
| Q331 | - |  |  | SI | Cuello Flexión Lateral Eva Derecho Pasivo |
| Q332 | - |  |  | SI | Cuello Rotación Eva Izquierdo Activo |
| Q333 | - |  |  | SI | Cuello Rotación Eva Izquierdo Pasivo |
| Q334 | - |  |  | SI | Cuello Rotación Eva Derecho Activo |
| Q335 | - |  |  | SI | Cuello Rotación Eva Derecho Pasivo |
| Q70 | - |  |  | SI | Tronco flexión izquierdo activo |
| Q71 | - |  |  | SI | Tronco Rotación izquierda activo |
| Q72 | - |  |  | SI | tronco rotación izquierda pasivo |
| Q73 | - |  |  | SI | Tronco Flexión Derecho Activo |
| Q74 | - |  |  | SI | Tronco flexión derecho pasivo |
| Q75 | - |  |  | SI | tronco extensión derecho activo |
| Q76 | - |  |  | SI | tronco extensión derecho pasivo |
| Q77 | - |  |  | SI | tronco rotación derecho activo |
| Q78 | - |  |  | SI | tronco rotación derecho pasivo |
| Q79 | - |  |  | SI | Rotación |
| Q80 | - |  |  | SI | Flexión |
| Q81 | - |  |  | SI | Flexión Lateral |
| Q82 | - |  |  | SI | Rotación |
| Q83 | - |  |  | SI | Cuello |
| Q84 | - |  |  | SI | Flexión |
| Q85 | - |  |  | SI | Extensión |
| Q86 | - |  |  | SI | Flexión Lateral |
| Q87 | - |  |  | SI | Rotación |
| Q88 | - |  |  | SI | Extensión |
| Q89 | - |  |  | SI | Tronco Flexión Fuerza Izquierda |
| Q90 | - |  |  | SI | Tronco flexión fuerza derecho |
| Q91 | - |  |  | SI | Tronco extensión fuerza izquierda |
| Q92 | - |  |  | SI | Tronco extensión fuerza derecho |
| Q93 | - |  |  | SI | Tronco fle. Lateral fuerza izquierdo |
| Q94 | - |  |  | SI | Tronco fle lateral fuerza derecho |
| Q95 | - |  |  | SI | Tronco rotacion fuerza izquierda |
| Q96 | - |  |  | SI | Tronco rotación fuerza derecho |
| Q97 | - |  |  | SI | Tronco extensión eva derecho activo |
| Q98 | - |  |  | SI | Tronco extensión eva derecho pasivo |
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