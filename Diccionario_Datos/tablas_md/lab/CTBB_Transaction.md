# lab.CTBB_Transaction

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo Banco de Sangre**. Configuración de hemoterapia.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBTR_RowID | varchar | PK |  | NO | - |
| BBTR_ActiveFlag | varchar |  |  | SI | Active Flag |
| BBTR_Code | varchar |  |  | NO | Transaction Code |
| BBTR_Description | varchar |  |  | SI | Description |
| BBTR_DisplayInPatientHistory | varchar |  |  | SI | Display in patient History |
| BBTR_LocationRequired | varchar |  |  | SI | Location Required |
| BBTR_PrintLabels | varchar |  |  | SI | Print Labels |
| BBTR_RequireComment | varchar |  |  | SI | Require Comment |
| BBTR_Transfusion | varchar |  |  | SI | Transfusion |
| BBTR_Transit | varchar |  |  | SI |  Transit |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*