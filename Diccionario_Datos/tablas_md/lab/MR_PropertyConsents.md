# lab.MR_PropertyConsents

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRPC_ParRef | varchar | PK |  | NO | MR_Property Parent Reference |
| MRPC_Consent_DR | varchar |  | FK | SI | Consent |
| MRPC_DocumentDR | varchar |  | FK | SI | Document |
| MRPC_OrderNumber | double |  |  | NO | Order Number |
| MRPC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*