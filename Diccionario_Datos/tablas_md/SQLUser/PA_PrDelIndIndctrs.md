# SQLUser.PA_PrDelIndIndctrs

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDII_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| PDII_Childsub | double |  |  | NO | Childsub |
| PDII_IndIndctr_DR | bigint |  | FK | SI | Des ref PAC_InductionIndicators |
| PDII_RowId | varchar |  |  | NO | - |
| PDII_SortOrder | double |  |  | SI | Sort order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*