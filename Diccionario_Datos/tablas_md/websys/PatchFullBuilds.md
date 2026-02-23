# websys.PatchFullBuilds

> To Show the History of Full Builds

**Schema:** websys
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* To Show the History of Full Builds

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AppliedDate | date |  |  | SI | - |
| AppliedTime | time |  |  | SI | - |
| BuildEditionCode | varchar |  |  | SI | - |
| BuildFileName | varchar |  |  | SI | - |
| BuildNumber | varchar |  |  | SI | - |
| CreateDate | date |  |  | SI | - |
| CreateTime | time |  |  | SI | - |
| ErrorMsg | varchar |  |  | SI | - |
| P4Branch | varchar |  |  | SI | - |
| P4Changelist | varchar |  |  | SI | - |
| P4LocalBranch | varchar |  |  | SI | - |
| P4LocalChangelist | varchar |  |  | SI | - |
| PlatformVersion | varchar |  |  | SI | - |
| ReleaseLevel | varchar |  |  | SI | - |
| Version | varchar |  |  | SI | 2015, 2016.1, 2016.2 etc. |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*