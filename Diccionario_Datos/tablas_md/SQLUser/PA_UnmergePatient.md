# SQLUser.PA_UnmergePatient

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| UNMRG_RowId | bigint | PK |  | NO | - |
| UNMRG_Action | varchar |  |  | SI | Action |
| UNMRG_Date | date |  |  | SI | Date |
| UNMRG_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| UNMRG_PAPMI_From_DR | bigint |  | FK | SI | Des Ref PAPMI From |
| UNMRG_PAPMI_To_DR | bigint |  | FK | SI | Des Ref PAPMI To |
| UNMRG_ReasonMerge_DR | bigint |  | FK | SI | Des Ref ReasonMerge |
| UNMRG_ReasonUnmerge_DR | bigint |  | FK | SI | Des Ref ReasonUnmerge |
| UNMRG_Time | time |  |  | SI | Time |
| UNMRG_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*