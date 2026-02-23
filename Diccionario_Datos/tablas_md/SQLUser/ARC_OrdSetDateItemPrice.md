# SQLUser.ARC_OrdSetDateItemPrice

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRICE_ParRef | varchar | PK |  | NO | ARC_OrdSetDateItem Parent Reference |
| ChildQ15DR | - |  |  | SI | Child Reference: Equipamiento |
| PRICE_Childsub | double |  |  | NO | Childsub |
| PRICE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRICE_CreatedDate | date |  |  | SI | Created Date |
| PRICE_CreatedTime | time |  |  | SI | Created Time |
| PRICE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRICE_DateFrom | date |  |  | SI | Date From |
| PRICE_DateTo | date |  |  | SI | Date To |
| PRICE_EpisodeType | varchar |  |  | SI | Episode Type |
| PRICE_Hodpital_DR | bigint |  | FK | SI | Hospital DR |
| PRICE_Price | double |  |  | SI | Price |
| PRICE_RowId | varchar |  |  | NO | - |
| PRICE_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| PRICE_UpdatedDate | date |  |  | SI | Updated Date |
| PRICE_UpdatedTime | time |  |  | SI | Updated Time |
| PRICE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Equipo |
| Q02 | - |  |  | SI | Parámetros Antropométricos |
| Q03 | - |  |  | SI | Peso y Talla |
| Q04 | - |  |  | SI | Antecedentes Farmacológicos |
| Q05 | - |  |  | SI | Paciente actualmente bajo tratamiento: |
| Q06 | - |  |  | SI | Antiagregante |
| Q07 | - |  |  | SI | Anticoagulante |
| Q08 | - |  |  | SI | Requerimientos para la realización del acto quirúr... |
| Q10 | - |  |  | SI | Talla |
| Q11 | - |  |  | SI | Peso |
| Q12 | - |  |  | SI | IMC_old |
| Q13 | - |  |  | SI | Antecedentes Farmacológicos |
| Q14 | - |  |  | SI | Requerimientos para la realización del acto quirúr... |
| Q16 | - |  |  | SI | Tipo de cama |
| Q17 | - |  |  | SI | Insumos de Especialidad |
| Q18 | - |  |  | SI | Instrumental Externo |
| Q19 | - |  |  | SI | Instrumental Quirúrgico Especial |
| Q20 | - |  |  | SI | Apoyo de Imagenología |
| Q21 | - |  |  | SI | Hemorreserva |
| Q22 | - |  |  | SI | IMC |
| Q23 | - |  |  | SI | Modalidad |
| Q25 | - |  |  | SI | Cirugías Adicionales |
| Q27 | - |  |  | SI | Convenio |
| Q28 | - |  |  | SI | Requiere Hemocomponentes |
| Q29 | - |  |  | SI | Cantidad |
| Q30 | - |  |  | SI | Comentarios&nbsp |
| Q31 | - |  |  | SI | Precauciones adicionales |
| Q32 | - |  |  | SI | Preparación Especial |
| Q33 | - |  |  | SI | Alergias |
| Q34 | - |  |  | SI | Comentarios Alergias |
| Q35 | - |  |  | SI | Complejidad |
| Q36 | - |  |  | SI | Equipamiento |
| Q37 | - |  |  | SI | Observaciones Generales |
| Q38 | - |  |  | SI | Proveedor |
| Q39 | - |  |  | SI | Cirugías Adicionales |
| Q40 | - |  |  | SI | Información Complementaria |
| Q41 | - |  |  | SI | Estadía Hospitalaria |
| Q42 | - |  |  | SI | Observaciones |
| Q43 | - |  |  | SI | Implantes/Insumos |
| Q44 | - |  |  | SI | Instrumental |
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