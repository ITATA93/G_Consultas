# SQLUser.LBDRDFT_Cell

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRDFTC_ParRef | varchar | PK |  | NO | The row containing this cell |
| LBCDFTC_LBCTI_DR | bigint |  | FK | SI | Column TestItem
LBCTIDR for column, if Type="TI" |
| LBDRDFTC_CellNo | double |  |  | SI | The cell number within the row (needed because rel... |
| LBDRDFTC_Flag | varchar |  |  | SI | Flag to be printed.  "(H)" or "(L)" or "(A") (or u... |
| LBDRDFTC_LBCTICode | varchar |  |  | SI | The TestItem Code for the column (for debugging) |
| LBDRDFTC_RowID | varchar |  |  | NO | - |
| LBDRDFTC_TextResult_DR | bigint |  | FK | SI | Text result in HTML Rich Text as a websys.Document... |
| LBDRDFTC_Value | varchar |  |  | SI | The text for the cell
For a TI column this can be... |
| LBDRDFTC_Width | integer |  |  | SI | The cell width in characters, not including the "|... |
| Q01 | - |  |  | SI | Muestra de Expectoración |
| Q02 | - |  |  | SI | Sangre |
| Q03 | - |  |  | SI | Otra |
| Q04 | - |  |  | SI | Virgen a Tratamiento TBC |
| Q05 | - |  |  | SI | Antes Tratado TBC |
| Q06 | - |  |  | SI | Abandono Tratamiento TBC |
| Q07 | - |  |  | SI | Contacto TBC |
| Q08 | - |  |  | SI | Extranjero |
| Q09 | - |  |  | SI | País |
| Q10 | - |  |  | SI | Coinfección Retrovial |
| Q11 | - |  |  | SI | Población Cerrada |
| Q12 | - |  |  | SI | Hogar |
| Q13 | - |  |  | SI | Reo |
| Q14 | - |  |  | SI | Otro |
| Q15 | - |  |  | SI | Profesional de Salud |
| Q16 | - |  |  | SI | N° Meses que esta con tratamiento TBC |
| Q17 | - |  |  | SI | Imágenes Pulmonares al RX |
| Q18 | - |  |  | SI | Recepción de la muestra |
| Q19 | - |  |  | SI | Fecha |
| Q20 | - |  |  | SI | Hora |
| Q21 | - |  |  | SI | Nombre Responsable Recepción |
| Q22 | - |  |  | SI | Nombre y Firma TM |
| Q23 | - |  |  | SI | N° de Cultivo |
| Q24 | - |  |  | SI | Resultado BK |
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