# SQLUser.AR_HICClaimRepSubRow

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRSR_ParRef | varchar | PK |  | NO | - |
| CRSR_ElementName | varchar |  |  | NO | Name of the element |
| CRSR_ElementValue | varchar |  |  | SI | Value of the element |
| CRSR_RowID | varchar |  |  | NO | - |
| CRSR_SubRowNumber | integer |  |  | NO | Sub-row number |
| Q01 | - |  |  | SI | Situacion Previa al Ingreso |
| Q02 | - |  |  | SI | Antecedentes Relevantes |
| Q03 | - |  |  | SI | Situación Socio Familiar |
| Q04 | - |  |  | SI | Dinámica Familiar |
| Q05 | - |  |  | SI | Situaciones de Crisis |
| Q06 | - |  |  | SI | Otras Situaciones |
| Q07 | - |  |  | SI | Área Socio-Emocional |
| Q08 | - |  |  | SI | Relaciones de Amistad |
| Q09 | - |  |  | SI | Relaciones Amorosas |
| Q10 | - |  |  | SI | Identidad Personal |
| Q11 | - |  |  | SI | Construcción identitaria en torno a la infracción ... |
| Q12 | - |  |  | SI | Otros Socio-Emocional |
| Q13 | - |  |  | SI | Eje Motivacional al Ingreso (drogodependencia) |
| Q14 | - |  |  | SI | Significación de proceso de hospitalización y expe... |
| Q15 | - |  |  | SI | Expectativas de Egreso (drogodependecia) |
| Q16 | - |  |  | SI | Fecha de Ingreso |
| Q17 | - |  |  | SI | Hora de Ingreso |
| Q18 | - |  |  | SI | Profesional Responsable |
| Q19 | - |  |  | SI | Autoestima |
| Q20 | - |  |  | SI | Hipótesis Diagnostica |
| Q21 | - |  |  | SI | Plan de Tratamiento |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*