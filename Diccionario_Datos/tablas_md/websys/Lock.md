# websys.Lock

> Record locking mechanism

**Schema:** websys
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Record locking mechanism

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID1 | varchar | PK |  | NO | - |
| ClassName | varchar |  |  | SI | - |
| ComponentName | varchar |  |  | SI | Indicates which component most recently acquired t... |
| Computer | varchar |  |  | SI | - |
| ComputerName | varchar |  |  | SI | - |
| Id | varchar |  |  | SI | Referenced Id of persistant class ClassName |
| IdExpression | varchar |  |  | NO | Derive lock id based on app server name, so we can... |
| LockDate | date |  |  | SI | Date Stamp |
| LockTime | time |  |  | SI | - |
| LoginLocation | varchar |  |  | SI | - |
| MachineLock | bit |  |  | SI | Log 74987 PeterC 04/01/10 |
| ManualLock | bit |  |  | SI |  74867 - Flag used for manual locking on orders sc... |
| SessionId | varchar |  |  | SI | - |
| UserDR | varchar |  | FK | SI | User that locked the record ;noalert |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*