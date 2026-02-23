# SQLUser.LBC_ProcedureStockItem

**Schema:** SQLUser
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPRSI_ParRef | bigint | PK |  | NO | Parent Procedure |
| LBCPRSI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPRSI_CreatedDate | date |  |  | SI | Created Date |
| LBCPRSI_CreatedTime | time |  |  | SI | Created Time |
| LBCPRSI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPRSI_DateFrom | date |  |  | SI | Effective date for the record |
| LBCPRSI_DateTo | date |  |  | SI | Last day the record is active  |
| LBCPRSI_Quantity | numeric |  |  | SI | Quantity in % |
| LBCPRSI_RowID | varchar |  |  | NO | - |
| LBCPRSI_StockCategory_DR | bigint |  | FK | SI | Stock Category |
| LBCPRSI_StockItem_DR | bigint |  | FK | SI | Stock Item |
| LBCPRSI_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPRSI_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPRSI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | FC Basal |
| Q02 | - |  |  | SI | FC Final |
| Q03 | - |  |  | SI | FC 5 Min. |
| Q04 | - |  |  | SI | FC 10 Min. |
| Q05 | - |  |  | SI | FR Basal |
| Q06 | - |  |  | SI | FR Final |
| Q07 | - |  |  | SI | FR 5 Min. |
| Q08 | - |  |  | SI | FR 10 Min. |
| Q09 | - |  |  | SI | PA Sistólica Basal |
| Q10 | - |  |  | SI | PA Sistólica Final |
| Q11 | - |  |  | SI | PA Sistólica 5 Min |
| Q12 | - |  |  | SI | PA Sistólica 10 Min. |
| Q13 | - |  |  | SI | SAT Basal |
| Q14 | - |  |  | SI | SAT Final |
| Q15 | - |  |  | SI | SAT 5 Min. |
| Q16 | - |  |  | SI | SAT 10 Min. |
| Q17 | - |  |  | SI | BORG Fatiga Basal |
| Q18 | - |  |  | SI | BORG Fatiga Final |
| Q19 | - |  |  | SI | BORG Fatiga 5 Min. |
| Q20 | - |  |  | SI | BORG Fatiga 10 Min. |
| Q21 | - |  |  | SI | Longitud del Trazo (Mts.) |
| Q22 | - |  |  | SI | N° de Vueltas |
| Q23 | - |  |  | SI | Distancia Recorrida |
| Q24 | - |  |  | SI | Metros Teóricos Hombres (Mts.) |
| Q25 | - |  |  | SI | % del Valor Teórico Hombres |
| Q26 | - |  |  | SI | Detenciones |
| Q27 | - |  |  | SI | Completa Test |
| Q28 | - |  |  | SI | Causa Detenciones |
| Q29 | - |  |  | SI | Causa Completa Test |
| Q30 | - |  |  | SI | Observaciones |
| Q31 | - |  |  | SI | Conclusión |
| Q32 | - |  |  | SI | PA Diastólica Basal |
| Q33 | - |  |  | SI | PA Diastólica 5 Min |
| Q34 | - |  |  | SI | PA Diastólica 10 Min |
| Q35 | - |  |  | SI | PA Diastólica Final |
| Q36 | - |  |  | SI | Metros Teóricos Mujeres (Mts.) |
| Q37 | - |  |  | SI | % del Valor Teórico Mujeres |
| Q38 | - |  |  | SI | Sexo |
| Q39 | - |  |  | SI | Resultado Test Marcha 6 Min |
| Q39ObsDR | - |  |  | SI | Resultado Test Marcha 6 Min DR |
| Q40 | - |  |  | SI | Talla |
| Q40ObsDR | - |  |  | SI | Talla DR |
| Q41 | - |  |  | SI | Edad |
| Q42 | - |  |  | SI | Peso |
| Q42ObsDR | - |  |  | SI | Peso DR |
| Q43 | - |  |  | SI | BORG Disnea Basal |
| Q44 | - |  |  | SI | BORG Disnea Final |
| Q45 | - |  |  | SI | BORG Disnea 5 Min |
| Q46 | - |  |  | SI | BORG Disnea 10 Min |
| Q47 | - |  |  | SI | Kg |
| Q48 | - |  |  | SI | cm |
| Q49 | - |  |  | SI | años |
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