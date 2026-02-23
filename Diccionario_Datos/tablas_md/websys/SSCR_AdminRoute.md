# websys.SSCR_AdminRoute

> /// Models a list of Admin Routes configured for a given Second-Signature Config Rule.

**Schema:** websys
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* /// Models a list of Admin Routes configured for a given Second-Signature Config Rule.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSCRule_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| ID | varchar |  |  | NO | - |
| SSCRule_AdminRoute_DR | bigint |  | FK | SI | Des Ref Hospital |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*