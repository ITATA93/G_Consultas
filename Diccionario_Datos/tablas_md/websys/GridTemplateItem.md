# websys.GridTemplateItem

**Schema:** websys
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GTIParRef | bigint | PK |  | NO | - |
| CellSettingsDR | bigint |  | FK | SI | - |
| ConditionalExpression | varchar |  |  | SI | Expression using row and col and GTEParReF which d... |
| ID | varchar |  |  | NO | - |
| ItemName | varchar |  |  | SI | - |
| Rank | integer |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*