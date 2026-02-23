# SQLUser.AR_CareProvPropOverride

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPPROPOV_RowId | bigint | PK |  | NO | - |
| CPPROPOV_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| CPPROPOV_PropAmount | double |  |  | SI | Proportion Amount |
| CPPROPOV_Reason | varchar |  |  | SI | Reason |
| CPPROPOV_UpdateDate | date |  |  | SI | UpdateDate |
| CPPROPOV_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| CPPROPOV_UpdateTime | time |  |  | SI | UpdateTime |
| CPPROPOV_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| ChildQ19DR | - |  |  | SI | Child Reference: 7. Evidencia recogida |
| Q01 | - |  |  | SI | N° |
| Q02 | - |  |  | SI | Fecha |
| Q03 | - |  |  | SI | Hora |
| Q04 | - |  |  | SI | Nombre Completo del Examinado |
| Q05 | - |  |  | SI | Apellido Paterno |
| Q06 | - |  |  | SI | Apellido Materno |
| Q07 | - |  |  | SI | RUT |
| Q08 | - |  |  | SI | Sexo |
| Q09 | - |  |  | SI | 1. Diagnóstico clínico de las lesiones y breve des... |
| Q10 | - |  |  | SI | 2. Método de Diagnóstico |
| Q11 | - |  |  | SI | 3. Describir brevemente origen de la lesión |
| Q12 | - |  |  | SI | Según relato lesionado |
| Q13 | - |  |  | SI | Según apreciación clínica |
| Q14 | - |  |  | SI | 4. Lesiones que ocasionarán al lesionado enfermeda... |
| Q15 | - |  |  | SI | días |
| Q16 | - |  |  | SI | 5. Diagnóstico médico legal de las lesiones |
| Q17 | - |  |  | SI | 6. Identificación persona que acompaña al lesionad... |
| Q18 | - |  |  | SI | Acompañado |
| Q20 | - |  |  | SI | Médico |
| Q21 | - |  |  | SI | Nombre Completo |
| Q22 | - |  |  | SI | RUT |
| Q23 | - |  |  | SI | Centro Asistencial |
| Q24 | - |  |  | SI | DAU N° |
| Q25 | - |  |  | SI | Edad |
| Q26 | - |  |  | SI | Parentesco |
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