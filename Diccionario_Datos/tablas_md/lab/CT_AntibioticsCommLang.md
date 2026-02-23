# lab.CT_AntibioticsCommLang

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTANB_ParRef | varchar | PK |  | NO | CT_AntibioticsComments Parent Reference |
| CTANB_Description | varchar |  |  | SI | Description |
| CTANB_Language_DR | bigint |  | FK | NO | Language DR |
| CTANB_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*