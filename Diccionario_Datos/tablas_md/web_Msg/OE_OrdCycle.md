# web_Msg.OE_OrdCycle

**Schema:** web_Msg
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CYCLE_Childsub | double |  |  | SI | Childsub |
| CYCLE_DayNumber | varchar |  |  | SI | Day Number |
| CYCLE_DayOfTheWeek | varchar |  |  | SI | Day of the week |
| CYCLE_DoseQty | varchar |  |  | SI | - |
| CYCLE_Instruction | varchar |  |  | SI | Instruction  |
| CYCLE_IsConditional | varchar |  |  | SI | Dosing cycle is a Conditional Dose |
| CYCLE_MinDoseQty | varchar |  |  | SI | - |
| CYCLE_ParRef | varchar |  |  | SI | OE_OrdItem Parent Reference
Required by User.OEOr... |
| CYCLE_RowId | varchar |  |  | SI | - |
| CYCLE_Time | time |  |  | SI | Dispensing Time |
| ID | varchar |  |  | NO | - |
| MedReconDCycleDR | bigint |  | FK | SI | Des Ref to OEDosingCycle
for tcui medhx |
| OrderID | varchar |  |  | SI | Des Ref to OEOrdItem |
| OtherID | varchar |  |  | SI | string to store non-OrderID - for medhx, medrec, e... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*