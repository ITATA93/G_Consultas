# SQLUser.LBDRDFTH_Cell

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRDFTHC_ParRef | varchar | PK |  | NO | The (Header) row containing this cell |
| LBCDFTHC_LBCTI_DR | bigint |  | FK | SI | Column TestItem
LBCTIDR for column, if Type="TI" |
| LBDRDFTHC_CellNo | double |  |  | SI | The cell number within the row (needed because rel... |
| LBDRDFTHC_ColSpan | integer |  |  | SI | The number of columns that the value spans ( 2 0r ... |
| LBDRDFTHC_LBCTICode | varchar |  |  | SI | The TestItem Code for the column (for debugging) |
| LBDRDFTHC_RowID | varchar |  |  | NO | - |
| LBDRDFTHC_Type | varchar |  |  | SI | Column Type
See StandardType LabDFTColumnType |
| LBDRDFTHC_Value | varchar |  |  | SI | The text to appear in this cell of the header |
| LBDRDFTHC_Width | integer |  |  | SI | The cell width in characters, not including the "|... |
| Q01 | - |  |  | SI | Autonomo |
| Q02 | - |  |  | SI | Total |
| Q03 | - |  |  | SI | Parcial |
| Q04 | - |  |  | SI | Requiere uso de dispositivo |
| Q05 | - |  |  | SI | Detalle |
| Q06 | - |  |  | SI | Requiere ayuda de otra persona, supervision o ense... |
| Q07 | - |  |  | SI | Requiere ayuda de otra persona y dispositivo |
| Q08 | - |  |  | SI | Dependiente, no participa en la actividad |
| Q09 | - |  |  | SI | Deambulacion |
| Q10 | - |  |  | SI | Sedestacion |
| Q11 | - |  |  | SI | Movilidad cama |
| Q12 | - |  |  | SI | Limitacion a la movilizacion |
| Q13 | - |  |  | SI | Intolerancia a la actividad fisica |
| Q14 | - |  |  | SI | Detalle |
| Q15 | - |  |  | SI | Ejercicio fisico habitual |
| Q16 | - |  |  | SI | Adecuado para la edad |
| Q17 | - |  |  | SI | Especifique |
| Q18 | - |  |  | SI | Diagnostico 1 |
| Q19 | - |  |  | SI | Diagnostico 2 |
| Q20 | - |  |  | SI | Conclusion |
| Q21 | - |  |  | SI | Objetivo Registro |
| Q22 | - |  |  | SI | Actividad Física |
| Q23 | - |  |  | SI | Movilidad |
| Q24 | - |  |  | SI | Tipo de Asistencia |
| Q25 | - |  |  | SI | Detalle Requier Uso Dispositivo |
| Q26 | - |  |  | SI | Detalle Requiere ayuda de otra persona y dispositi... |
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