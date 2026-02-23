# SQLUser.PAC_PatCnt

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PCNT_RowID1 | double | PK |  | NO | - |
| PCNT_AnaestCnt | double |  |  | SI | Anaesthesia Counter |
| PCNT_IPCnt | double |  |  | SI | In Patient Counter |
| PCNT_OPCnt | double |  |  | SI | Out Patient Counter |
| PCNT_OperCnt | double |  |  | SI | Operation Counter |
| PCNT_QUE1Cnt | double |  |  | SI | QUE1 Counter |
| PCNT_RowID | double |  |  | NO | PA_PatCnt Row ID |
| Q02Q1 | - |  |  | SI | Date |
| Q02Q10 | - |  |  | SI | Blood glucose levels (BGL) in previous 24 hours wi... |
| Q02Q2 | - |  |  | SI | Time |
| Q02Q3 | - |  |  | SI | TPN rate at review |
| Q02Q4 | - |  |  | SI | Days on TPN |
| Q02Q5 | - |  |  | SI | Pathology comments |
| Q02Q6 | - |  |  | SI | Glycaemic control target |
| Q02Q7 | - |  |  | SI | Current frequency of BGL check |
| Q02Q8 | - |  |  | SI | Additional comments |
| Q02Q9 | - |  |  | SI | Bag and line changed within last 24 hours |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*