# SQLUser.PA_PrDelIndMethods

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PDIM_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| PDIM_Childsub | double |  |  | NO | Childsub |
| PDIM_IndMth_DR | bigint |  | FK | SI | Des Ref PAC_InductionMethods |
| PDIM_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*