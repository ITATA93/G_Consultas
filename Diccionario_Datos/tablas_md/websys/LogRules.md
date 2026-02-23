# websys.LogRules

> Rules for Audit Trail of component activity.

**Schema:** websys
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

*Descripción original:* Rules for Audit Trail of component activity.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Component | bigint |  |  | SI | - |
| LogAfterSave | bit |  |  | SI | - |
| LogDelete | bit |  |  | SI | - |
| LogNew | bit |  |  | SI | - |
| LogOpen | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*