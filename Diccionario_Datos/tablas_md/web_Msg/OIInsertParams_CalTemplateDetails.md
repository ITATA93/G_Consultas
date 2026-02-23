# web_Msg.OIInsertParams_CalTemplateDetails

**Schema:** web_Msg
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| DCTDAsPerProtocol | varchar |  |  | SI | As Per Protocol |
| DCTDDose | double |  |  | SI | Dose |
| DCTDDurationType | varchar |  |  | SI | DurationType |
| DCTDDurationValue | double |  |  | SI | Duration Value |
| DCTDEvent | varchar |  |  | SI | Event |
| DCTDMaintenanceInstruction | varchar |  |  | SI | Maintenance Instruction |
| DCTDMinDose | double |  |  | SI | Minimum Dose |
| DCTDPHCFRDR | bigint |  | FK | SI | Des Ref to PHCFR (Frequency) |
| DCTDParRef | varchar |  |  | SI | - |
| DCTDPrefParamsDosingDR | varchar |  | FK | SI | Dosing Cycle |
| DCTDSequence | integer |  |  | SI | Sequence |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*