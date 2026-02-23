# websys.PatchHistory

> Store the history of patches applied to an environment

**Schema:** websys
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

*Descripción original:* Store the history of patches applied to an environment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AppliedDate | date |  |  | SI | Date the patch was applied  |
| AppliedTime | time |  |  | SI | Time the patch was applied |
| BuildDescription | varchar |  |  | SI | Optional description that can be entered at build ... |
| BuildEditionCode | varchar |  |  | SI | The edition code of the build that has been applie... |
| BuildNumber | varchar |  |  | SI | The number of the build that has been applied |
| Message | varchar |  |  | SI | Full error message in case the patch application f... |
| P4Branch | varchar |  |  | SI | Perforce branch with system code (classes, routine... |
| P4Changelist | varchar |  |  | SI | Latest changelist from P4Branch included in this p... |
| P4LocalBranch | varchar |  |  | SI | Perforce branch with local edition configuration u... |
| P4LocalChangelist | varchar |  |  | SI | Latest changelist from P4LocalBranch included in t... |
| PatchDate | date |  |  | SI | Date the patch was created  |
| PatchFileName | varchar |  |  | SI | Full patch file name, without the .zip suffix |
| PatchLevel | varchar |  |  | SI | Superpatch number optionally followed by edition c... |
| PatchTime | time |  |  | SI | Time the patch was created |
| PatchType | varchar |  |  | SI | - |
| Status | varchar |  |  | SI | Patch application status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*