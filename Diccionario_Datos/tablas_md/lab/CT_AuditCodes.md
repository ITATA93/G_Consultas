# lab.CT_AuditCodes

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTAU_RowID | varchar | PK |  | NO | - |
| CTAU_AccountNo | varchar |  |  | SI | Account No |
| CTAU_Code | varchar |  |  | NO | Audit Code |
| CTAU_Desc | varchar |  |  | SI | Description |
| CTAU_PrintedAccountName | varchar |  |  | SI | Printed Account Name |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*