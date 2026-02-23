# SQLUser.ARC_ItemProcPhase

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROCPH_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| PROCPH_Childsub | double |  |  | NO | Childsub |
| PROCPH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROCPH_CreatedDate | date |  |  | SI | Created Date |
| PROCPH_CreatedTime | time |  |  | SI | Created Time |
| PROCPH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROCPH_DateFrom | date |  |  | SI | Date From |
| PROCPH_DateTo | date |  |  | SI | Date To |
| PROCPH_ProcPhase_DR | bigint |  | FK | SI | Des Ref ProcPhase |
| PROCPH_RowId | varchar |  |  | NO | - |
| PROCPH_UpdatedDate | date |  |  | SI | Updated Date |
| PROCPH_UpdatedTime | time |  |  | SI | Updated Time |
| PROCPH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nro. de Frasco |
| Q02 | - |  |  | SI | Año |
| Q03 | - |  |  | SI | Fecha Toma de Muestra |
| Q04 | - |  |  | SI | Hora Toma de Muestra |
| Q05 | - |  |  | SI | II. BREVE APRECIACIÓN CLÍNICA |
| Q06 | - |  |  | SI | Breve Apreciación Clínica |
| Q07 | - |  |  | SI | III. OBSERVACIONES |
| Q08 | - |  |  | SI | Presencia de TEC |
| Q09 | - |  |  | SI | Rechaza Toma de Muestra |
| Q10 | - |  |  | SI | Sospecha Presencia de Drogas |
| Q11 | - |  |  | SI | Resultado Test de Droga en Saliva (-/+ sustancia d... |
| Q12 | - |  |  | SI | IV. IDENTIFICACIÓN DEL PROFESIONAL QUE TOMA LA MUE... |
| Q13 | - |  |  | SI | Nombre |
| Q14 | - |  |  | SI | V. IDENTIFICACIÓN DEL PARTE POLICIAL |
| Q15 | - |  |  | SI | Nro. Placa Func. Policial |
| Q16 | - |  |  | SI | Nro. De Parte Policial |
| Q17 | - |  |  | SI | Fecha y Hora del Suceso que motiva el Examen |
| Q18 | - |  |  | SI | Hora |
| Q19 | - |  |  | SI | Comisaría o Unidad Policial Emisora del Parte |
| Q20 | - |  |  | SI | Fiscalía o Tribunal receptor del Parte |
| Q21 | - |  |  | SI | VI. IDENTIFICACIÓN DEL MÉDICO RESPONSABLE DEL PROC... |
| Q22 | - |  |  | SI | Nombre |
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