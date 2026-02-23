# lab.CT_TestMethodTranslation

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTMT_ParRef | varchar | PK |  | NO | CT_TestMethod Parent Reference |
| CTTMT_Comment | varchar |  |  | SI | Comment |
| CTTMT_Description | varchar |  |  | SI | Description |
| CTTMT_Language_DR | bigint |  | FK | NO | Language DR |
| CTTMT_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*