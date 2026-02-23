# lab.CT_MicroPanelItemsActions

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMPA_ParRef | varchar | PK |  | NO | CT_MicrobiologyPanelItems Parent Reference |
| CTMPA_ActionType | varchar |  |  | SI | Action Type |
| CTMPA_Group | varchar |  |  | SI | Group |
| CTMPA_InfoText | varchar |  |  | SI | Info Text |
| CTMPA_Order | double |  |  | NO | Order Number |
| CTMPA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*