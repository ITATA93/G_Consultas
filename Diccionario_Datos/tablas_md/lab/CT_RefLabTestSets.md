# lab.CT_RefLabTestSets

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTRLT_ParRef | varchar | PK |  | NO | CT_ReferralLaboratory Parent Reference |
| CTRLT_ExternalTestSet | varchar |  |  | SI | CTRLT External Test Set |
| CTRLT_RowID | varchar |  |  | NO | - |
| CTRLT_TestSet_DR | varchar |  | FK | NO | CTRLT TestSet DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*