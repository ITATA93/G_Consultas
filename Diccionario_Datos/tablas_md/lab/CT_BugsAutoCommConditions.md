# lab.CT_BugsAutoCommConditions

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBSC_ParRef | varchar | PK |  | NO | CT_BugsAutoComments Parent Reference |
| CTBSC_Antibiotic_DR | varchar |  | FK | NO | Antibiotic DR |
| CTBSC_Result_DR | varchar |  | FK | SI | Result DR |
| CTBSC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*