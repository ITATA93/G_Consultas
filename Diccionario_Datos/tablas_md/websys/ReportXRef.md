# websys.ReportXRef

> Cross Reference for report criteria

**Schema:** websys
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cross Reference for report criteria

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ActiveDateFrom | date |  |  | SI | Log 39853 - AI - 22-11-2005 : Add 2 new fields : A... |
| ActiveDateTo | date |  |  | SI | Log 39853 - AI - 22-11-2005 : Add 2 new fields : A... |
| ApptCancelInitiator | varchar |  |  | SI | Log 54141 YC - Add field |
| ApptStatus | varchar |  |  | SI | Log 54141 YC - Add field |
| CareProvider | varchar |  |  | SI | - |
| Hospital | bigint |  |  | SI | - |
| IntendedManagement | bigint |  |  | SI | - |
| Interpreter | bigint |  |  | SI | Log 54141 YC - Add field |
| ItemCategory | bigint |  |  | SI | - |
| LetterType | bigint |  |  | SI | - |
| Location | bigint |  |  | SI | - |
| Location2 | bigint |  |  | SI | - |
| Module1 | bigint |  |  | SI | - |
| OrderItem | varchar |  |  | SI | - |
| ReasonForRemoval | bigint |  |  | SI | Log 53055 YC
Reason For Removal |
| RefStatus | bigint |  |  | SI | Log 54141 YC - Add field |
| RefStatusReason | bigint |  |  | SI | Log 54141 YC - Add field |
| Report | bigint |  |  | SI | - |
| ReportReference | varchar |  |  | SI | - |
| StatePPP | bigint |  |  | SI | - |
| Transport | bigint |  |  | SI | Log 54141 YC - Add field |
| Trust | bigint |  |  | SI | - |
| WaitingListType | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*