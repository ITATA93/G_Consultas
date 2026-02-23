# SQLUser.NRC_InterventionActivity

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NRCIA_ParRef | bigint | PK |  | NO | Parent table |
| ChildQ55DR | - |  |  | SI | Child Reference: Daily shift assessment |
| NRCIA_ARCIM_DR | varchar |  | FK | SI | Order Item |
| NRCIA_Code | varchar |  |  | NO | Code  |
| NRCIA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NRCIA_CycleDur | double |  |  | SI | Cycle Period |
| NRCIA_CycleDurType | varchar |  |  | SI | Cycle Period Type |
| NRCIA_CycleReps | double |  |  | SI | Cycle Repetitions |
| NRCIA_DefaultAutoOrderValid | bit |  |  | SI | Order Item Valid Automatic Order |
| NRCIA_Desc | varchar |  |  | NO | Description |
| NRCIA_Included | bit |  |  | SI | Included or suggested |
| NRCIA_OrderMethod | varchar |  |  | NO | Order Method |
| NRCIA_PrefParams_DR | bigint |  | FK | SI | Order Item Default Parameters |
| NRCIA_RowID | varchar |  |  | NO | - |
| Q133Q1 | - |  |  | SI | Date |
| Q133Q10 | - |  |  | SI | Staff |
| Q133Q2 | - |  |  | SI | Time |
| Q133Q3 | - |  |  | SI | Arterial lumen |
| Q133Q4 | - |  |  | SI | Venous lumen |
| Q133Q5 | - |  |  | SI | Unused lumens flushed |
| Q133Q6 | - |  |  | SI | Arterial lumen condition |
| Q133Q7 | - |  |  | SI | Venous lumen condition |
| Q133Q8 | - |  |  | SI | Insertion length at skin (cm) |
| Q133Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*