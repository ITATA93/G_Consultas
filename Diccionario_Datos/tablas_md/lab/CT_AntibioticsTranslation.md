# lab.CT_AntibioticsTranslation

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTANA_ParRef | varchar | PK |  | NO | CT_Antibiotics Parent Reference |
| CTANA_Description | varchar |  |  | SI | Description |
| CTANA_Language_DR | bigint |  | FK | NO | Language DR  |
| CTANA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*