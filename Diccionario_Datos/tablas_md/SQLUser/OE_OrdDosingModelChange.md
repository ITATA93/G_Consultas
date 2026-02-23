# SQLUser.OE_OrdDosingModelChange

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEOrdDMC_ParRef | varchar | PK |  | NO | Parent Reference |
| OEOrdDMC_CalendarAddNodes | bit |  |  | SI | Calendar Additional Administrations |
| OEOrdDMC_CalendarConditionChanged | bit |  |  | SI | Calendar  Condition Changed |
| OEOrdDMC_CalendarDoseAmountChanged | bit |  |  | SI | Calendar Dose Amount Changed |
| OEOrdDMC_CalendarDoseTimeChanged | bit |  |  | SI | Calendar Dose Time Changed |
| OEOrdDMC_CalendarInstructChanged | bit |  |  | SI | Calendar  Instruction Changed |
| OEOrdDMC_CalendarNoChanges | bit |  |  | SI | Calendar No Changes |
| OEOrdDMC_CalendarPerProtocol | bit |  |  | SI | Calendar As Per Protocol |
| OEOrdDMC_Childsub | double |  |  | NO | Childsub |
| OEOrdDMC_CycleConditionChanged | bit |  |  | SI | Cycle Condition Changed |
| OEOrdDMC_CycleDoseAmountChanged | bit |  |  | SI | Cycle Dose Amount Changed |
| OEOrdDMC_CycleDoseTimeChanged | bit |  |  | SI | Cycle Dose Time Changed |
| OEOrdDMC_CycleInstructChanged | bit |  |  | SI | Cycle  Instruction Changed |
| OEOrdDMC_CycleNoChanges | bit |  |  | SI | Cycle No Changes |
| OEOrdDMC_RowId | varchar |  |  | NO | - |
| Q41Q1 | - |  |  | SI | Joint |
| Q41Q2 | - |  |  | SI | Laterality |
| Q41Q3 | - |  |  | SI | Motion |
| Q41Q4 | - |  |  | SI | ROM (Degrees) |
| Q41Q5 | - |  |  | SI | Muscle power |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*