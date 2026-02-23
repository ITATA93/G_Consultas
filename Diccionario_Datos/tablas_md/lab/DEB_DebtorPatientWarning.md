# lab.DEB_DebtorPatientWarning

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEBPW_ParRef | varchar | PK |  | NO | DEB_Debtor Parent Reference |
| DEBPW_DateEnd | date |  |  | SI | Date End |
| DEBPW_DateStart | date |  |  | SI | Date Start |
| DEBPW_PatientWarningDR | varchar |  | FK | SI | Patient Warning |
| DEBPW_RowID | varchar |  |  | NO | - |
| DEBPW_Seq | numeric |  |  | NO | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*