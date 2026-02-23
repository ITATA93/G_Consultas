# SQLUser.LB_InstrumentTestItemResult

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBITIR_ParRef | bigint | PK |  | NO | Parent TestSet DR |
| ChildQ80DR | - |  |  | SI | Child Reference: Motor |
| LBITIR_Active | varchar |  |  | SI | Flag to indicate if the result is active and is to... |
| LBITIR_BloodProductID | varchar |  |  | SI | Blood product ID as provided by the instrument (do... |
| LBITIR_Comments | varchar |  |  | SI | Test item result comments |
| LBITIR_InstrumentFlags | varchar |  |  | SI | Instrument flag link to instrument flag code table... |
| LBITIR_InstrumentTestItemID | varchar |  |  | SI | Test item ID as provided by the instrument (Channe... |
| LBITIR_NumberOfRepeats | varchar |  |  | SI | Number of repeats |
| LBITIR_OriginalInstrumentFlags | varchar |  |  | SI | Original instrument flag descriptions (as sent by ... |
| LBITIR_Pathogen_DR | bigint |  | FK | SI | If the result is a pathogen this dr links to the p... |
| LBITIR_PerformedDate | date |  |  | SI | Date test performed |
| LBITIR_PerformedTime | time |  |  | SI | Time test performed |
| LBITIR_QCRunData_DR | varchar |  | FK | SI | Link to the QC Run Data |
| LBITIR_ReasonHeld | varchar |  |  | SI | The reason why result is held on the instrument gr... |
| LBITIR_ReasonHeldComment | varchar |  |  | SI | Optional additional comment for the reason why res... |
| LBITIR_ResultAbnormalFlag | varchar |  |  | SI | Result abnormal flag
Either an internal (stored) ... |
| LBITIR_ResultValue | varchar |  |  | SI | Result value |
| LBITIR_RowID | varchar |  |  | NO | - |
| LBITIR_StaffNotes | varchar |  |  | SI | Test item result staff notes |
| LBITIR_TestItem_DR | bigint |  | FK | SI | Test Item |
| LBITIR_UpdateDate | date |  |  | SI | Date of last update |
| LBITIR_UpdateTime | time |  |  | SI | Time of last update |
| LBITIR_User_DR | bigint |  | FK | SI | The user that entered this result manually (blank ... |
| Q74Q1 | - |  |  | SI | Pulso |
| Q74Q2 | - |  |  | SI | Lateralidad |
| Q74Q3 | - |  |  | SI | Hallazgo |
| Q74Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*