# SQLUser.NR_NurseRosterRoom

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NURR_ParRef | bigint | PK |  | NO | PA_Nurse_Rostering Parent Reference |
| NURR_Childsub | double |  |  | NO | Childsub |
| NURR_Room_DR | bigint |  | FK | SI | Room Des Ref to PACRoom |
| NURR_RowId | varchar |  |  | NO | - |
| Q18Q1 | - |  |  | SI | Fetus number |
| Q18Q2 | - |  |  | SI | Heart monitoring |
| Q18Q3 | - |  |  | SI | Baseline |
| Q18Q4 | - |  |  | SI | 3 accelerations |
| Q18Q5 | - |  |  | SI | Variability |
| Q18Q6 | - |  |  | SI | Decelerations |
| Q18Q7 | - |  |  | SI | Acceptable |
| Q18Q8 | - |  |  | SI | Difficult to interpret |
| Q18Q9 | - |  |  | SI | Reassuring |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*