# lab.CT_BugsAntiBioticsActions

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBUB_ParRef | varchar | PK |  | NO | CT_BugsAntiBiotics Parent Reference |
| CTBUB_ActionType | varchar |  |  | SI | Action Type |
| CTBUB_Group | varchar |  |  | SI | Group |
| CTBUB_InfoText | varchar |  |  | SI | Info Text |
| CTBUB_Order | double |  |  | NO | Order number |
| CTBUB_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*