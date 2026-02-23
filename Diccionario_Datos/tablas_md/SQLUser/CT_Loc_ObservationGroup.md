# SQLUser.CT_Loc_ObservationGroup

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBS_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| CQ17 | - |  |  | SI | (null) |
| CQ18 | - |  |  | SI | (null) |
| OBS_Childsub | double |  |  | NO | Childsub |
| OBS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OBS_CreatedDate | date |  |  | SI | Created Date |
| OBS_CreatedTime | time |  |  | SI | Created Time |
| OBS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OBS_ObsGroup_DR | bigint |  | FK | SI | Des Ref Obs Group |
| OBS_RowId | varchar |  |  | NO | - |
| OBS_UpdatedDate | date |  |  | SI | Updated Date |
| OBS_UpdatedTime | time |  |  | SI | Updated Time |
| OBS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Tipo de vivienda |
| Q10 | - |  |  | SI | ¿Cómo llega el agua para ser ocupada? |
| Q11 | - |  |  | SI | Sistema de eliminación de excretas |
| Q12 | - |  |  | SI | Sistema de disposición de basuras |
| Q13 | - |  |  | SI | Sistema eléctrico |
| Q14 | - |  |  | SI | Combustible que usa |
| Q15 | - |  |  | SI | Sistema de calefaccion |
| Q16 | - |  |  | SI | ¿Tiene animales domésticos? |
| Q17 | - |  |  | SI | Animales domésticos |
| Q18 | - |  |  | SI | Vectores |
| Q19 | - |  |  | SI | ¿Qué problemas de contaminación o deterioro del en... |
| Q2 | - |  |  | SI | Tenencia de la vivienda |
| Q20 | - |  |  | SI | Ingreso Familiar |
| Q21 | - |  |  | SI | Ingreso Per Cápita |
| Q22 | - |  |  | SI | Conexión al Cableado Eléctrico |
| Q23 | - |  |  | SI | Distancia al Paradero |
| Q24 | - |  |  | SI | Conexion Telefonica: Fijo |
| Q25 | - |  |  | SI | Celular |
| Q26 | - |  |  | SI | Tipo Trabajo del Jefe de Hogar |
| Q27 | - |  |  | SI | Comunicaciones |
| Q28 | - |  |  | SI | Número de Integrantes o Miembros de la Familia |
| Q29 | - |  |  | SI | Tipo de Establecimiento Educativo de uno o más int... |
| Q3 | - |  |  | SI | N° de Habitaciones (Total) |
| Q30 | - |  |  | SI | Matdrial de la Vivienda |
| Q31 | - |  |  | SI | Higiene General |
| Q4 | - |  |  | SI | N° de dormitorios |
| Q5 | - |  |  | SI | N° de camas |
| Q6 | - |  |  | SI | ¿Baño dentro de la casa? |
| Q7 | - |  |  | SI | ¿Cocina dentro de la casa? |
| Q8 | - |  |  | SI | Conservación de la vivienda |
| Q9 | - |  |  | SI | Fuente de origen del agua |
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