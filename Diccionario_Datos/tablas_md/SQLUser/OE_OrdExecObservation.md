# SQLUser.OE_OrdExecObservation

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBS_ParRef | varchar | PK |  | NO | OE_OrdExec Parent Reference |
| ChildQ64DR | - |  |  | SI | Child Reference: Special Test (+ or - ) |
| OBS_Childsub | double |  |  | NO | Childsub |
| OBS_LatestObsEntryDate | date |  |  | SI | LatestObsEntryDate  |
| OBS_LatestObsEntryTime | time |  |  | SI | LatestObsEntryTime  |
| OBS_ObservationEntry_DR | varchar |  | FK | SI | Des Ref MRObservationEntry |
| OBS_RowId | varchar |  |  | NO | - |
| OBS_TotalFluidIntake | double |  |  | SI | TotalFluidIntake   |
| Q63Q1 | - |  |  | SI | Muscle |
| Q63Q2 | - |  |  | SI | Strength left |
| Q63Q3 | - |  |  | SI | Strength right |
| Q63Q4 | - |  |  | SI | Resisted isometric test |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*