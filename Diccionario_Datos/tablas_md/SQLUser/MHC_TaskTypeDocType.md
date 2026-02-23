# SQLUser.MHC_TaskTypeDocType

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_ParRef | bigint | PK |  | NO | MHC_TaskType Parent Reference |
| DOC_Childsub | double |  |  | NO | Childsub |
| DOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DOC_CreatedDate | date |  |  | SI | Created Date |
| DOC_CreatedTime | time |  |  | SI | Created Time |
| DOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DOC_DocType_DR | bigint |  | FK | SI | Des Ref MHCDocumentType |
| DOC_RowId | varchar |  |  | NO | - |
| DOC_UpdatedDate | date |  |  | SI | Updated Date |
| DOC_UpdatedTime | time |  |  | SI | Updated Time |
| DOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Nombre del Paciente |
| Q02 | - |  |  | SI | Apellido Paterno |
| Q03 | - |  |  | SI | Apellido Materno |
| Q04 | - |  |  | SI | Fecha de Nacimiento |
| Q05 | - |  |  | SI | Edad |
| Q06 | - |  |  | SI | Unidad |
| Q07 | - |  |  | SI | Sexo |
| Q08 | - |  |  | SI | Rut |
| Q09 | - |  |  | SI | Diagnostico |
| Q10 | - |  |  | SI | Con Antibiotico |
| Q11 | - |  |  | SI | Profilaxis |
| Q12 | - |  |  | SI | Cetirizina |
| Q13 | - |  |  | SI | Amikacina |
| Q14 | - |  |  | SI | Nitrofurantoina |
| Q15 | - |  |  | SI | cefortin (ex-cloxacilina) |
| Q16 | - |  |  | SI | Rifampicina |
| Q17 | - |  |  | SI | Ampicilina |
| Q18 | - |  |  | SI | Cefadroxilo |
| Q19 | - |  |  | SI | Gemtamicina |
| Q20 | - |  |  | SI | Penicilina |
| Q21 | - |  |  | SI | Ceftazidima |
| Q22 | - |  |  | SI | Ciprofloxacino |
| Q23 | - |  |  | SI | Sulfametropin |
| Q24 | - |  |  | SI | Tetraciclina |
| Q25 | - |  |  | SI | Cefazolina |
| Q26 | - |  |  | SI | Otros |
| Q27 | - |  |  | SI | Fecha de inicio ATB |
| Q28 | - |  |  | SI | N° dias de tratamoiento |
| Q29 | - |  |  | SI | Urocultivo |
| Q30 | - |  |  | SI | Ceprocultivo |
| Q31 | - |  |  | SI | Hemocultio(*) |
| Q32 | - |  |  | SI | Secreciones |
| Q33 | - |  |  | SI | Otras Heridas |
| Q34 | - |  |  | SI | Tejidos |
| Q35 | - |  |  | SI | Especificar |
| Q36 | - |  |  | SI | Cateter |
| Q37 | - |  |  | SI | Tincion de GRAM |
| Q38 | - |  |  | SI | Responsable de recolección |
| Q39 | - |  |  | SI | Fecha y hora toma muestra |
| Q40 | - |  |  | SI | Responsable recepción |
| Q41 | - |  |  | SI | Fecha y hora recepción |
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