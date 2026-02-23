# websys.MonitorSystem

> Key details of the system captured every day

**Schema:** websys
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Key details of the system captured every day

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CPUArch | varchar |  |  | SI | - |
| CPUMHz | varchar |  |  | SI | - |
| CPUModel | varchar |  |  | SI | - |
| CPUnChips | varchar |  |  | SI | - |
| CPUnCores | varchar |  |  | SI | - |
| CPUnThreads | varchar |  |  | SI | - |
| InstanceName | varchar |  |  | SI | - |
| NodeName | varchar |  |  | SI | - |
| PerformanceStatisticsCapture | varchar |  |  | SI | - |
| PerformanceStatisticsCaptureVerbose | varchar |  |  | SI | - |
| PerformanceStatisticsIconCapture | varchar |  |  | SI | - |
| RunDate | date |  |  | SI | Date of data from websys.Monitor
RunDate and RunT... |
| RunTime | time |  |  | SI | Time this run was started
RunDate and RunTime uni... |
| SystemMode | varchar |  |  | SI | $System.Version.SystemMode() |
| TCEnableCaching | varchar |  |  | SI | - |
| ZVString | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*