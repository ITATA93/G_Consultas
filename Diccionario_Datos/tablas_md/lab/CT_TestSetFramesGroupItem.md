# lab.CT_TestSetFramesGroupItem

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSI_ParRef | varchar | PK |  | NO | CT_TestSetFramesGroup Parent Reference |
| CTTSI_DefaultResult | varchar |  |  | SI | Default Result |
| CTTSI_Extra | varchar |  |  | SI | Extra |
| CTTSI_RowID | varchar |  |  | NO | - |
| CTTSI_Sequence | numeric |  |  | SI | Sequence number |
| CTTSI_TestItem_DR | varchar |  | FK | NO | Test Item |
| CTTSI_Title | varchar |  |  | SI | Display Title |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*