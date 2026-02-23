# SQLUser.ARC_ItemEpisodicBillingAlias

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PALIAS_ParRef | varchar | PK |  | NO | ARC_EpisodicBilling Parent Reference |
| CQ04AT2 | - |  |  | SI | (null) |
| CQ08AT3 | - |  |  | SI | (null) |
| CQ15AT3 | - |  |  | SI | (null) |
| CQ18AT2 | - |  |  | SI | (null) |
| CQ20AT3 | - |  |  | SI | (null) |
| CQ21AT3 | - |  |  | SI | (null) |
| CQ23AT2 | - |  |  | SI | (null) |
| CQ24AT2 | - |  |  | SI | (null) |
| CQ25AT2 | - |  |  | SI | (null) |
| CQ26AT2 | - |  |  | SI | (null) |
| CQ27AT3 | - |  |  | SI | (null) |
| PALIAS_Childsub | double |  |  | NO | Childsub |
| PALIAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PALIAS_CreatedDate | date |  |  | SI | Created Date |
| PALIAS_CreatedTime | time |  |  | SI | Created Time |
| PALIAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PALIAS_DateFrom | date |  |  | SI | DateFrom |
| PALIAS_DateTo | date |  |  | SI | DateTo |
| PALIAS_InsType_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| PALIAS_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides  |
| PALIAS_PayorAlias | varchar |  |  | SI | Payor Alias |
| PALIAS_RowId | varchar |  |  | NO | - |
| PALIAS_UpdatedDate | date |  |  | SI | Updated Date |
| PALIAS_UpdatedTime | time |  |  | SI | Updated Time |
| PALIAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01AT1 | - |  |  | SI | Fecha del Accidente |
| Q02AT1 | - |  |  | SI | Hora |
| Q03AT1 | - |  |  | SI | Lugar del Accidente |
| Q04AT1 | - |  |  | SI | Unidad Policial que tomo el procedimiento_old |
| Q04AT2 | - |  |  | SI | Unidad Policial que Tomó el Procedimiento |
| Q05AT1 | - |  |  | SI | Vigencia Poliza |
| Q06AT1 | - |  |  | SI | Compañia de Seguro |
| Q07AT1 | - |  |  | SI | Comuna |
| Q08AT1 | - |  |  | SI | Juzgado policía Local_OLD |
| Q08AT3 | - |  |  | SI | Juzgado Policía Local_old2 |
| Q09AT1 | - |  |  | SI | Fiscalía_old |
| Q10AT1 | - |  |  | SI | Tipo de vehiculo_old |
| Q11AT1 | - |  |  | SI | N° de Poliza |
| Q12AT1 | - |  |  | SI | Parte |
| Q13AT2 | - |  |  | SI | RUN del conductor |
| Q14AT2 | - |  |  | SI | Patente |
| Q15AT2 | - |  |  | SI | Marca/Modelo_old |
| Q15AT3 | - |  |  | SI | Marca |
| Q16AT2 | - |  |  | SI | Nombre Conductor |
| Q17AT2 | - |  |  | SI | Licencia |
| Q18AT2 | - |  |  | SI | Denunciado |
| Q19AT2 | - |  |  | SI | Municipalidad que entrega el permiso_old |
| Q20AT2 | - |  |  | SI | Tipo de Accidente_old |
| Q20AT3 | - |  |  | SI | Tipo de Accidente |
| Q21AT2 | - |  |  | SI | Servicio de Salud |
| Q21AT3 | - |  |  | SI | ¿Conductor es menor de edad? |
| Q22AT2 | - |  |  | SI | Municipalidad que Entregó Permiso de Circulación |
| Q22AT3 | - |  |  | SI | RUN del Responsable |
| Q23AT2 | - |  |  | SI | Tipo de Vehículo |
| Q23AT3 | - |  |  | SI | Nombre del reponsable |
| Q24AT2 | - |  |  | SI | Fiscalia_old1 |
| Q24AT3 | - |  |  | SI | Dirección del responsable |
| Q25AT2 | - |  |  | SI | Fiscalía |
| Q25AT3 | - |  |  | SI | Teléfono del responsable |
| Q26AT2 | - |  |  | SI | Juzgado Policía Local |
| Q27AT3 | - |  |  | SI | Modelo |
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