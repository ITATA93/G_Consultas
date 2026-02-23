# lab.BBP_PackTransactions

**Schema:** lab
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBPT_ParRef | varchar | PK |  | NO | BBP_PackDetails Parent Reference |
| BBPT_Comment_DR | varchar |  | FK | SI | Comment |
| BBPT_Comments | varchar |  |  | SI | Comments |
| BBPT_CurrentPatientDebtor_DR | varchar |  | FK | SI | Current Patient Debtor DR |
| BBPT_CurrentVTSRowID_DR | varchar |  | FK | SI | Current VTS RowID DR - transactional |
| BBPT_Date | date |  |  | SI | Date |
| BBPT_InActive | varchar |  |  | SI | InActive |
| BBPT_NewLocation_DR | varchar |  | FK | SI | New Location DR |
| BBPT_NewPatientDebtor_DR | varchar |  | FK | SI | New Patient Debtor DR |
| BBPT_NewStatus_DR | varchar |  | FK | SI | New Status DR |
| BBPT_NewVisitTS_DR | varchar |  | FK | SI | New Visit TS DR - latest compatible |
| BBPT_RowID | varchar |  |  | NO | - |
| BBPT_Sequence | numeric |  |  | NO | Sequence |
| BBPT_Time | time |  |  | SI | Time |
| BBPT_Transaction_DR | varchar |  | FK | SI | Transaction DR |
| BBPT_TransitDestination_DR | varchar |  | FK | SI | Transit Destination |
| BBPT_TransitETADate | date |  |  | SI | Transit ETA Date |
| BBPT_TransitETATime | time |  |  | SI | Transit ETA Time |
| BBPT_TransitModeOfTransport_DR | varchar |  | FK | SI | Transit Mode of Transport |
| BBPT_User_DR | varchar |  | FK | SI | User DR |
| BBPT_XMStatus | varchar |  |  | SI | XM Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*