# SQLUser.PA_PregLabDelCompl

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDLDC_ParRef | bigint | PK |  | NO | PA_Pregnancy Parent Reference |
| PDLDC_Childsub | double |  |  | NO | Childsub |
| PDLDC_Complication_DR | bigint |  | FK | SI | Des ref Pac_LabDelComplications |
| PDLDC_RowId | varchar |  |  | NO | - |
| PDLDC_SortOrder | double |  |  | SI | Sort order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*