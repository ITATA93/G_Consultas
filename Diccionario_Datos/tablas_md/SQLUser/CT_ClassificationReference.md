# SQLUser.CT_ClassificationReference

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCR_RowID | bigint | PK |  | NO | - |
| CTCR_ClassificationSystem_DR | bigint |  | FK | NO | Clasification System |
| CTCR_Code | varchar |  |  | SI | Code |
| CTCR_Comment | varchar |  |  | SI | Comment |
| CTCR_Desc | varchar |  |  | SI | Description |
| CTCR_ICD_DR | bigint |  | FK | SI | ICD Reference |
| CTCR_LOINC_DR | bigint |  | FK | SI | LOINC Reference |
| CTCR_ObjectReference | varchar |  |  | SI | - |
| CTCR_SNOMED_DR | bigint |  | FK | SI | SNOMED Reference |
| Q01 | - |  |  | SI | Toser |
| Q02 | - |  |  | SI | Mucosidad |
| Q03 | - |  |  | SI | Dolor Opresivo |
| Q04 | - |  |  | SI | Limitación Acividad Fisica |
| Q05 | - |  |  | SI | Limitación Actividad Doméstica |
| Q06 | - |  |  | SI | Sensación de Seguridad |
| Q07 | - |  |  | SI | Problemas para Dormir |
| Q08 | - |  |  | SI | Energía |
| Q09 | - |  |  | SI | Resultado CAT |
| Q09ObsDR | - |  |  | SI | Resultado CAT DR |
| Q10 | - |  |  | SI | Nunca Toso |
| Q11 | - |  |  | SI | No tengo flema (mucosidad) en el pecho |
| Q12 | - |  |  | SI | No siento ninguna opresión en el pecho |
| Q13 | - |  |  | SI | Cuando subo una pendiente o un tramo de escaleras,... |
| Q14 | - |  |  | SI | No me siento limitado para realizar actividades do... |
| Q15 | - |  |  | SI | Me siento seguro al salir de casa a pesar de la af... |
| Q16 | - |  |  | SI | Duermo sin problemas |
| Q17 | - |  |  | SI | Tengo mucha energía |
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